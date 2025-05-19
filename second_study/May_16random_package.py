# random：生成伪随机数和随机选择
import random
print(f"生成一个0-1范围内的随机浮点数：{random.random()}")

print(f"生成一个【2-10】范围内的随机浮点数：{random.uniform(2,10)}")

print(f"生成一个【2，10】范围内的随机整数：{random.randint(2,10)}")

list1 = ["西瓜","圣女果","哈密瓜","葡萄"]
print(f"从非空序列中随机选择一个元素：{random.choice(list1)}")