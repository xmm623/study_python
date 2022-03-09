from test_privileges import Admin

superadmin = Admin('hha','haha',67)
superadmin.describe_user()
superadmin.privileges.show_privileges()