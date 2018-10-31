import urllib
import http.cookiejar
from bs4 import BeautifulSoup

def get_contest_data(contest_id, username, password):
    login_url = 'https://vjudge.net/user/login'
    rank_url  = 'https://vjudge.net/contest/rank/single/' + contest_id
    cookie  = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener  = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)
    values  = {
        'username': username,
        'password': password
    }
    values  = urllib.parse.urlencode(values).encode(encoding='UTF-8')
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    req  = urllib.request.Request(login_url, values, headers)
    res  = opener.open(req)
    ans  = res.read().decode('UTF-8')
    soup = BeautifulSoup(ans, 'html.parser')
    true  = True
    false = False
    if str(soup) == 'success':
        print('Login successfully!')
        req = urllib.request.Request(rank_url)
        res = opener.open(req)
        ans = res.read().decode('UTF-8')
        ret = eval(ans)
        print('Analyze contest json successfully!')
        return ret
    else:
        print('Login failed!')
        exit(0)