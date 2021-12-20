import socket


class Checker:
	def __init__(self, host:str):
		self.__host = host

	def check_port(self, port:str):
			try:
				sock = socket.socket()
				sock.connect((self.__host, int(port)))
				return True
			except socket.error:
				return False

	def check_port_list(self, port_start_num:int, port_end_num:int):
		port_list = [i for i in range(port_start_num, port_end_num+1)]
		result = {port: self.check_port(port) for port in port_list}
		return result