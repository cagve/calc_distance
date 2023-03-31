from scipy.spatial.distance import hamming
import distance as dis



def hamming_distance(list1,list2):
    """
    Hamming distance between two strings. If it is a list convert it to string.
    """
    if type(list1) == list:
        list1 = str(list1)
    if type(list2) == list:
        list2 = str(list2)

    return sum(c1 != c2 for c1, c2 in zip(list1, list2))


def min_dis_xY(valuationX,setY):
    """
    Minimum distance between set and a point
    """
    min = 0
    if len(setY) == 0:
        min = len(valuationX)
    else:
        min = hamming_distance(valuationX,setY[0])
        for valuationY in setY:
            if min > hamming_distance(valuationX,valuationY):
                min = hamming_distance(valuationX,valuationY)
    return min 


