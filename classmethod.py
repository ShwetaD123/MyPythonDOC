
class Fullname(object):

    def __init__(self,fname,mname,lname):
        print('---Inside Constructor --',)
        self.firstName = fname
        self.lastName = lname
        self.middleName = mname
        print('First Name --',fname)
        print('Middle Name --',lname)
        print('Last Name --',mname)



    @classmethod
    def tosepeate(cls,fullname):
        print('---Inside ClassMethod --', )
        fname,mname,lname = fullname.split(' ')
        myname=cls(fname,mname,lname)
        print('fname',fname,'--','mname--',mname,'--','lname--',lname)
        return myname


ob=Fullname.tosepeate('Shweta Kishor Dongre')
print(ob.__dict__)

# ---Inside ClassMethod --
# ---Inside Constructor --
# First Name -- Shweta
# Middle Name -- Dongre
# Last Name -- Kishor
# fname Shweta -- mname-- Kishor -- lname-- Dongre
# {'firstName': 'Shweta', 'lastName': 'Dongre', 'middleName': 'Kishor'}



class DateTime(object):

    def __init__(self, day=10, month=10, year=2000):
        print('---Inside Constructor --',)
        self.day = day
        self.month = month
        self.year = year
        print('Day--', day)
        print('Month--',month )
        print('year--',year )


    @classmethod
    def from_string(cls, string_date):
        print('---Inside ClassMethod --', )
        day, month, year = map(int, string_date.split('-'))
        myDate = cls(day, month, year)
        return myDate

    @staticmethod
    def is_valid_date(date_as_string):
        print('---Inside StaticMethod --', )

        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

dateObj = DateTime.from_string('20-05-1994')
is_valid_date = DateTime.is_valid_date('20-05-1994')
print(is_valid_date)

# ---Inside ClassMethod --
# ---Inside Constructor --
# Day-- 20
# Month-- 5
# year-- 1994
# ---Inside StaticMethod --
# True
#
# Process

