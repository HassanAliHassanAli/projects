To design a highly available, fault-tolerant microservices architecture for a global E-commerce platform expecting massive traffic spikes using AWS services, we'll need to consider several key components:

1. **Load Balancing**: Use an Application Load Balancer (ALB) to distribute incoming application traffic across multiple targets in your VPC.

2. **Auto-Scaling**: Set up Auto Scaling Groups (ASGs) with Auto Scaling policies based on the traffic patterns and expected load spikes to ensure that enough instances are available to handle the increased load.

3. **Database Replication**: Utilize Amazon RDS for PostgreSQL or MySQL databases, set up Multi-AZ replication for high availability, and consider using Read Replicas in separate Availability Zones to further distribute read workload and improve scalability.

4. **Caching**: Deploy an Amazon ElastiCache cluster of Redis or Memcached nodes to cache frequently accessed data and reduce the load on your database by serving these requests locally within the VPC.

5. **Virtual Private Cloud (VPC)**: Create a secure VPC with public and private subnets, internet gateway, and route tables to isolate your resources and provide network security.

### Terraform Configuration Script

```terraform
# Terraform configuration for an AWS E-commerce platform
provider "aws" {}

resource "aws_vpc" "ecommerce_platform" {
  cidr_block = "10.0.0.0/16"
  tags         = {
    Name = "Ecommerce Platform"
  }
}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.ecommerce_platform.id
  cidr_block        = ["10.0.1.0/24", "10.0.2.0/24"]
  availability_zone = "${random_aws_availability_zones.zone_name[0]}"
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.ecommerce_platform.id
  cidr_block        = ["10.0.3.0/24", "10.0.4.0/24"]
  availability_zone = "${random_aws_availability_zones.zone_name[1]}"
}

resource "aws_internet_gateway" "ecommerce_platform" {
  vpc_id = aws_vpc.ecommerce_platform.id
  tags   = {
    Name = "Ecommerce Platform Internet Gateway"
  }
}

resource "aws_route_table" "public" {
  count             = 2
  vpc_id            = aws_vpc.ecommerce_platform.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.ecommerce_platform.id
  }
}

resource "aws_route_table_association" "public_subnets" {
  count             = 2
  subnet_id         = aws_subnet.public[count-1].id
  route_table_id   = aws_route_table.public[count-1].id
}

resource "aws_route_table_association" "private_subnets" {
  count             = 2
  subnet_id         = aws_subnet.private[count-1].id
  route_table_id   = aws_route_table.public[count-1].id
}

resource "aws_security_group" "ecommerce_platform" {
  name_prefix = "ecommerce-platform"
  vpc_id      = aws_vpc.ecommerce_platform.id

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 22
    to_port     = 22
    protocol    = "-1"
  }

  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = -1
    to_port     = -1
    protocol    = "-1"
  }
}

resource "aws_security_group_inbound" {
  count             = 2
  vpc_id            = aws_vpc.ecommerce_platform.id
  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = -1
    to_port     = -1
    protocol    = "-1"
    security_groups = [aws_security_group.ecommerce_platform]
  }
}

resource "aws_alb" "ecommerce_platform" {
  name_prefix           = "ecommerce-platform-alb"
  load_balancer_type    = "internet-facing"
  subnets               = aws_subnet.public.*.id
  security_groups       = [aws_security_group_inbound]
  tags                   = {
    Name = "Ecommerce Platform Application Load Balancer"
  }
}

resource "aws_alb_target_group" "ecommerce_platform" {
  name_prefix           = "ecommerce-platform-target-group"
  port                 = 80
  protocol             = "HTTP"
  vpc_id               = aws_vpc.ecommerce_platform.id
  target_type          = "ip"
  health_check_path    = "/health-check"
}

resource "aws_elastic_load_balancing_policy" "ecommerce-platform-policy" {
  name         = "Ecommerce Platform Policy"
  type         = "TargetGroupPolicy"
  policy_name  = "Ecommerce Platform Policy"

  for_each        = toset(["v1", "v2"])

  policy_types = [
    "StickinessPolicy",
    "DefaultTargets",
  ]

  for each in tolist(policy_types) do
    policy_statement {
      action   = "${each}"
      scope     = "TargetGroup"
      resource = "*"
    }
  end
}

resource "aws_alb_listener" "ecommerce-platform-listener-1" {
  load_balancer_arn = aws_alb.ecommerce_platform.id
  port              = 80
  protocol          = "HTTP"
  ssl_certificate_arn = "<Your SSL Certificate ARN>"
  certificate_id       = "<Your Certificate ID>"
}

resource "aws_alb_listener" "ecommerce-platform-listener-2" {
  load_balancer_arn = aws_alb.ecommerce_platform.id
  port              = 443
  protocol          = "HTTPS"
  ssl_certificate_arn = "<Your SSL Certificate ARN>"
  certificate_id       = "<Your Certificate ID>"
}

resource "aws_autoscaling_group" "ecommerce-platform-asg" {
  name_prefix           = "ecommerce-platform-asg-"
  vpc_zone_identifier    = "${split(",", aws_subnet.private.*.availability_zone)}"
  min_size              = 1
  max_size              = 50
  desired_capacity       = 3

  health_check_type     = "EC2"
  health_threshold      = 2

  tags                 = {
    Name         = "Ecommerce Platform ASG"
    Environment  = "${var.environment}"
  }

  instance_healthcheck = "http://169.254.169.254/latest/meta-data/health-status"

  target_group_arns     = [aws_alb_target_group.ecommerce_platform.id]

  launch_config {
    name_prefix           = "ecommerce-platform-lc-"
    image_id               = "<Your Amazon ECR Image ID>"
    instance_type          = "t2.micro"
    key_name                = "your-key-pair-name"
    security_groups        = [aws_security_group.ecommerce_platform]
    user_data              = <<-EOF
      #!/bin/bash -l
      echo "Adding a custom health check"
      aws ec2 create-instance-healthcheck --instance-id "${azs(0, length(azs('aws_instance.ecommerce-platform-asg-')))::instance_id}" --health-check-type EC2 --health-threshold 2
    EOF

    instance_profile_arn = "<Your IAM Role ARN>"
  }

  load_balancer {
    target_group_arn   = aws_alb_target_group.ecommerce_platform.id
  }

  policy {
    name      = "Ecommerce Platform Auto Scaling Policy"
    type      = "LoadBalancerPolicy"
    policy_name = "Ecommerce Platform Load Balancer Policy"

    for_each        = toset(["v1", "v2"])

    policy_types = [
      "TargetGroupPolicy",
      "DefaultTargets",
    ]

    for each in tolist(policy_types) do
      policy_statement {
        action   = "${each}"
        scope     = "LoadBalancer"
        resource = "*"
      }
    end

  }

}

resource "aws_rds_cluster" "ecommerce_platform_cluster" {
  engine           = "aurora-postgresql"
  master_username  = "<Your RDS Master Username>"
  master_password  = "<Your RDS Master Password>"
  db_subnet_group_name  = aws_db_subnet_group.ecommerce_platform.id
  vpc_security_groups = [aws_security_group.ecommerce_platform]

  engine_mode        = "async"

  cluster_identifier      = "ecommerce-platform-cluster-${var.environment}"
  availability_zones     = ["<Your Availability Zones>"]
}

resource "aws_rds_cluster_instance" "ecommerce_platform_read_replica" {
  instance_class       = "db.t2.micro"
  db_subnet_group_name = aws_db_subnet_group.ecommerce_platform.id
  vpc_security_groups = [aws_security_group.ecommerce_platform]

  engine_mode        = "async"
  multi_az           = true

  engine = "aurora-postgresql"

  master_username  = "<Your RDS Master Username>"
  master_password  = "<Your RDS Master Password>"

  cluster_identifier      = aws_rds_cluster.ecommerce_platform_cluster.id
}

resource "aws_db_subnet_group" "ecommerce_platform" {
  name_prefix           = "ecommerce-platform-db"
  subnet_ids             = [aws_subnet.private[0].id, aws_subnet.public[0].id]
}

resource "aws_elasticache_cache_node" "ecommerce_platform" {
  cluster_id     = "<Your ElastiCache Cluster ID>"
  node_type      = "cache.m1.large"
  vpc_security_groups = [aws_security_group.ecommerce_platform]

  engine = "redis"

  master_password = "<Your Redis Master Password>"

  node_count = 3

}

resource "aws_elasticache_cache_subnet_group" "ecommerce_platform" {
  name_prefix           = "ecommerce-platform-cache"
  subnet_ids             = [aws_subnet.private[0].id, aws_subnet.public[0].id]
}

resource "aws_s3_bucket" "ecommerce_platform" {
  bucket_name = "ecommerce-platform-bucket-${var.environment}"
  acl        = "private"
}

resource "aws_s3_bucket_website" "ecommerce_platform" {
  bucket = aws_s3_bucket.ecommerce_platform
  website_index_document = "index.html"

  access_control = "PublicRead"
}
```

This Terraform script will create a secure VPC with public and private subnets, an Application Load Balancer, and an Auto Scaling Group. It also provisions database replication using Amazon RDS for PostgreSQL or MySQL databases, and caching is set up through Amazon ElastiCache clusters of Redis or Memcached nodes.

Please note that you need to replace `<Your AWS Account ID>`, `<Your VPC ID>`, `<Your Availability Zones>`, `<Your RDS Master Username/Password>` and `<Your Certificate ID/ARN>` with the actual values specific to your environment.