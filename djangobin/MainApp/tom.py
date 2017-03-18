import hashlib
import random



def saltizer():
    rand_word = str(random.random())
    rand_word = rand_word.encode('utf8')
    salt = hashlib.sha1(rand_word).hexdigest()[:5]
    print(salt)
    return salt