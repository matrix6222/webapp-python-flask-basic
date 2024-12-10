from Model.DB import DB


class Api:
	def __init__(self, path_db):
		self._path_db = path_db
		self.db = DB(self._path_db)

	def get_post_list(self):
		return self.db.posts.get_titles()
