-- FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.

SELECT P.PRODUCT_ID, P.PRODUCT_NAME, P.PRICE * SUM(O.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT P INNER JOIN FOOD_ORDER O
USING (PRODUCT_ID)
WHERE O.PRODUCE_DATE LIKE "2022-05%"
GROUP BY P.PRODUCT_ID
ORDER BY 3 DESC, 1 ASC;