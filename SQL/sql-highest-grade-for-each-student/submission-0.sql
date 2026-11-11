-- Write your query below
SELECT  student_id, 
    exam_id,
    score
FROM(
    SELECT 
        student_id, 
        exam_id,
        score,
        RANK() OVER(PARTITION BY student_id ORDER BY score DESC) as rnk,
        ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rn
    FROM exam_results
) e
WHERE rnk = 1 and rn = 1