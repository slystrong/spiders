import base64

from chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree


url = "https://checkcoverage.apple.com/cn/zh/"
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
html = etree.HTML(browser.page_source)


def get_html():
	browser.get(url)
	# wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '*')))
	html = etree.HTML(browser.page_source)
	nums = wait.until(EC.presence_of_element_located((By.ID, 'serial-number')))
	result = wait.until(EC.presence_of_element_located((By.ID, 'captcha-input')))
	search = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-label')))
	nums.send_keys('DMPT7A2YHP9X')
	img_src = html.xpath('//img[@class="captcha-image"][1]/@src')[0][23:]
	password = Chaojiying_Client('carmack', 'Vff635241', '96001')
	imgdata = base64.b64decode(img_src)
	file = open('1.jpg', 'wb')
	file.write(imgdata)
	file.close()
	# text = password.PostPic(imgdata, 1902)
	im = open('1.jpg', 'rb').read()
	text = password.PostPic(im, 1902)
	print(text['pic_str'])
	# print(text)
	result.send_keys(text['pic_str'])
	search.click()


def main():
	get_html()


if __name__ == '__main__':
	main()