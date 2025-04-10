# 集合的定义：集合是 可变的、无序的、元素唯一 的容器，用 花括号 {} 或 set() 创建。
# 创建集合
set1 = {1,2,3,4,"haha"}
print(set1)
set3 = set([2,3,6,7,8,9,"helow",(1,2,"good")])
print(set3)
# 创建空集合
set2 = set()
print(set2)

# 集合的基本操作
# 添加元素
set1.add("new")
print(set1)
set1.update([5,6,7])
print(set1)
# 删除元素
set1.remove(5)  # 如果元素不存在，会报错
print(set1)
set1.discard(5) # 如果元素不存在，不会报错
print(set1)
set1.pop() # 随机删除一个元素
print(set1)

# 集合的运算
setA = {1, 2, 3, 4} 
setB = {3, 4, 5, 6}
# 并集
setC = setA | setB
print(setC)
# 交集
setD = setA & setB
print(setD)
# 差集:只在 setA 中存在的元素
setE = setA - setB
print(setE) 
# 对称差集:仅在 setA 或 setB 中存在的元素
setF = setA ^ setB
print(setF)

# 集合的其他操作 
# 判断元素是否在集合中  
print(1 in setA)    
print(5 not in setA)
# 集合的长度
print(len(setA))
# 清空集合
setA.clear()
print(setA)
# 集合的拷贝
setG = setB.copy()
print(setG)
