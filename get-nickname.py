from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
import json

#　info.json 読み込み
json_oepn = open('info.json')
info = json.load(json_oepn)

# infoから各情報を追加
channel_access_token = info["channel_access_token"] #チャンネルアクセストークン
user_id = info["user_id"] #ユーザーID

line_bot_api = LineBotApi(channel_access_token)

# ユーザーネーム取得・出力
try:
    profile = line_bot_api.get_profile(user_id)
    nick_name = profile.display_name
    print(nick_name, ":", user_id)
except LineBotApiError as e:
    print("error - failed to get nickname.")
    print("----------")
    print(e)
