# messaging-api_push-stickers
LINEのMessaging APIを用いてスタンプを送信

ソースファイルの説明
----
**get_user-id.js(GAS)**
<br>
GASでWebアプリを作成し、Webhookで受信したJSONファイルから相手のユーザーIDを取得し、指定したメールアドレスにそのIDを送信

**info.json**
<br>
プログラム実行時に必要な各情報を入力

**MAIN: push-stickers.py** 
<br>
info.jsで指定した情報を元に指定した回数、連続してスタンプを送信

**get-nickname.py**
<br>
info.jsで指定したユーザーIDのニックネームを取得

**get_quota_consumption.py**
<br>
今月に送信したメッセージ数を取得 (Official Account Managerからのメッセージも含む)

注意事項
----
**このプログラムにはスタンプを連続して送信するコードがありますが、開発ガイドラインで短期間に大量のリクエストを送ることは禁止されています<br>節度を守って、自己責任で実行してください** <br>
WebhookについてはうまくいかなかったのでとりあえずGASを使用
<br>
<br>
詳しいことは以下のドキュメントを参照
<br>
https://developers.line.biz/ja/docs/messaging-api/


