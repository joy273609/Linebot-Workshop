from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    RichMenuRequest,
    CreateRichMenuAliasRequest
)
import requests
import os

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))

with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)
    line_bot_blob_api = MessagingApiBlob(api_client)

    # Step 1. 創建圖文選單(圖文選單的大小、名稱、聊天室的文字、按鈕的區域)
    # 若要可以切換圖文選單，需要在 action 中加入 richmenuswitch
    # richMenuAliasId:要切換的圖文選單的ID data:按鈕被點擊時送出的資料
    """
    "action": {
        "type": "richmenuswitch",
        "richMenuAliasId": "richmenu_b",
        "data": "richmenu-changed-to-b"
    }
    """
    # ============================== 創建圖文選單a ==============================
    # 這邊就要把其中一個區域的 action 改成 richmenuswitch 並且指定b的別名ID
    rich_menu_a_str = """{
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
                    "type": "richmenuswitch",
                    "richMenuAliasId": "richmenu_b",
                    "data": "richmenu-changed-to-b"
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
    rich_menu_a_id = line_bot_api.create_rich_menu(
        rich_menu_request=RichMenuRequest.from_json(rich_menu_a_str)
    ).rich_menu_id

    # Step 2. 設定 Rich Menu 的圖片
    # 方式一: 使用 URL
    rich_menu_a_url = "https://example.com/richmenu1.png"
    response = requests.get(rich_menu_a_url)
    line_bot_blob_api.set_rich_menu_image(
        rich_menu_id=rich_menu_a_id,
        body=response.content,
        _headers={'Content-Type': 'image/png'}
    )

    # 方式二: 使用本地端的圖片
    with open('./static/richmenu_a.png', 'rb') as image:
        line_bot_blob_api.set_rich_menu_image(
            rich_menu_id=rich_menu_a_id,
            body=bytearray(image.read()),
            _headers={'Content-Type': 'image/png'}
        )

    # Step 3. 將a設定為預設的圖文選單
    line_bot_api.set_default_rich_menu(rich_menu_a_id)

    # Step 4. 設定圖文選單的別名ID
    line_bot_api.create_rich_menu_alias(
        CreateRichMenuAliasRequest(
            rich_menu_alias_id="richmenu_a", # 想要設定的別名ID
            rich_menu_id=rich_menu_a_id # 要設定的圖文選單ID
        )
    )

    # ============================== 創建圖文選單b ==============================
    # 這邊就要把其中一個區域的 action 改成 richmenuswitch 並且指定a的別名ID
    rich_menu_b_str = """{
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
                    "type": "richmenuswitch",
                    "richMenuAliasId": "richmenu_a",
                    "data": "richmenu-changed-to-a"
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
    rich_menu_b_id = line_bot_api.create_rich_menu(
        rich_menu_request=RichMenuRequest.from_json(rich_menu_b_str)
    ).rich_menu_id

    # Step 2. 設定 Rich Menu 的圖片
    # 方式一: 使用 URL
    rich_menu_b_url = "https://example.com/richmenu2.png"
    response = requests.get(rich_menu_b_url)
    line_bot_blob_api.set_rich_menu_image(
        rich_menu_id=rich_menu_b_id,
        body=response.content,
        _headers={'Content-Type': 'image/png'}
    )

    # 方式二: 使用本地端的圖片
    with open('./static/richmenu2.png', 'rb') as image:
        line_bot_blob_api.set_rich_menu_image(
            rich_menu_id=rich_menu_b_id,
            body=bytearray(image.read()),
            _headers={'Content-Type': 'image/png'}
        )

    # Step 3. 因為已經將a設定為預設的圖文選單，所以這邊不用再設定
    # line_bot_api.set_default_rich_menu(rich_menu_b_id)

    # Step 4. 設定圖文選單的別名ID
    line_bot_api.create_rich_menu_alias(
        CreateRichMenuAliasRequest(
            rich_menu_alias_id="richmenu_b", # 想要設定的別名ID
            rich_menu_id=rich_menu_b_id # 要設定的圖文選單ID
        )
    )

    # 查詢rich menu / 別名
    # richmenu_list = line_bot_api.get_rich_menu_list()
    # richmenu_alias_list = line_bot_api.get_rich_menu_alias_list()
    # for rich_menu in richmenu_list.richmenus:
    #     print(rich_menu.rich_menu_id)

    # 刪除所有rich menu
    # for rich_menu in richmenu_alias_list.aliases:
    #     line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
    #     line_bot_api.delete_rich_menu_alias(rich_menu.rich_menu_alias_id)
