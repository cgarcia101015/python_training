# With this syntax, you don't need to use the dot notation when you call a function.
# Because we've explicitly imported the function make_pizza() in the import statement, we
# can call it by name when we use the function. 
# from module_name import function_name
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a function an alias
# from module_name import function_name as fn
from pizza import make_pizza as mp

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a module an alias
# import module_name as mn
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing all functions in a module
# from module_name import *
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

