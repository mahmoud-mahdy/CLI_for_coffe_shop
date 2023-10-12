# Rectangle Class [Pytest]

You have been asked to write a python class named `Rectangle` with the following requirements:

1. It should receive two positive integer arguments (width, length) at initialization.
1. It should have a method named `get_area` that when is called, it returns the area of rectangle (width * length).
1. If a non-numeric arg has been used for width or length, it should throw `TypeError`.
1. If any numeric arg rather than a positive integer has been used for width or length, it should throw `ValueError`.

Given the requirements, do the following:

- Put your Rectangle class code in a file named `rectangle.py`
- Put your tests in a file named `test_rectangle.py`
- Use `python3 -m pytest` to run your test cases

The initial python class code would be like this:

```python
class Rectangle:
   def __init__(self, width, length):
      pass
   
   def get_area(self):
      pass
```

## Bonus

Try to add following feature to your Rectangle class:

1. User wants to be able to change width and length values later and get the area based on new values.
