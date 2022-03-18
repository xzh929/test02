a = 1
for i in range(9, 0, -1):
    b = (a+1)*2
    a = b
print(a)

c = 2.0
d = 1.0
sum = 0
for i in range(0,21):
    sum += c/d
    temp = c
    c = c+d
    d = temp
print(sum)


def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
sum1 = 0
for i in range(1,21):
    sum1 += factorial(i)
print(sum1)

test_list = [0, 0, 1, 1, 2, 3, 4, 5, 5]
print(list(set(test_list)))


test_str = 'string'
anti_str = test_str[::-1]
print(anti_str)


test_list1 = [0, 0, 1, 1, 2, 3, 4, 5, 5]
sum2 = sum(map(lambda x: x+3, test_list1[1::2]))
print(sum2)


test_list2 = [-2, 1, 3, -6]
test_list2.sort(key=abs)
print(test_list2)


test_list3 = [-2, 1, 3, -6]
test_list4 = [-2, 1, 3, -6]
merge_list = test_list3+test_list4
print(merge_list)


# lambda可以定义多个参数行为，并用单一值返回。构造函数，符号重载等
# 元组元素不能修改，列表元素能修改，字典以键值对存储数据且无序


alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
sort_list = sorted(alist,key=lambda x:x['age'],reverse=True)
print(sort_list)


test_str = 'k:1|k1:2|k2:3|k3:4'
cut_str = test_str.split('|')
test_dict = dict()
for i in cut_str:
    cut_str1 = i.split(':')
    test_dict[cut_str1[0]] = int(cut_str1[1])
print(test_dict)


def fib(n): #
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)


n = input('输入几项：')
for i in range(1, int(n)+1):
    print(fib(i))


class student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)


zm = student('zhangming',20,[69,88,100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())


class dictclass():
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        self.dict.pop(key)

    def get_dict(self, key):
        if key in self.dict:
            return self.dict[key]
        return 'not found'

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()


test_dict1 = dictclass({'a': 1, 'b': 2, 'c': 3})
print(test_dict1.get_dict('c'))
print(test_dict1.del_dict('c'))
print(test_dict1.get_key())
print(test_dict1.update_dict({'d': 4, 'e': 5}))


class Listinfo():
    def __init__(self, list_value):
        self.list = list_value

    def add_key(self, key_name):
        self.list.append(key_name)
        return self.list

    def get_key(self, num):
        return self.list[num]

    def update_list(self, new_list):
        self.list.extend(new_list)
        return self.list

    def del_key(self):
        return self.list.pop(-1)


list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])
print(list_info.add_key('1'))
print(list_info.get_key(2))
print(list_info.update_list([1, 2]))
print(list_info.del_key())


class Setinfo():
    def __init__(self,set_value):
        self.set = set_value

    def add_setinfo(self,key_name):
        self.set.add(key_name)
        return self.set

    def get_intersection(self,another_set):
        return self.set & another_set

    def get_union(self, another_set):
        return self.set | another_set

    def del_different(self, another_set):
        return self.set - another_set


set1 = set([1, 2, 3, 4, 5])
set2 = set([2, 7])
set_info = Setinfo(set1)
print(set_info.add_setinfo(8))
print(set_info.get_intersection(set2))
print(set_info.get_union(set2))
print(set_info.del_different(set2))


class Student():
    def __init__(self, name, age, sex, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

    def display(self):
        return print('名字：', self.name, '年龄：', self.age, '性别：', self.sex, '住址：',self.address)


student = Student('xzh', 24, '男', '成都')
student.display()