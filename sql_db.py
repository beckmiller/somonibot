import sqlite3

class SQLighter:

	def __init__(self, database_file):
		''' Connecting to database'''
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()

	def get_subsriptions(self, status = True):
		'''Getting all active subscribed bot users'''
		with self.connection:
			return self.cursor.execute('SELECT * FROM `subsctiptions` WHERE `status` = ?', (status,)).fetchall()

	def subscriber_exists(self, user_id):
		'''Checking is user exists in database'''
		with self.connection:
			result = self.cursor.execute('SELECT * FROM `subsctiptions` WHERE `user_id` = ?', (user_id,)).fetchall()
			return bool(len(result))

	def add_subscriber(self, user_id, status=True):
		'''Add a new user'''
		with self.connection:
			return self.cursor.execute('INSERT INTO `subsctiptions` (`user_id`, `status`) VALUES (?,?)', (user_id, status))

	def update_subscription(self, user_id, status):
		'''Update user subscription'''
		return self.cursor.execute('UPDATE `subsctiptions` SET `status` = ? WHERE `user_id` = ?', (status, user_id))

	def close(self):
		'''Closing database connection'''
		self.connection.close()