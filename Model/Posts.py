from time import time
import sqlite3


class Posts:
	def __init__(self, path_db):
		self._path_db = path_db

	def add(self, title, content, thread_id, author_id, hidden=0):
		time_s = int(time())
		cmd = '''INSERT INTO POSTS (TITLE, CONTENT, THREAD_ID, AUTHOR_ID, TIME_CREATE, TIME_EDIT, HIDDEN) VALUES (?, ?, ?, ?, ?, ?, ?);'''
		values = (title, content, thread_id, author_id, time_s, time_s, hidden, )
		with sqlite3.connect(self._path_db) as conn:
			cursor = conn.cursor()
			cursor.execute(cmd, values)
			conn.commit()

	def get_by_id(self, post_id):
		cmd = '''SELECT ID, TITLE, CONTENT, THREAD_ID, AUTHOR_ID, TIME_CREATE, TIME_EDIT, HIDDEN FROM POSTS WHERE ID = ?;'''
		values = (post_id, )
		with sqlite3.connect(self._path_db) as conn:
			cursor = conn.cursor()
			cursor.execute(cmd, values)
			data = cursor.fetchone()
		if data is not None:
			data = {
				'id': data[0],
				'title': data[1],
				'content': data[2],
				'thread_id': data[3],
				'time_create': data[4],
				'time_edit': data[5],
				'hidden': data[6]
			}
		return data

	def get_titles(self):
		cmd = '''SELECT ID, TITLE FROM POSTS'''
		with sqlite3.connect(self._path_db) as conn:
			cursor = conn.cursor()
			cursor.execute(cmd)
			data = cursor.fetchall()
		ret = []
		for row in data:
			dictionary = {
				'id': row[0],
				'title': row[1]
			}
			ret.append(dictionary)
		return ret
