from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    RichMenuRequest
)
import requests
import os

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))

with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)
    line_bot_blob_api = MessagingApiBlob(api_client)

    # Step 1. 創建圖文選單(圖文選單的大小、名稱、聊天室的文字、按鈕的區域)
    rich_menu_str = """{
        "size": {
            "width": 2500,
            "height": 1686
        },
        "selected": true,
        "name": "圖文選單 1",
        "chatBarText": "查看更多資訊",
        "areas": [
            {
                "bounds": {
                    "x": 0,
                    "y": 0,
                    "width": 833,
                    "height": 843
                },
                "action": {
                    "type": "message",
                    "text": "A"
                }
            },
            {
                "bounds": {
                    "x": 834,
                    "y": 0,
                    "width": 833,
                    "height": 843
                },
                "action": {
                    "type": "message",
                    "text": "B"
                }
            },
            {
                "bounds": {
                    "x": 1663,
                    "y": 0,
                    "width": 834,
                    "height": 843
                },
                "action": {
                    "type": "message",
                    "text": "C"
                }
            },
            {
                "bounds": {
                    "x": 0,
                    "y": 843,
                    "width": 833,
                    "height": 843
                },
                "action": {
                    "type": "message",
                    "text": "D"
                }
            },
            {
                "bounds": {
                    "x": 834,
                    "y": 843,
                    "width": 833,
                    "height": 843
                },
                "action": {
                    "type": "message",
                    "text": "E"
                }
            },
            {
                "bounds": {
                    "x": 1662,
                    "y": 843,
                    "width": 838,
                    "height": 843
                },
                "action": {
                    "type": "message",
                    "text": "F"
                }
            }
        ]
    }"""
    # 創建的時候會回傳 rich_menu_id
    rich_menu_id = line_bot_api.create_rich_menu(
        rich_menu_request=RichMenuRequest.from_json(rich_menu_str)
    ).rich_menu_id

    # Step 2. 設定 Rich Menu 的圖片
    # 方式一: 使用 URL
    rich_menu_url = "https://example.com/richmenu.png"
    response = requests.get(rich_menu_url)
    line_bot_blob_api.set_rich_menu_image(
        rich_menu_id=rich_menu_id,
        body=response.content,
        _headers={'Content-Type': 'image/png'}
    )

    # 方式二: 使用本地端的圖片
    with open('./static/richmenu.png', 'rb') as image:
        line_bot_blob_api.set_rich_menu_image(
            rich_menu_id=rich_menu_id,
            body=bytearray(image.read()),
            _headers={'Content-Type': 'image/png'}
        )

    # Step3. 設定預設的圖文選單
    line_bot_api.set_default_rich_menu(rich_menu_id)