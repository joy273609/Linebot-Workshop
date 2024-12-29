import re

# 字串取代{{variable}}
def replace_variable(text: str, variable_dict: dict, max_count: int = 0):
    def replace(match):
        key = match.group(1)
        return str(variable_dict.get(key, match.group(0)))

    # 匹配 {{variable}} 的正規表達式
    pattern = r'\{\{([a-zA-Z0-9_]*)\}\}'
    replaced_text = re.sub(pattern, replace, text, count=max_count)
    return replaced_text

# 裡面有兩個要替換變數 {{image_url}} 和 {{title}}
original_text = """{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "{{image_url}}",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{{title}}",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": true,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}"""

# 替換變數的值
variable_dict = {
    "image_url": "https://developers-resource.landpress.line.me/fx/img/line_flex_message_guide_1.jpg",
    "title": "東京旅行"
}

# 取代變數
replaced_text = replace_variable(original_text, variable_dict)
print(replaced_text)