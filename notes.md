# 学习笔记

## Python 通用规则

### 变量规则

- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为 message_1，但不能将其命名为 1_message。
- 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名 greeting_message 可行，但变量名 greeting message 会引发错误。
- 不要将 Python 关键字和函数名用作变量名，即不要使用 Python 保留用于特殊用途的单词，如 print（请参见附录 A.4）
- 变量名应既简短又具有描述性。例如，name 比 n 好，student_name 比 s_n 好，name_length 比 length_of_persons_name 好。
- 慎用小写字母 l 和大写字母 O，因为它们可能被人错看成数字 1 和 0。

### 函数编写指南

- 应给函数指定描述性名称，且只在其中使用小写字母和下划线。
- 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
  - 给形参指定默认值时，等号两边不要有空格
    - `def function_name(parameter_0, parameter_1='default value')`
  - 对于函数调用中的关键字实参，也应遵循这种约定
    - `function_name(value_0, parameter_1='value')`
- 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。

### 类编码风格

- 应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
- 实例名和模块名都采用小写格式，并在单词之间加上下划线。
- 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。

## 常用方法

### 修改字符串大小写

- `STRING.title()` 首字母大写
- `STRING.upper()` 全大写
- `STRING.lower()` 全小写

### 合并（拼接）字符串

- `STRING_COMBINE = STRING_A + STRING_B`

### 使用制表符或换行符来添加空白

- 制表符 `\t`
- 换行符 `\n`

### 删除空白

- `STRING.rstrip()` 删除尾部空白
- `STRING.lstrip()` 删除开头空白
- `STRING.strip()` 删除两端空白

### 数字

在 Python 中，可对整数执行加（+）减（-）乘（\*）除（/）运算。Python 使用两个乘号（\*\*）表示乘方运算。
Python 还支持运算次序，因此你可在同一个表达式中使用多种运算。你还可以使用括号来修改运算次序，让 Python 按你指定的次序执行运算。

- Python 将带小数点的数字都称为浮点数。但需要注意的是，结果包含的小数位数可能是不确定的。
- 使用函数 `str()`避免类型错误
- 有几个专门用于处理数字列表的 Python 函数: `min(LIST)` `max(LIST)` `sum(LIST)`

## 列表

在 Python 中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
Python 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让 Python 返回最后一个列表元素。

- 在列表末尾添加元素
  - `LIST.append('element')`
- 在列表中插入元素
  - `LIST.insert( INDEX_NUM, 'element')`
- 使用 del 语句删除元素
  - `del LIST[INDEX_NUM]`
- 使用方法 pop()删除元素

  - 方法 pop()可删除列表末尾的元素，并让你能够接着使用它。
    - `LIST.pop()`
  - 方法 pop()可括号中指定要删除的元素的索引。
    - `LIST.pop(INDEX_NUM)`

- 根据值删除元素
  `LIST.remove('element')`

  > 注意:方法`remove()`只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。

### 列表排序

- 永久排序 `LIST.sort()`
  按字母反向排序 `LIST.sort(reverse=True)`
- 临时排序 `sorted(LIST)`
  反向排序 `sorted(LIST,reverse=True)`
- 列表反转排序 `LIST.reverse()`

### 操作列表

- for 循环 `for element in LIST:`
- 函数`range(NUM1,NUM2)`

  > - 函数 range()让 Python 从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值。
  > - 函数 range()时，还可指定步长。第三个参数用作指定步长。

- 函数`list()`

  > - 用于将元组转换为列表。
  > - 注：元组与列表是非常类似的，区别在于元组的元素值不能修 Vditor 改，元组是放在括号中，列表是放于方括号中。

- 使用`range()`创建数字列表 `list(range(NUM1,NUM2))`

### 列表解析

- 列表解析将`for`循环和创建新元素的代码合并成一行，并自动附加新元素。

```python
quares.py
squares = [value**2 for value in range(1,11)]
print(squares)
```

