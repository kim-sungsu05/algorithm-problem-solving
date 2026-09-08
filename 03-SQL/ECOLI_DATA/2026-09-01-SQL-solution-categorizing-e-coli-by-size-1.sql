-- ==============================================================
-- ■ 문제 요약
-- 대장균의 크기(SIZE_OF_COLONY)에 따라 100 이하는 'LOW', 
-- 100 초과 1000 이하는 'MEDIUM', 1000 초과는 'HIGH'로 라벨을 붙인 뒤, 
-- 개체 ID(ID)와 크기 분류(SIZE) 두 컬럼을 ID 기준 오름차순으로 정렬하여 출력
-- ==============================================================

SELECT id,
    CASE
        WHEN size_of_colony <= 100 THEN 'LOW'
        WHEN size_of_colony > 1000 THEN 'HIGH'
        ELSE 'MEDIUM'
    END AS SIZE
FROM ecoli_data
ORDER BY id ASC;