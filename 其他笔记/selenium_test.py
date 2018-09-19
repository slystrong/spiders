from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree

browser = webdriver.Chrome()
browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 10)
KEYWORD = '编程机器人'

def index_page(page):
	try:
		url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
		print(url)
		browser.get(url)
		page_source = browser.page_source
		browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
		if page > 1:
			input = wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
			submit = wait.until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
			input.clear()
			input.send_keys(page)
			submit.click()
			wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
			wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
	except TimeoutException:
		index_page(page)

	return page_source

def parse_page(page_source):
	etree_html = etree.HTML(page_source)
	print(type(etree_html))
	products = etree_html.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')

	for product in products:
		item = {}
		item['price'] = product.xpath('.//div[contains(@class, "price")]/strong/text()')[0].strip()
		item['title'] = product.xpath('.//div[contains(@class, "title")]/a/text()[2]')[0].strip()
		item['shop'] = 	product.xpath('.//div[contains(@class, "shop")]/a/span[2]/text()')[0].strip()
		item['image'] = product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src')[0].strip()
		item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()')[0]
		item['location'] = product.xpath('.//div[contains(@class, "location")]//text()')[0]
		print(item)
		yield item


def main():
	for page in range(100):
		page_source = index_page(page + 1)

		products = parse_page(page_source)
		for product in products:
			print(product['title'])
			print(product['price'])

if __name__ == '__main__':
	main()