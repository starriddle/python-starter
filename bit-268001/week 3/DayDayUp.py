"""
天天向上的力量

工作日模式要努力到什么水平，才能与每天努力1%一样？
-A君: 一年365天，每天进步1%，不停歇
-B君: 一年365天，每周工作5天休息2天，休息日下降1% ，要多努力呢？
每周工作5天休息2天，计算工作日的努力参数是多少才能与每天努力1%一样。

要求如下：
(1) 一年365天，以第0天的能力值为基数，记为1.0；
(2) 当好好学习时，能力值相比前一天提高1%；当没有学习时，由于遗忘等原因能力值相比前一天下降1%；

输出结果结果保留小数点后三位，冒号后有一个空格）
"""

def weekUp(upfactor,downfactor):
    weekup = 1.0
    for i in range(365):
        if i % 7 in [6,0]:
            weekup *= 1 - downfactor
        else:
            weekup *= 1 + upfactor
    return weekup
def dayUp(factor):
    dayup = 1.0
    for i in range(365):
        dayup *= 1 + factor
    return dayup
result = dayUp(0.01)
weekdayfactor = 0.01
while weekUp(weekdayfactor, 0.01) < result:
    weekdayfactor += 0.001
print("工作日的努力参数是: {:.3f}".format(weekdayfactor))
