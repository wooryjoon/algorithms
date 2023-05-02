-- 코드를 입력하세요
-- 상품코드, 매출액 (판매량 * 가격)
SELECT A.PRODUCT_CODE, SUM(A.PRICE * B.SALES_AMOUNT) AS SALES
FROM PRODUCT A 
INNER JOIN OFFLINE_SALE B ON A.PRODUCT_ID = B.PRODUCT_ID
GROUP BY A.PRODUCT_CODE
ORDER BY SALES DESC, A.PRODUCT_CODE ASC

# select p.product_code, sum(p.price * o.sales_amount) as sales
# from product p
# inner join offline_sale o on p.product_id = o.product_id
# group by p.product_code
# order by sales desc, p.product_code asc
# ;