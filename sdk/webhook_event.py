from linebot.v3.webhooks import (
    MessageEvent,
    FollowEvent,
    UnfollowEvent,
    JoinEvent,
    LeaveEvent,
    PostbackEvent,
    MemberJoinedEvent,
    MemberLeftEvent,
    
    # Message event 的訊息類型
    TextMessageContent,
    LocationMessageContent,
    StickerMessageContent,
    ImageMessageContent,
    VideoMessageContent,
    AudioMessageContent,
    FileMessageContent
)

#app.logger.info()，代表只會出現在終端機
@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    app.logger.info("Got text message")

@line_handler.add(MessageEvent, message=LocationMessageContent)
def handle_location_message(event):
    app.logger.info("Got location message")

@line_handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker_message(event):
    app.logger.info("Got sticker message")

@line_handler.add(MessageEvent, message=(ImageMessageContent, VideoMessageContent, AudioMessageContent, FileMessageContent))
def handle_media_message(event):
    app.logger.info("Got media message")

@line_handler.add(PostbackEvent)
def handle_postback(event):
    app.logger.info("Got postback event")

@line_handler.add(FollowEvent)
def handle_follow(event):
    app.logger.info("Got follow event")

@line_handler.add(UnfollowEvent)
def handle_unfollow(event):
    app.logger.info("Got unfollow event")

@line_handler.add(JoinEvent)
def handle_join(event):
    app.logger.info("Got join event")

@line_handler.add(LeaveEvent)
def handle_leave(event):
    app.logger.info("Got leave event")

@line_handler.add(MemberJoinedEvent)
def handle_member_joined(event):
    app.logger.info("Got memberJoined event")

@line_handler.add(MemberLeftEvent)
def handle_member_left(event):
    app.logger.info("Got memberLeft event")