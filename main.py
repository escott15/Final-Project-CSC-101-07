###
import pandas as pd
from household_energy_consumption import *

totaldataorganized = create_households()

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

# This function that, given a list of households and a total energy consumption threshold value, will return
# a dictionary resembling a statistical two-way table. Each entry of the table will be determined by whether
# a house has an AC or not and whether a household's energy consumption exceeds the threshold value.
# (Note: energy in kWh)
# Inputs: list[Household], float
# Output: dict[str,int]
def create_ac_dict(households:list[Household], threshold:float)->dict[str,int]:
    over_ac = 0
    over_no_ac = 0
    under_ac = 0
    under_no_ac = 0
    for house in households:
        over_or_under = house.calc_avg_consumption() > threshold
        if over_or_under and house.ac:
            over_ac += 1
        elif over_or_under and not house.ac:
            over_no_ac += 1
        elif not over_or_under and house.ac:
            under_ac += 1
        else:
            under_no_ac += 1
    return {
        'Total Over, has AC': over_ac,
        'Total Over, no AC': over_no_ac,
        'Total Under, has AC': under_ac,
        'Total Under, no AC': under_no_ac,
    }

# This function takes in a dictionary created by create_ac_dict() and converts it into a two-way table.
# The function then prints the two-way table, returning nothing
# Input: dict[str,int]
# Output: None (function prints)
def ac_crosstab(dict_data:dict[str,int])->None:
    over_ac = dict_data['Total Over, has AC']
    over_no = dict_data['Total Over, no AC']
    under_ac = dict_data['Total Under, has AC']
    under_no = dict_data['Total Under, no AC']
    df = pd.DataFrame(
        {
            'Usage Over': [over_ac, over_no, over_ac+over_no],
            'Usage Under': [under_ac, under_no, under_ac+under_no],
            'Total' : [over_ac+under_ac, over_no+under_no, over_ac+over_no+under_ac+under_no]
        },
        index= ["Has AC", "No AC", "Total"]
    )
    print(df)

# This function that, given a list of households, a threshold value for total energy consumption and
# a threshold value for consumption during peak hours, will return a dictionary resembling a statistical
# two-way table. Each entry of the table will be determined by whether a household's total and peak hour
# energy consumption exceeds the threshold value. (Note: energy in kWh)
# Inputs: list[Household], float, float
# Output: dict[str,int]
def create_peak_dict(households:list[Household], threshold_t:float, threshold_p:float)->dict[str,int]:
    t_over_p_over = 0
    t_over_p_under = 0
    t_under_p_over = 0
    t_under_p_under = 0
    for house in households:
        over_under_t = house.calc_avg_consumption() >threshold_t
        over_under_p = house.calc_avg_peak_hours() > threshold_p
        if over_under_t and over_under_p:
            t_over_p_over += 1
        elif over_under_t and not over_under_p:
            t_over_p_under += 1
        elif not over_under_t and over_under_p:
            t_under_p_over += 1
        else:
            t_under_p_under += 1
    return {
        'Total over, Peak over': t_over_p_over,
        'Total over, Peak under': t_over_p_under,
        'Total under, Peak over': t_under_p_over,
        'Total under, Peak under': t_under_p_under,
    }

# This function takes in a dictionary created by create_peak_dict() and converts it into a two-way table.
# The function then prints the two-way table, returning nothing
# Input: dict[str,int]
# Output: None (function prints)
def peak_crosstab(dict_data:dict[str,int])->None:
    to_po = dict_data['Total over, Peak over']
    to_pu = dict_data['Total over, Peak under']
    tu_po = dict_data['Total under, Peak over']
    tu_pu = dict_data['Total under, Peak under']
    df = pd.DataFrame(
        {
            'Usage Over': [to_po, to_pu, to_po+to_pu],
            'Usage Under': [tu_po, tu_pu, tu_po+tu_pu],
            'Total' : [to_po+tu_po, to_pu+tu_pu, to_po+to_pu+tu_po+tu_pu]
        },
        index= ["Peak Over", "Peak Under", "Total"]
    )
    print(df)


if __name__ == '__main__':
    median1 = median_calc('total kwh')
    data1 = create_ac_dict(totaldataorganized, median1)
    ac_crosstab(data1)

    median2 = median_calc('peak hours usage kwh')
    data2 = create_peak_dict(totaldataorganized, median1, median2)
    peak_crosstab(data2)



