import hashlib


# 有必要将密码加密，提高安全性
def encrypt_password(password, x='calvin666'):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))  # 可在密码后加入乱七八糟的字符串再加密
    h.update(x.encode('utf8'))
    return h.hexdigest()
