import pygsheets
import os

# 建立google cloud憑證
gc = pygsheets.authorize(service_account_env_var='GDRIVE_API_CREDENTIALS')
# 連結試算表
sh = gc.open_by_url(os.getenv("SPREADSHEET_URL"))

# 取得工作表
wks = sh.worksheet_by_title("sheet1")

#-----新增-----
# 新增一列資料
# wks.append_table(values=["name", "country", "place"])
wks.append_table(values=["a", "b", "c"])


#-----修改-----
# # 更新單一儲存格
# wks.update_value('A5', 'Hello World!')
# # 更新多個儲存格(row)
# wks.update_values('A5:C5', [['Hello', 'World', '!']])
# # 更新多個儲存格(column)
# wks.update_values('E2:E4', [['Hello'],['World'],['!']])

#-----刪除-----
# 刪除一列(row)資料
# wks.delete_rows(1)

#-----取得-----
# 取得整列(row)
# row = wks.get_row(1)
# print(row)

# 取得所有資料
data = wks.get_all_records()
print(data)

# # 取得單一儲存格
# cell = wks.get_value('A1')
# print(cell)

# # 取得多個儲存格
# cells = wks.get_values('A1', 'C1')
# print(cells)