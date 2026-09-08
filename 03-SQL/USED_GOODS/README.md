# Table: [USED_GOODS_BOARD]

中古取引掲示板の投稿情報を管理するテーブルです。

### Schema

| Column Name | Data Type | Nullable | Constraint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **BOARD_ID** | VARCHAR(5) | FALSE | PK | 掲示板投稿ID |
| **WRITER_ID** | VARCHAR(50) | FALSE | - | 作成者ID |
| **TITLE** | VARCHAR(100) | FALSE | - | 掲示板投稿タイトル |
| **CONTENTS** | VARCHAR(1000) | FALSE | - | 掲示板投稿内容 |
| **PRICE** | NUMBER | FALSE | - | 価格 |
| **CREATED_DATE** | DATE | FALSE | - | 作成日 |
| **STATUS** | VARCHAR(10) | FALSE | - | 取引状態 |
| **VIEWS** | NUMBER | FALSE | - | 閲覧数 |


<br>

# Table: [USED_GOODS_REPLY]

中古取引掲示板の投稿に対するコメント情報を管理するテーブルです。

### Schema

| Column Name | Data Type | Nullable | Constraint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **REPLY_ID** | VARCHAR(10) | FALSE | PK | コメントID |
| **BOARD_ID** | VARCHAR(5) | FALSE | FK | 掲示板投稿ID |
| **WRITER_ID** | VARCHAR(50) | FALSE | - | 作成者ID |
| **CONTENTS** | VARCHAR(1000) | TRUE | - | コメント内容 |
| **CREATED_DATE** | DATE | FALSE | - | 作成日 |

<br>

# Table: [USED_GOODS_USER]

中古取引ユーザー情報を管理するテーブルです。

### Schema

| Column Name | Data Type | Nullable | Constraint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **USER_ID** | VARCHAR(50) | FALSE | PK | ユーザーID |
| **NICKNAME** | VARCHAR(100) | FALSE | - | ニックネーム |
| **CITY** | VARCHAR(100) | FALSE | - | 市 |
| **STREET_ADDRESS1** | VARCHAR(100) | FALSE | - | 道路名住所 |
| **STREET_ADDRESS2** | VARCHAR(100) | TRUE | - | 詳細住所 |
| **TLNO** | VARCHAR(20) | FALSE | - | 電話番号 |

---

2つのテーブルを結合（ジョイン）する際、一方のテーブルには外部キーを持たせず、もう一方のテーブルにのみ外部キーを設定するのが、データベースにおける外部キーの最も基本的な使い方です。<br>
外部キーの関係は、常に参照される「親テーブル」と、参照する「子テーブル」に役割が分かれます。（現在の中古取引テーブルがその例です。）<br>ですが、リレーションを構築する目的に応じて、外部キーはいくらでも増やすことができます。
* 1つのテーブルに複数の外部キーが存在する場合（複数の情報を同時に参照）
* 2つのテーブル間で外部キーを紐付ける場合（同一のテーブルを異なる目的で2回以上参照）


---

### 解いた問題リスト

#### 1. 条件に合う中古取引コメントの照会 (Level 1)
* **問題の出典**: [Programmers - 条件に合う中古取引コメントの照会](https://school.programmers.co.kr/learn/courses/30/lessons/164673)
* **解答ファイルへ移動**: [SQL-solytion-select-october-used-goods-reply.sql](./2026-09-05-SQL-solytion-select-october-used-goods-reply.sql)
* **主要キーワード**: `TO_CHAR`

#### 2. 条件に合うユーザーと総取引金額の照会 (Level 3)
* **問題の出典**: [Programmers - 条件に合うユーザーと総取引金額の照会](https://school.programmers.co.kr/learn/courses/30/lessons/164668)
* **解答ファイルへ移動**: [SQL-solution-select-users-with-high-total-sales.sql](./2026-09-05-SQL-solution-select-users-with-high-total-sales.sql)
* **主要キーワード**: `GROUP BY`