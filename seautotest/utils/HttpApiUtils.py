import unittest
from time import sleep

import requests
import json

from seautotest.control.httpcaps import Runmian
from seautotest.utils.fileutils import Excel


class testdemo(unittest.TestCase):
    def setUp(self):
        self.run = Runmian()
    def test01(self):

        files = "../element/element.xls"
        e = Excel('r', files)
        list_read = e.read()
        num=list_read.__len__()
        for  i  in range(1,num):
            url1 = list_read[i][2]
            methods = list_read[i][1]
            header = eval(list_read[i][3])
        # header = {
        #     "Cookie": "experimentation_subject_id=ImZkYzMzYzFmLTk0ZmMtNGE3Yi05ODZhLTMwZTUxYTI1M2E5ZiI%3D--0165edbdd5ed55fb8197475489c68d47e5c14f0a; _ati=7830550694778; 3AB9D23F7A4B3C9B=KHQLJ6NW5BDIOGJA3AYJLEUEXJUOYXW37UL4LAZGZAAMLTA44Q6CTIWGDNBDAHJVXTVLMTFS5QZP4TQLPLQP23PIPE; ARK_ID=JS60c5e0f6a34555a67bf1472d0890ae9260c5",
        #     "token": "eyJhbGciOiJIUzI1NiJ9.eyJwYXRoIjpbInBvc3QvdjEvdXNlcnMiLCJkZWxldGUvdjEvdXNlcnMvLioiLCJwdXQvdjEvdXNlcnMvLioiLCJnZXQvdjEvdXNlcnMiLCJnZXQvdjEvdXNlcnMvLioiLCJnZXQvdjEvdmlzaXRlZC9tZXNzYWdlL2RldGlhbCIsImdldC92MS9kYXRhL3Nlc3Npb25Gb3JlY2FzdCIsImdldC92MS9kYXRhL2Z1bmN0aW9uRXZhbHVhdGUiLCJnZXQvdjEvZGF0YS9zaG9wcGluR3VpZGUiLCJnZXQvdjEvdmlzaXRlZC9tZXNzYWdlIiwicG9zdC92MS9mZWVkYmFja3Mvc2VhcmNoIiwicG9zdC92MS91c2VyL2xvZ2luL21lc3NhZ2UiLCJwb3N0L3YxL2xvZ2luL2FuYWx5emUiLCJwb3N0L3YxL2JhY2svc2hvcC93aGl0ZS9mdW5jdGlvbi9zZWFyY2giLCJwb3N0L3YxL3NhdmUvYmFjay9zaG9wL3doaXRlL2Z1bmN0aW9uIiwicHV0L3YxL3VwZGF0ZS9iYWNrL3Nob3Avd2hpdGUvZnVuY3Rpb24iLCJkZWxldGUvdjEvYmFjay9zaG9wL3doaXRlL2Z1bmN0aW9uL2RlbGV0ZSIsImdldC92MS9iYWNrL3Nob3Avd2hpdGUvZnVuY3Rpb24vYmFzaWMiLCJnZXQvdjEvYmFjay93aGl0ZS9mdW5jdGlvbi9zZWFyY2giLCJnZXQvdjEvc2hvcC9zZXJhY2giLCJwb3N0L3YxL21lbWJlci9jZW50ZXIvc2VhcmNoIl0sIm5hbWUiOiJhMTIzNDU2IiwiZXhwIjoxNjE4Mjc4OTE3LCJhY2NvdW50IjoidGVzdDAwMSJ9.97cBLsc1YbrwUqaqkz2D9aeejIfRlFeEISyfC48bqL0"
        # }
            res1 = self.run.run_main(url1, methods, headers=header)
            print(res1)

    # def test02(self):

