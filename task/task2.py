'''
# 任務二：存入資料庫

## 步驟一：建立資料表
在 SQL Editor 自己撰寫 `CREATE TABLE`，建立 `waste_log` 資料表：
| 欄位 | 型別 | 約束 |
| --- | --- | --- |
| waste_id | text | 主鍵 |
| waste_date | date | 不可空值 |
| store_id | integer | 不可空值；參照 `stores(store_id)` |
| product_id | integer | 不可空值；參照 `products(product_id)` |
| cups | integer | 不可空值；必須大於 0 |
| reason | text | 不可空值；只能是「過期」「做錯」「客退」 |

## 步驟二：寫入資料
建立 `practice-02/task2.py`：
1. 以 `csv.DictReader` 讀入任務一的 `output/practice-02/waste_clean.csv`。
2. 把每一筆整理成參數 Tuple，放進 List。
3. 以參數化的 `INSERT` 搭配 `executemany()` 寫入，並加上 `ON CONFLICT (waste_id) DO NOTHING`。
4. 寫入後查詢資料表的筆數並印出。

## 步驟三：以 SQL 查詢損失
在 SQL Editor 撰寫一句查詢：JOIN `stores` 與 `products`，依門市分組，列出各門市的報廢杯數合計與損失金額合計（杯數 × 售價），依損失金額由高到低排序。

**參考**：練習一的任務二；PostgreSQL 課程第 4、6 單元。
**驗收**
- `task2.py` 印出「資料表筆數： 79」；再執行一次仍是 79。
- 四家門市的損失金額合計為 8,070 元。
'''