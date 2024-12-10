import sqlite3


class Templates:
	@staticmethod
	def create_table_posts():
		cmd = '''CREATE TABLE IF NOT EXISTS POSTS (
			ID INTEGER PRIMARY KEY,
			TITLE TEXT NOT NULL,
			CONTENT TEXT NOT NULL,
			THREAD_ID INT NOT NULL,
			AUTHOR_ID INT NOT NULL,
			TIME_CREATE INT NOT NULL,
			TIME_EDIT INT NOT NULL,
			HIDDEN INT NOT NULL
		);'''
		return cmd

	@staticmethod
	def create_table_users():
		cmd = '''CREATE TABLE IF NOT EXISTS USERS (
			ID INTEGER PRIMARY KEY,
			LOGIN TEXT NOT NULL,
			PASSWORD TEXT NOT NULL,
			BAN INT NOT NULL,
			AVATAR BLOB NOT NULL
		);'''
		return cmd

	@staticmethod
	def create_table_threads():
		cmd = '''CREATE TABLE IF NOT EXISTS THREADS (
			ID INTEGER PRIMARY KEY,
			NAME TEXT NOT NULL,
			ICON BLOB NOT NULL
		);'''
		return cmd

	@staticmethod
	def create_table_read():
		cmd = '''CREATE TABLE IF NOT EXISTS READ (
			ID INTEGER PRIMARY KEY,
			USER_ID INT NOT NULL,
			THREAD_ID INT NOT NULL
		);'''
		return cmd

	@staticmethod
	def create_table_write():
		cmd = '''CREATE TABLE IF NOT EXISTS WRITE (
			ID INTEGER PRIMARY KEY,
			USER_ID INT NOT NULL,
			THREAD_ID INT NOT NULL
		);'''
		return cmd

	@staticmethod
	def create_table_admins():
		cmd = '''CREATE TABLE IF NOT EXISTS ADMINS (
			ID INTEGER PRIMARY KEY,
			USER_ID INT NOT NULL
		);'''
		return cmd


if __name__ == '__main__':
	path_db = 'db.db'
	with sqlite3.connect(path_db) as conn:
		cursor = conn.cursor()
		cursor.execute(Templates.create_table_posts())
		cursor.execute(Templates.create_table_users())
		cursor.execute(Templates.create_table_threads())
		cursor.execute(Templates.create_table_read())
		cursor.execute(Templates.create_table_write())
		cursor.execute(Templates.create_table_admins())
		conn.commit()

