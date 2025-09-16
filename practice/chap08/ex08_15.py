# 8-15  打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_ 
# functions.py 的文件中；在 print_models.py 的开头编写一条 import 语句，并修改这个文
# 件以使用导入的函数。
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 

printing_functions.print_models(unprinted_designs,completed_models)