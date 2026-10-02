# Write your MySQL query statement below
UPDATE salary 
SET sex=CASE
        when sex='m' THEN 'f'
        else 'm'
END