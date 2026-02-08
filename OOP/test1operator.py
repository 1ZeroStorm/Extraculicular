from test_subject import createobjsample

class robot(createobjsample):
    def __init__(self, name, year):
        super().__init__(att1=name)
        self.year = year
    
    def op1(self):
        print("diving")
    
    def op2(self):
        print("shooting")

    def op3(self):
        print("flying")

my_robot = robot("RoboWarrior", 2025)
my_robot.op1()
my_robot.op2()
my_robot.op3()