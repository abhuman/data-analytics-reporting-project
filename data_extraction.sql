SELECT
    department,
    month,
    COUNT(user_id) AS total_users,
    SUM(transactions) AS total_transactions,
    SUM(amount) AS total_amount
FROM operational_data
WHERE status = 'Completed'
GROUP BY department, month;
