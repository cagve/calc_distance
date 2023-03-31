import axiom as ax
import distance as dis
from itertools import chain, combinations, product

def powerset(iterable):
    powerset = list(chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1)))
    return powerset

def list_to_string(list_of_list):
    """
    List of lists into list of string
    """
    list_of_string = []
    for t in list_of_list:
        list_of_list.append(str(t))
        print(t)
    return list_of_string

def tuple_to_list(list_of_tuples):
    """
    List of tuples into list of list
    """
    list_of_list = []
    for t in list_of_tuples:
        list_of_list.append(list(t))
    return list_of_list
    

# Function that create all possibles combinations over valuations of size m.
def generate_valuations(n):
    valuations_list = list(product([0,1], repeat=n))
    return valuations_list


def compute_display(valset,func):
    result = []
    for i in valset:
        row = [] 
        for j in valset:
            row.append(func(i,j))
        result.append(row)
    return result

def satisfy_axiom(valset,func):
    m = combinations(valset, 3)
    for i in m: 
       ax.satisfy_metric_3(i[0],i[1],i[2],func) 

def test():
    val = generate_valuations(3)
    val = tuple_to_list(val)
    valset = list(powerset(val))
    valset = tuple_to_list(valset)
    valstr = list(map(lambda set_val: str(set_val), valset))

    # rows = compute(valset,dis.sum_min_set_element)
    satisfy_axiom(valset,dis.sum_min_set_element)

    # df = pd.DataFrame(rows)
    # df.columns = valstr
    # df.index = valstr
    # print(df)
    print("FINISHED")

test()