要使用这种语法，首先指定一个描述性的列表名，如 squares；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为`value**2`，它计算平方值。接下来，编写一个`for`循环，用于给表达式提供值，再加上右方括号。在这个示例中，`for`循环为`for value in range(1,11)`，它将值 1~10 提供给表达式`value**2`。请注意，这里的 for 语句末尾没有冒号。

### 列表切片

- 列表切片 `LIST[NUM1:NUM2]`
  - NUM1 ——开始的索引位，从 0 开始数起；
  - NUM2 ——结束的索引位，截止该位前的元素。
  - 可以为空，相当于从第一位开始/直到最后一位结尾
  - 支持负值指定倒数第 x 位

### 复制列表

- 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让 Python 创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。

## 元组

- Python 将不能修改的值称为不可变的，而不可变的列表被称为元组。
- 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。

### 修改元组

- 可以给存储元组的变量赋值

## 条件测试

### if 判断

- Python 根据条件测试的值为`True`还是`False`来决定是否执行`if`语句中的代码。如果条件测试的值为`True`，Python 就执行紧跟在`if`语句后面的代码；如果为`False`，Python 就忽略这些代码。
- 总之，如果你只想执行一个代码块，就使用`if-elif-else`结构；如果要运行多个代码块，就使用一系列独立的`if`语句。
- 在 if 语句中将列表名用在条件表达式中时，Python 将在列表至少包含一个元素时返回`True`，并在列表为空时返回`False`。

## 字典

- 在 Python 中，字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何 Python 对象用作字典中的值。
- 在 Python 中，字典用放在花括号{}中的一系列键—值对表示。
  - `alien_0 = {'color': 'green', 'points': 5}`
- 键—值对是两个相关联的值。
- 键和值之间用冒号分隔，而键—值对之间用逗号分隔。
- 要获取与键相关联的值，可依次指定字典名和放在方括号内的键。
- 注意，键—值对的排列顺序与添加顺序不同。Python 不关心键—值对的添加顺序，而只关心键和值之间的关联关系。
  - `alien_0['y_position'] = 25`
- 对于字典中不再需要的信息，可使用`del`语句将相应的键—值对彻底删除。使用 del 语句时，必须指定字典名和要删除的键。
  - `del alien_0['points']`
  - **注意：删除的键—值对永远消失了。**

### 遍历字典

- 编写用于遍历字典的`for`循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，可使用任何名称。
  - `for k, v in user_0.items()`
- 在不需要使用字典中的值时，方法`keys()`很有用。
  - `for name in favorite_languages.keys():`
  - 方法`keys()`并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键。
- 要以特定的顺序返回元素，一种办法是在 for 循环中对返回的键进行排序。为此，可使用函数`sorted()`来获得按特定顺序排列的键列表的副本
  - `for name in sorted(favorite_languages.keys()):`
- 如果你感兴趣的主要是字典包含的值，可使用方法`values()`，它返回一个值列表，而不包含任何键。
  - `for language in favorite_languages.values():`
- 为剔除重复项，可使用集合（set）。集合类似于列表，但每个元素都必须是独一无二的。通过对包含重复元素的列表调用`set()`，可让 Python 找出列表中独一无二的元素，并使用这些元素来创建一个集合。
  - `for language in set(favorite_languages.values()):`

### 嵌套

- 将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。

## 输入函数

- `input()`：让程序暂停运行，等待用户输入一些文本。
  - 函数`input()`接受一个参数：即要向用户显示的提示或说明，让用户知道该如何做。
  - 使用函数`input()`时，Python 将用户输入解读为字符串。
- `int()`：它让 Python 将输入视为数值。
  - 函数`int()`将数字的字符串表示转换为数值表示
- 求模运算符
  - 处理数值信息时，求模运算符（`%`）是一个很有用的工具，它将两个数相除并返回余数。

## while 循环

- for 循环用于针对集合中的每个元素都一个代码块，而 while 循环不断地运行，直到指定的条件不满足为止。

