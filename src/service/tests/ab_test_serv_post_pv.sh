ab -n $1 -c $2 -k -e ab_logs/ab_logs_req_$1_currency_$2.out -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" -H "Referer: http://fangself.com.cn/subcontent/postgresql_installconfigoncentos7.html" -H "Origin: http://fangself.com.cn" -H "Connection: keep-alive" -H "Pragma: no-cache" -H "Cache-Control: no-cache" -p ab_test_serv_post_pv_content.txt  "http://127.0.0.1:8001/pv"
