import requests
import base64

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5,zh-TW;q=0.4',
    'Connection': 'keep-alive',
    'Content-Length': '46',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=40DF7DEBC05162EB167A854584FB5D40',
    'Host': 'www.esinograin.com',
    'Origin': 'https://www.esinograin.com',
    'Referer': 'https://www.esinograin.com/resources/getGgInfo?ggid=dd647b82118c4b049314b438fdb97478',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': 'null'
}

ggid = "dd647b82118c4b049314b438fdb97478"

url = "https://www.esinograin.com/api/others/getTransactionAnnouncementDetail"

rsp = requests.post(url, headers=headers, data={"jyggId": ggid, "acuId": ""})

b64 = rsp.json()["data"]["jyggNr"].split('"')[1].split(",")[1]
# print(b64)
image_byte = base64.b64decode(b64.encode())

with open(f"{ggid}.jpg", "wb") as f:
    f.write(image_byte)
