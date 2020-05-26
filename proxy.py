import requests
from lxml import html

class Proxy(object):
	proxy_url = 'https://www.ip-adress.com/proxy_list/'
	proxi_list = []
	url_list = []
	def __init__(self):
		r = requests.get(self.proxy_url)
		st = html.fromstring(r.content)
		result = st.xpath("//tr/td[1]/a/text()")
		self.proxi_list = result
	def get_proxy(self):
		for proxy in self.proxi_list:
			url = 'http://' + proxy
			try:
				r = requests.get('http://ya.ru', proxies={'http': url})
				if r.status_code == 200:
					return url
			except requests.exceptions.ConnectionError:
				continue
	def get_proxys(self):
		for proxy in self.proxi_list:
			url = 'http://' + proxy
			try:
				r = requests.get('http://ya.ru', proxies={'http': url})
				if r.status_code == 200:
					self.url_list.append(url)
			except requests.exceptions.ConnectionError:
				continue
		return self.url_list