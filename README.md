# JSON-Flattener
A trivial Python tool for converting JSON to a flattened dictionary.

#### Usage
```python
>>> data = {
    "store": {
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

>>> import json_flattener
>>> result = json_flattener.flatten(data, ordered=True)
>>> print(list(result.items()))
[
 ('$.store.book[0].category', 'reference'),
 ('$.store.book[0].author', 'William Strunk, Jr.'),
 ('$.store.book[0].title', 'The Elements of Style'),
 ('$.store.book[0].price', 5.95),
 ('$.store.book[1].category', 'fiction'),
 ('$.store.book[1].author', 'Harper Lee'),
 ('$.store.book[1].title', 'To Kill a Mockingbird'),
 ('$.store.book[1].price', 12.99),
 ('$.store.ball.color', 'blue'),
 ('$.store.ball.price', 2.95)
]
```

#### Installation
    pip install json_flattener
