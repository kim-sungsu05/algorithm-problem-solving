# Table: [ANIMAL_INS]

動物保護施設に入った動物の情報を管理するテーブルです。

### Schema

| Column Name | Data Type | Nullable | Constraint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **ANIMAL_ID** | VARCHAR(N) | FALSE | PK | 動物のID |
| **ANIMAL_TYPE** | VARCHAR(N) | FALSE | - | 生物種 |
| **DATETIME** | DATETIME | FALSE | - | 保護開始日 |
| **INTAKE_CONDITION** | VARCHAR(N) | FALSE | - | 保護開始時の状態 |
| **NAME** | VARCHAR(N) | TRUE | - | 名前 |
| **SEX_UPON_INTAKE** | VARCHAR(N) | FALSE | - | 性別および不妊手術の有無 |

---

### 解いた問題リスト

#### 1. 動物の数の照会 (Level 2)
* **問題の出典**: [Programmers - 動物の数の照会](https://school.programmers.co.kr/learn/courses/30/lessons/59406)
* **解答ファイルへ移動**: [SQL-solution-count-animals.sql](./2026-09-09-SQL-solution-count-animals.sql)
* **主要キーワード**: `COUNT`

#### 2. 同名動物数探し (Level 2)
* **問題の出典**: [Programmers - 同名動物数探し](https://school.programmers.co.kr/learn/courses/30/lessons/59041?language=oracle)
* **解答ファイルへ移動**: [QL_solution_duplicate_animal_names.sql](./2026-09-18-SQL_solution_duplicate_animal_names.sql)
* **主要キーワード**: `GROUP BY`