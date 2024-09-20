## jssyntax

Write python using js syntax

## Installation
pip install jssyntax

## Usage

1) List
```

from jssyntax import List

numbers = List([1, 2, 3, 4, 5])

# 调用forEach方法
list = []
numbers.forEach(lambda item, index, array: 
    #使用元组来确保两个handle都在lambda表达式中
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

# 测试 forEach 方法
example_dict.forEach(lambda key, value: print(f"键: {key}, 值: {value}"))

# 测试map方法
mapped_dict = example_dict.map(lambda key, value: (key.upper(), value * 2))
print("将键转换为大写，值乘以 2 后的字典:", mapped_dict)

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

```

3) Set
```
# 创建一个集合
example_set = Set([1, 2, 3, 3, 4, 5])
print("初始集合:", example_set)

# 测试 forEach 方法
example_set.forEach(lambda item: print(f"元素: {item}"))

# 测试 map 方法
mapped_set = example_set.map(lambda item: item * 2)
print("映射后的集合:", mapped_set)

# 测试 has 方法
print("集合中是否包含 3:", example_set.has(3))
print("集合中是否包含 6:", example_set.has(6))

# 测试 filter 方法
filtered_set = example_set.filter(lambda item: item % 2 == 0)
print("过滤后的集合:", filtered_set)

# 测试 add 方法
example_set.add(6)
print("添加元素 6 后的集合:", example_set)

# 测试 delete 方法
example_set.delete(3)
print("删除元素 3 后的集合:", example_set)

# 测试 clear 方法
example_set.clear()
print("清空后的集合:", example_set)

# 测试 size 方法
example_set = Set([1, 2, 3, 4, 5])
print("集合的大小:", example_set.size())

# 测试 values 方法
print("集合的所有值:", example_set.values())

# 测试 union 方法
other_set = Set([4, 5, 6, 7])
union_set = example_set.union(other_set)
print("两个集合的并集:", union_set)

# 测试 intersection 方法
intersection_set = example_set.intersection(other_set)
print("两个集合的交集:", intersection_set)

# 测试 difference 方法
difference_set = example_set.difference(other_set)
print("两个集合的差集:", difference_set)

```


4) match 
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
