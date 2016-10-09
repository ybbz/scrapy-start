# scrapy-start

Scrapy练习项目:  
爬取百度搜索结果,豆瓣电影Top250,博客等

## 介绍

- baidu_search:百度搜索结果
- douban_top_movies:豆瓣电影Top250
- blog:博客内容
- atom:苹果官网

## 爬取命令示例

生成文件

```
scrapy crawl douban -o movies.json
```