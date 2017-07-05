from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/callback', methods=['POST'])

def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    print("ผู้ใช้：", user)
    sendText(user, 'งง')
    return '', 200

def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    authorization = 'mOO1A40zvrJda8pQtdHRg3t2Ns/ui0axNP1nhiX3z5XWDoCHSP9x99u/XZWG2BfsX9ex4S0P060Hk9RPNXPgc72Sr6VxN+mO6sUhtSf5iSekhT72RI0trKd/HaxJY3dRc90ZUUrNuyG7tkhiqpyvEwdB04t89/1O/w1cDnyilFU='

    headers ={
        'Content-Type': 'application/json; charset=UTF-8', 'Authorization': authorization
    }

    data = json.dumps({
        "replyToken": user, "messages": [{"type": "text", "text": text}]
    })

    r = requests.post(LINE_API, headers=headers, data=data)

    if __name__ == '__main__':app.run(debug=True)