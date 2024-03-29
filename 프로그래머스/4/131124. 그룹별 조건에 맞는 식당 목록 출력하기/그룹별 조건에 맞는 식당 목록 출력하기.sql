# # SELECT
# #     A.MEMBER_NAME, B.REVIEW_TEXT,DATE_FORMAT(B.REVIEW_DATE,"%Y-%m-%d") AS REVIEW_DATE
# # FROM 
# #     MEMBER_PROFILE A
# #     JOIN
# #     REST_REVIEW B
# #     ON A.MEMBER_ID = B.MEMBER_ID
# # WHERE
# #     A.MEMBER_ID IN
# #             (SELECT 
# #             MEMBER_ID
# #         FROM 
# #             REST_REVIEW
# #         GROUP BY 
# #             MEMBER_ID
# #         ORDER BY 
# #             COUNT(*) DESC
# #         LIMIT 1) AS TEMP
# # ORDER BY
# #     B.REVIEW_DATE ASC,
# #     B.REVIEW_TEXT ASC

# # 리뷰를 가장 많이 작성한 회원 ID 찾는 테이블 만들기

# SELECT
#     A.MEMBER_NAME,
#     B.REVIEW_TEXT,
#     DATE_FORMAT(B.REVIEW_DATE,"%Y-%m-%d") AS REVIEW_DATE
# FROM
#     MEMBER_PROFILE A
#     JOIN
#     REST_REVIEW B
#     ON A.MEMBER_ID = B.MEMBER_ID
# WHERE
#     A.MEMBER_ID 
#     =
#         (SELECT 
#             MEMBER_ID
#         FROM 
#             REST_REVIEW
#         GROUP BY
#             MEMBER_ID
#         ORDER BY
#             COUNT(*) DESC
#         LIMIT 1)
# ORDER BY
#     REVIEW_DATE ASC,
#     REVIEW_TEXT ASC


# MEMBER : 고객 정보
# REVIEW : 식당의 리뷰 정보
# 테이블 조인, 그룹바이로 멤버 기준 해서 SUM으로 뽑고 ORDER BY 정렬 후 LIMIT 1한 그 회원

SELECT A.MEMBER_NAME, B.REVIEW_TEXT, DATE_FORMAT(B.REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
FROM 
    MEMBER_PROFILE AS A
    JOIN
    REST_REVIEW AS B
    ON
    A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID =
                (SELECT MEMBER_ID 
                FROM REST_REVIEW
                GROUP BY MEMBER_ID
                ORDER BY COUNT(*) DESC
                LIMIT 1)
ORDER BY
    B.REVIEW_DATE ASC,
    B.REVIEW_TEXT ASC

