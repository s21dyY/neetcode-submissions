-- Write your query below
WITh CTE1 AS (
    SELECT customer_id,
        SUM(CASE WHEN product_name='A' THEN 1 ELSE 0 END) AS conditionA,
        SUM(CASE WHEN product_name='B' THEN 1 ELSE 0 END) AS conditionB,
        SUM(CASE WHEN product_name='C' THEN 1 ELSE 0 END) AS conditionC
    FROM orders 
    GROUP BY customer_id
)

SELECT o.customer_id,customer_name
FROM CTE1 o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE conditionA > 0 and conditionB>0 and conditionC  = 0
ORDER BY customer_name