### break 语句

- 要立即退出`while`循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用`break`语句。
- `break`语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
- 任何 Python 循环中都可使用`break`语句。例如，可使用`break`语句来退出遍历列表或字典的`for`循环。

### continue 语句

- 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用`continue`语句，它不像`break`语句那样不再执行余下的代码并退出整个循环。

## 函数

- 函数是带名字的代码块，用于完成具体的工作。

### 函数定义

- 使用关键字 def 来告诉 Python 你要定义一个函数。向 Python 指出了函数名，还可能在括号内指出函数为完成其任务需要什么样的信息。
  - `def greet_user():`
  - 在这里，函数名为`greet_user()`，它不需要任何信息就能完成其工作，因此括号是空的（即便如此，括号也必不可少）。最后，定义以冒号结尾。
  - 文档字符串用三引号括起，Python 使用它们来生成有关程序中函数的文档。
- 函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。import 语句允许在当前运行的程序文件中使用模块中的代码。
- 通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

### 调用函数

- 可依次指定函数名以及用括号括起的必要信息。

### 向函数传递信息

- 可在函数定义`def greet_user()`的括号内添加`username`。通过在这里添加`username`，就可让函数接受你给`username`指定的任何值。

## 实参和形参

- 在函数`greet_user()`的定义中，变量`username`是一个形参——函数完成其工作所需的一项信息。在代码`greet_user('jesse')`中，值'jesse'是一个实参。实参是调用函数时传递给函数的信息。我们调用函数时，将要让函数使用的信息放在括号内。在`greet_user('jesse')`中，将实参'jesse'传递给了函数`greet_user()`，这个值被存储在形参 username 中。
- **注意：大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参，不要大惊小怪。**

### 传递实参

#### 位置实参

- **这要求实参的顺序与形参的顺序相同。**

#### 关键字实参

- 其中每个实参都由变量名和值组成；还可使用列表和字典。
- 关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆。
- 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
  - `describe_pet(animal_type='hamster', pet_name='harry')`
  - `describe_pet(pet_name='harry', animal_type='hamster')`
- **注意：使用关键字实参时，务必准确地指定函数定义中的形参名。**

#### 参数默认值

- 编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python 将使用指定的实参值；否则，将使用形参的默认值。
  - `def describe_pet(pet_name, animal_type='dog'):`
    - 这里修改了函数 describe_pet()的定义，在其中给形参 animal_type 指定了默认值'dog'。这样，调用这个函数时，如果没有给 animal_type 指定值，Python 将把这个形参设置为'dog'
    - **_请注意，在这个函数的定义中，修改了形参的排列顺序。由于给 animal_type 指定了默认值，无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名字。然而，Python 依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。这就是需要将 pet_name 放在形参列表开头的原因所在。_**
- **注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让 Python 依然能够正确地解读位置实参。**

#### 等效的函数调用

- 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
  - `def describe_pet(pet_name, animal_type='dog'):`

```python
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

- 注意: 使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最容易理解的调用方式即可。

### 返回值

- 函数返回的值被称为返回值。在函数中，可使用`return`语句将值返回到调用函数的代码行。

#### 让实参变成可选的

- 可使用默认值来让实参变成可选的。
- 可给实参`middle_name`指定一个默认值——空字符串，并在用户没有提供中间名时不使用这个实参。为让`get_formatted_name()`在没有提供中间名时依然可行，可给实参`middle_name`指定一个默认值——空字符串，并将其移到形参列表的末尾。
- Python 将非空字符串解读为`True`，因此如果函数调用中提供了中间名，`if middle_name`将为`True`

### 传递列表

- 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。将列表传递给函数后，函数就能直接访问其内容。

```python
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

- 有时候，需要禁止函数修改列表。可向函数传递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。 要将列表的副本传递给函数，可以像下面这样做：
  - `function_name(list_name[:])`
  - 切片表示法[:]创建列表的副本。
- _虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。_

### 传递任意数量的实参

