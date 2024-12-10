from Controllers.View import View
from Controllers.Api import Api


class App:
	def __init__(self):
		self.view = View()
		self.api = Api('Model/db.db')
