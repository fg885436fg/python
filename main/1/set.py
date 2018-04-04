#set 不能重复
s = set([1, 2, 3,4,4,4,4,])

s.add(5)
s.add(5)
s.remove(5)
print(s)

#不可变对象
a="abc";
b =a.replace("a","A");
print(a);
print(b);