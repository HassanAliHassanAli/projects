-- 1. إنشاء قاعدة البيانات الجديدة
CREATE DATABASE InstacartDB;
GO
USE InstacartDB;
GO

-- 2. إنشاء جدول الأقسام (departments)
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department VARCHAR(255) NOT NULL
);

-- 3. إنشاء جدول الممرات (aisles)
CREATE TABLE aisles (
    aisle_id INT PRIMARY KEY,
    aisle VARCHAR(255) NOT NULL
);

-- 4. إنشاء جدول المنتجات (products)
-- لاحظ هنا إننا بنربط المنتج بالقسم والممر بتاعه (علاقات الـ ERP)
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(500) NOT NULL,
    aisle_id INT FOREIGN KEY REFERENCES aisles(aisle_id),
    department_id INT FOREIGN KEY REFERENCES departments(department_id)
);

-- 5. إنشاء جدول الطلبات الأساسية (orders)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    eval_set VARCHAR(50),
    order_number INT,
    order_dow INT,
    order_hour_of_day INT,
    days_since_prior_order FLOAT NULL -- سيبناها Null زي ما اتفقنا عشان أول طلب للعميل
);

-- 6. إنشاء جدول تفاصيل الطلبات والمنتجات (order_products_prior)
-- ده الجدول الأضخم اللي هيستقبل الـ 32 مليون صف
CREATE TABLE order_products_prior (
    order_id INT FOREIGN KEY REFERENCES orders(order_id),
    product_id INT FOREIGN KEY REFERENCES products(product_id),
    add_to_cart_order INT,
    reordered INT,
    PRIMARY KEY (order_id, product_id)
);