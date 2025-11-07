


class Household:
    def __init__(
            self,
            house_id:str,
            dates:list[str],
            energy_consumption_kwh:list[float],
            household_size:list[int],
            avg_temp_c:list[float],
            has_ac:list[bool],
            peak_hours_kwh_usage:list[float]
        ):
        self.house_id = house_id
        self.dates = dates
        self.energy_consumption_kwh = energy_consumption_kwh
        self.household_size = household_size
        self.avg_temp_c = avg_temp_c
        self.has_ac = has_ac
        self.peak_hours_kwh_usage = peak_hours_kwh_usage
