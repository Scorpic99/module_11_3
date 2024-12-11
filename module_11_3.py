import inspect
import sys


def introspection_info(obj):
    return {'type': type(obj), 'attributes': dir(obj), 'methods': inspect.getmembers(obj), 'module': inspect.getmodule(obj)}


number_info = introspection_info(42)
for i in number_info:
    print(f'{i}: {(number_info[i])}')
