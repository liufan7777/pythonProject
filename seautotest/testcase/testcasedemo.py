import unittest

import requests
import json

from seautotest.control.httpcaps import Runmian


class testdemo(unittest.TestCase):
    def setUp(self):
        self.run = Runmian()

    def test01(self):
        url = "http://apidev.admindd.yiyitech.com/v1/visited/message?startTime=2021-03-23&endTime=2021-03-23&platform="
        header = {
            "Cookie": "experimentation_subject_id=ImZkYzMzYzFmLTk0ZmMtNGE3Yi05ODZhLTMwZTUxYTI1M2E5ZiI%3D--0165edbdd5ed55fb8197475489c68d47e5c14f0a; _ati=7830550694778; 3AB9D23F7A4B3C9B=KHQLJ6NW5BDIOGJA3AYJLEUEXJUOYXW37UL4LAZGZAAMLTA44Q6CTIWGDNBDAHJVXTVLMTFS5QZP4TQLPLQP23PIPE; ARK_ID=JS60c5e0f6a34555a67bf1472d0890ae9260c5",
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJwYXRoIjpbInBvc3QvdjEvdXNlcnMiLCJkZWxldGUvdjEvdXNlcnMvLioiLCJwdXQvdjEvdXNlcnMvLioiLCJnZXQvdjEvdXNlcnMiLCJnZXQvdjEvdXNlcnMvLioiLCJnZXQvdjEvdmlzaXRlZC9tZXNzYWdlL2RldGlhbCIsImdldC92MS9kYXRhL3Nlc3Npb25Gb3JlY2FzdCIsImdldC92MS9kYXRhL2Z1bmN0aW9uRXZhbHVhdGUiLCJnZXQvdjEvZGF0YS9zaG9wcGluR3VpZGUiLCJnZXQvdjEvdmlzaXRlZC9tZXNzYWdlIiwicG9zdC92MS9mZWVkYmFja3Mvc2VhcmNoIiwicG9zdC92MS91c2VyL2xvZ2luL21lc3NhZ2UiLCJwb3N0L3YxL2xvZ2luL2FuYWx5emUiLCJwb3N0L3YxL2JhY2svc2hvcC93aGl0ZS9mdW5jdGlvbi9zZWFyY2giLCJwb3N0L3YxL3NhdmUvYmFjay9zaG9wL3doaXRlL2Z1bmN0aW9uIiwicHV0L3YxL3VwZGF0ZS9iYWNrL3Nob3Avd2hpdGUvZnVuY3Rpb24iLCJkZWxldGUvdjEvYmFjay9zaG9wL3doaXRlL2Z1bmN0aW9uL2RlbGV0ZSIsImdldC92MS9iYWNrL3Nob3Avd2hpdGUvZnVuY3Rpb24vYmFzaWMiLCJnZXQvdjEvYmFjay93aGl0ZS9mdW5jdGlvbi9zZWFyY2giLCJnZXQvdjEvc2hvcC9zZXJhY2giLCJwb3N0L3YxL21lbWJlci9jZW50ZXIvc2VhcmNoIl0sIm5hbWUiOiLmtYvor5UiLCJleHAiOjE2MTY2NTE3MzYsImFjY291bnQiOiJ0ZXN0MDAxIn0.U8_oMO8q1ut5gDhG9de5wwioOhHi-oQS_-5wTIvrl2U"
        }
        res1 = self.run.run_main(url, "get", headers=header)
        print(res1)

    # def test02(self):
    #     url1 = "http://apidev.admindd.yiyitech.com/v1/visited/message?startTime=2021-03-23&endTime=2021-03-23&platform="
    #     header1 = {
    #         "Cookie": "experimentation_subject_id=ImZkYzMzYzFmLTk0ZmMtNGE3Yi05ODZhLTMwZTUxYTI1M2E5ZiI%3D--0165edbdd5ed55fb8197475489c68d47e5c14f0a; _ati=7830550694778; 3AB9D23F7A4B3C9B=KHQLJ6NW5BDIOGJA3AYJLEUEXJUOYXW37UL4LAZGZAAMLTA44Q6CTIWGDNBDAHJVXTVLMTFS5QZP4TQLPLQP23PIPE; ARK_ID=JS60c5e0f6a34555a67bf1472d0890ae9260c5",
    #         "token": "eyJhbGciOiJIUzI1NiJ9.eyJwYXRoIjpbInBvc3QvdjEvdXNlcnMiLCJkZWxldGUvdjEvdXNlcnMvLioiLCJwdXQvdjEvdXNlcnMvLioiLCJnZXQvdjEvdXNlcnMiLCJnZXQvdjEvdXNlcnMvLioiLCJnZXQvdjEvdmlzaXRlZC9tZXNzYWdlL2RldGlhbCIsImdldC92MS9kYXRhL3Nlc3Npb25Gb3JlY2FzdCIsImdldC92MS9kYXRhL2Z1bmN0aW9uRXZhbHVhdGUiLCJnZXQvdjEvZGF0YS9zaG9wcGluR3VpZGUiLCJnZXQvdjEvdmlzaXRlZC9tZXNzYWdlIiwicG9zdC92MS9mZWVkYmFja3Mvc2VhcmNoIiwicG9zdC92MS91c2VyL2xvZ2luL21lc3NhZ2UiLCJwb3N0L3YxL2xvZ2luL2FuYWx5emUiLCJwb3N0L3YxL2JhY2svc2hvcC93aGl0ZS9mdW5jdGlvbi9zZWFyY2giLCJwb3N0L3YxL3NhdmUvYmFjay9zaG9wL3doaXRlL2Z1bmN0aW9uIiwicHV0L3YxL3VwZGF0ZS9iYWNrL3Nob3Avd2hpdGUvZnVuY3Rpb24iLCJkZWxldGUvdjEvYmFjay9zaG9wL3doaXRlL2Z1bmN0aW9uL2RlbGV0ZSIsImdldC92MS9iYWNrL3Nob3Avd2hpdGUvZnVuY3Rpb24vYmFzaWMiLCJnZXQvdjEvYmFjay93aGl0ZS9mdW5jdGlvbi9zZWFyY2giLCJnZXQvdjEvc2hvcC9zZXJhY2giLCJwb3N0L3YxL21lbWJlci9jZW50ZXIvc2VhcmNoIl0sIm5hbWUiOiLmtYvor5UiLCJleHAiOjE2MTY2NTE3MzYsImFjY291bnQiOiJ0ZXN0MDAxIn0.U8_oMO8q1ut5gDhG9de5wwioOhHi-oQS_-5wTIvrl2U"
    #     }
    #     res2 = requests.get(url1, headers=header1)
    #     # print(res2.status_code)
    #     self.assertEqual(res2.status_code, 200, "pass")
    #     suite = unittest.TestSuite
    #     suite.addTest(testdemo)
    #     unittest.TextTestRunner().run(suite)
    #     # runner = HTMLTestRunner.REPORT_TEST_OUTPUT_TMPL(stream=testdemo, title="demo", description="test")
    #     runner = HTMLTestRunner("123")
    #     runner.run(suite)
