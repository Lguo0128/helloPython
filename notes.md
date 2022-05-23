# 2.2.1 变量的命名与使用
## 变量规则：
- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
- 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
- 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print（请参见附录A.4）
- 变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
- 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

# 常用方法
## 修改字符串大小写
STRING.title()      首字母大写<br>
STRING.upper()      全大写<br>
STRING.lower()      全小写<br>

## 合并（拼接）字符串
STRING_COMBINE = STRING_A + STRING_B<br>

## 使用制表符或换行符来添加空白
制表符  \t<br>
换行符  \n<br>

## 删除空白
STRING.rstrip()      删除尾部空白<br>
STRING.lstrip()      删除开头空白<br>
STRING.strip()      删除两端空白<br>
