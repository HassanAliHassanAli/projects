USE InstacartDB;
GO

-- 1. التأكد من عدد الصفوف في أضخم جدول (المفروض يطلع حوالي 32 مليون)
SELECT COUNT(*) AS Total_Rows 
FROM order_products_prior;

-- 2. نظرة سريعة على أول 10 صفوف من جدول الطلبات عشان نتأكد من شكل البيانات
SELECT TOP 10 * 
FROM orders;