from unittest import TestCase

from kal.helper import *


class UtilsTest(TestCase):
    def test_dig(self):
        obj = {
            "string_key": "Test String",
            "int_key": 123456789,
            "boolean_key": True,
            "dict_key": {
                "string_key": "This is String in dict",
                "list_key": ["list_item_1", "list_item_2"]
            },
            "list_key": ["list_item_1", "list_item_2", "list_item_3"]
        }

        self.assertEqual(dig(obj, 'string_key'), obj['string_key'])
        self.assertEqual(dig(obj, 'int_key'), obj['int_key'])
        self.assertEqual(dig(obj, 'boolean_key'), obj['boolean_key'])

        # Dict
        self.assertEqual(dig(obj, 'dict_key'), obj['dict_key'])
        self.assertEqual(dig(obj, 'dict_key', 'string_key'), obj['dict_key']['string_key'])
        self.assertEqual(dig(obj, 'dict_key', 'list_key'), obj['dict_key']['list_key'])
        self.assertEqual(dig(obj, 'dict_key', 'list_key', 0), obj['dict_key']['list_key'][0])
        self.assertEqual(dig(obj, 'dict_key', 'list_key', 1), obj['dict_key']['list_key'][1])

        # List
        self.assertEqual(dig(obj, 'list_key'), obj['list_key'])
        self.assertEqual(dig(obj, 'list_key', 0), obj['list_key'][0])
        self.assertEqual(dig(obj, 'list_key', 1), obj['list_key'][1])
        self.assertEqual(dig(obj, 'list_key', 2), obj['list_key'][2])
        self.assertEqual(dig(obj, 'list_key', -1), obj['list_key'][2])

        # Default Value
        self.assertEqual(dig(obj, 'not_exists_key', default='NO'), 'NO')
        self.assertEqual(dig(obj, 'dict_key', 'not_exists_key', default='NO'), 'NO')
        self.assertEqual(dig(obj, 'list_key', 999, default='NO'), 'NO')
