# [SQL]

> **一行要約: SQL（Structured Query Language）は、データベースに対して目的のデータを絞り込んで取得するために「問い合わせ」を行う言語です**

---

## 1.コア概念
* **[SQL]: SQLは大きく5つに分類され、DQL、DML、DDL、DCL、TCLとして定義されます。** 

| 区分 | 意味 | 機能 | コマンド |
| :--- | :--- | :--- | :--- |
| **DQL** | データ問い合わせ言語 | データの照会 | SELECT |
| **DML** | データ操作言語 | データの追加・更新・削除 | INSERT、UPDATE、DELETE |
| **DDL** | データ定義言語 | テーブル構造の作成・変更・削除 | CREATE、ALTER、DROP、TRUNCATE |
| **DCL** | データ制御言語 | 権限の付与・剥奪 | GRANT、REVOKE |
| **TCL** | トランザクション制御言語 | 処理（トランザクション）の確定・取消 | COMMIT、ROLLBACK、SAVEPOINT |

<br>

## 2.DQLのコード例
```sql
SELECT id, user_name, email, age
FROM users
WHERE age >= 20
ORDER BY id DESC;
```

<br>

## 3.DMLのコード例


### INSERT - データの追加
```sql
INSERT INTO users (id, user_name, age)
VALUES (hello_world, sungsu, 20);
```

### UPDATE - データの更新
```sql
UPDATE users
SET age = 22
WHERE user_name = 'sungsu';
```

### DELETE - データの削除
```sql
DELETE FROM users
WHERE user_name = 'sungsu';
```

<br>

## 4.DDLのコード例
**DDLは実行時にAutoCommitされ、それ以前に実行されたSQL文も自動的にコミットされます。**



### CREATE - テーブルの作成
```sql
CREATE TABLE dept_basic (
    dept_id NUMBER CONSTRAINT pk_dept_id PRIMARY KEY,
    dept_name VARCHAR2(50) CONSTRAINT nn_dept_name NOT NULL
);
```

### ALTER - テーブルの変更
```sql
-- カラムの追加
ALTER TABLE dept_basic
ADD (location VARCHAR(100));

-- カラムの変更
ALTER TABLE dept_basic
MODIFY (dept_name VARCHAR2(100));

-- カラムの削除
ALTER TABLE dept_basic
DROP COLUMN location;
```

### DROP - テーブルの削除
```sql
DROP TABLE dept_basic;
```

### TRUNCATE - テーブル内データの全削除
```sql
TRUNCATE TABLE dept_basic;
```

<br>

## 5.DCLのコード例


### GRANT - 権限の付与
```sql
GRANT SELECT, INSERT, UPDATE ON dept_basic TO sungsu;

GRANT ALL PRIVILEGES ON dept_basic TO sungsu;
```

### REVOKE - 権限の剥奪
```sql
REVOKE INSERT ON dept_basic FROM sungsu;

REVOKE ALL PRIVILEGES ON dapt_basic FROM sungsu;
```

<br>

## 6.TCLのコード例


### COMMIT
```sql
-- これまでに実行したDMLの操作内容をデータベースに永久確定します。
INSERT INTO dept_basic (dept_id, dept_name) VALUE (102, 'dongmin');
COMMIT;
```

### ROLLBACK
```sql
-- 最後にCOMMITした時点以降に実行したすべてのDML操作を取り消し、元の状態に戻します。
DELETE FROM dept_basic;
ROLLBACK;
```

### SAVEPOINT
```sql
-- 復元先となるポイントを作成しておく機能です。
INSERT INTO dept_basic (dept_id, dept_name) VALUE (102, 'dongmin');
SAVEPOINT point1;

DELETE FROM dept_basic WHERE dept_id = 102;

ROLLBACK TO point1;
```