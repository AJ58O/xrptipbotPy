import requests

class xrptipbot:
	def __init__(self, token):
		self.token = token
		self.baseUrl = "https://www.xrptipbot.com/app/api"

	def login(self, platform, model):
		url = self.baseUrl + "/action:login/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token,
			"platform":platform,
			"model":model
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def unlink(self):
		url = self.baseUrl + "/action:unlink/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def get_balance(self):
		url = self.baseUrl + "/action:balance/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def tip(self, amount, to, existingDestination):
		url = self.baseUrl + "/action:tip/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token,
			"amount":amount,
			"to":to,
			"existingDestination":existingDestination
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def get_stats(self):
		url = self.baseUrl + "/action:userinfo/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def get_contacts(self):
		url = self.baseUrl + "/action:contacts/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def lookup_user(self, query):
		url = self.baseUrl + "/action:lookup/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token,
			"query":query
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def create_paper_wallet(self, note):
		url = self.baseUrl + "/action:paper-proposal/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token,
			"note":note
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r

	def bump(self, amount, aps=None, geo=None, nfc=None):
		url = self.baseUrl + "/action:bump/"
		headers = {"Content-Type":"application/json"}
		payload = {
			"token":self.token,
			"amount":amount,
			"aps":aps,
			"geo":geo,
			"nfc":nfc
		}
		r = requests.post(url=url, json=payload, headers=headers)
		return r		

