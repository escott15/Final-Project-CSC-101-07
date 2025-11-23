from data import *

# This function is specifically designed to read the 'household_energy_consumption.txt' file and convert
# all the lines of text into a list of Household class objects
# Input: None (Although the 'household_energy_consumption.txt' file is required to run anything
# Output: list[Household]
def create_households()->list[Household]:
    # Open and read the 'household_energy_consumption.txt' file, then use .readline() function to
    # create a list that can be operated on
    main_data = open('household_energy_consumption.txt', 'r')
    data_list = main_data.readlines()
    main_data.close()

    # This segment modifies the elements of data_list so that each string is stripped of new lines and
    # turned into a list where each element is a data point for a household on a given day. Append that
    # list to data_set
    data_set = []
    for string in data_list:
        string = string.strip("\n")
        new_list = string.split(',')
        data_set.append(new_list)

    # In this segment, for every list in data_set, gather all the data for an individual household over the
    # course of a week and store each data point into its own categorical list. Once the loop encounters a
    # new household, create a household object with the lists and repeat.
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

if __name__ == '__main__':
    #print(create_households()[200].calc_avg_peak_hours())
    #print('\n')
    #print(create_households()[400])
    #print('\n')
    print(create_households()[600])
    #print('\n')





