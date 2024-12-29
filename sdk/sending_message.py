from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    PushMessageRequest,
    MulticastRequest,
    BroadcastRequest,
    TextMessage,

    # 要處理例外狀況時需要引入
    ApiException,
    ErrorResponse
)
import os

configuration = Configuration(access_token=os.getenv('CHANNEL_ACCESS_TOKEN'))

with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)
    # line_bot_api.reply_message(
    #     ReplyMessageRequest(
    #         reply_token=event.reply_token,
    #         messages=[TextMessage(text='Reply message')],

    #         #每個訊息都可以設定是否要靜音傳送 預設為 False
    #         notification_disabled=True
    #     )
    # )
    res = line_bot_api.push_message_with_http_info(
        PushMessageRequest(
            to='U4e87142fae6a522e7a4a928eaa65c025', # user id
            messages=[TextMessage(text='Push message')]
        )
    )
    print(res.status_code)
    # line_bot_api.multicast(
    #     MulticastRequest(
    #         to=['Uxxxxxxxxxx', 'Uxxxxxxxxxx'], # 多個 user id
    #         messages=[TextMessage(text='Multicast message')]
    #     )
    # )
    # line_bot_api.broadcast(
    #     BroadcastRequest(
    #         messages=[TextMessage(text='Broadcast message')]
    #     )
    # )

    # # 所有回覆訊息都有 with_http_info() 方法，可以取得更多的回應資訊
    # response = line_bot_api.reply_message_with_http_info(
    #     ReplyMessageRequest(
    #         reply_token=event.reply_token,
    #         messages=[TextMessage(text='see application log')]
    #     )
    # )
    # app.logger.info("Got response with http status code: " + str(response.status_code))
    # app.logger.info("Got x-line-request-id: " + response.headers['x-line-request-id'])
    # app.logger.info("Got response with http body: " + str(response.data))


    # try:
    #     line_bot_api.reply_message_with_http_info(
    #         ReplyMessageRequest(
    #             reply_token='invalid-reply-token',
    #             messages=[TextMessage(text='see application log')]
    #         )
    #     )
    # except ApiException as e:
    #     app.logger.info("Got response with http status code: " + str(e.status))
    #     app.logger.info("Got x-line-request-id: " + e.headers['x-line-request-id'])
    #     app.logger.info("Got response with http body: " + str(ErrorResponse.from_json(e.body)))