# 9-11 导入Admin 类：以为完成练习9-8 而做的工作为基础，将User、Privileges 和
# Admin 类存储在一个模块中，再创建一个文件，在其中创建一个 Admin 实例并对其调用
# 方法show_privileges()，以确认一切都能正确地运行。

# 9-12 多个模块：将User 类存储在一个模块中，并将Privileges 和Admin 类存储在
# 另一个模块中。再创建一个文件，在其中创建一个 Admin 实例，并对其调用方法
# show_privileges()，以确认一切都依然能够正确地运行。

import ex09_07to08

admin = ex09_07to08.Admin("Linda","Guo")

admin.privileges.show_privileges()