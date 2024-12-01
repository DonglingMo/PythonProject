import unittest

from testcase.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # 指定测试前置条件
    # def setUp(self):
    def test_get_formatted_name(self):
        name = get_formatted_name('Tom', 'Smith')
        self.assertEqual(name, 'Tom Smith')  # add assertion here


if __name__ == '__main__':
    unittest.main()
