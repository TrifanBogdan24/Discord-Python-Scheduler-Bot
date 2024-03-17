#!/usr/bin/env python3


from datetime import datetime


# global variables:
week_parity_code = '1'        # '0', '1', '-'
is_holiday = False          # False, True
weekly_activities = []
other_activities = []
deadlines = []




class ScheduleUser:
    def __init__(self, id, username):
        """constructor care instantiaza clasa
        """
        self.id = id
        self.username = username
        self.week_parity = 1  # prima saptama (impar)
        self.is_holiday = False
        self.weekly_activities = []
        self.other_activities = []
        self.deadlines = []
        self.birthdays = []


    @staticmethod
    def get_user_by_id(id, users):
        """ extrage un user dintr-o lista de utilizatarii
        intoarce `None` daca `id`-ul acestuia nu se afla in lista
        """

        if type(users) != list:
            return None

        for user in users:
            if type(user) != ScheduleUser:
                continue
            if user.id == id:
                return user
        
        return None


class DataHandler:
    """clasa inglobeaza mai multe metode statice
    """

    _instance = None        # `_var` -> internal class variable



    @staticmethod
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


    @staticmethod
    def get_timestamp(h_m):
        try:
            (hour, minute) = h_m.split(':')
            hour = int(hour)
            minute = int(minute)
            return (60 * hour + minute)
        except:
            return 0


    @staticmethod
    def get_h_m(timestamp):
        hour = int(timestamp / 60)
        minute = int(timestamp % 60)
        return f"{hour}:{minute}"



    @staticmethod
    def is_valid_day_str(day_str):
        return (DataHandler.get_day_idx(day_str) != None) 
        

    @staticmethod
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


    @staticmethod
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



    @staticmethod
    def is_valid_week_varity(week_parity):
        return (self.get_week_parity_code(week_parity) != None)


    @staticmethod
    def get_week_parity_code(week_parity):
        week_parity = week_parity.strip().lower()

        if week_parity in ['par', 'even', '0', 0]:
            return '0'
        if week_parity in ['impar', 'odd', '1', 1]:
            return '1'
        if week_parity in ['', '-']:
            return '-'
        return None


    @staticmethod
    def is_valid_month(mself, onth_str):
        return (get_month_idx(month_str) != None)


    @staticmethod
    def get_month_idx(month_str):
        month = month_str.strip().lower()

        if month in ['ian', 'jan', 'ianurie', 'january', '1', 1]:
            return 1
        if month in ['feb', 'februarie', 'february', '2', 2]:
            return 2
        if month in ['mar', 'martie', 'march', '3', 3]:
            return 3
        if month in ['apr', 'aprilie', 'april', '4', 4]:
            return 4
        if month in ['mai', 'may', '5', 5]:
            return 5
        if month in ['iun', 'iunie', 'june', '6', 6]:
            return 6
        if month in ['iul', 'jul', 'iulie', 'july', '7', 7]:
            return 7
        if month in ['aug', 'august', '8', 8]:
            return 8
        if month in ['sep', 'septembrie', 'september', '9', 9]:
            return 9
        if month in ['oct', 'octombrie', 'october', '10', 10]:
            return 10
        if month in ['nov', 'noiembrie', 'november', '11', 11]:
            return 11
        if month in ['dec', 'decembrie', 'december', '12', 12]:
            return 12
        return None

    @staticmethod
    def get_month_str(month_idx):
        if month_idx == 1:
            return 'ian'
        if month_idx == 2:
            return 'feb'
        if month_idx == 3:
            return 'apr'
        if month_idx == 4:
            return 'mai'
        if month_idx == 5:
            return 'iun'
        if month_idx == 6:
            return 'iul'
        if month_idx == 7:
            return 'aug'
        if month_idx == 8:
            return 'sep'
        if month_idx == 9:
            return 'oct'
        if month_idx == 10:
            return 'nov'
        if month_idx == 11:
            return 'dec'
        return None
        









