-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

WITH RECURSIVE CTE (N) AS (
    SELECT 0

    UNION ALL

    SELECT N + 1 FROM CTE
    WHERE N < 23
)
SELECT N AS HOUR, COUNT(A.ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS A RIGHT JOIN CTE C
ON HOUR(A.DATETIME) = C.N
GROUP BY N
ORDER BY 1 ASC;
