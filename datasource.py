import requests
import bs4

def changeMonth(month='index'):

    global ns,n1,n2,t1,t2,t3,t4,t5,t6,t7,t8,x1,z1

    url = f'https://invoice.etax.nat.gov.tw/{month}.html'
    web = requests.get(url)
    web.encoding='utf-8'

    soup = bs4.BeautifulSoup(web.text, "html.parser")
    td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  # 取出中獎號碼的位置
    ns = td[0].getText()  # 特別獎
    n1 = td[1].getText()  # 特獎
    # 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
    n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]

    #取出對獎方式
    ts = soup.select('.container-fluid')[0].select('p.mb-0')
    t1 = ts[0].getText()
    t2 = ts[1].getText()
    t3 = ts[2].getText()
    t4 = ts[3].getText()
    t5 = ts[4].getText()
    t6 = ts[5].getText()
    t7 = ts[6].getText()
    t8 = ts[7].getText()

    #取出領獎時間
    xs = soup.select('.container-fluid')[0].select('td.text-center')[0:9]
    x1 = xs[8].getText()

    #取出對獎月份
    zs = soup.select('.etw-web')[0].select('a.etw-on')[0:9]
    z1 = zs[0].getText()

    return z1