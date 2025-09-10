# 变量的命名与使用

## 变量规则

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

STRING_COMBINE = STRING_A + STRING_B

## 使用制表符或换行符来添加空白

制表符  `\t`  <br>
换行符  `\n`  <br>

## 删除空白

`STRING.rstrip()`      删除尾部空白 <br>
`STRING.lstrip()`      删除开头空白 <br>
`STRING.strip()`      删除两端空白  <br>

## 数字

在Python中，可对整数执行加（+）减（-）乘（*）除（/）运算。Python使用两个乘号（**）表示乘方运算。
Python还支持运算次序，因此你可在同一个表达式中使用多种运算。你还可以使用括号来修改运算次序，让Python按你指定的次序执行运算。

- Python将带小数点的数字都称为浮点数。但需要注意的是，结果包含的小数位数可能是不确定的。
- 使用函数 str()避免类型错误
- 有几个专门用于处理数字列表的Python函数:  min(LIST)  max(LIST)  sum(LIST)

## 列表

在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素。

- 在列表末尾添加元素<br>
  `LIST.append('element')`
- 在列表中插入元素<br>
  `LIST.insert( INDEX_NUM, 'element')`
- 使用del语句删除元素<br>
  `del LIST[INDEX_NUM]`
- 使用方法pop()删除元素

  > - 方法pop()可删除列表末尾的元素，并让你能够接着使用它。 <br>
      `LIST.pop()`
  > - 方法pop()可括号中指定要删除的元素的索引。 <br>
      `LIST.pop(INDEX_NUM)`
  >
- 根据值删除元素
  `LIST.remove('element')`

  > 注意:方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。

### 列表排序

- 永久排序  `LIST.sort()`
  按字母反向排序 `LIST.sort(reverse=True)`
- 临时排序  `sorted(LIST)`
  反向排序 `sorted(LIST,reverse=True)`
- 列表反转排序  `LIST.reverse()`

### 操作列表

- for循环   `for element in LIST:`
- 函数 range()  `range(NUM1,NUM2)`

  > - 函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值。
  > - 函数range()时，还可指定步长。第三个参数用作指定步长。
  >
- 函数 list()   `list()`

  > - 用于将元组转换为列表。
  > - 注：元组与列表是非常类似的，区别在于元组的元素值不能修Vditor改，元组是放在括号中，列表是放于方括号中。
  >
- 使用range()创建数字列表 `list(range(NUM1,NUM2))`

### 列表解析

- 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。

```python
quares.py
squares = [value**2 for value in range(1,11)] 
print(squares) 
```

要使用这种语法，首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为value\*\*2，它计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。在这个示例中，for循环为for value in range(1,11)，它将值1~10提供给表达式value\*\*2。请注意，这里的for语句末尾没有冒号。

### 列表切片
- 列表切片 `LIST[NUM1:NUM2]`
  - NUM1 ——开始的索引位，从0开始数起；
  - NUM2 ——结束的索引位，截止该位前的元素。
  - 可以为空，相当于从第一位开始/直到最后一位结尾
  - 支持负值指定倒数第x位

### 复制列表
- 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。 

## 元组
- Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
- 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
### 修改元组
  - 可以给存储元组的变量赋值

## 条件测试
### if判断
- Python根据条件测试的值为True还是False来决定是否执行if语句中的代码。如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。
- 总之，如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。