import requests


# 简单封装requests方法

class Runmian:

    def send_get(self, url, data, headers):
        res = requests.get(url=url, data=data, headers=headers).json()
        return res

    def send_post(self, url, data,json,headers):
        res = requests.post(url=url, data=data,json=json, headers=headers).json()
        return res

    def run_main(self, url, method, data=None,json=None,  headers=None):

        res = None

        if method == "get":

            res = self.send_get(url, data, headers)
        else:
            res = self.send_post(url, data, json, headers)
        return res
