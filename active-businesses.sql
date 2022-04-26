# Write your MySQL query statement below

# For all event types --> get the average occurrences across all businesses for that event (aka # of times that event occurs / total # of events) --> AVERAGE ACTIVITY FOR EACH EVENT

SELECT e1.business_id 
FROM Events e1
LEFT JOIN
(SELECT event_type, AVG(occurences) as avg_activity
FROM Events 
GROUP BY event_type) e2
on e1.event_type =e2.event_type
GROUP BY e1.business_id
Having SUM(IF(e1.occurences > e2.avg_activity, 1, 0)) > 1
