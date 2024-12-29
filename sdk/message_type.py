from linebot.v3.messaging import (
    TextMessage,
    Emoji, # 若要在TextMessage中加入表情符號，需要引入
    # 若要在TextMessage中加入快速回覆，需要引入
    QuickReply,
    QuickReplyItem,

    StickerMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,

    # ImagemapMessage需要引入的物件
    ImagemapMessage,
    ImagemapBaseSize,
    ImagemapArea,
    ImagemapExternalLink,
    ImagemapVideo,
    # Imagemap的Action是獨立的Action物件，不可以用原始的Action物件
    URIImagemapAction,
    MessageImagemapAction,
    ClipboardImagemapAction,

    # TemplateMessage需要引入的物件
    TemplateMessage,
    ButtonsTemplate,
    ConfirmTemplate,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,

    # FlexMessage需要引入的物件
    FlexMessage,
    FlexContainer,

    # 若要在發送訊息時指定發送者及特定頭貼，需要引入
    Sender
)

# 純文字訊息
TextMessage(text="這是文字訊息")

# 純文字訊息，並加入表情符號(emojis)
TextMessage(text='$ LINE 表情符號 $', emojis=[
    Emoji(index=0, product_id="5ac1bfd5040ab15980c9b435", emoji_id="001"),
    Emoji(index=12, product_id="5ac1bfd5040ab15980c9b435", emoji_id="002")
])

# 純文字訊息，並指定發送者及特定頭貼(sender)
TextMessage(text="這是指定發送者及頭像的文字訊息", sender=Sender(name="NTUE", icon_url="https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"))

# 純文字訊息，並回覆指定訊息(quoteToken)
TextMessage(text="這是會回覆某個訊息的文字訊息", quoteToken=event.message.quote_token)

# 快速回覆(quickReply)
TextMessage(text="這是文字訊息", quickReply=QuickReply(items=[QuickReplyItem(action=Action物件)])) #最多13個

# 貼圖訊息
StickerMessage(package_id="446", sticker_id="1988")

# 圖片訊息
ImageMessage(original_content_url="https://example.com/original.jpg", preview_image_url="https://example.com/preview.png")

# 影片訊息
VideoMessage(original_content_url="https://example.com/original.mp4", preview_image_url="https://example.com/preview.png")

# 音訊訊息
# duration:音訊長度(毫秒)
AudioMessage(original_content_url="https://example.com/original.m4a", duration=60000)

# 位置訊息
# latitude:緯度 longitude:經度
LocationMessage(title='Taiwan', address='Taipei', latitude=25.0475, longitude=121.5173)

# 影像地圖訊息
# base_url:圖片的基本網址(六張不同大小圖片的資料夾位置) alt_text:圖片的替代文字 base_size:圖片的基本大小(寬度, 高度)
ImagemapMessage(
    base_url="https://example.com/bot/images/rm001",
    alt_text="this is an imagemap",
    base_size=ImagemapBaseSize(width=1040, height=1040), # 圖片的基本大小(寬度, 高度)通常是最大的圖片大小
    # 如果要加入影像地圖的影片，需要加入ImagemapVideo物件，並指定影片的原始網址、預覽圖片網址、區域大小，以及外部連結
    video=ImagemapVideo(
        original_content_url="https://example.com/video.mp4",
        preview_image_url="https://example.com/video_preview.jpg",
        area=ImagemapArea(x=0, y=0, width=1040, height=585),
        external_link=ImagemapExternalLink(
            link_uri="https://example.com/line",
            label="View details"
        )
    ),
    # 影像地圖的動作(URIImagemapAction, MessageImagemapAction, ClipboardImagemapAction)只能是這三種，不可以用原始的Action物件(最多50個)
    actions=[
        URIImagemapAction(
            link_uri="https://example.com/",
            area=ImagemapArea(x=0, y=0, width=520, height=1040)
        ),
        MessageImagemapAction(
            text="hello",
            area=ImagemapArea(x=520, y=0, width=520, height=1040)
        ),
        ClipboardImagemapAction(
            label="copy",
            text="hello",
            area=ImagemapArea(x=0, y=0, width=1040, height=1040)
        )
    ]
)


# 模板訊息
# alt_text:聊天室顯示的文字 template:模板物件(ButtonTemplate, ConfirmTemplate, CarouselTemplate, ImageCarouselTemplate)
TemplateMessage(alt_text="this is a template message", template=這裡放入Template其中一種物件)

# 按鈕模板
ButtonsTemplate(
    thumbnail_image_url="https://example.com/bot/images/image.jpg",
    imageAspectRatio="rectangle", # rectangle(1.51:1)預設, square(1:1)
    imageSize="cover", # cover(滿版)預設, contain(兩側會留白)
    imageBackgroundColor="#FFFFFF", # 背景顏色
    title="Menu",
    text="Please select",
    defaultAction=Action物件, #當點擊圖片、標題或文字時的動作
    actions=[Action物件] #按鈕動作(最多4個)
)

# 確認模板
ConfirmTemplate(
    text="Are you sure?",
    actions=[Action物件] #按鈕動作(只能是2個)
)

# 輪播模板
CarouselTemplate(
    columns=[CarouselColumn物件], #最多10個
    imageAspectRatio="rectangle", # rectangle(1.51:1)預設, square(1:1)
    imageSize="cover" # cover(滿版)預設, contain(兩側會留白)
)

# 輪播模板中的每個元素
CarouselColumn(
    thumbnail_image_url="https://example.com/bot/images/item1.jpg",
    imageBackgroundColor="#FFFFFF", # 背景顏色
    title="this is menu",
    text="description",
    defaultAction=Action物件, #當點擊圖片、標題或文字時的動作
    actions=[Action物件] #按鈕動作(最多3個)
)

# 圖片輪播模板
ImageCarouselTemplate(
    columns=[ImageCarouselColumn物件] #最多10個
)

ImageCarouselColumn(
    imageUrl="https://example.com/bot/images/item1.jpg",
    action=Action物件 #按鈕動作
)

# Flex訊息
line_flex_str = """{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://developers-resource.landpress.line.me/fx/img/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
          },
          {
            "type": "text",
            "text": "4.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "Flex Tower, 7-7-4 Midori-ku, Tokyo",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "10:00 - 23:00",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "CALL",
          "uri": "https://line.me/"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "WEBSITE",
          "uri": "https://line.me/",
          "altUri": {
            "desktop": "https://www.google.com"
          }
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}"""
FlexMessage(alt_text="this is a flex message", contents=FlexContainer.from_json(line_flex_str))