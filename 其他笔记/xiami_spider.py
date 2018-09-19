from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
from kaisha import str2url

browser = webdriver.Chrome()
browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 10)

def index_page():
	url = 'https://www.xiami.com/chart/index/c/103/type/0?spm=a1z1s.2943549.6827461.1.a26OKv'
	browser.get(url)
	wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="songwrapper"]')))

	page_source = browser.page_source

	return page_source

def parse_page(page_source):
	etree_html = etree.HTML(page_source)
	data_mp3_list = etree_html.xpath('//tr[@class="songwrapper"]/@data-mp3')
	print(len(data_mp3_list))

	for data_mp3 in data_mp3_list:
		mp3_url = str2url(data_mp3)
		print(data_mp3)
		print(mp3_url)

def main():
	page_source = index_page()
	products = parse_page(page_source)

if __name__ == '__main__':
	main()