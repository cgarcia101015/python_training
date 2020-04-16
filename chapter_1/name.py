"""
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
"""
#Using variables in strings
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

first_name = "carlos"
last_name = "garcia"

full_name = "{} {}".format(first_name, last_name)
print(full_name)
"""
# Adding Whitespace to Strings with Tabs or Newlines
"""
print("Python")

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
"""
#Stipping Whitespace
favorite_language = 'python '
print(favorite_language)

print(favorite_language.rstrip())


