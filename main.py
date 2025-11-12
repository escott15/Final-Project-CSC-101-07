
from household_energy_consumption import *

totaldataorganized = create_households()

"""
Sorts any given list of floats or int into ascending order
input type: list of floats or int or str
output type: none 
"""
def insertion_sort(lst: list[float | int | str ])-> None:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j+1] = key

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

def median_households_totalkwh(data=None)-> float:
    median_lst = []
    if data is None:
        data = totaldataorganized
    for item in data:
        for date in item:
            median_lst.append(item.get(date))

