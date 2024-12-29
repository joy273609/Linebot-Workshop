import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json

cred = credentials.Certificate(json.loads(os.getenv('FIREBASE_CREDENTIALS')))
firebase_admin.initialize_app(cred)
db = firestore.client()

# 取得collection的reference
doc_ref = db.collection('test').document('doc')

# 新增資料
doc_ref.set({
    'name': 'Los Angeles',
    'state': 'CA',
    'country': 'USA'
})

# 更新資料
doc_ref.update({
    'population': 10000000
})

# 取得collection所有資料
docs = db.collection('test').stream()
print([doc.to_dict() for doc in docs])

# 取得document資料
doc = doc_ref.get()
print(doc.to_dict())

# 刪除資料
doc_ref.delete()