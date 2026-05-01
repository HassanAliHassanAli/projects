USE InstacartDB;
GO

-- تعديل الـ Master View لإضافة أعمدة تحليلية (Feature Engineering)
ALTER VIEW vw_Master_Sales_Data AS
SELECT 
    o.order_id,
    o.user_id,
    o.order_number,
    o.order_dow AS day_of_week,
    
    -- 1. ميزة: هل الطلب في عطلة نهاية الأسبوع أم أيام العمل؟
    -- في بيانات Instacart، الأيام 0 و 1 هم الأكثر ازدحاماً (غالباً السبت والأحد)
    CASE 
        WHEN o.order_dow IN (0, 1) THEN 'Weekend'
        ELSE 'Weekday'
    END AS Day_Type,
    
    o.order_hour_of_day,
    
    -- 2. ميزة: تحديد أوقات الذروة (Peak Hours)
    CASE 
        WHEN o.order_hour_of_day BETWEEN 9 AND 16 THEN 'Peak Hours (9 AM - 4 PM)'
        WHEN o.order_hour_of_day BETWEEN 17 AND 22 THEN 'Evening (5 PM - 10 PM)'
        ELSE 'Off-Peak / Night'
    END AS Time_of_Day,
    
    o.days_since_prior_order,
    
    -- 3. ميزة: تصنيف نوع الطلب (طلب أول لعميل جديد ولا عميل مستمر؟)
    CASE 
        WHEN o.days_since_prior_order IS NULL THEN 'First-Time Order'
        ELSE 'Returning Customer'
    END AS Customer_Loyalty_Status,
    
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