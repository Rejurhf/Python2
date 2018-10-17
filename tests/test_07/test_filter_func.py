# Rejurhf
# 12.10.2018

from unittest import TestCase
# from unittest.mock import patch, call
from nose.tools import assert_list_equal, assert_equal # assert_equals
from ch07.filter_func import filter_ints, is_positive

class FIlterIntsTestCase(TestCase):
    # @patch('ch07.filter_func.is_positive')
    # def test_filter_ints(self, is_positive_mock):
    #     # preparation
    #     v = [3, -4, 0, 5, 8]
    #
    #     #execution
    #     filter_ints(v)
    #
    #     #verification
    #     assert_equals(
    #         [call(3), call(-4), call(0), call(5), call(8)],
    #         is_positive_mock.call_args_list
    #     )

    def test_filter_ints_return_value(self):
        v1 = [3, -4, 0, -2, 5, 0, 8, -1]
        v2 = [7, -3, 0, 0, 9, 1]

        assert_list_equal([3, 5, 8], filter_ints(v1))
        assert_list_equal([7, 9, 1], filter_ints(v2))

    def test_is_positive(self):
        # assert_equal(False, is_positive(-1)) # before boundary
        assert_equal(False, is_positive(0)) # on the boundary
        # assert_equal(True, is_positive(1)) # after the boundary
        for n in range(1, 10 ** 4):
            assert_equal(False, is_positive(-n))
            assert_equal(True, is_positive(n))
