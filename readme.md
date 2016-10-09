# Paper Crawler

一个利用关键词爬取CCF 推荐排名上的期刊、会议文章链接的工具

## 使用方法

### 1. 安装依赖环境

```shell
pip3 install -r requirements.txt
```

### 2. 在config.ini文件中填入需要爬取的期刊、会议链接

如需要爬取人工智能A类期刊、会议论文，则这样填写（相应链接可以从这个页面找到 <http://www.ccf.org.cn/sites/ccf/biaodan.jsp?contentId=2903940690839> ）：

```
[journal]
http://dblp.uni-trier.de/db/journals/ai/
http://dblp.uni-trier.de/db/journals/pami/
http://dblp.uni-trier.de/db/journals/ijcv/
http://dblp.uni-trier.de/db/journals/jmlr/

[conference]
http://dblp.uni-trier.de/db/conf/aaai/
http://dblp.uni-trier.de/db/conf/cvpr/
http://dblp.uni-trier.de/db/conf/iccv/
http://dblp.uni-trier.de/db/conf/icml/
http://dblp.uni-trier.de/db/conf/ijcai/
http://dblp.uni-trier.de/db/conf/nips/
http://dblp.uni-trier.de/db/conf/acl/

```

注意期刊和会议链接分开在两个域中。

### 3.开启爬虫 

```shell
python3 main.py start-year keyword
```

### 4. 结果保存在journal.md和conference.md文件中

