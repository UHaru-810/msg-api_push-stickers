from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import json
import re

#　info.json 読み込み
json_oepn = open('info.json')
info = json.load(json_oepn)

line_bot_api = LineBotApi(info["channel_access_token"])

# 今月に送信したメッセージ数を取得・出力 (Official Account Managerからのメッセージも含む)
try:
    get_quota_consumption = str(line_bot_api.get_message_quota_consumption())
    quota_consumption = re.sub(r"\D", "",get_quota_consumption) # 数字のみ抽出
    print("messeage_quota_consumption:", quota_consumption)
except LineBotApiError as e:
    print("error - failed to get message quoata consumption.")
    print("----------")
    print(e)