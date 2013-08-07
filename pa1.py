#!/usr/bin/python
# Author: Duo Zhao for Cryptography I programming assignement 1

import sys

m=[''] * 10

c=[
#cyphertex 0
"315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf\
2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22\
c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b22080956098781\
5f65286764703de0f3d524400a19b159610b11ef3e",

#cyphertex 1
"234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9\
606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3\
a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f",

#cyphertex 2
"32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a\
2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66\
e935de81230b59b7afb5f41afa8d661cb",

#cyphertex 3
"32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3\
306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3\
a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6\
447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa",

#cyphertex 4
"3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9\
607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86\
e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec8\
5b7c2070",

#cyphertex 5
"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de\
287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c62\
1854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca\
4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f\
19983122b11be87a59c355d25f8e4",

#cyphertex 6
"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf\
606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2\
bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681\
596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a\
3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce",

#cyphertex 7
"315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a\
3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3\
b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e0\
4f6565517f317da9d3",

#cyphertex 8
"271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de\
2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6\
e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd1\
5f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027",

#cyphertex 9
"466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccf\
afb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3\
cd04ff50d66f1d559ba520e89a2cb2a83"]

#target text
target=\
"32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8\
257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16\
e9f52f904"

k = '0' *  len(target)
klist = list(k)

klist[0:2]='66' # 66 39 6e 89 c9 db d8 cc 98 74 35 2a cd 63 95
klist[2:4]='39'
klist[4:6]='6e'
klist[6:8]='89'
klist[8:10]='c9'
klist[10:12]='db'
klist[12:14]='d8'
klist[14:16]='cc'
klist[16:18]='98'
klist[18:20]='74'
klist[20:22]='35'
klist[22:24]='2a'
klist[24:26]='cd'
klist[26:28]='63'
klist[28:30]='95' # 66 39 6e 89 c9 db d8 cc 98 74 35 2a cd 63 95
klist[30:32]='10' # 10 2e af ce 78 aa
klist[32:34]='2e'
klist[34:36]='af' # af ce 78 aa 7f ed 28 a0 7f 6b c9 8d 29 c5 0b 69 b0
klist[36:38]='ce'
klist[38:40]='78'
klist[40:42]='aa'
klist[42:44]='7f'
klist[44:46]='ed'
klist[46:48]='28'
klist[48:50]='a0'
klist[50:52]='7f'
klist[52:54]='6b'
klist[54:56]='c9'
klist[56:58]='8d'
klist[58:60]='29'
klist[60:62]='c5'
klist[62:64]='0b'
klist[64:66]='69'
klist[66:68]='b0' # b0 33 9a 19 f8 aa 40 1a 9c 6d
klist[68:70]='33' # af ce 78 aa 7f ed 28 a0 7f 6b c9 8d 29 c5 0b 69 b0 33
klist[70:72]='9a'
klist[72:74]='19'
klist[74:76]='f8'
klist[76:78]='aa'
klist[78:80]='40'
klist[80:82]='1a' # 1a 9c 6d 70 8f 80 c0 66 c7 63
klist[82:84]='9c'
klist[84:86]='6d'
klist[86:88]='70'
klist[88:90]='8f'
klist[90:92]='80'
klist[92:94]='c0'
klist[94:96]='66'
klist[96:98]='c7'
klist[98:100]='63'
klist[100:102]='fe'
klist[102:104]='f0'
klist[104:106]='12'
klist[106:108]='31'
klist[108:110]='48'
klist[110:112]='cd'
klist[112:114]='d8' #d8
klist[114:116]='e8'
klist[116:118]='02'
klist[118:120]='d0'
klist[120:122]='5b'
klist[122:124]='a9'
klist[124:126]='87'
klist[126:128]='77'
klist[128:130]='33'
klist[130:132]='5d'
klist[132:134]='ae'
klist[134:136]='fc'
klist[136:138]='ec'
klist[138:140]='d5'
klist[140:142]='9c'
klist[142:144]='43'
klist[144:146]='3a'
klist[146:148]='6b'
klist[148:150]='26'
klist[150:152]='8b'
klist[152:154]='60'
klist[154:156]='bf'
klist[156:158]='4e'
klist[158:160]='f0' #fd3c9a61
klist[160:162]='3c'
klist[162:164]='9a'
klist[164:166]='61'

def hexStrXor(a, b):
	"""For the XOR operation on two bit stream in hex string representation. """
	return "".join([ "%01x" % (int(x,16) ^ int(y,16)) for (x, y) in zip (a,b)])

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def inPool(val):
	if val >= ord('a') and val <= ord('z'):
		return True
	if val >= ord('A') and val <= ord('Z'):
		return True
	if val == ord(' '):
		return True
	if val == ord(',') or val == ord('.') or val == ord('"') or val == ord("'"):
		return True
	#if val >= ord('') and val <= ord('9'): return True
	return False


def main():
	k = "".join(klist)# the same key to encrypt two messages

	# for s in c:
	# 	for t in c:
	# 		print hexStrXor(s, t)

	for s in c:
		sys.stdout.write("%s " % s[:2])
	sys.stdout.write('\n')


	for i in range(0, len(target), 2):
		sys.stdout.write("%03d: " % i)
		for j in range(0, 256, 1):
			keyHex = "%02x" % j
			keyFlag = True
			#sys.stdout.write(keyHex)
			for s in c:
				msgHex = hexStrXor(keyHex, s[i:i+2])
				msgVal = int(msgHex, 16)
				if not inPool(msgVal):
					keyFlag = False
					break
			if keyFlag:
				sys.stdout.write("%s " % keyHex)
		sys.stdout.write("\n")


	for i, s in enumerate(c):
		m[i] = hexStrXor(k, s[0:len(target)])
		msgStr = m[i].decode("hex")
		print "%d: %s" % (i, m[i])
		print "%d: %s\n" % (i, msgStr)

	# for i in range(0, len(target), 2):
	# 	print "klist[%d:%d]='20'" % (i, i+2)

	print k
	print "hex:", hexStrXor(' encryption '.encode('hex'), c[3][66:86])
	# print k[3][0:30], m[0:30], c[3][0:30]
	# # print m[5][158:164].decode("hex")
	# print m[3].decode("hex")

	print len(target), len(k)
	print hexStrXor(target, k).decode('hex')
	return 1

main()



