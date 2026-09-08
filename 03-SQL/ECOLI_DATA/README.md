# Table: [ECOLI_DATA]

実験室で培養した大腸菌個体の分化情報、親子関係、形質およびサイズデータを管理するテーブルです。

### Schema

| Column Name | Data Type | Nullable | Constraint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **ID** | INTEGER | FALSE | PK | 大腸菌個体ID |
| **PARENT_ID** | INTEGER |TRUE | FK (Self Referencing), 最初の個体はNULL | 親個体ID |
| **SIZE_OF_COLONY** | INTEGER | FALSE | - | 個体のサイズ |
| **DIFFERENTIATION_DATE** | DATE | FALSE | - | 分化した日付 |
| **GENOTYPE** | INTEGER | FALSE | - | 個体の形質 |

---

### 解いた問題リスト

#### 1. 大腸菌のサイズに応じた分類 1 (Level 3)
* **問題の出典**: [Programmers - 大腸菌のサイズに応じた分類 1](https://school.programmers.co.kr/learn/courses/30/lessons/299307)
* **解答ファイルへ移動**: [SQL-solution-categorizing-e-coli-by-size-1.sql](./2026-09-01-SQL-solution-categorizing-e-coli-by-size-1.sql)
* **主要キーワード**: `CASE`

#### 2. 四半期ごとに分化した大腸菌の個体数を求める (Level 2)
* **問題の出典**: [Programmers - 大腸菌のサイズに応じた分類 1](https://school.programmers.co.kr/learn/courses/30/lessons/299308)
* **解答ファイルへ移動**: [SQL-solution-categorizing-e-coli-by-size-1.sql](./2026-09-02-SQL-solution-quarterly-ecoli-count.sql)
* **主要キーワード**: `CONCAT`