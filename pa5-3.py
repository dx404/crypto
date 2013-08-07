#!/Library/Frameworks/EPD64.framework/Versions/Current/bin/python

import gmpy2
from gmpy2 import mpz, powmod, f_mod

p=mpz('134078079299425970995740249982058461274793658205923933\
77723561443721764030073546976801874298166903427690031\
858186486050853753882811946569946433649006084171')

g=mpz('11717829880366207009516117596335367088558084999998952205\
59997945906392949973658374667057217647146031292859482967\
5428279466566527115212748467589894601965568')

h=mpz('323947510405045044356526437872806578864909752095244\
952783479245297198197614329255807385693795855318053\
2878928001494706097394108577585732452307673444020333')

B=2**20
x_result = mpz(0)
x0_result = mpz(0)
x1_result = mpz(0)
# build the hash table of h/g^x_1 x_1 from 0 to 2^20
left_table = dict()
for x1 in range(0, B): # 2**20 + 1 ?
    key = powmod(g, -x1, p) # seperate ?
    key = f_mod(h * key, p)
    left_table[key] = x1

for x0 in range(0, B):
    right_val = powmod(g, x0 * B, p)
    try:
        x1_result = left_table[right_val]
        x0_result = x0
        x_result = x0_result * B + x1_result
        break
    except KeyError: 
        continue

print x_result
print "     {} = {} * B + {}".format(x_result, x0_result, x1_result)
