#!/usr/bin/python

import sys

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def hexStrXor(a, b):
	"""For the XOR operation on two bit stream in hex string representation. """
	return "".join([ "%01x" % (int(x,16) ^ int(y,16)) for (x, y) in zip (a,b)])

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
	k = '' # the same key to encrypt two messages

	m0 = "attack at dawn".encode('hex')
	c0 = "6c73d5240a948c86981bc294814d"

	m1 = "attack at dusk".encode('hex')
	c1 = ""

	k = hexStrXor(m0, c0)
	c1 = hexStrXor(k, m1)


	print m0
	print c0
	print k
	print c1

	print hexStrXor(k, c1).decode('hex')
	print hexStrXor(m0, m1)
	print hexStrXor(c0, c1)




	return 1


main()



