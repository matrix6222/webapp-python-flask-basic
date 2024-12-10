from Utils.Utils import Utils
import os


class View:
	def __init__(self):
		self._folder_html = 'View/html/'
		self._folder_js = 'View/js/'

		self._page_post_list = 'post_list.html'

	def get_page_post_list(self):
		return self.load_html(self._page_post_list)

	def load_html(self, name):
		return self._load(self._folder_html, name)

	def load_js(self, name):
		return self._load(self._folder_js, name)

	@staticmethod
	def _load(folder, name):
		if name in os.listdir(folder):
			data = Utils.load_text(os.path.join(folder, name))
			return data
		return None
