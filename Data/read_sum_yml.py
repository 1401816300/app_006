import yaml

# 空列表
sum_list = []
# 打开文件
with open("./sum.yml", "r") as f:
    # yaml读取文件
    data = yaml.safe_load(f)
    print("data:", data)
    # print("values:",data.values()) # 返回列表 存储所有values
    for i in data.values():
        # print("tup:", (i.get("a"), i.get("b"), i.get("c")))
        # 添加元组数据到列表
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
print("sum_list:", sum_list)
