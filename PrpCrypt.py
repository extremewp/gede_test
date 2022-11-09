import base64
import binascii

from Crypto.Cipher import AES
class PrpCrypt:
    def test_get_enAes(data='19520409998'):
        # 解决加密明文不是16的整数倍问题
        pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        # 去除加密明文右侧的空白符
        data = pad(data.rstrip())
        # 这个用作iv,初始化向量
        key16 = 'gd_encryptionkey'
        # 这个是AES加密用到的keyF
        key32 = 'gd_encryptionkey'
        # 统一编码一下
        iv = key16.encode('utf-8')
        key = key32.encode('utf-8')
        data1 = data.encode('utf-8')
        # 定义加密模式
        model = AES.MODE_CBC
        # 创建AES对象
        endata = AES.new(key, model, iv)
        # 进行加密
        endata_res = endata.encrypt(data1)
        # 将返回的字节型数据转进行base64编码
        res = binascii.b2a_hex(endata_res)
        print(res.decode())


    def test_01(self):
            data = '19520409998'
            print(len(data))
            res=16- len(data) % 16
            print(res)
            print((16 - len(data) % 16))
            rcs=chr(16 - len(data) % 16)
            print(rcs)
    def get_deAes(self,data):
        # 这个用作iv,初始化向量
        key16 = '2f03e088357803f1'
        # 这个是AES加密用到的key
        key32 = 'a0ea98d540989e5aa96709oipd388bjk'
        iv = key16.encode('utf-8')
        key = key32.encode('utf-8')
        # 定义加密模式
        model = AES.MODE_CBC
        # 创建AES对象
        dedata = AES.new(key, model, iv)
        #进行解密
        res = dedata.decrypt(base64.b64decode(data))
        return res.decode()


    def asd(self):
        name = ["A","B","C"]
        zengjia = input("请输入:")
        aa = ["1","2"]
        name.append(zengjia)   #将整个列表添加，包括列表的【】
        name.extend(aa)   #讲列表中的元素增加到另外一个里面
        name.insert(1,"d")  #在列表的1号位，插入数据d#print(name)
        print(name)
if __name__ == '__main__':
    a =PrpCrypt()
    a.asd()