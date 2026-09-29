# -*- coding: utf-8 -*-
"""简单数据处理示例：数组、求和、排序"""

# 数组
nums = [8, 3, 15, 6, 9, 2, 11]

# 求和
total = sum(nums)

# 排序（升序 / 降序）
asc = sorted(nums)
desc = sorted(nums, reverse=True)

# 统计
avg = total / len(nums)

print("原数组:", nums)
print("求和:", total)
print("平均值:", avg)
print("最大值:", max(nums), "最小值:", min(nums))
print("升序:", asc)
print("降序:", desc)
