'''
# 任務三：分析與報表(選項）
建立 `practice-02/task3.py`：
1. 以 `pd.read_sql()` 讀取資料：JOIN `waste_log`、`stores`、`products`，取出門市名稱、品項名稱、售價、杯數、報廢原因。
2. 新增損失金額欄位 `loss`：杯數 × 售價。
3. 以 `groupby` 印出各報廢原因的損失金額。
4. 產生門市報表：
    - 依門市分組，算出損失金額合計，欄名改為 `total_loss`。
    - 先篩選出原因是「做錯」的紀錄，再依門市分組算出損失金額，欄名改為 `mistake_loss`。
    - 以門市名稱合併兩張表。
    - 新增 `mistake_share` 欄位：`mistake_loss` ÷ `total_loss`，取到小數第二位。
    - 依 `mistake_share` 由高到低排序。
5. 以 `to_csv()` 輸出 `output/practice-02/waste_report.csv`。

**參考**：練習一的任務三；第 5 單元第三、四節（`groupby`、`rename`、`merge`）。

**驗收**
- `waste_report.csv` 有 4 列，每家門市一列。
- `total_loss` 的合計與任務二的 SQL 查詢結果相同。
- 觀察：損失金額最高的門市，是不是「做錯」比例最高的門市？
'''