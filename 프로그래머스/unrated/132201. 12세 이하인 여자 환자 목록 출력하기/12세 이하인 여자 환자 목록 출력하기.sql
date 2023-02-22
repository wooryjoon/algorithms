-- 코드를 입력하세요
# 12세 이하, 여자
# 전화번호가 없는 경우 NULL로 출력
# 결과는 나이 기준 오름차순, 그다음으로는 환자이름 오름차순
SELECT PT_NAME,PT_NO, GEND_CD, AGE,IFNULL(TLNO,'NONE') AS TLNO
FROM PATIENT
WHERE AGE <=12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC