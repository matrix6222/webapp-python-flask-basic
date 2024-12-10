class Utils:
	@staticmethod
	def load_text(path):
		with open(path, 'r') as file:
			data = file.read()
		return data
