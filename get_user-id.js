// GAS用

function doPost(e) {
  const event = JSON.parse(e.postData.contents).events[0];  //JSONからユーザーIDを取得
  const event_type = event.type; //イベントタイプを取得
  const user_id = event.source.userId; //ユーザーIDを取得

  const addres = PropertiesService.getScriptProperties().getProperty('adress'); //宛先(アドレス)をスクリプトプロパティで取得
  const subject = 'Messaging API Webhook'; //件名
  const body = "event-type: " + event_type + "\n" + "user-id: " + user_id; //本文(イベントタイプとユーザーID)

  GmailApp.sendEmail(addres, subject, body); //メールを送信
}