- 形参名`*toppings`中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的所有值都封装到这个元组中。
  - `def make_pizza(*toppings):`

### 结合使用位置实参和任意数量实参

- 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

### 使用任意数量的关键字实参

- 形参`**user_info`中的两个星号让 Python 创建一个名为`user_info`的空字典，并将收到的所有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典那样访问`user_info`中的名称—值对。

## 类

### 创建和使用类

```python
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
```

- 类中的函数称为方法;
- 方法`__init__()`是一个特殊的方法，每当你根据 Dog 类创建新实例时，Python 都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免 Python 默认方法与普通方法发生名称冲突。
  - 为何必须在方法定义中包含形参`self`呢？因为 Python 调用这个`__init__()`方法来创建 Dog 实例时，将自动传入实参`self`。每个与类相关联的方法调用都自动传递实参`self`，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
- 以`self`为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量。像这样可通过实例访问的变量称为属性。
- 方法`__init__()`并未显式地包含`return`语句，但 Python 自动返回一个表示这条小狗的实例。
  - _我们通常可以认为首字母大写的名称（如 Dog）指的是类，而小写的名称（如 my_dog）指的是根据类创建的实例。_
  - 访问属性: 可使用句点表示法。
  - 调用方法: 使用句点表示法来调用 Dog 类中定义的任何方法。
  - 创建多个实例: 可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或占用列表或字典的不同位置。

### 继承

- 如果你要编写的类是另一个现成类的特殊版本，可使用`继承`。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
- 创建子类时，父类必须包含在当前文件中，且位于子类前面。
- 定义子类时，必须在括号内指定父类的名称。
  - 方法`__init__()`接受创建 Car 实例所需的信息
  - `super()`是一个特殊函数，帮助 Python 将父类和子类关联起来。这行代码让 Python 调用 ElectricCar 的父类的方法`__init__()`，让 ElectricCar 实例包含父类的所有属性。
  - 父类也称为超类（superclass），名称 super 因此而得名。

#### 给子类定义属性和方法

- 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。

#### 重写父类的方法

- 可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python 将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

#### 将实例用作属性

- 可以将大型类拆分成多个协同工作的小类。

## 导入

- Python 允许你将类存储在模块中，然后在主程序中导入所需的模块。

### 导入模块

- 要让函数是可导入的，得先创建模块。模块是扩展名为.py 的文件，包含要导入到程序中的代码。

#### 导入整个模块

- 只需编写一条`import`语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。如果你使用这种`import`语句导入了名为`module_name.py`的整个模块，就可使用下面的语法来使用其中任何一个函数
  - `module_name.function_name()`

#### 导入特定的函数

- 导入方法的语法如下：
  - `from module_name import function_name`
  - `from module_name import function_0, function_1, function_2`
- 若使用这种语法，调用函数时就无需使用句点。由于我们在 import 语句中显式地导入了函数 make_pizza()，因此调用它时只需指定其名称。

#### 使用 as 给函数指定别名

- 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名——函数的另一个名称，类似于外号。
  - `from module_name import function_name as fn`

#### 使用 as 给模块指定别名

- 通过给模块指定简短的别名（如给模块 pizza 指定别名 p），让你能够更轻松地调用模块中的函数。
  - `import module_name as mn`

#### 导入模块中的所有函数

- 使用星号（\*）运算符可让 Python 导入模块中的所有函数.
  - `from module_name import *`
- 由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。

#### 避免导入时执行某些代码

- 总是使用 `if __name__ == "__main__":`来保护模块中的执行代码

```python
# 模块测试代码
if __name__ == "__main__":
    # 仅用于测试和演示
```

## 文件与异常

### 文件读取

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

- 函数`open()`接受一个参数：要打开的文件的名称。
  - Python 在当前执行的文件所在的目录中查找指定的文件。
