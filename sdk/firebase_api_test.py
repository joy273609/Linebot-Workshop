import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json
from datetime import datetime

#------初始化Firebase------
# 建立憑證
cred = credentials.Certificate(json.loads(os.getenv('FIREBASE_CREDENTIALS')))
# 初始化
firebase_admin.initialize_app(cred)
db = firestore.client()

# 提示使用者輸入資料
pet_name = input("請輸入寵物名稱: ")
visit_date_input = input("請輸入回診日期 (YYYY-MM-DD): ")
kg_input = input("請輸入體重 (kg): ")
crea_input = input("請輸入CREA值: ")
bun_input = input("請輸入BUN值: ")

# 取得collection的reference
doc_ref = db.collection('test').document('doc')

visit_date = datetime.strptime(visit_date_input,'%Y-%m-%d')
# 新增資料
doc_ref.set({
    'pet name': pet_name,
    'date': visit_date,
    'kg': float(kg_input),  # 轉換為數字
    'CREA': float(crea_input),
    'BUN': float(bun_input),
})

# # 更新資料
# doc_ref.update({
#     'population': 10000000
# })

# # 取得collection所有資料
# docs = db.collection('test').stream()
# print([doc.to_dict() for doc in docs])

# # 取得document資料
# doc = doc_ref.get()
# print(doc.to_dict())

# # 刪除資料
# doc_ref.delete()