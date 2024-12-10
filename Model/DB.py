from Model.Posts import Posts


class DB:
	def __init__(self, path_db):
		self._path_db = path_db
		self.posts = Posts(self._path_db)


if __name__ == '__main__':
	db = DB('db.db')
	# db.posts.add('title 1', '# Markdown test', 0, 0)
	# print(db.posts.get_by_id(0))
	# print(db.posts.get_by_id(1))
	# print(db.posts.get_by_id(2))
	# print(db.posts.get_by_id(3))
	# print(db.posts.get_by_id(4))
	# print(db.posts.get_by_id(5))
	# print(db.posts.get_by_id(6))
	for x in db.posts.get_titles():
		print(x)
	controllers = 123
