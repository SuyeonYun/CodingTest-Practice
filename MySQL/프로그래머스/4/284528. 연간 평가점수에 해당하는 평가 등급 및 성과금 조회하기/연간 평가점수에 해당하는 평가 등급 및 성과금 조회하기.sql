-- 코드를 작성해주세요
WITH 
    GRADE_T AS (
    SELECT 
        E.EMP_NO, 
        E.EMP_NAME,
        E.SAL,
        CASE 1
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C' 
        END AS GRADE
    FROM HR_GRADE G RIGHT JOIN HR_EMPLOYEES E
    USING (EMP_NO)
    GROUP BY EMP_NO
)
SELECT 
    EMP_NO, EMP_NAME, GRADE,
    CASE 1
        WHEN GRADE = 'S' THEN SAL * 0.2
        WHEN GRADE = 'A' THEN SAL * 0.15
        WHEN GRADE = 'B' THEN SAL * 0.1
        ELSE 0 
    END AS BONUS
FROM GRADE_T
ORDER BY 1 ASC;
