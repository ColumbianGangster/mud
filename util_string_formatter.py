from filereading_config import newline


def wrap_text_to_console_screen(text):
	text = __remove_existing_new_lines(text)
	text = __insert_new_lines(78, text)


def __remove_existing_new_lines(text):
	return text.replace('\n', ' ').replace('\r', '')


# A superior implementation needs to be found
# Impl drew inspiration from: http://stackoverflow.com/questions/538346/iterating-over-a-string
def __insert_new_lines(every_x_characters, text):
	newtext = ""
	for i, c in enumerate(text):
		newtext = newtext + c
		if i + 1 % every_x_characters == 0:
			newtext = newtext + newline