import inspect

class Map(dict):
    
    def forEach(self, func):
        for key, value in self.items():
            if len(inspect.signature(func).parameters) == 1:
                func(key)
            elif len(inspect.signature(func).parameters) == 2:
                func(key, value)
            else:
                func(key, value, self)
        return self

    def map(self, func):
        """
        实现类似 JavaScript 中的 map 方法。
        :param func: 映射函数，返回新的键值对
        :return: 映射后的新字典
        """
        result = {}
        for key, value in self.items():
            if len(inspect.signature(func).parameters) == 1:
                new_key, new_value = func(value)
            elif len(inspect.signature(func).parameters) == 2:
                new_key, new_value = func(key, value)
            else:
                new_key, new_value = func(key, value, self)
            result[new_key] = new_value
        return Map(result)

    def keys(self):
        """
        返回字典中所有键的列表。
        :return: 键的列表
        """
        return list(self.keys())


    def values(self):
        """
        返回字典中所有值的列表。
        :return: 值的列表
        """
        return list(self.values())

    def set(self, key, value):
        """
        设置字典中指定键的值。
        :param key: 键
        :param value: 值
        :return: 更新后的字典
        """
        self[key] = value
        return self
    
    def delete(self, key):
        """
        删除字典中指定的键。
        :param key: 要删除的键
        :return: 删除的值，如果键不存在则返回 None
        """
        if key in self:
            value = self[key]
            del self[key]
            return value
        return None

    def entries(self):
        """
        返回字典中所有键值对的列表。
        :return: 键值对的列表
        """
        return [(key, value) for key, value in self.items()]

    def filter(self, func):
        result = {}
        for key, value in self.items():
            if len(inspect.signature(func).parameters) == 1:
                if func(key):
                    result[key] = value
            elif len(inspect.signature(func).parameters) == 2:
                if func(key, value):
                    result[key] = value
            else:
                if func(key, value, self):
                    result[key] = value
        return Map(result)
        
    def size(self):
        """
        返回字典中键值对的数量。
        :return: 键值对的数量
        """
        return len(self)

    def clear(self):
        """
        清空字典中的所有键值对。
        :return: 清空后的字典
        """
        super().clear()
        return self
    

if __name__ == '__main__':
    # 使用示例
    example_dict = Map({
        'a': 1,
        'b': 2,
        'c': 3
    })


    print("初始字典:", example_dict)

    # 测试 forEach 方法
    example_dict.forEach(lambda key, value: print(f"键: {key}, 值: {value}"))
    # 测试 map 方法
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


    # size
    print(example_dict.size())
    #clear
    example_dict.clear()
    print(example_dict)
    