- 函数`open()`返回一个表示文件的对象。
- 关键字`with`在不再需要访问文件后将其关闭。
  - 使用关键字`with`时，`open()`返回的文件对象只在`with`代码块内可用。
  - 如果要在`with`代码块外访问文件的内容，可在`with`代码块内将文件的各行存储在一个列表中，并在`with`代码块外使用该列表
- 使用方法`read()`读取这个文件的全部内容，并将其作为一个长长的字符串存储在变量 contents 中。
- 因为`read()`到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删除多出来的空行，可在`print`语句中使用`rstrip()`
- 注意：读取文本文件时，Python 将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，就必须使用函数`int()`将其转换为整数，或使用函数`float()`将其转换为浮点数。

#### 逐行读取

- 要以每次一行的方式检查文件，可对文件对象使用 for 循环
  - `for line in file_object:`
- 逐行读取方法： `file_object.readlines()`

### 文件写入

- 调用`open()`时需要提供另一个实参，告诉 Python 你要写入打开的文件。
  - **打开文件时，可指定读取模式（`'r'`）、写入模式（`'w'`）、附加模式（`'a'`）或让你能够读取和写入文件的模式（`'r+'`）。**
  - 如果你省略了模式实参，Python 将以默认的只读模式打开文件。
  - 如果你要写入的文件不存在，函数`open()`将自动创建它。
    - 然而，以写入（`'w'`）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python 将在返回文件对象前清空该文件。
  - 注意: Python 只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数`str()`将其转换为字符串格式。
- 函数`write()`不会在你写入的文本末尾添加换行符

### 文件路径

- 要让 Python 打开不与程序文件位于同一个目录中的文件，需要提供文件路径，它让 Python 到系统的特定位置去查找。
- `相对文件路径`让 Python 到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。
  - 在 Linux 和 OS X 中，你可以这样编写代码: `with open('text_files/filename.txt') as file_object:`
  - 在 Windows 系统中，在文件路径中使用反斜杠（\）而不是斜杠（/）: `with open('text_files\filename.txt') as file_object:`
- `绝对路径`通常比`相对路径`更长，因此将其存储在一个变量中，再将该变量传递给 open()会有所帮助。

  - 在 Linux 和 OS X 中，你可以这样编写代码:

  ```python
  file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
  with open(file_path) as file_object:
  ```

  - 在 Windows 系统中，在文件路径中使用反斜杠（\）而不是斜杠（/）:

  ```python
  file_path = 'C:\\Users\\ehmatthes\\other_files\\text_files\\filename.txt'
  with open(file_path) as file_object:
  ```

  - 推荐方法

    - 使用原始字符串（Raw strings） - 最常用的方法
      - `path = r"C:\Users\Name\Documents\file.txt"`
    - 使用正斜杠（Forward slashes） - Python 会自动转换
      - `path = "C:/Users/Name/Documents/file.txt"`
    - 使用双反斜杠 - 需要转义每个反斜杠
      - `path = "C:\\Users\\Name\\Documents\\file.txt"`

  - Python 的 os.path 和 pathlib 模块可以正确处理各种路径格式

  ```python
  import os
  from pathlib import Path

  # 使用 os.path 处理路径
  path = os.path.join("C:", "Users", "Name", "Documents", "file.txt")

  # 使用 pathlib（现代方法）
  path = Path("C:/Users/Name/Documents/file.txt")
  ```

#### 分析文本

- 方法`split()`：以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
- 方法`len()`：来确定这个列表的长度
- Python 有一个`pass`语句，可在代码块中使用它来让 Python 什么都不要做

#### 存储数据 (序列化数据)

- 函数`json.dump()`接受两个实参：要存储的`数据`以及可用于存储数据的`文件对象`。
  - `json.dump(data,file_object)`
- 函数`json.load()`传参`文件对象`
  - `json.load(file_object)`

### 异常

- Python 使用被称为`异常`的特殊对象来管理程序执行期间发生的错误。每当发生让 Python 不知所措的错误时，它都会创建一个`异常对象`。
- 异常是使用`try-except`代码块处理的。
  - 使用了`try-except`代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的 traceback。

