from data import *


def create_households()->list[Household]:
    main_data = open('household_energy_consumption.txt', 'r')
    data_list = main_data.readlines()
    main_data.close()

    data_set = []
    for string in data_list:
        string = string.strip("\n")
        new_list = string.split(',')
        data_set.append(new_list)

    i_d = data_set[0][0]
    dates = []
    energy_consumption_kwh = []
    household_size = ''
    avg_temp = []
    has_ac = ''
    peak_hours = []
    house_data = []
    for data in data_set:
        if data[0] == i_d:
            dates.append(data[1])
            energy_consumption_kwh.append(float(data[2]))
            household_size = data[3]
            avg_temp.append(float(data[4]))
            if data[5] == 'Yes':
                has_ac = True
            elif data[5] == 'No':
                has_ac = False
            peak_hours.append(float(data[6]))
        else:
            house_data.append(Household(i_d, dates, energy_consumption_kwh, int(household_size),has_ac,avg_temp,peak_hours))
            i_d = data[0]
            dates = [data[1]]
            energy_consumption_kwh = [float(data[2])]
            household_size = data[3]
            avg_temp = [float(data[4])]
            if data[5] == 'Yes':
                has_ac = True
            elif data[5] == 'No':
                has_ac = False
            peak_hours = [float(data[6])]
    house_data.append(Household(i_d, dates, energy_consumption_kwh, int(household_size),has_ac,avg_temp,peak_hours))

    return house_data

print(create_households()[200].calc_avg_peak_hours())




