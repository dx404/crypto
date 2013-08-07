#!/Library/Frameworks/EPD64.framework/Versions/Current/bin/python
# sys.argv[1] as the input file name
import sys
from Crypto.Hash import SHA256
#recursion version
class VideoHash:
    def __init__(self, name):
        self.block_size = 1024
        self.file_obj = open(name, 'rb')
        self.block_list = []
        
    def read_one_block(self):
        return self.file_obj.read(self.block_size)
    
    def read_all_blocks(self):
        current_block = self.read_one_block()
        while current_block != '':
            self.block_list.append(current_block)
            current_block = self.read_one_block()
    
    def getVideoRawHash_itr(self):
        self.read_all_blocks()
        hash = ''
        for block in reversed(self.block_list):
            hash = SHA256.new(block + hash).digest()
        return hash
    
    def getVideoHexHash_itr(self):
        return self.getVideoRawHash_itr().encode('hex')
    #not work for deep recursions
    def getVideoRawHash_recr(self):
        current_block = self.read_one_block()
        if len(current_block) == 0:
            return ''
        else:
            return SHA256.new(current_block + self.getVideoRawHash_recr()).digest()
    
    def getVideoHexHash_recr(self):
        return self.getVideoRawHash_recr().encode('hex')

videoHash_i = VideoHash(sys.argv[1])
videoHash_r = VideoHash(sys.argv[1])
sys.setrecursionlimit(15000)
print videoHash_i.getVideoHexHash_itr()
print videoHash_r.getVideoHexHash_recr()
print len(videoHash_i.block_list)
