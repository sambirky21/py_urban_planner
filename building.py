import datetime
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories

class Building:

    def __init__(self, story, address, desinger="Sam Birky"):
        self.designer = desinger
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = story
        # Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.
    def construct(self):
        self.date_constructed = datetime.datetime.now()
        # Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.
    def purchase(self, purchased_by):
        self.owner = purchased_by
        # print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')
    def __str__(self):
        return print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')

eight_hundred_eighth = Building(12, "800 8th Street")
eight_hundred_eighth.purchase("Bob")
eight_hundred_eighth.construct()
eight_hundred_eighth.__str__()
#1
five_hundred_fifth = Building(5, "500 5th Street")
five_hundred_fifth.purchase("Bob")
five_hundred_fifth.construct()
five_hundred_fifth.__str__()
#2
four_hundred_fourth = Building(4, "400 4th Street")
four_hundred_fourth.purchase("Bob")
four_hundred_fourth.construct()
four_hundred_fourth.__str__()
#3
three_hundred_third = Building(3, "300 3rd Street")
three_hundred_third.purchase("Bob")
three_hundred_third.construct()
three_hundred_third.__str__()
#4
two_hundred_second = Building(2, "200 2nd Street")
two_hundred_second.purchase("Bob")
two_hundred_second.construct()
two_hundred_second.__str__()
#5
one_hundred_first = Building(2, "100 1st Street")
one_hundred_first.purchase("Bob")
one_hundred_first.construct()
one_hundred_first.__str__()