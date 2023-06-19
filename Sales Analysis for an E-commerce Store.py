# Monthly Revenue:
SELECT EXTRACT(YEAR_MONTH FROM order_date) AS month,
       SUM(order_total) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

# Top Selling Products by Quantity:
SELECT p.product_name,
       SUM(oi.quantity) AS total_quantity
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 10;

# Customer Analysis - CLV (Customer Lifetime Value):
SELECT c.customer_id,
       c.customer_name,
       SUM(o.order_total) AS total_spent,
       COUNT(DISTINCT o.order_id) AS total_orders,
       SUM(o.order_total) / COUNT(DISTINCT o.order_id) AS clv
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY clv DESC;

# Sales by Geography:
SELECT country,
       SUM(order_total) AS total_sales
FROM orders
GROUP BY country
ORDER BY total_sales DESC;

# Product Category Analysis:
SELECT pc.category_name,
       SUM(oi.quantity) AS total_quantity,
       SUM(oi.quantity * oi.price) AS category_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN product_categories pc ON p.category_id = pc.category_id
GROUP BY pc.category_name
ORDER BY category_revenue DESC;