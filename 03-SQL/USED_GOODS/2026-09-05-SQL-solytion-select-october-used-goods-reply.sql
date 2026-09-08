-- ==============================================================
-- ■ 문제 요약
-- 댓글 작성일이 아닌 게시글 작성일을 기준으로 2022년 10월 데이터를 필터링하고 두 테이블을 INNER JOIN한 뒤, 
-- 댓글 작성일을 YYYY-MM-DD 포맷으로 변환하여 댓글 작성일과 게시글 제목 순으로 각각 오름차순 정렬
-- ==============================================================

SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, 
       TO_CHAR(r.created_date, 'YYYY-MM-DD') AS "CREATED_DATE"
FROM used_goods_board b JOIN used_goods_reply r
ON b.board_id = r.board_id
WHERE TO_CHAR(r.created_date, 'YYYY-MM') = '2022-10'
ORDER BY r.created_date ASC, b.title ASC;

-- ==============================================================
-- ■ 배운점
-- 날짜 형식을 변환할 때에는 CONCAT이 아닌, TO_CHAR를 사용해야한다.
-- (CONCAT은 글자를 뒤에 이어붙이는 함수)
-- ==============================================================