from urllib.request import Request, urlopen
import json
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

class OsuApi():
	def __init__(self, key):
		self.key = key

	def parsing(self, url):
		try:
			req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			webpage = urlopen(req, context=context).read().decode()

			return webpage


		except Exception as e:
			print("ERROR: " + str(e))

	def get_user(self, user):
		a = json.loads( self.parsing(f"https://osu.ppy.sh/api/get_user?k={self.key}&u={user}") )
		return a[0]

	def get_user_best(self, user):
		a = json.loads( self.parsing(f"https://osu.ppy.sh/api/get_user_best?k={self.key}&u={user}") )
		return a

	def get_beatmaps(self, b):
		a = json.loads( self.parsing(f"https://osu.ppy.sh/api/get_beatmaps?k={self.key}&b={b}") )
		return a[0]


	def get_custom(self, url):
		a = json.loads( self.parsing(url.replace("$key", self.key)) )
		return a
