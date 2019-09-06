curl -i "http://127.0.0.1:8001/pv" -H "User-Agent: $3" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" --compressed -H "Referer: $2" -H "Origin: http://fangself.com.cn" -H "Connection: keep-alive" -H "Pragma: no-cache" -H "Cache-Control: no-cache" --data "tokens=$1"

