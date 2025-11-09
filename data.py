


class Household:
    def __init__(
            self,
            house_id:str,
            dates:list[str],
            energy_consumption_kwh:list[float],
            household_size:int,
            avg_temp_c:list[float],
            has_ac:str,
            peak_hours_kwh_usage:list[float]
        ):
        self.house_id = house_id
        self.dates = dates
        self.energy_consumption_kwh = energy_consumption_kwh
        self.household_size = household_size
        self.avg_temp_c = avg_temp_c
        self.has_ac = has_ac
        self.peak_hours_kwh_usage = peak_hours_kwh_usage

    def __repr__(self):
        return ("Household Details:\n"
                "ID- {}\n"
                "Dates Monitored- {}\n"
                "Energy Consumption in kWh (per day): {}\n"
                "Household size: {}\n"
                "Average Temperature in C: {}\n"
                "AC in Household: {}\n"
                "Hours of Consumption During Peak Hours: {}\n".format(
                self.house_id,
                self.dates,
                self.energy_consumption_kwh,
                self.household_size,
                self.avg_temp_c,
                self.has_ac,
                self.peak_hours_kwh_usage))

    def calc_avg_consumption(self):
        sum = 0
        for n in self.energy_consumption_kwh:
            sum += n
        return sum / len(self.energy_consumption_kwh)

    def calc_avg_temp(self):
        sum = 0
        for n in self.avg_temp_c:
            sum += n
        return sum / len(self.avg_temp_c)

    def calc_avg_peak_hours(self):
        sum = 0
        for n in self.peak_hours_kwh_usage:
            sum += n
        return sum / len(self.peak_hours_kwh_usage)

