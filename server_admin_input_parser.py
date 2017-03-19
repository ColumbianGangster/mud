def parse(server_admin_input):
	server_admin_input = __remove_duplicate_spaces(server_admin_input)
	return server_admin_input.split(' ')


def get_command_from_input(input):
	return input[0]


def __remove_duplicate_spaces(sentence):
	return " ".join(sentence.split())


