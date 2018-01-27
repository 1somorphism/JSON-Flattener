# -*- coding: utf-8 -*-

"""
JSON Flattening Library

JSONtoDict is a small library for converting a JSON string / file to a Python
dictionary that maps JSON paths to data values in JSON.

Simple usage:
    >>> import json_flattener
    >>> json_flattener.flatten('demo.json')

The content of demo.json:
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

Returned value of the above function call:
{
    '$.store.book[0].category': 'reference',
    '$.store.book[0].author': 'William Strunk, Jr.',
    '$.store.book[0].title': 'The Elements of Style',
    '$.store.book[0].price': 5.95,
    '$.store.book[1].category': 'fiction',
    '$.store.book[1].author': 'Harper Lee',
    '$.store.book[1].title': 'To Kill a Mockingbird',
    '$.store.book[1].price': 12.99,
    '$.store.ball.color': 'blue',
    '$.store.ball.price': 2.95
}
"""

import sys
import json
from .flattener import DictFlattener, OrderedDict

__version__ = '0.0.1'

if sys.version_info[0] == 2:
    assert NotImplementedError("Python 2 is not supported")


def flatten(input_data, ordered=False):
    """ The main function of this library.
    """
    pairing_type = OrderedDict if ordered else dict

    if hasattr(input_data, 'read'):
        json_object = json.load(input_data, object_pairs_hook=pairing_type)
    elif type(input_data) == str:
        json_object = json.loads(input_data, object_pairs_hook=pairing_type)
    elif type(input_data) in [dict, list]:
        json_object = input_data
    else:
        raise ValueError('Function only accepts str, dict, list or file objects')

    dict_flattener = DictFlattener(ordered=ordered)
    dict_flattener.flatten(json_object)
    return dict_flattener.return_output()
