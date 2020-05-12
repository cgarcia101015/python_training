from privileges import *

new_admin = Admin('tony', 'montana', '37', 'tonytoca@gmail.com', 'miami',)

new_admin.admin.show_privileges()
print(new_admin.describe_user())
print(new_admin.greet_user())