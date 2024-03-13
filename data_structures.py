#!/usr/bin/env python3


from datetime import datetime


# global variables:
week_parity_code = 1        # 0, 1
is_holiday = False          # False, True
weekly_activities = []
other_activities = []
deadlines = []



class WeeklyActivity:
    def __init__(self, name, location, description, day, start_time, stop_time, week_parity):
        self.name = name
        self.location = location
        self.description = description
        self.day = day
        self.start_time = start_time
        self.stop_time = stop_time
        self.week_parity = week_parity

    def __str__(self):
        to_string = ''
        
        if self.stop_time in [None, '', '-']:
            to_string = f"{self.name}, begins at {self.start_time}, {self.location}"
        else:
            to_string = f"{self.name}, {self.start_time} - {self.stop_time}, {self.location}"
        
        return to_string

    @staticmethod
    def new(name, location, description, day, start_time, stop_time, week_parity):
        """ un constructor mai restrictiv:
        imi doresc ca field-urile sa faca parte dintr-o multime specifica de valori
        """

        err_msg = ''

        valid_start_t = is_valid_h_m(start_time)
        valid_stop_t = is_valid_h_m(stop_time)

        if not valid_start_t:
            err_msg += f"Err: Invalid start time `{start_time}`; expected `%H:%M` format\n" 
        
        if not valid_stop_t and stop_time not in ['-', '']:
            err_msg += f"Err: Invalid stop time `{stop_time}`; expected `%H:%M` format\n"
        
        if valid_start_t and valid_stop_t and stop_time not in ['-', '']:
            start_timestamp = get_timestamp(start_time)
            stop_timestamp = get_timestamp(stop_time)
            if start_timestamp > stop_timestamp:
                err_msg += f"Err: Invalid time schedule {start_time} -> {stop_time}"
        

        if not is_valid_day_str(day):
            err_msg += f"Err: Invalid name of a day {day}"


        if err_msg == '':
            print(f"{err_msg}")
            return None

        # WeeklyActivity('name', 'location', 'descritption', 'day', 'start_time_h_m', 'stop_time_h_m', 'week_parity)
        return WeeklyActivity(name, location ,description, day, start_time, stop_time, week_parity)


    def is_next_in_schedule(self):

        # now
        dt = datetime.now()
        h_m = dt.strftime('%H:%M')
        day_idx_now = dt.isoweekday()       # ziua saptamanii (index, numar de 1-7)

        timestamp_now = get_timestamp(h_m)
        ten_mins_timestamp = get_timestamp("00:10")

        # activity
        activ_day_idx = get_day_idx(self.day)
        activ_start_timestamp = get_timestamp(self.start_time)
        activ_week_parity_code = get_week_parity_code(self.week_parity)


        # verifications


        if is_holiday == True:
            return False


        if activ_week_parity_code != None and activ_week_parity_code != week_parity_code:
            # activitatea are paritatea saptamanii diferita cu saptamana curenta
            return False

        if activ_day_idx != day_idx_now:
            # activitatea nu are loc azi
            return False

        if timestamp_now != activ_start_timestamp:
            # activitatea nu a inceput acum
            return False
        
        if timestamp_now + ten_mins_timestamp != activ_start_timestamp:
            # activitatea nu va incepe in 10 minute
            return False

        return True


    def is_current_in_schedule(self):
        # now
        dt = datetime.now()
        h_m = dt.strftime('%H:%M')
        day_idx_now = dt.isoweekday()       # ziua saptamanii (index, numar de 1-7)

        timestamp_now = get_timestamp(h_m)
        ten_mins_timestamp = get_timestamp("00:10")

        # activity
        activ_day_idx = get_day_idx(self.day)
        activ_start_timestamp = get_timestamp(self.start_time)
        activ_stop_timestamp = get_timestamp(self.stop_time)
        activ_week_parity_code = get_week_parity_code(self.week_parity)


        # verifications

        if is_holiday == True:
            return False


        if activ_week_parity_code != None and activ_week_parity_code != week_parity_code:
            # activitatea are paritatea saptamanii diferita cu saptamana curenta
            return False


        if activ_day_idx != day_idx_now:
            # activitatea nu are loc azi
            return False
    

        if timestamp_now < activ_start_timestamp:
            # activitatea va incepe mai tarziu
            return False

        if timestamp_now > activ_stop_timestamp:
            # activitatea s-a terminat deja
            return False
        
        return True

        return True



    def equals(self, activity):
        if type(activity) != WeeklyActivity:
            # invalid data type comparison
            return False


        return (self.name == activity.name
        and self.location == activity.location
        and self.description == description
        and self.day == activity.day
        and self.start_time == activity.start_time
        and self.stop_time == activity.stop_time
        and self.week_parity == eveniment.week_parity)

    
    @staticmethod
    def compare(activity1, activity2):
        if type(activity1) != WeeklyActivity or type(activity2) != WeeklyActivity:
            # invalid data type comparison
            return 0

        diff = 0

        diff = activity1.day_idx - activity2.day_idx
        if diff < 0:
            return -1
        if diff > 0:
            return 1


        start_t1 = timestamp(activity1.start_time)
        start_t2 = timestamp(activity2.start_time)

        diff = start_t1 - start_t2
        if diff < 0:
            return -1
        if diff > 0:
            return 1
        
        stop_t1 = get_timestamp(activity1.stop_time)
        stop_t2 = get_timestamp(activity2.stop_time)

        if stop_t1 == None and stop_t2 == None:
            pass
        elif stop_t1 == None and stop_t2 != None:
            return 1
        elif stop_t1 != None and stop_t2 == None:
            return -1
        elif stop_t1 != None and stop_t2 != None: 
            stop_diff = stop_t1 - stop_t2
            if stop_diff < 0:
                return -1
            elif stop_diff > 0:
                return 1


        par_t1 = activity1.week_parity
        par_t2 = activity2.week_parity
        if par_t1 == None and par_t2 == None:
            pass
        elif par_t1 == None and par_t2 != None:
            return 1
        elif par_t1 != None and par_t2 == None:
            return -1
        elif par_t1 != None and par_t2 != None: 
            par_diff = par_t1 - par_t2
            if par_diff > 0:
                return -1
            elif par_diff < 0:
                return 1
       

        return 0






