USE InstacartDB;
GO

-- 1. فحص القيم المفقودة في الطلبات لمعرفة حجم العملاء الجدد
-- هنعد كل الطلبات، ونعد الطلبات اللي فيها (days_since_prior_order) فارغ
SELECT 
    COUNT(*) AS Total_Orders,
    SUM(CASE WHEN days_since_prior_order IS NULL THEN 1 ELSE 0 END) AS First_Time_Orders
FROM orders;

-- 2. التحقق من جودة جدول المنتجات (اكتشاف التكرارات)
-- الكود ده هيجيب أي منتج متسجل بنفس الاسم أكتر من مرة
SELECT 
    product_name, 
    COUNT(*) AS Duplicate_Count
FROM products
GROUP BY product_name
HAVING COUNT(*) > 1
ORDER BY Duplicate_Count DESC;