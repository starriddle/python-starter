#!/usr/bin/python3

"""
实例5：身体质量指数BMI

BMI ：Body Mass Index 国际上常用的衡量人体肥胖和健康程度重要标准，主要用于统计分析
定义：BMI = 体重 (kg) /身高2(m2)
获取用户输入的身高和体重值，计算并给出国际和国内的 BMI 分类

分类      国际BMI值      国内BMI值
偏瘦      < 18.5          < 18.5
正常      18.5 ~ 25       18.5 ~ 24
偏胖      25 ~ 30         24 ~ 28
肥胖      >= 30           >=28

要求如下：
(1) 混合计算并给出国际和国内的 BMI 分类；
(2) 使用input()获得测试用例输入时，不要增加提示字符串。
"""

height, weight = eval(input())
bmi = weight / height ** 2
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif bmi < 24:
    who, nat = "正常", "正常"
elif bmi < 25:
    who, nat = "正常", "偏胖"
elif bmi < 28:
    who, nat = "偏胖", "偏胖"
elif bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI数值为:{:.2f}".format(bmi))
print("BMI指标为:国际'{}',国内'{}'".format(who, nat))
