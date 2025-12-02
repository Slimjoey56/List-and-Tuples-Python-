#Understanding Immutable Objects in Python: Int, Float, Bool
# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result =  False
# print(id(result))
from xmlrpc.server import resolve_dotted_attribute

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))
