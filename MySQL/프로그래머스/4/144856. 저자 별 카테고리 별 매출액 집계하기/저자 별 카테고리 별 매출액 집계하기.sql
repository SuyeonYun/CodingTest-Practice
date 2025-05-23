-- 코드를 입력하세요
SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(B.PRICE * S.SALES) AS TOTAL_SALES
FROM BOOK_SALES S LEFT JOIN BOOK B
USING(BOOK_ID) LEFT JOIN AUTHOR A
USING(AUTHOR_ID)
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC;