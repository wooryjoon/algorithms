-- 코드를 입력하세요
# 2021년 인문, 
# ID와 출판일 출력
SELECT BOOK_ID,DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d')
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021 AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE ASC