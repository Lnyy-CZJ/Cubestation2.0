import pandas as pd
import openpyxl

df =pd.read_excel("../fdata.xlsx",engine='openpyxl')

#计算排名
df['期中成绩排名'] = df['期中成绩'].rank(ascending=False, method='min')

# 计算平均分
average_score = df['期中成绩'].mean()

# 计算及格率
pass_rate = (df['期中成绩'] >= 66).mean()

# 计算优秀率
excellent_rate = (df['期中成绩'] >= 99).mean()

result_df = pd.DataFrame({
    '指标': ['平均分', '及格率', '优秀率'],
    '数值': [average_score, pass_rate, excellent_rate]
})
# 计算分数在区间1-3的人数和占比
range_count1 = df[df['期中成绩'].between(0, 65.5)].shape[0]
range_percentage1 = range_count1 / df.shape[0] * 100

# 计算分数在区间4-8的人数和占比
range_count2 = df[df['期中成绩'].between(66, 76.5)].shape[0]
range_percentage2 = range_count2 / df.shape[0] * 100

# 计算分数在区间9-10的人数和占比
range_count3 = df[df['期中成绩'].between(77, 87.5)].shape[0]
range_percentage3 = range_count3 / df.shape[0] * 100

range_count4 = df[df['期中成绩'].between(88, 98.5)].shape[0]
range_percentage4 = range_count4 / df.shape[0] * 100

range_count5 = df[df['期中成绩'].between(99, 105)].shape[0]
range_percentage5 = range_count5 / df.shape[0] * 100

range_count6 = df[df['期中成绩'].between(105.5, 120)].shape[0]
range_percentage6 = range_count6 / df.shape[0] * 100

print("0-66区间人数：", range_count1,"占比",range_percentage1)
print("66-76.5区间人数：", range_count2,"占比",range_percentage2)
print("区间人数：", range_count3,"占比",range_percentage3)
print("区间人数：", range_count4,"占比",range_percentage4)
print("区间人数：", range_count5,"占比",range_percentage5)
print("区间人数：", range_count6,"占比",range_percentage6)
print(result_df)

# # 将结果输出到新的Excel表格
# df.to_excel('out3.xlsx', sheet_name='结果')
# result_df.to_excel('成绩统计结果.xlsx', index=False)


# df['第一单元排名'] = df['第一单元'].rank(ascending=False, method='min')
# df['第二单元排名'] = df['第二单元'].rank(ascending=False, method='min')
# df['进退一'] = df['第一单元排名'] - df['第二单元排名']
#
# df['复习一排名'] = df['复习一'].rank(ascending=False, method='min')
# df['进退二'] = df['第二单元排名'] - df['复习一排名']
#
# df['复习二排名'] = df['复习二'].rank(ascending=False, method='min')
# df['进退三'] = df['复习一排名'] - df['复习二排名']
#
# df['第三单元排名'] = df['第三单元'].rank(ascending=False, method='min')
# df['进退四'] = df['复习二排名'] - df['第三单元排名']

# df['第四单元排名'] = df['第四单元'].rank(ascending=False, method='min')
# df['进退五'] = df['第三单元排名'] - df['第四单元排名']

# print(df)
# df.to_excel('out3.xlsx', sheet_name='结果')



#测试代码
# data = {'A': [1, 2, 3,3,4,5,9,6],
#         'B': [1, 1, 3,5,4,5,8,6]}
# df = pd.DataFrame(data)
# df['A排名'] = df['A'].rank(ascending=False, method='min')
# df['B排名'] = df['B'].rank(ascending=False, method='min')
# # 计算分数在区间1-3的人数和占比
# range_1_3_count = df[df['A'].between(1, 3)].shape[0]
# range_1_3_percentage = range_1_3_count / df.shape[0] * 100
#
# # 计算分数在区间4-8的人数和占比
# range_4_8_count = df[df['A'].between(4, 8)].shape[0]
# range_4_8_percentage = range_4_8_count / df.shape[0] * 100
#
# # 计算分数在区间9-10的人数和占比
# range_9_10_count = df[df['A'].between(9, 10)].shape[0]
# range_9_10_percentage = range_9_10_count / df.shape[0] * 100
#
# print("区间1-3的人数：", range_1_3_count)
# print("区间1-3的占比：", range_1_3_percentage)
# print("区间4-8的人数：", range_4_8_count)
# print("区间4-8的占比：", range_4_8_percentage)
# print("区间9-10的人数：", range_9_10_count)
# print("区间9-10的占比：", range_9_10_percentage)
# print(df)