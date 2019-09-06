from subprocess import run, PIPE
from string import  ascii_letters
import random
ABS_L = "/srv/temp/trackingsite/visitrck/sanic/tests/"
ITEM_NUMS = 1000
x_origin = [ i for i in  ascii_letters]
tks = []
for _ in range(ITEM_NUMS):
    random.shuffle(x_origin)
    tks.append("".join(x_origin))
#tks = [ "".join(random.shuffle(x_origin)) for _ in range (ITEM_NUMS)]
rfs = [ "http://fingerecho.cn/?from=%s"%(i) for i in tks]
with open("ua.txt","r") as f:
    ua_origin = f.readlines()
uas = [random.choices(ua_origin) for _ in range(ITEM_NUMS)]
def test_serv_post_pv_template(tk,rf,ua):
    ua = ua[0]
    print(['test_serv_post_pv_template.sh',tk,rf,ua])
    #rd = run(['{abs}test_serv_post_pv_template.sh'.format(abs=ABS_L),tk,rf,ua],stdout=PIPE,timeout=3000)
    cmcmds = ["curl", "-i", "http://127.0.0.1:8001/pv","-H", "User-Agent: %s"%(ua), "-H",  "Accept: */*","-H", "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","--compressed", "-H", "Referer: %s"%(rf), "-H", "Origin: http://fangself.com.cn", "-H", "Connection: keep-alive","-H", "Pragma: no-cache", "-H", "Cache-Control: no-cache", "--data", "tokens=%s"%(tk)]
    rd = run(cmcmds,stdout=PIPE)
    out = rd.stdout
    return out
if __name__ == "__main__":
    for i in range(ITEM_NUMS):
        ...
        test_serv_post_pv_template(tks[i],rfs[i],uas[i])
