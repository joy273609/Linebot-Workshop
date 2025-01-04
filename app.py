from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    PushMessageRequest,
    TextMessage,
    Emoji,
    QuickReply,
    QuickReplyItem,
    MessageAction,
    PostbackAction,
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    FollowEvent,
    PostbackEvent,
)
import os
import re

app = Flask(__name__)

# 設定帳號資訊
configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

# #新增PUSH API 功能，放在最外層表示程式會直接執行，而非觸發事件
# with ApiClient(configuration) as api_client:
#     line_bot_api = MessagingApi(api_client)
#     res = line_bot_api.push_message_with_http_info(
#         PushMessageRequest(
#             to='U5a4fe94effdd1aab6dd6a6b6101647da', # user id
#             messages=[TextMessage(text='Push message')]
#         )
#     )

#設定主頁內容
# @app.route("/",methods=['GET'])
# def home():
#     return "success"

#原始內容，讓line伺服器可以進行驗證及連結
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

###############以下為觸發事件###############
### 處理ReplyMessage
# Echo Bot
# @line_handler.add(MessageEvent, message=TextMessageContent)
# def handle_message(event):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text=event.message.text)]
#             )
#         )

# 設定自動回覆
# @line_handler.add(MessageEvent, message=TextMessageContent)
# def handle_message(event):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text='$ 這是自動回覆 $',
#                                       emojis=[
#                                         Emoji(index=0, product_id="670e0cce840a8236ddd4ee4c", emoji_id="115"),
#                                         Emoji(index=11, product_id="670e0cce840a8236ddd4ee4c", emoji_id="117") ])]
#             ))
        
# 設定自動+快速回覆
# @line_handler.add(MessageEvent, message=TextMessageContent)
# def handle_quick_message(event):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text="$ 這是快速回覆 $", 
#                                     emojis=[
#                                         Emoji(index=0, product_id="670e0cce840a8236ddd4ee4c", emoji_id="115"),
#                                         Emoji(index=9, product_id="670e0cce840a8236ddd4ee4c", emoji_id="117") ],
#                                     quickReply=
#                                     QuickReply(items=[
#                                         QuickReplyItem(action=MessageAction(label="Say hello", text="Hello"))]
#                                                         )
#                                     )
                                    
#                         ]
#             ))       

# #設定PostbackAction
# # label:按鈕上顯示的文字 data:按鈕被點擊時送出的資料 displayText:按鈕被點擊時顯示在聊天室的文字
# # inputOption:另外的action(closeRichMenu:關閉圖文選單, openRichMenu:開啟圖文選單, openKeyboard:開啟鍵盤, openVoice:開啟語音輸入)
# # fillInText:幫使用者在鍵盤輸入框填入文字(只有在openKeyboard時才有用)
# @line_handler.add(MessageEvent, message=TextMessageContent)
# def handle_quick_message(event):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)
#         line_bot_api.reply_message_with_http_info(
#             ReplyMessageRequest(
#                 reply_token=event.reply_token,
#                 messages=[TextMessage(text="請選擇動作", 
#                                     quickReply=
#                                     QuickReply(items=[
#                                         QuickReplyItem(action=PostbackAction(label="新增就診資料", data="action=buy&itemid=123", displayText="請輸入就診資料", 
#                                                                              inputOption="openKeyboard", 
#                                                                              fillInText="---\nName: \nPhone: \nBirthday: \n---")
#                                                                              ),
#                                         QuickReplyItem(action=PostbackAction(label="查詢就診資料", data="action=buy&itemid=123", 
#                                                                              displayText="Buy", inputOption="openKeyboard", 
#                                                                              fillInText="---\nName: \nPhone: \nBirthday: \n---")
#                                                                              )
#                                                     ]
#                                                         )
#                                     )
                                    
#                         ]
#             ))      

# @line_handler.add(PostbackEvent)
# def handle_postback(event):
#     postback_data = event.source.data

@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_quick_message(event):
   
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        event_message = event.message.text

        #正規表達
        pattern = r"寵物名稱:.*看診日期:.*體重:.*腎指數:.*血壓:.*"

        if event_message == "新增看診紀錄":
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="請複製公版訊息進行下一步"),
                            TextMessage(text="新增: \n寵物名稱: \n看診日期: \n體重: \n腎指數: \n血壓:",
                                        )        
                            ]))

        elif  event_message == "查詢看診紀錄":
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="請選填想查詢的資料"),
                            TextMessage(text="查詢: \n寵物名稱: \n看診日期: \n體重: \n腎指數: \n血壓:")     
                            ]))
                
        elif re.search(pattern, event_message):
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="查詢中，請稍候...")]
                ))

# 處理followEvent
@line_handler.add(FollowEvent)
def handle_follow_test(event):
    app.logger.info("only in terminal : 歡迎使用看診小幫手")

@line_handler.add(FollowEvent)
def handle_follow(event):
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                                    reply_token=event.reply_token,
                                    messages=[TextMessage(
                                                text='$ 歡迎使用看診小幫手 $',
                                                emojis=[
                                                    Emoji(index=0, product_id="670e0cce840a8236ddd4ee4c", emoji_id="115"),
                                                    Emoji(index=12, product_id="670e0cce840a8236ddd4ee4c", emoji_id="117")],
                                                        )
                                            ]
                                    )
                                        )


if __name__ == "__main__":
    app.run()