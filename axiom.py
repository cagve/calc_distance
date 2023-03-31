def satisfy_metric_1(set1,set2, dfunc):
    dis = dfunc(set1,set2)
    if set1==set2 and dis!=0:
        print("Not satisfy ax1")

def satisfy_metric_2(set1,set2,dfunc):
    dis1 = dfunc(set1,set2)
    dis2 = dfunc(set2,set1)
    if dis1 != dis2:
        print("Not satisfy ax2")

def satisfy_metric_3(set1,set2,set3,dfunc):
    dis1 = dfunc(set1,set2)
    dis2 = dfunc(set2,set3)
    dis3 = dfunc(set1,set3)

    if not dis3<=dis1+dis2:
        print("Not satisfy ax3")
