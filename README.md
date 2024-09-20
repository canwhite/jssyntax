## jssyntax

Write python using js syntax

## Installation
pip install jssyntax

## Usage

1) List
```

from jssyntax import List

numbers = List([1, 2, 3, 4, 5])

#forEach
list = []
numbers.forEach(lambda item, index, array: 
    #使用元祖来确保两个handle都在lambda表达式中
    (print(f"Item: {item}, Index: {index}, Array: {array}"),
        list.append(item))
)
print(list)


# 调用 map 方法
squared_numbers = numbers.map(lambda item, index, array: item ** 2)
print(squared_numbers)


even_index = numbers.findIndex(lambda item, index, array: item % 2 == 0)
print(f"第一个偶数的位置是: {even_index}")


# 使用 splice 方法
removed_elements = numbers.splice(1, 2, 10, 20)
print(f"删除的元素: {removed_elements}")
print(f"修改后的列表: {numbers}")


# 调用 filter 方法
filtered_numbers = numbers.filter(lambda item, index, array: item % 2 == 0)
print(f"过滤后的列表: {filtered_numbers}")

#push和pop
numbers.push(100)
print(numbers)
numbers.pop()
print(numbers)


# 调用 reduce 方法
sum_of_numbers = numbers.reduce(lambda acc, item, index, array: acc + item, 0)
print(f"所有数字的和是: {sum_of_numbers}")

#flatmap 
print(numbers.join(","))
print(numbers.flatMap(lambda item: [item, item * 2]))

#includes
print(numbers.includes(100))
print(numbers.includes(1000))


```
2) Map 
```
# 使用示例
example_dict = Map({
    'a': 1,
    'b': 2,
    'c': 3
})


print("初始字典:", example_dict)

# 测试 set 方法
example_dict.set('d', 4)
print("设置键 'd' 后的字典:", example_dict)

# 测试 delete 方法
deleted_value = example_dict.delete('b')
print("删除键 'b' 后的字典:", example_dict)
print("被删除的值:", deleted_value)

# 测试 entries 方法
entries = example_dict.entries()
print("字典的键值对列表:", entries)

# 测试 filter 方法
filtered_dict = example_dict.filter(lambda key, value: value > 2)
print("过滤值大于 2 的键值对后的字典:", filtered_dict)

# 测试 forEach 方法
example_dict.forEach(lambda key, value: print(f"键: {key}, 值: {value}"))

```


3) match 
```
# 示例使用
response = {'status': 'success'}
# 匿名函数需要lambad关键字，add = lambda x, y: x + y

#使用列表推导式，不用续行符
result = [
    match(response)
    .with_(lambda x: x['status'] == 'success', lambda x: 'Success')
    .with_(lambda x: x['status'] == 'error', lambda x: 'Error')
    .otherwise(lambda x: 'Unknown')
    .execute()
][0]

print(result)  


```


## PS：

```
# 清理旧的构建文件
rm -rf dist/ build/ jssyntax.egg-info/

# 重新构建
python setup.py sdist bdist_wheel

# 上传到 PyPI
twine upload dist/* --verbose


```
