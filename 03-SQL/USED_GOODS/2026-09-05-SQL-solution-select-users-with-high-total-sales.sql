-- ==============================================================
-- ■ 문제 요약
-- 거래 상태가 완료(STATUS = 'DONE')된 중고 거래 건만 필터링한 뒤
-- 회원별 총거래금액을 GROUP BY와 HAVING 절로 집계하여 70만 원 이상인 회원의 ID, 닉네임, 총거래금액을 추출하고 오름차순 정렬
-- ==============================================================

SELECT u.user_id, u.nickname, SUM(b.price) AS "TOTAL_SALES"
FROM used_goods_board b JOIN used_goods_user u
ON b.writer_id = u.user_id
-- 거래 완료된 게시물만을 GROUP BY 전에 필터링
WHERE b.status = 'DONE'
GROUP BY u.user_id, u.nickname
HAVING SUM(b.price) >= 700000
ORDER BY SUM(b.price) ASC;

-- ==============================================================
-- ■ 배운점
-- SUM() 함수는 특정 컬럼의 전체 합계를 구할 때 사용한다
-- 컬럼 내 NULL값은 자동으로 제외하고 합산, GROUP BY절과 함께 사용하면 그룹별 합계를 구할 수 있다
-- ==============================================================