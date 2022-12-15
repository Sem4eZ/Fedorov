from unittest import TestCase
from contest.main import DataSet


class DataSetTests(TestCase):
    def test_average_method_on_correct_list(self):
        dict_for_tests = {1: [1, 1, 4], 10: [7, 4, 20]}
        self.assertEqual(DataSet.average(dict_for_tests), {1: 2, 10: 10})

    def test_average_method_on_empty_list(self):
        dict_for_tests = {10: []}
        self.assertRaises(ZeroDivisionError, DataSet.average, dict_for_tests)

    def test_average_method_on_invalid_list(self):
        dict_for_tests = {10: ['2', 2]}
        self.assertRaises(TypeError, DataSet.average, dict_for_tests)

    def test_average_method_on_empty_dict(self):
        dict_for_tests = {}
        self.assertEqual(DataSet.average(dict_for_tests), {})

    def test_average_method_string_keys(self):
        dict_for_tests = {'string': [1, 2]}
        self.assertEqual(DataSet.average(dict_for_tests), {'string': 1})

    def test_sort_list_of_tuple_reverse_false(self):
        list_of_tuple_for_tests = [(0, 1), (10, 0), (1, -2)]
        DataSet.sort_list_of_tuples_by_value(list_of_tuple_for_tests, reverse=False)
        self.assertEqual(list_of_tuple_for_tests, [(1, -2), (10, 0), (0, 1)])

    def test_sort_list_of_tuple_reverse_true(self):
        list_of_tuple_for_tests = [(0, 1), (10, 0), (1, -2)]
        DataSet.sort_list_of_tuples_by_value(list_of_tuple_for_tests)
        self.assertEqual(list_of_tuple_for_tests, [(0, 1), (10, 0), (1, -2)])

    def test_sort_list_of_one_tuple(self):
        list_of_tuple_for_tests = [(0, 1)]
        DataSet.sort_list_of_tuples_by_value(list_of_tuple_for_tests)
        self.assertEqual(list_of_tuple_for_tests, [(0, 1)])

    def test_sort_list_of_empty_tuple(self):
        list_of_tuple_for_tests = []
        DataSet.sort_list_of_tuples_by_value(list_of_tuple_for_tests)
        self.assertEqual(list_of_tuple_for_tests, [])

    def test_sort_list_of_lists(self):
        list_of_tuple_for_tests = [[-2, 0], [1, 1]]
        DataSet.sort_list_of_tuples_by_value(list_of_tuple_for_tests)
        self.assertEqual(list_of_tuple_for_tests, [[1, 1], [-2, 0]])

    def test_sort_list_of_lists_with_char(self):
        list_of_tuple_for_tests = [[-2, 'a'], [1, 'b']]
        DataSet.sort_list_of_tuples_by_value(list_of_tuple_for_tests)
        self.assertEqual(list_of_tuple_for_tests, [[1, 'b'], [-2, 'a']])
