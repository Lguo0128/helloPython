# 变量的命名与使用
## 变量规则：
- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
- 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
- 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print（请参见附录A.4）
- 变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
- 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

# 常用方法
## 修改字符串大小写
`STRING.title()`      首字母大写<br>
`STRING.upper()`      全大写<br>
`STRING.lower()`      全小写<br>

## 合并（拼接）字符串
STRING_COMBINE = STRING_A + STRING_B<br>

## 使用制表符或换行符来添加空白
制表符  \t<br>
换行符  \n<br>

## 删除空白
`STRING.rstrip()`      删除尾部空白<br>
`STRING.lstrip()`      删除开头空白<br>
`STRING.strip()`      删除两端空白<br>

## 数字
在Python中，可对整数执行加（+）减（-）乘（*）除（/）运算。Python使用两个乘号表示乘方运算。<br>
Python还支持运算次序，因此你可在同一个表达式中使用多种运算。你还可以使用括号来修改运算次序，让Python按你指定的次序执行运算。<br>
- Python将带小数点的数字都称为浮点数。但需要注意的是，结果包含的小数位数可能是不确定的。<br>
- 使用函数 str()避免类型错误<br>

## 列表
在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。<br>
Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素。<br>
- 在列表末尾添加元素<br>
    `el.append('element')`
- 在列表中插入元素<br>
    `el.insert( INDEX_NUM, 'element')`
- 使用del语句删除元素<br>
    `del el[INDEX_NUM]`
- 使用方法pop()删除元素<br>
    > - 方法pop()可删除列表末尾的元素，并让你能够接着使用它。<br> `el.pop()`
    > - 方法pop()可括号中指定要删除的元素的索引。<br> `el.pop(INDEX_NUM)`
- 根据值删除元素<br>
    `el.remove('element')`
    >注意:方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。