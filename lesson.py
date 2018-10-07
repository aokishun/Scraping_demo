# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

# アクセスするURL
url = "http://www.nikkei.com/markets/kabu/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url=url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 摘出した日経平均株価を時間とともに出力します。
with open('/Users/aochaaaaannnn/lesson/python/Scraping_demo/db/nikkei_heikin.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    span = soup.select_one("#CONTENTS_MARROW > div.mk-top_stock_average.cmn-clearfix > div.cmn-clearfix > div.mkc-guidepost > div.mkc-prices > span.mkc-stock_prices").text
        # csvに記述するレコードを作成します
    csv_list = []
        # 現在の時刻を年、月、日、時、分、秒で取得します
    time_ = datetime.now().strftime("%Y/%m/%d")
        # 1カラム目に時間を挿入します
    csv_list.append(time_)
    # 2カラム目に日経平均を記録します
    csv_list.append(span)
    # csvに追記敷きます
    writer.writerow(csv_list)
    # ファイル破損防止のために閉じます
    f.close()
