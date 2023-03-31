import functions as func

def sum_min_set_element(list1,list2):
    # to instanciate compute(valset,func.sum_min_set_element)
    distance = 0
    for element in list1:
        distance = distance+func.min_dis_xY(element,list2)
    for element in list2:
        distance = distance+func.min_dis_xY(element,list2)
    return distance
