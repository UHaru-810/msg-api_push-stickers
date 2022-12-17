from linebot import LineBotApi
from linebot.models import StickerSendMessage
from linebot.exceptions import LineBotApiError
import json
import re
import sys

def main():
    #　info.json 読み込み
    json_oepn = open('info.json')
    info = json.load(json_oepn)

    # infoから各情報を追加
    channel_access_token = info["channel_access_token"] # チャンネルアクセストークン
    user_id = info["user_id"] # ユーザーID
    specify_package = info["package_id"] # スタンプ
    specify_sticker = info["sticker_id"] # スタンプ
    repeat_num = info["repeat_num"] #繰り返し回数

    line_bot_api = LineBotApi(channel_access_token)

    nick_name = get_profile(line_bot_api, user_id) #ユーザーネーム取得

    # 確認
    print("nickname:", nick_name)
    print("repeat-num:", repeat_num)
    confirm = input("press Enter to continue...") #実行確認用なので入力内容チェックなどはなし
    print("-----> ----->")

    # スタンプを送信
    try:
        for i in range(repeat_num): # infoから取得した回数繰り返す
            line_bot_api.push_message(user_id, StickerSendMessage(package_id=specify_package, sticker_id=specify_sticker))
        print("succeseed.")
    except LineBotApiError as e:
        print("error - failed to push message.")
        print("----------")
        print(e)
        sys.exit()

    quota_consumption = get_quota_consumption(line_bot_api)
    print("messeage_quota_consumption:", quota_consumption)

# ----------

# ユーザーネーム取得
def get_profile(line_bot_api, user_id):
    try:
        profile = line_bot_api.get_profile(user_id)
        nick_name = profile.display_name
        return nick_name
    except LineBotApiError as e:
        print("error - failed to get nickname.")
        print("----------")
        print(e)
        sys.exit()

# 今月に送信したメッセージ数を取得 (Official Account Managerからのメッセージも含む)
def get_quota_consumption(line_bot_api):
    try:
        get_quota_consumption = str(line_bot_api.get_message_quota_consumption())
        quota_consumption = re.sub(r"\D", "",get_quota_consumption) # 数字のみ抽出
        return quota_consumption
    except LineBotApiError as e:
        print("error - failed to get message quoata consumption.")
        print("----------")
        print(e)
        sys.exit()

if __name__ == "__main__":
    main()