# 使用dict和set
names = {"蓝宇冰": "牛逼", "大蓝宇冰": "更牛逼"}
print(names["大蓝宇冰"])
names["大蓝宇冰"] =9527
print(names["大蓝宇冰"])

print("宇冰" in names)

print(names.get("宇冰","不存在"))