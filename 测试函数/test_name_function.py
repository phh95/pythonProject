import unittest
from name_function import get_formatted_name

# 测试类

class NamesTestCase(unittest.TestCase):
    """测试 name_function.py"""

    def test_first_last_name(self):
        """能正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') # 检查两个值是否相等

# 用 if 代码块测试特殊的变量 __name__，这个变量是在程序执行的时候设置的

if __name__ == '__main__':
    unittest.main()


