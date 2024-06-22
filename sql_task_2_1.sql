CREATE TABLE random_ints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value INT
);

-- MySQL процедура
DELIMITER //
CREATE PROCEDURE GenerateRandomIntegers()
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE random_value INT;

    WHILE i < 1000000 DO
        SET random_value = FLOOR(RAND() * (2147483647 - (-2147483648)) + (-2147483648));
        INSERT INTO random_ints (value) VALUES (random_value);
        SET i = i + 1;
    END WHILE;
END//

DELIMITER ;

CALL GenerateRandomIntegers();