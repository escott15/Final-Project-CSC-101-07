###
from data import Household

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
input type: str, list or None
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


# This function that, given a list of households and an energy consumption threshold value, will return
# a dictionary resembling a statistical two-way table. Each entry of the table will be determined by whether
# a house has an AC or not and whether a household's energy consumption exceeds the threshold value.
# Inputs: list[Household], float
# Output: dict[str,int]
def create_ac_dict(households:list[Household], threshold:float)->dict[str,int]:
    over_ac = 0
    over_no_ac = 0
    under_ac = 0
    under_no_ac = 0
    for house in households:
        over_or_under = over_threshold(house.calc_avg_consumption(), threshold)
        if over_or_under and house.ac:
            over_ac += 1
        elif over_or_under and not house.ac:
            over_no_ac += 1
        elif not over_or_under and house.ac:
            under_ac += 1
        else:
            under_no_ac += 1
    return {
        'Overconsumption with AC': over_ac,
        'Overconsumption without AC': over_no_ac,
        'Underconsumption with AC': under_ac,
        'Underconsumption without AC': under_no_ac,
    }

# This function that, given a list of households, a threshold value for total energy consumption and
# a threshold value for consumption during peak hours, will return a dictionary resembling a statistical
# two-way table. Each entry of the table will be determined by whether a household's total and peak hour
# energy consumption exceeds the threshold value.
# Inputs: list[Household], float, float
# Output: dict[str,int]
def create_peak_hours_dict(households:list[Household], threshold_t:float, threshold_p:float)->dict[str,int]:
    t_over_p_over = 0
    t_over_p_under = 0
    t_under_p_over = 0
    t_under_p_under = 0
    for house in households:
        over_under_t = over_threshold(house.calc_avg_consumption(), threshold_t)
        over_under_p = over_threshold(house.calc_avg_peak_hours(), threshold_p)
        if over_under_t and over_under_p:
            t_over_p_over += 1
        elif over_under_t and not over_under_p:
            t_over_p_under += 1
        elif not over_under_t and over_under_p:
            t_under_p_over += 1
        else:
            t_under_p_under += 1
    return {
        'Total energy over threshold and energy during peak hours over threshold': t_over_p_over,
        'Total energy over threshold and energy during peak hours under threshold': t_over_p_under,
        'Total energy under threshold and energy during peak hours over threshold': t_under_p_over,
        'Total energy under threshold and energy during peak hours under threshold': t_under_p_under,
    }
