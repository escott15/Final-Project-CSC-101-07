
from household_energy_consumption import *

totaldataorganized = create_households()

"""
Sorts any given list of floats or int into ascending order
input type: list of floats or int or str
output type: none 
"""
# Given an input float and a threshold float, return True if input is larger than threshold, return False otherwise
def over_threshold(value:float,threshold:float)->float:
    if value > threshold:
        return True
    else:
        return False
"""
the purpose of this function is to get the median of the total_kwh of all the households
input type: none
output type: Float 
"""
def median_calc(arg:str, data:list[int|float|str]=None)-> float | None:
    median_lst = []
    median = 0
    if data is None:
        data = totaldataorganized
        if arg == 'total kwh':
            for item in data:
                for date in item.data:
                    median_lst.append(item.data.get(date).get('total kwh'))
            list.sort(median_lst)
            median = round(len(median_lst) / 2)
        elif arg == 'peak hours usage kwh':
            for item in data:
                for date in item.data:
                    median_lst.append(item.data.get(date).get('peak hours usage kwh'))
            list.sort(median_lst)
            median = round(len(median_lst) / 2)
        elif arg == 'avg temp c':
            for item in data:
                for date in item.data:
                    median_lst.append(item.data.get(date).get('avg temp c'))
            list.sort(median_lst)
            median = round(len(median_lst) / 2)
    else:
        for i in data:
            median_lst.append(i)
            list.sort(median_lst)
            median = round(len(median_lst) / 2)
    return median_lst[median]

if __name__ == '__main__':
    print(median_calc('peak hours usage kwh'))
