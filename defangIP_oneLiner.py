def defangIPaddr(address):
	return '[.]'.join(address.split("."))

print(defangIPaddr("192.168.0.1"))