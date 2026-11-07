# 根据之前的学习，int/str/tuple都是不可变的
# list/dict(value部分)/set都是可变的
# id的值是会变的

# 不可变：改了的话其实就是创建了一个新对象
a = "hello"
print(id(a))            # 123279287739824
a = a + " world"            
print(id(a))                # 128395353100784
# 可以看到str再改变之后两次的id值并不一样，说明它们不再是同一个变量


# 可变：对变量的修改不会改变id值，说明还是同一个变量空间
lst = [1, 2, 3]
print(id(lst))         # 138667602976000
lst.append(4)       
print(id(lst))          # 138667602976000
# 可以看到两次id值相同，说明它们还是同一变量空间

# 注意：默认参数是可变对象(这里使用了函数的相关知识)
# 但是，函数的默认参数一定不要写可变对象，写target=None（可以让函数自己判断类型）
def add(item, target=[]):           # 危险 不能这么写
    target.append(item)
    return target

print(add(1))       # [1]
print(add(2))           # [1, 2]