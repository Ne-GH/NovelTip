
import urllib.request
from lxml import etree


def get_html(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

'''
* @brief : 根据传入的html信息，解析出小说名称
* @param html : 网页的html信息
* @return : 解析成功返回存放小说名称的字符串，解析失败返回""
* @note : 查找网页中的title,如果小说名称不在title中，则解析名称失败
'''
def get_novel_title(html) :

    html_list = html.split('\n')

    for html_line in html_list:
        begin_h1 = html_line.find("<h1")

        if html_line.find("<h1") == -1:
            continue
        if html_line.find("title") == -1:
            continue

        pos_beg = html_line.find(">",begin_h1)
        pos_end = html_line.find("<",pos_beg)

        return html_line[pos_beg+1:pos_end]
    return ""



class Novel:
    def __init__(self,novel_catalog_website):
        self.novel_catalog_website = novel_catalog_website
        self.website_is_ok = self.__check_website(novel_catalog_website)
        self.title = ''
        self.last_chapter_count = 0
        self.cur_chapter_count = 0

    def __check_website(self,novel_catalog_website)-> bool:
        try:
            return urllib.request.urlopen(novel_catalog_website).code == 200
        except Exception as err:
            print("网页连接失败！！")
            return False

    ### @TODO 返回当前页面章节数量
    def parse_novel_catalog_website(self):
        ### 获取http 信息
        connect = get_html(self.novel_catalog_website)
        ### 根据网页信息解析出小说标题
        self.title = get_novel_title(connect)
        # print(self.title)

        html = etree.HTML(connect)
        chapter_list = []
        title_list = html.xpath("//li/a/span/text()")
        print(len(title_list))
        for part in title_list:
            chapter_list.append(part)

        chapter_count = len(title_list)

        return chapter_count,chapter_list


