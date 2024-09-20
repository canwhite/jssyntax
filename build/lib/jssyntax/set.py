class Set(set):
    def forEach(self, func):
        for item in self:
            func(item)
        return self

    def map(self, func):
        result = []
        for item in self:
            result.append(func(item))
        return Set(result)

    def has(self, item):
        return item in self    

    def filter(self, func):
        result = []
        for item in self:
            if func(item):
                result.append(item)
        return Set(result)
        
    # add 方法中调用了 self.add(item) 而不是 super().add(item)，导致无限递归。
    def add(self, item):
        super().add(item)
        return self

    def delete(self, item):
        if item in self:
            self.remove(item)
        return self

    def clear(self):
        super().clear()
        return self

    def size(self):
        return len(self)

    def values(self):
        return list(self)

    def union(self, other_set):
        return Set(self | other_set)

    def intersection(self, other_set):
        return Set(self & other_set)

    def difference(self, other_set):
        return Set(self - other_set)

    def isSubsetOf(self, other_set):
        return self <= other_set

    def isSupersetOf(self, other_set):
        return self >= other_set


if __name__ == "__main__":


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

    # 测试 isSubsetOf 方法
    subset_set = Set([1, 2, 3])
    print("集合是否是另一个集合的子集:", subset_set.isSubsetOf(example_set))

    # 测试 isSupersetOf 方法
    print("集合是否是另一个集合的超集:", example_set.isSupersetOf(subset_set))