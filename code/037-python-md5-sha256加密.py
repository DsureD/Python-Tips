import hashlib
import base64

str1 = "3.14159265358979323846"
md5_str = hashlib.md5(str1.encode()).hexdigest()
print(md5_str)  # e10adc3949ba59abbe56e057f20f883e 共32位长度


sha_256_str = hashlib.sha256(str1.encode()).hexdigest()
print(sha_256_str)  # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92 共64位长度
