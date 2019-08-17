import requests

url = "https://gitee.fyping.cn:65533/serve/tck"
#url = "http://localhost:65533/serve/tck"
#url = "http://localhost:8010/serve/tck"


url = "https://gitee.fyping.cn:65533/serve/leav"
url = "http://localhost:65533/serve/leav"
url = "http://localhost:8010/serve/leav"
url = "http://localhost:8018/uv"
sess = requests.Session()
#sess.verify = '/srv/trackingsite/config/certificate/test.crt'
sess.verify = False
res = sess.post(url,data={'_xsrf':r'bhubyoifcwft7j3sarqbjcae','email':'hellowrdljl'})
res.encoding = "utf-8"

print(res.text)