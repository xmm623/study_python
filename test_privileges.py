"""用户权限等"""

from test_admin import User

class Privileges():
    """权限"""
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        """打印管理员的权限"""
        print("This Privileges are:")
        for privilege in self.privileges:
            print(f"\n{privilege}")


class Admin(User):
    """管理员"""
    def __init__(self,first_name,last_name,age):
        """初始化父类属性"""
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()