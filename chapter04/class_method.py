class Date:
    def __init__(self,year,month,day):
        self.year,self.month,self.day = year,month,day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

    def tomorrow(self):
        self.day +=1

    @staticmethod
    def parse_from_sting_static(date_string):
        year,month,day=tuple(date_string.split("-"))
        return Date(int(year),int(month),int(day))

    @classmethod
    def parse_from_sting_class(cls,date_string):
        year,month,day=tuple(date_string.split("-"))
        return cls(int(year),int(month),int(day))

    @staticmethod
    def valid_sting(date_string):
        year, month, day = tuple(date_string.split("-"))
        if int(year)>0 and (int(month)>0 and int(month)<=12) and (int(day)>0 and int(day)<=31):
            return True
        else:
            return False



new_date = Date(2018,12,30)
print(new_date)
new_date.tomorrow()
print(new_date)
new_date=Date.parse_from_sting_static("2018-12-30")
print(new_date)
new_date=Date.parse_from_sting_class("2018-12-30")
print(new_date)
print(Date.valid_sting("2019-02-31"))