import port_checker


if __name__ == '__main__':
	host = input('Enter host: ')
	checker = port_checker.Checker(host)

	print('[1] -- Check port -- ')
	print('[2] -- Check port_list -- ')
	
	menu = input('Menu item: ')
	
	if menu == '1':
		port = input('Enter port: ')
		print(checker.check_port(port))
	elif menu == '2':
		port_start_num = int(input("Enter start port num: "))
		port_end_num = int(input("Enter end port num: "))
		print(checker.check_port_list(port_start_num, port_end_num))
	else:
		print('Error: Menu item was not found')