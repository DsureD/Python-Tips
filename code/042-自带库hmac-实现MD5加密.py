import hmac

key = 'key123456'  # key密钥
data = 'ethod=serverle'  # 要加密的内容
hmac_enc = hmac.new(key.encode('utf-8'), data.encode('utf-8'), 'md5').hexdigest()  # 这里是md5，还可以sha1，sha256等
print(hmac_enc)  # 5e7baf605dea189a0a518ad027e2e8f6
