USE SupplyChain_DB;

-- كود لعرض أول 10 صفوف من الداتا عشان نفهم شكلها
SELECT TOP 10 * FROM OrdersData;

USE SupplyChain_DB;

SELECT 
    Order_Region, 
    COUNT(Order_Id) AS Total_Late_Orders
FROM 
    OrdersData
WHERE 
    Delivery_Status = 'Late delivery'
GROUP BY 
    Order_Region
ORDER BY 
    Total_Late_Orders DESC;

	USE SupplyChain_DB;

SELECT 
    Order_Region, 
    Shipping_Mode,
    COUNT(Order_Id) AS Total_Late_Orders
FROM 
    OrdersData
WHERE 
    Delivery_Status = 'Late delivery' 
    AND Order_Region IN ('Central America', 'Western Europe') -- فلترنا على أكتر منطقتين فيهم مشاكل
GROUP BY 
    Order_Region, 
    Shipping_Mode
ORDER BY 
    Total_Late_Orders DESC;

	USE SupplyChain_DB;

SELECT 
    Shipping_Mode,
    AVG(CAST(Days_for_shipping_real AS FLOAT)) AS Avg_Actual_Days,
    AVG(CAST(Days_for_shipment_scheduled AS FLOAT)) AS Avg_Scheduled_Days,
    (AVG(CAST(Days_for_shipping_real AS FLOAT)) - AVG(CAST(Days_for_shipment_scheduled AS FLOAT))) AS Delay_Difference
FROM 
    OrdersData
WHERE 
    Delivery_Status = 'Late delivery'
GROUP BY 
    Shipping_Mode
ORDER BY 
    Delay_Difference DESC;

	USE SupplyChain_DB;

SELECT TOP 5
    Category_Name,
    Product_Name,
    COUNT(Order_Id) AS Total_Late_Orders
FROM 
    OrdersData
WHERE 
    Delivery_Status = 'Late delivery'
GROUP BY 
    Category_Name, 
    Product_Name
ORDER BY 
    Total_Late_Orders DESC;

	USE SupplyChain_DB;

SELECT TOP 5
    Order_Region, 
    SUM(CAST(Sales AS FLOAT)) AS Total_Revenue_At_Risk, -- إجمالي الفلوس المتعطلة
    COUNT(Order_Id) AS Total_Late_Orders
FROM 
    OrdersData
WHERE 
    Delivery_Status = 'Late delivery'
GROUP BY 
    Order_Region
ORDER BY 
    Total_Revenue_At_Risk DESC;

