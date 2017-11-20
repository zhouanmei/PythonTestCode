import  urllib.request
import urllib.parse
import urllib.request, urllib.parse, http.cookiejar
import random
import pymysql.cursors
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'+str(random.uniform(0,1)))]
        urllib.request.install_opener(opener)
        html_bytes = urllib.request.urlopen(url).read()
        html_string = html_bytes.decode('utf-8')
        return html_string
    except BaseException as e:
        print("获取网页错误：",str(e))

def getCurrentPage(html_code):
    currentPage=-1
    try:
        currentPage=int(BeautifulSoup(html_code,"lxml").find(name="span",class_="current-comment-page").string.replace('[','').replace(']','') )
    except BaseException as e:
        print("获取当前页错误：",str(e))
    finally:
        return currentPage

def getNextUrl(html_code):
    nextPageUrl="000"
    try:
        doc=BeautifulSoup(html_code,"lxml")
        href_=doc.find(name="a",class_="previous-comment-page").get("href")
        nextPageUrl="http:"+href_
    except BaseException as e:
        print("获取下一页URL错误：",str(e))
    finally:
        return nextPageUrl

def getPicId(html_code):
    id_="0000000"
    try:
        id_=html_code.find(name="span",class_="righttext").string
    except BaseException as e:
        print("获取图片ID错误：", str(e))
    finally:
        return id_

def getPicUrl(html_code):
    picUrl_="0000000"
    try:
        picUrl_=html_code.find(name="a",class_="view_img_link").get("href")
    except BaseException as e:
        print("获取图片地址错误：", str(e))
    finally:
        return "http:"+picUrl_

def getPicOO(html_code):
    picOO_=-1
    try:
        picOO_=int(html_code.find(name="span",class_="tucao-like-container").find(name="span").string)
    except BaseException as e:
        print("获取支持数错误：", str(e))
    finally:
        return picOO_

def getPicXX(html_code):
    picXX_=-1
    try:
        picXX_=int(html_code.find(name="span",class_="tucao-unlike-container").find(name="span").string)
    except BaseException as e:
        print("获取反对数错误：", str(e))
    finally:
        return picXX_

def getPicTucao(html_code):
    picTu_=-1
    try:
        picTu_=int(html_code.find(name="a",class_="tucao-btn").string.split("[")[1].split("]")[0])
    except BaseException as e:
        print("获取吐槽数错误：", str(e))
    finally:
        return picTu_

def getPicAuthor(html_code):
    author_='0000000'
    try:
        author_=html_code.find(name="strong").string
    except BaseException as e:
        print("获取作者错误：", str(e))
    finally:
        return author_


html_doc=getHtml("https://jandan.net/pic")
#print(getCurrentPage(html_doc))
#print(getNextUrl(html_doc))

currentPage=getCurrentPage(html_doc)
nextUrl=getNextUrl(html_doc)
while nextUrl!="000":
    if currentPage!=-1 and nextUrl!="000":
        for row in BeautifulSoup(html_doc,"lxml").find_all(name="div",class_="row"):
            author=getPicAuthor(row)
            picId=getPicId(row)
            picOO=getPicOO(row)
            picXX=getPicXX(row)
            picTucao=getPicTucao(row)
            picUrl=getPicUrl(row)
            #print(author,picId,picUrl,picOO,picXX,picTucao)
            con = pymysql.Connect(host='localhost', port=3306, user='root', passwd='', db='test', charset='utf8')
            # 插入数据
            cursor = con.cursor()
            sql = "INSERT INTO jandan_wuliao (page, pic_id, pic_url,oo,xx,tucao,author) VALUES ( %d, '%s', '%s',%d, %d, %d, '%s' )"
            data = (currentPage,picId,picUrl,picOO,picXX,picTucao,author)
            cursor.execute(sql % data)
            con.commit()
            con.close()

    nextUrl=getNextUrl(html_doc)
    html_doc=getHtml(nextUrl)
    currentPage = getCurrentPage(html_doc)
    print("解析"+str(currentPage)+"页。")


