# -*- coding: utf-8 -*-
"""
디비생성 테스트
목표:  CreateDb.py 실행시
      디비 연결 확인, 디비생성 , 디비 삭제를 테스
비고: 상위 파일을 임포트 하기위해 os, sys 모듈 사용(사용하지 않을 경우 상위 모듈을 임포트 할수 없다)

test_db_connect(): 디비 연결 확인 테스트 함수
test_create_db(): 새로운 디비 생성 함수
test_drop_db(): 새로운 디비 생성후 삭제 함수
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest
from createDb import CreateDb


class CreateDBTest(unittest.TestCase):
    """
    테스트 클래스
    """

    def setUp(self):
        """
        테스트에 필요한 설정을 초기화
        """
        self.test_module = CreateDb('root', '', 'Test3')
        self.result_con = self.test_module.db_con()

    def tearDown(self):
        """
        테스트 종료시 실행되는 함수
        """
        self.test_module.close_db()

    def test_db_connect(self):
        """
        디비 연결 확인
        """
        self.assertEqual(self.result_con[2], True)

    def test_create_db(self):
        """
        새로운 디비 생성
        """
        self.result = self.test_module.new_create_db()
        self.assertEqual(self.result[1], True)

    def test_drop_db(self):
        """
        새로운 디비 삭제
        """
        self.result = self.test_module.drop_database()
        self.assertEqual(self.result, 0)


def make_suite(testcase, tests):
    """
    테스트 함수를 한번에 실행 시키기위한 함수
    :param testcase: 테스트 클래스
    :param tests:  테스트 클래스 안의 리스트형식의 테스트 함수명
    """
    return unittest.TestSuite(map(testcase, tests))


if __name__ == '__main__':
    suite = make_suite(CreateDBTest, ['test_db_connect', 'test_create_db', 'test_drop_db'])
    allunitests = unittest.TestSuite([suite])
    unittest.TextTestRunner(verbosity=2).run(allunitests)
