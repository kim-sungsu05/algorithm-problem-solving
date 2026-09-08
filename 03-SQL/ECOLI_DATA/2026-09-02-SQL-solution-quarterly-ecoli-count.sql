-- ==============================================================
-- ■ 문제 요약
-- 이 문제는 대장균 분화 날짜(DIFFERENTIATION_DATE)에서 분기를 추출하여 '1Q', '2Q' 형태로 출력하고,
-- 각 분기별 총 개체 수를 집계해 오름차순으로 정렬
-- ==============================================================

SELECT 
    TO_CHAR(differentiation_date, 'Q') || 'Q' AS QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM ecoli_data
GROUP BY TO_CHAR(differentiation_date, 'Q')
ORDER BY QUARTER ASC;