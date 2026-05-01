USE InstacartDB;
GO

-- إنشاء الـ Master View اللي هيقرا منه Power BI
CREATE VIEW vw_Master_Sales_Data AS
SELECT 
    o.order_id,
    o.user_id,
    o.order_number,
    o.order_dow AS day_of_week,
    o.order_hour_of_day,
    o.days_since_prior_order,
    op.product_id,
    p.product_name,
    d.department,
    a.aisle
FROM orders o
JOIN order_products_prior op ON o.order_id = op.order_id
JOIN products p ON op.product_id = p.product_id
JOIN departments d ON p.department_id = d.department_id
JOIN aisles a ON p.aisle_id = a.aisle_id;
GO