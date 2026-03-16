import re

def main():
	# do not change below code
	all_ips = read_ips()
	correct_ips = filter_ips(all_ips)
	for p in correct_ips:
		print(p)
	print(len(correct_ips))


def read_ips():

	# read all content of file as string
	with open("ips.txt", "r") as file:
		content = file.read()

	# split by whitespace/newlines
	ips = content.split()

	# put all ips in a list
	# filter out double ips, only unique ips in the list
	unique_ips = list(set(ips))

	# return list
	return unique_ips


def get_pattern():
	# uses regex to determine of IP address is a valid IP in the range:
	# 47.82.11.0 - 47.82.11.255
    # return the pattern, so something like r"^47.....$"
	return r"^47\.82\.11\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"


def filter_ips(all_ips):
	correct = list()

	# receives a list with a lot of possible IP addresses
	pattern = get_pattern()

	for ip in all_ips:
		if re.match(pattern, ip):
			correct.append(ip)

	# remove duplicates
	correct = list(set(correct))
	
	# returns a list with valid IP addresses
	return correct


if __name__ == "__main__":
	main()
