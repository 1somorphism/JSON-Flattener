import unittest
import json_flattener

DATA = """
{"store": {
    "book": [
      { "category": "reference",
        "author": "William Strunk, Jr.",
        "title": "The Elements of Style",
        "price": 5.95
      },
      { "category": "fiction",
        "author": "Harper Lee",
        "title": "To Kill a Mockingbird",
        "price": 12.99
      }
    ],
    "ball": {
      "color": "blue",
      "price": 2.95
    }
  }
}
"""


class TestFlattener(unittest.TestCase):
    def test_empty_list(self):
        data = []
        actual = json_flattener.flatten(data)
        assert actual == {'$': []}

    def test_empty_dict(self):
        data = {}
        actual = json_flattener.flatten(data)
        assert actual == {'$': {}}

    def test_regular_string_data(self):
        actual = json_flattener.flatten(DATA)
        assert actual.get('$.store.book[0].category') == 'reference'

    def test_regular_string_data_ordered_output(self):
        actual = json_flattener.flatten(DATA, ordered=True)
        actual_list = list(actual.items())
        expected_list = [('$.store.book[0].category', 'reference'),
                         ('$.store.book[0].author', 'William Strunk, Jr.'),
                         ('$.store.book[0].title', 'The Elements of Style'),
                         ('$.store.book[0].price', 5.95),
                         ('$.store.book[1].category', 'fiction'),
                         ('$.store.book[1].author', 'Harper Lee'),
                         ('$.store.book[1].title', 'To Kill a Mockingbird'),
                         ('$.store.book[1].price', 12.99),
                         ('$.store.ball.color', 'blue'),
                         ('$.store.ball.price', 2.95)]
        assert actual_list == expected_list

    def test_regular_object_data(self):
        data = {"firstName": "John", "lastName": "Doe"}
        actual = json_flattener.flatten(data)
        assert actual.get('$.lastName') == 'Doe'


if __name__ == '__main__':
    unittest.main()