class WeeklyActivity:
    def __init__(self, user_id, name, location, description, week_day, start_time, stop_time, week_parity):
        """constructorul default al clasei
        """
        self.user_id = user_id
        self.name = name
        self.location = location
        self.description = description
        self.week_day = week_day
        self.start_time = start_time
        self.stop_time = stop_time
        self.week_parity = week_parity


    def __new__(cls, user_id, name, location, description, week_day, start_time, stop_time, week_parity):
        """ un constructor mai restrictiv:
        imi doresc ca field-urile sa faca parte dintr-o multime specifica de valori
        
        se fac niste verificari inainte de atribuire
    

        - `week_day` = trebuie sa fie o zi din saptamana (sau indexul ei din saptmana)

        RO: ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']
        EN: ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        idx: [0, 1, 2, 3, 4, 5, 6, 7]


        - `start_time` = trebuie sa fie timpul in format `HH:MM` (ora : minut)
        - `stop_time` = trebuie sa fie timpul in format `HH:MM` (ora : minut)
        - `stop_time` = poate sa fie '' sau '-' daca nu se cunoasta ora de sfarsit


        - `week_parity` = paritatea sptamanii: sapt para / impara / nu conteaza
        ['odd', 'par', 0]
        ['even', 'impar', 1]
        ['-', '']



        ex arg: ID, 'nume', 'locatie', 'descriere', 'luni', '10:00', '-', 'par
        """

        # eliminam spatiile de la capaetele sirurilor de caractere
        name = name.strip()
        location = location.strip()
        description = description.strip()
        week_day = week_day.strip()
        start_time = start_time.strip()
        stop_time = stop_time.strip()
        week_parity = week_parity.strip()


        err_msg = ''

        valid_start_t = DataHandler.is_valid_h_m(start_time)
        valid_stop_t = DataHandler.is_valid_h_m(stop_time)

        if not valid_start_t:
            err_msg += f"Err: Invalid start time `{start_time}`; expected `%H:%M` format\n" 
        
        if not valid_stop_t and stop_time not in ['-', '']:
            err_msg += f"Err: Invalid stop time `{stop_time}`; expected `%H:%M` format\n"
        
        if valid_start_t and valid_stop_t and stop_time not in ['-', '']:
            start_timestamp = DataHandler.get_timestamp(start_time)
            stop_timestamp = DataHandler.get_timestamp(stop_time)
            
            if start_timestamp > stop_timestamp:
                err_msg += f"Err: Invalid time schedule {start_time} -> {stop_time}"
        

        if not DataHandler.is_valid_day_str(week_day):
            err_msg += f"Err: Invalid name of a day {week_day}"


        if err_msg != '':
            print(f"{err_msg}")
            return None

        # WeeklyActivity(user_id, 'name', 'location', 'descritption', 'day', 'start_time_h_m', 'stop_time_h_m', 'week_parity)
        return super().__new__(cls)

    def __str__(self):
        """metoda `toString`: transforma campurile clasei intr-un sir de caractere
        """
        to_string = ''
        
        if self.stop_time in [None, '', '-']:
            to_string = f"{self.name}, begins at {self.start_time}, {self.location}"
        else:
            to_string = f"{self.name}, {self.start_time} - {self.stop_time}, {self.location}"
        

        if self.description not in ['', '-']:
            to_string += f"\nDescription: {self.description}"

        return to_string


    def is_next_in_schedule(self):
        """verifica daca exista o diferenta de exact 0 sau 10 minute
        intre eveniment si ora curentul

        intoarce true/false
        """


        # now
        dt = datetime.now()
        h_m = dt.strftime('%H:%M')
        week_day_idx_now = dt.isoweekday()       # ziua saptamanii (index, numar de 1-7)

        timestamp_now =  DataHandler.get_timestamp(h_m)
        ten_mins_timestamp =  DataHandler.get_timestamp("00:10")

        # activity
        activ_week_day_idx = DataHandler.get_day_idx(self.week_day)
        activ_start_timestamp = DataHandler.get_timestamp(self.start_time)
        activ_week_parity_code = DataHandler.get_week_parity_code(self.week_parity)


        # verifications


        if is_holiday == True:
            return False


        if activ_week_parity_code != None and activ_week_parity_code != week_parity_code:
            # activitatea are paritatea saptamanii diferita cu saptamana curenta
            return False

        if activ_week_day_idx != week_day_idx_now:
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
        # acum
        dt = datetime.now()
        h_m = dt.strftime('%H:%M')
        week_day_idx_now = dt.isoweekday()       # ziua saptamanii (index, numar de 1-7)

        timestamp_now = DataHandler.get_timestamp(h_m)
        ten_mins_timestamp = DataHandler.get_timestamp("00:10")

        # activitatea
        activ_week_day_idx = DataHandler.get_day_idx(self.week_day)
        activ_start_timestamp = DataHandler.get_timestamp(self.start_time)
        activ_stop_timestamp = DataHandler.get_timestamp(self.stop_time)
        activ_week_parity_code = DataHandler.get_week_parity_code(self.week_parity)


        # verificari

        if is_holiday == True:
            return False


        if activ_week_parity_code != None and activ_week_parity_code != week_parity_code:
            # activitatea are paritatea saptamanii diferita cu saptamana curenta
            return False


        if activ_week_day_idx != week_day_idx_now:
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


        return (self.user_id == activity.user_id
        and self.name == activity.name
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


        start_t1 = DataHandler.get_timestamp(activity1.start_time)
        start_t2 = DataHandler.get_timestamp(activity2.start_time)

        diff = start_t1 - start_t2
        if diff < 0:
            return -1
        if diff > 0:
            return 1
        
        stop_t1 = DataHandler.get_timestamp(activity1.stop_time)
        stop_t2 = DataHandler.get_timestamp(activity2.stop_time)

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
    def __init__(self, user_id, name, location, description, day, month, year, start_timestamp, stop_timestamp):
        """constructorul default al clasei
        """
        self.user_id = user_id
        self.name = name
        self.description = description
        self.day = day
        self.month = month
        self.year = year
        self.start_timestamp = start_timestamp
        self.stop_timestamp = stop_timestamp


    def __new__(user_id, name, location, description, day, month, year, start_timestamp, stop_timestamp):
        """un constructor mai restrictiv al clasei

        - `day` = ziua din calendar
        - `month` = luna din calendar
        RO abv: ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'nov', 'dec']
        RO full: ['ianuare', 'februare', 'martie', 'aprilie', 'mai', 'iuniu', 'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie']
        EN abv: ['jan', 'feb', 'mar', 'apr', 'may', 'june, 'july', aug', 'sept', 'oct', 'nov', 'dec]
        EN full: ['januray', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        idx: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        - `year` = anul

        - `start_time` = trebuie sa fie timpul in format `HH:MM` (ora : minut)
        - `stop_time` = trebuie sa fie timpul in format `HH:MM` (ora : minut)
        - `stop_time` = poate sa fie '' sau '-' daca nu se cunoasta ora de sfarsit

        """


        # eliminam spatiile de la capetle sirurilor de caractere
        name = name.strip()
        location = location.strip()
        description = description.strip()
        month = month.strip()
        year = year.strip()
        start_time = start_time.strip()
        stop_time = stop_time.strip()

        err_msg = ''

        valid_start_t = DataHandler.is_valid_h_m(start_time)
        valid_stop_t = DataHandler.is_valid_h_m(stop_time)

        if not valid_start_t:
            err_msg += f"Err: Invalid start time `{start_time}`; expected `%H:%M` format\n" 
        
        if not valid_stop_t and stop_time not in ['-', '']:
            err_msg += f"Err: Invalid stop time `{stop_time}`; expected `%H:%M` format\n"
        
        
        if valid_start_t and valid_stop_t and stop_time not in ['-', '']:
            start_timestamp = DataHandler.get_timestamp(start_time)
            stop_timestamp = DataHandler.get_timestamp(stop_time)
            
            if start_timestamp > stop_timestamp:
                err_msg += f"Err: Invalid time schedule {start_time} -> {stop_time}"
        

        if not DataHandler.is_valid_day_str(week_day):
            err_msg += f"Err: Invalid name of a day {week_day}"


        if err_msg == '':
            print(f"{err_msg}")
            return None

        
        return super().__new__(cls)






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





class Deadline:
    def __init__(self, user_id, name, description, day, month, year, time):
        """constructorul defualt al clasei
        """
        self.user_id = user_id
        self.name = name
        self.description = description
        self.day = day
        self.month = momth
        self.year = year
        self.time = time

    
    def __new__(self, user_id, description, name, day, month, year, time):
        """un constructor mai restrictiv:
        
        se face niste verificari inainte de atribuire:
        - blocul `(day-month-year)` trebuie sa formeeze o data existenta in calendare
        - time trebuie sa contina timpul in format `HH:MM` (ora : minut)
        """

        err_msg = ''

        if err_msg != '':
            return None

        return super().__new__(cls)



class Birthday:
    def __init__(self, user_id, name, day, month, year):
        self.user_id = user_id
        self.name = name
        self.day = day
        self.month = month
        self.year = year



if __name__ == '__main__':
    pass

