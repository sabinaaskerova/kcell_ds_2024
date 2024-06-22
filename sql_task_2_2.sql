-- Медиана значений
SELECT AVG(value) AS median
FROM (
    SELECT value
    FROM random_ints
    ORDER BY value
    LIMIT 2 - (SELECT COUNT(*) FROM random_ints) % 2
    OFFSET (SELECT (COUNT(*) - 1) / 2 FROM random_ints)
);