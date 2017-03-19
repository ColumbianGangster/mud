def parse(player_character_input):
	player_character_input = __remove_duplicate_spaces(player_character_input)
	if ';' in player_character_input:
		# This allows the user to nest commands, such as: n;w;s;open e;e;u;d;w;barter cake for heal;
		player_character_input = player_character_input.split(";")
		# This prevents two edge cases:
		# # User puts ; a the end
		# # User nests many ;;;;;; together 
		player_caracter_input = __remove_empty_strings_from_list_of_strings(player_character_input)
	return player_character_input


def __remove_duplicate_spaces(sentence):
	return " ".join(sentence.split())


# Highest performance approach, as defined by the following SO article:
# http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
def __remove_empty_strings_from_list_of_strings(list_of_strings):
	str_list = list(filter(None, str_list))
	return str_list