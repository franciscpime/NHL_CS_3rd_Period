def ask() -> str:
	text = input("Write: ")
	return text


def titlize(s: str) -> str:
	result = ""
	new_word = True

	for c in s:
		if c == " ":
			result += c
			new_word = True
		else:
			if new_word:
				result += c.upper()
				new_word = False
			else:
				result += c.lower()

	return result


def main():
	# do not change code below
	s = ask()
	s = titlize(s)
	print(f"The title is: {s}")

if __name__ == "__main__":
	# do not change code below
	main()