#### `try-except` `try-except-else`代码块

- 当你认为可能发生了错误时，可编写一个 try-except 代码块来处理可能引发的异常。

  - 处理 ZeroDivisionError 异常的 try-except 代码块类似于下面这样：

    ```python
    try:
        answer = print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
    ```

- `try-except-else`代码块的工作原理大致如下：
  - 只有可能引发异常的代码才需要放在 try 语句中。
  - 依赖于 try 代码块成功执行的代码都应放到 else 代码块中。
  - except 代码块告诉 Python，如果它尝试运行 try 代码块中的代码时引发了指定的异常，该怎么办。

#### 常见异常类型

- `ZeroDivisionError`
- `FileNotFoundError`
- `ValueError`
- `TypeError`

## Python 标准库

- Python 标准库是一组模块，安装的 Python 都包含它。

### 创建字典并记录其中的键—值对的添加顺序，可使用模块`collections`中的`OrderedDict`类

```python
from collections import OrderedDict
favorite_languages = OrderedDict()
```

### 代码测试工具 `unittest`

- `单元测试`用于核实函数的某个方面没有问题；
- `测试用例`是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
- `全覆盖式测试用例`包含一整套单元测试，涵盖了各种可能的函数使用方式。

- 要为函数编写测试用例，可先导入模块 unittest 以及要测试的函数，再创建一个继承 unittest.TestCase 的类，并编写一系列方法对函数行为的不同方面进行测试。

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```

- 测试类必须继承 unittest.TestCase 类，这样 Python 才知道如何运行你编写的测试。
- `断言方法`用来核实得到的结果是否与期望的结果一致。

| 方 法                   | 用 途                  |
| ----------------------- | ---------------------- |
| assertEqual(a, b)       | 核实 a == b            |
| assertNotEqual(a, b)    | 核实 a != b            |
| assertTrue(x)           | 核实 x 为 True         |
| assertFalse(x)          | 核实 x 为 False        |
| assertIn(item, list)    | 核实 item 在 list 中   |
| assertNotIn(item, list) | 核实 item 不在 list 中 |

- 方法 `setUp()`
  - 在 TestCase 类中包含了方法`setUp()`，Python 将先运行它，再运行各个以 test\_打头的方法。这样，在你编写的每个测试方法中都可使用在方法`setUp()`中创建的对象了。
  - 可在`setUp()`方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。

### pygame

- Pygame 是一个流行的 Python 库，用于开发视频游戏。 它是围绕 Simple DirectMedia Library (SDL) 的免费、开源和跨平台包装器。 Pygame 提供的 SDL 功能抽象使得使用 Python 开发多媒体应用程序变得非常容易。
- w3schools 在线学习地址： <https://www.w3ccoo.com/pygame/pygame_overview.html>

```python
import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

| -模块-               | -说明-                           |
| -------------------- | -------------------------------- |
| `pygame._sdl2.touch` | 用于处理触摸输入                 |
| `pygame.camera`      | 相机使用                         |
| `pygame.cdrom`       | 音频 CD 控制                     |
| `pygame.cursors`     | 光标资源                         |
| `pygame.display`     | 控制显示窗口和屏幕               |
| `pygame.draw`        | 绘制形状                         |
| `pygame.event`       | 与事件和队列交互                 |
| `pygame.examples`    | 示例程序模块                     |
| `pygame.fastevent`   | 与多线程的事件和队列交互         |
| `pygame.font`        | 加载和渲染字体                   |
| `pygame.freetype`    | 加载和渲染计算机字体             |
| `pygame.gfxdraw`     | 绘制形状                         |
| `pygame.image`       | 图像传输                         |
| `pygame.joystick`    | 与游戏杆、游戏手柄和轨迹球交互   |
| `pygame.key`         | 与键盘交互                       |
| `pygame.locals`      | pygame 常量                      |
| `pygame.mask`        | 图像蒙版                         |
| `pygame.math`        | 向量类                           |
| `pygame.midi`        | 与 MIDI 输入输出交互             |
| `pygame.mixer`       | 加载和播放声音                   |
| `pygame.mixer.music` | 控制流式音频                     |
| `pygame.mouse`       | 与鼠标一起工作                   |
| `pygame.pixelcopy`   | 一般的像素数组复制               |
| `pygame.scrap`       | 剪贴板支持                       |
| `pygame.sndarray`    | 访问声音样本数据                 |
| `pygame.sprite`      | 基本的游戏对象类                 |
| `pygame.surfarray`   | 使用数组接口访问图像表面像素数据 |
| `pygame.tests`       | 单元测试套件包                   |
| `pygame.time`        | 监控时间                         |
| `pygame.transform`   | 转换图面                         |

