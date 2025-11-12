import pprint


"""
house_ID: Identification number for reach house
            format -> HXXXXX (H00001), (H12049)
date: Date for each year that data was taken
        format -> MM/DD/YYYY
energy_consumption_kwh: total energy consumed on a date in kwh
household size: size of household by person count
has_ac: has ac or not
avg_temp_c: The average temperature in Celsius outside the household. (external)
peak_hours_usage_kwh: Energy usage in kwh during high demand hours of the date.
"""

class Household:
    def __init__(
            self,
            house_id:str,
            dates:list[str],
            energy_consumption_kwh:list[float],
            household_size:int,
            has_ac:bool,
            avg_temp_c:list[float],
            peak_hours_usage_kwh:list[float]
            ):
        self.house_id = house_id
        self.ac = has_ac
        self.dates = dates
        self.household_size = household_size
        self.data = {date: {} for date in dates}
        for i, date in enumerate(self.dates):
            self.data[date]['total kwh'] = energy_consumption_kwh[i]
            self.data[date]['avg temp c'] = avg_temp_c[i]
            self.data[date]['peak hours usage kwh'] = peak_hours_usage_kwh[i]

    def __repr__(self):
        return (
            'house_id: {},\n'
            'household size: {},\n'
            'has_ac: {},\n'
            'dates recorded: {} - {}\n'
            'all data recorded:\n{}'
        ).format(
            self.house_id,
            self.household_size,
            self.ac,
            self.dates[0],
            self.dates[-1],
            pprint.pformat(self.data, indent=4)
        )
    def __eq__(self, other):
        return (self is other or
        type(self) is type(other) and
        self.house_id == other.house_id and
        self.household_size == other.household_size and
        self.ac == other.ac and
        self.dates == other.dates and
        self.data == other.data
                )

    # Calculates the average total consumption of a household in kWh
    def calc_avg_consumption(self)->float:
        total_sum = 0
        for point in self.data:
            total_sum += self.data[point]['total kwh']
        return round(total_sum / len(self.data),3)

    # Calculates the average peak hour consumption of a household in kWh
    def calc_avg_peak_hours(self)->float:
        total_sum = 0
        for point in self.data:
            total_sum += self.data[point]['peak hours usage kwh']
        return round(total_sum / len(self.data),3)
