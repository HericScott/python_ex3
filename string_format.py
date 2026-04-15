#Python offers multiple ways to format strings. The str.format method is a popular method, but since Python 3.6, a new way called f-strings (formatted string literals) was introduced. F-strings offer a concise way to embed expressions inside string literals.

#Given the following variables:

name = "victor"
profession = "programmer"

#solution


print(f"hello, {name}. your are a {profession}.")

house = "duplex"
name = "ade"
profession = "banker"

print(f"my father is a {profession}. And we live in a {house}, {name}.")

name = "victor"
profession = "programmer"

print("hello, {}. your are a {}." . format(name, profession))