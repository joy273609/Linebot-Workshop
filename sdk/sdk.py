from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    ShowLoadingAnimationRequest
)
import os

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))

with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)
    line_bot_blob_api = MessagingApiBlob(api_client)

    # =============================== 取得使用者資訊 ===============================
    # 取得使用者資訊(傳入使用者ID)
    line_bot_api.get_profile('Uxxxxxxxxxx')
    # 取得群組成員資訊(傳入群組ID、使用者ID)
    line_bot_api.get_group_member_profile('Gxxxxxxxxxx', 'Uxxxxxxxxxx')

    # ================================= Rich Menu =================================
    # 取得所有圖文選單
    line_bot_api.get_rich_menu_list()
    # 取得default圖文選單ID
    line_bot_api.get_default_rich_menu_id()
    # 取得指定圖文選單(傳入圖文選單ID)
    line_bot_api.get_rich_menu('richmenu-xxxxxx')
    # 取得指定圖文選單別名(傳入圖文選單別名ID)
    line_bot_api.get_rich_menu_alias('richmenu-alias-xxxxxx')
    # 取得所有圖文選單別名
    line_bot_api.get_rich_menu_alias_list()
    # 取得指定圖文選單的圖片(傳入圖文選單ID)
    line_bot_blob_api.get_rich_menu_image('richmenu-xxxxxx')

    # 刪除default圖文選單
    line_bot_api.cancel_default_rich_menu()
    # 刪除指定圖文選單(傳入圖文選單ID)
    line_bot_api.delete_rich_menu('richmenu-xxxxxx')
    # 刪除指定圖文選單別名(傳入圖文選單別名ID)
    line_bot_api.delete_rich_menu_alias('richmenu-alias-xxxxxx')

    # ================================ 顯示等待動畫 ================================
    line_bot_api.show_loading_animation(
        ShowLoadingAnimationRequest(
            chatId=event.source.user_id, # user id
            loadingSeconds=5 # 顯示等待動畫的秒數(5~60秒 每5秒為單位 預設為20秒)
        )
    )