import requests

url = "http://localhost:65533/uv"
#url = "http://vva.fyping.cn:65533"
url = "https://gitee.fyping.cn:65533/uv"
res = requests.post(url,data={"tokens":"1234567890123456789"})
print(res.status_code)
print(res.text)