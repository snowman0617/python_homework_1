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

from db import get_connection
from pathlib import Path
import pandas as pd

OUTPUT_CSV = Path("output") / "practice-02" / "waste_report.csv"



SQL = ('''select s.store_name, p.product_name, p.price, w.cups, w.reason from waste_log as w
join stores as s on w.store_id = s.store_id
join products as p on  w.product_id = p.product_id''')

with get_connection() as gc:
    df = pd.read_sql(SQL, gc)

df["loss"] = df["cups"] * df["price"]
reason_groupby = df.groupby("reason", as_index=False)
reason_loss = reason_groupby["loss"].sum()
reason_loss = reason_loss.rename(columns={"loss": "total_loss"})
print("="*10,"報廢原因", "="*10)
print (reason_loss)

store_groupby = df.groupby("store_name", as_index=False)
store_loss = store_groupby["loss"].sum()
store_loss = store_loss.rename(columns={"loss": "total_loss"})
print("="*10,"各店報廢損失", "="*10)
print (store_loss)

mistake_df = df[df["reason"] == "做錯"]
mis_store_groupby = mistake_df.groupby("store_name", as_index=False)
mis_store_loss = mis_store_groupby["loss"].sum()
mis_store_loss = mis_store_loss.rename(columns={"loss": "mistake_loss"})
print("="*10,"各店做錯損失", "="*10)
print (mis_store_loss)

store_merge = pd.merge(store_loss, mis_store_loss, on = "store_name")
store_merge["mistake_share"] = (store_merge["mistake_loss"]/store_merge["total_loss"]).round(2)
store_merge = store_merge.sort_values("mistake_share", ascending=False)
print("="*10,"總表", "="*10)
print (store_merge)

OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
store_merge.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")