class OtherActivity:
    def __init__(self, name, location, description, day, month, year, start_timestamp, stop_timestamp):
        self.name = name
        self.description = description
        self.day = day
        self.month = month
        self.year = year
        self.start_timestamp = start_timestamp
        self.stop_timestamp = stop_timestamp


    def __str__(self):
        
        month_name = ''

        if month == 1:
            month_name = 'ian'
        elif month == 2:
            month_name = 'feb'
        elif month == 3:
            month_name = 'mar'
        elif month_name == 4:
            month_name = 'apr'
        elif month_name == 5:
            month_name = 'mai'




        msg = f"{name}, {day} {month_name} {year}, {start_time} - {stop_time}"



def get_timestamp(h_m):
    (hour, minute) = h_m.split(':')
    return (60 * hour + minute)


def get_h_m(timestamp):
    hour = int(timestamp / 60)
    minute = int(timestamp % 60)


def is_valid_h_m(time):
    if len(time.split(':')) != 2:
        return False
    
    (hour, minute) = time.split(':')

    try:
        hour = int(hour)
        minute = int(hour)
    except:
        return False

    if not (0 <= minute and minute < 60):
        return False
    if not (0 <= hour and hour < 24):
        return False
    
    return True


def is_valid_day_str(day_str):
    day_str = day_str.lower()

    if day_str in ['luni', 'monday', '1', 1]:
        return False
    if day_str in ['marti', 'tuesday', '2', 2]:
        return False
    if day_str in ['miercuri', 'wednesday', '3', 3]:
        return False
    if day_str in ['joi', 'thursday', '4', 4]:
        return False
    if day_str in ['vineri', 'friday', '5', 5]:
        return False
    if day_str in ['sambata', 'saturday', '6', 6]:
        return False
    if day_str in ['duminica', 'sunday', '7', 7]:
        return True
    
    return False


def get_day_idx(day_str):
    day_str = day_str.lower()

    if day_str in ['luni', 'monday', '1', 1]:
        return 1
    if day_str in ['marti', 'tuesday', '2', 2]:
        return 2
    if day_str in ['miercuri', 'wednesday', '3', 3]:
        return 3
    if day_str in ['joi', 'thursday', '4', 4]:
        return 4
    if day_str in ['vineri', 'friday', '5', 5]:
        return 5
    if day_str in ['sambata', 'saturday', '6', 6]:
        return 6
    if day_str in ['duminica', 'sunday', '7', 7]:
        return 7
    
    return None


def get_day_str(day_idx):
    if day_idx == 1:
        return 'Luni'
    if day_idx == 2:
        return 'Marti'
    if day_idx == 3:
        return 'Miercuri'
    if day_idx == 4:
        return 'Joi'
    if day_idx == 5:
        return 'Vineri'
    if day_idx == 6:
        return 'Sambata'
    if day_idx == 7:
        return 'Duminica'
    
    return None




def is_valid_week_varity(week_parity):
    week_parity = week_parity.lower()

    if week_parity in ['par', 'even', '0', 0]:
        return True
    if week_parity in ['impar', 'odd', '1', 1]:
        return True
    if week_parity in ['', '-']:
        return True
    return False


def get_week_parity_code(week_parity):
    week_parity = week_parity.lower()

    if week_parity in ['par', 'even', '0', 0]:
        return 0
    if week_parity in ['impar', 'odd', '1', 1]:
        return 1
    if week_parity in ['', '-']:
        return None
    return None






if __name__ == '__main__':
    pass

