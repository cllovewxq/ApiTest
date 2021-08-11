# -*- coding: utf-8 -*-
# 转换类
# 作者: 三石
# 时间: 2021-07-09


import base64
from work.config import WorkConfig
from work.utils import UtilsLog
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5


class UtilsRsa(object):
    def __init__(self):
        """
        转换工具类
        """
        self.logger = UtilsLog()

        self.rsa_public = WorkConfig().files_rsa_path + "/public.pem"

        self.rsa_public_key = RSA.importKey(open(self.rsa_public).read())
        # self.rsa_private_key = RSA.importKey(open(self.rsa_private).read())

    def encrypt_str(self, plain_text):
        """
        字符串加密
        :param plain_text: 明文
        :return:
        """
        cipher = PKCS1_v1_5.new(self.rsa_public_key)
        plain_text = cipher.encrypt(message=plain_text.encode(encoding="utf-8"))
        cipher_text = base64.b64encode(plain_text)
        cipher_text = str(cipher_text, encoding="utf-8")
        return cipher_text

