'''
任務一：讀取與清理

建立 `practice-02/task1.py`，完成以下步驟：
1. 以 `csv.DictReader` 讀入 `data/waste_log.csv`。
2. 寫一個函式 `clean_row(row)`，整理一筆資料：
    - 杯數空白時回傳 `None`，表示這筆不要。
    - 否則回傳整理好的 Dictionary：`store_id`、`product_id`、`cups` 轉成整數，`reason` 去除前後空白。
3. 以迴圈逐筆呼叫 `clean_row()`，把不是 `None` 的結果放進 List。
4. 以 Dictionary 統計各報廢原因的筆數與杯數合計，印出結果。
5. 以 `csv.DictWriter` 輸出 `output/practice-02/waste_clean.csv`，編碼使用 `utf-8`。
**參考**：練習一的任務一；第 1 單元第四節；第 2 單元第四節。
**驗收**
- 原始 84 筆，清理後 79 筆。
- 印出的報廢原因只有「過期」「做錯」「客退」三種，沒有前面帶空白的重複類別。
'''
