from linebot.v3.messaging import (
    URIAction,
    MessageAction,
    PostbackAction,
    DatetimePickerAction,
    CameraAction,
    CameraRollAction,
    LocationAction,
    RichMenuSwitchAction,
    ClipboardAction
)

URIAction(label="Go to line.me", uri="https://line.me/")

MessageAction(label="Say hello", text="Hello")

# label:按鈕上顯示的文字 data:按鈕被點擊時送出的資料 displayText:按鈕被點擊時顯示在聊天室的文字
# inputOption:另外的action(closeRichMenu:關閉圖文選單, openRichMenu:開啟圖文選單, openKeyboard:開啟鍵盤, openVoice:開啟語音輸入)
# fillInText:幫使用者在鍵盤輸入框填入文字(只有在openKeyboard時才有用)
PostbackAction(label="Buy", data="action=buy&itemid=123", displayText="Buy")
PostbackAction(label="Buy", data="action=buy&itemid=123", displayText="Buy", inputOption="openKeyboard", fillInText="---\nName: \nPhone: \nBirthday: \n---")


# label:按鈕上顯示的文字 data:按鈕被點擊時送出的資料 mode:選擇器的模式(datetime:日期時間, date:日期, time:時間) initial:選擇器的初始值 max:選擇器的最大值 min:選擇器的最小值
DatetimePickerAction(label="Select date", data="storeId=12345", mode="datetime", initial="2017-12-25T00:00", max="2018-01-24T23:59", min="2017-12-25T00:00")
DatetimePickerAction(label="Select date", data="storeId=12345", mode="date", initial="2017-12-25", max="2018-01-24", min="2017-12-25")
DatetimePickerAction(label="Select date", data="storeId=12345", mode="time", initial="10:00", max="23:59", min="00:00")

CameraAction(label="Camera")

CameraRollAction(label="Camera roll")

LocationAction(label="Location")

# label:按鈕上顯示的文字 richMenuAliasId:圖文選單的別名ID data:按鈕被點擊時送出的資料
RichMenuSwitchAction(label="Switch rich menu", richMenuAliasId="richmenu-alias-id", data="action=richmenuswitch")

# label:按鈕上顯示的文字 text:要複製到剪貼簿的文字
ClipboardAction(label="Copy to clipboard", text="text to copy")