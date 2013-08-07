#!/usr/local/bin/python
import httplib, urllib2, urllib, sys
from Crypto.Cipher import XOR

host = 'crypto-class.appspot.com'
cipher = 'f20bdba6ff29eed7b046d1df9fb70000\
58b1ffb4210a580f748b4ac714c001bd\
4a61044426fb515dad3f21f18aa577c0\
bdf302936266926ff37dbf7035d5eeb4'

def zero_extend(text, align_size):
    return '\x00' * (align_size - len(text)) + text

def pad_it(text, block_size):
    org_size = len(text)
    pad_size = block_size - org_size % block_size
    return text + pad_size * chr(i)

def xor(s1, s2):
    return XOR.new(s1).encrypt(s2)

class PaddingPadding:
    block_size = 16 # 16 bytes
    
    def __init__(self, host, erVal):
        self.host = host
        self.pad = [chr(i) * i for i in range(self.block_size + 1)]
        self.pad_align = ['\x00' * (self.block_size - i) + chr(i) * i for i in range(self.block_size + 1)]
        self.iv = erVal[: 2 * self.block_size].decode('hex')
        self.cipher = erVal[2 * self.block_size:].decode('hex')
        self.num_of_blocks = len(self.cipher) / self.block_size
        
    def query(self, val):
        conn = httplib.HTTPConnection(self.host) # no http p
        conn.request('GET', '/po?er=' + val)
        res = conn.getresponse()
        conn.close()
        return res.status
    
    def getBlock(self, index):
        s = self.block_size
        return self.cipher[s * index: s * (index + 1)]
    
    def getBlockFrom(self, start, end):
        s = self.block_size
        return self.cipher[s * start: s * end]
    
    def getBlockReplaceBy(self, index, newblock):
        s = self.block_size
        before = self.cipher[:s * index]
        after =  self.cipher[s * (index + 1):]
        return before + newblock + after
    

text = ''
# b0 = 'The Magic Words '
po = PaddingPadding(host, cipher[:64])
plain = ''
for i in reversed(range(po.block_size)):
    for g in range(256):
        pad_itr = zero_extend(chr(g) + plain, po.block_size)
        pad_mask = po.pad_align[po.block_size - i]
        new_iv = xor(xor(pad_itr, pad_mask), po.iv)
        query_str =  new_iv + po.cipher
        status = po.query(query_str.encode('hex')) # print query_str.encode('hex'), status
        if status == 404:
            plain = chr(g) + plain
            print chr(g), ':', status, i, g
            break
        if g == 255:
            print 'error: not found'
            sys.exit()
text += plain
print plain

# b1 = 'are Squeamish Os'
# b2 = 'sifrage'    
for block_index in range(0, po.num_of_blocks - 1): # cipher index
    po = PaddingPadding(host, cipher[: 32 * (block_index + 3)])
    plain = ''
    for i in reversed(range(po.block_size)):
        for g in range(6, 256):
          #  print 'cipher: ', po.cipher.encode('hex')
            pad_itr = zero_extend(chr(g) + plain, po.block_size)
            pad_mask = po.pad_align[po.block_size - i]
            new_cipher_block = xor(xor(pad_itr, pad_mask), po.getBlock(block_index))
            query_str =  po.iv + po.getBlockReplaceBy(block_index, new_cipher_block)
            status = po.query(query_str.encode('hex')) 
           # print 'block: ', po.getBlock(block_index).encode('hex')
            # print g, block_index, query_str.encode('hex'), status
            if status == 404 or (status == 200):
                plain = chr(g) + plain
                print chr(g), ':', status, i, g
                break
            if g == 255:
                print 'error: not found'
                sys.exit()
    print plain


for block_index in range(1, 2): # cipher index
    po = PaddingPadding(host, cipher[: 32 * (block_index + 3)])
    plain = ''
    for i in reversed(range(po.block_size)):
        for g in range(6, 256):
#             print 'cipher: ', po.cipher.encode('hex')
            pad_itr = zero_extend(chr(g) + plain, po.block_size)
            pad_mask = po.pad_align[po.block_size - i]
            new_cipher_block = xor(xor(pad_itr, pad_mask), po.getBlock(block_index))
            query_str =  po.iv + po.getBlockReplaceBy(block_index, new_cipher_block)
            status = po.query(query_str.encode('hex')) 
           # print 'block: ', po.getBlock(block_index).encode('hex')
           # print g, block_index, query_str.encode('hex'), status
            if (status == 404) or (status == 200):
                plain = chr(g) + plain
                print chr(g), ':', status, i, g
                break
            if g == 255:
                print 'error: not found'
                sys.exit()
    print "'" + plain + "'"