#### 初始化 `pygame.init()`

- 初始化背景设置，让 Pygame 能够正确地工作。

#### 显示 `pygame.display`

- 调用`pygame.display.set_mode()`来创建一个名为`screen`的显示窗口，这个游戏的所有图形元素都将在其中绘制。
- 在 Pygame 中，`surface` 是屏幕的一部分，用于显示游戏元素。
  - `display.set_mode()`返回的 `surface` 表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个 `surface`。
- 调用了`pygame.display.flip()`，命令 Pygame 让最近绘制的屏幕可见。
  - 调用方法`screen.fill()`，用背景色填充屏幕
    - 这个方法只接受一个实参：一种颜色。

#### 事件交互 `pygame.event`

- 为访问 Pygame 检测到的事件，我们使用方法`pygame.event.get()`。
  - 例如，玩家单击游戏窗口的关闭按钮时，将检测到`pygame.QUIT`事件，而我们调用`sys.exit()`来退出游戏。
- 每当用户按键时，都将在 Pygame 中注册一个事件。事件都是通过方法`pygame.event.get()`获取的。每次按键都被注册为一个 KEYDOWN 事件。

#### 图像相关 `pygame.image`

- 调用`pygame.image.load()`加载图像，传参图像路径，返回一个`surface`
- 使用`get_rect()`获取相应`surface`的属性`rect`对象（矩形）
  - 处理 rect 对象时，可使用矩形四角和中心的 x 和 y 坐标。可通过设置这些值来指定矩形的位置。
  - 要将游戏元素居中，可设置相应 rect 对象的属性 center、centerx 或 centery。
  - 要让游戏元素与屏幕边缘对齐，可使用属性 top、bottom、left 或 right；
  - 要调整游戏元素的水平或垂直位置，可使用属性 x 和 y，它们分别是相应矩形左上角的 x 和 y 坐标。
  - _注意：在 Pygame 中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。在 1200×800 的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)。_
- 使用 Pygame 方法`blit()`绘制加载的图像，传参示例：`blit(self.image, self.rect))`

#### 游戏对象类 `pygame.sprite`

- 通过使用`pygame.sprite`，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。

#### 绘制形状 `pygame.draw`

| -说明-     | -方法-                                               |
| ---------- | ---------------------------------------------------- |
| 绘制矩形   | `rect(surface, color, rect)`                         |
| 绘制多边形 | `polygon(surface, color, points)`                    |
| 绘制圆形   | `circle(surface, color, center, radius)`             |
| 绘制椭圆   | `ellipse(surface, color, rect)`                      |
| 绘制椭圆弧 | `arc(surface, color, rect, start_angle, stop_angle)` |
| 绘制直线   | `line(surface, color, start_pos, end_pos, width)`    |

## 其他参考

- 很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。本节使用的文本来自项目 Gutenberg（<http://gutenberg.org/>），这个项目提供了一系列不受版权限制的文学作品，如果你要在编程项目中使用文学文本，这是一个很不错的资源。

- 最安全、最不费钱的方式是使用 <http://pixabay.com> 等网站提供的图形，这些图形无需许可，你可以对其进行修改。
