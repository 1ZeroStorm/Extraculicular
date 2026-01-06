
# Parent Class
class worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def info(self):
        return f"name: {self.name} \nsalary: {self.salary}"
    
    def work(self):
        return f"{self.name} (worker) is working."

# Child Class (inherits from worker)
class Programmer(worker):
    def __init__(self, name, language, salary):
        # Call parent constructor
        super().__init__(name, salary)
        self.language = language
        
    def work(self):
        return f"{self.name} (Programmer) is code writing."

if __name__ == "__main__":
    worker1 = worker("Andi", 5000000)
    programmer1 = Programmer("Budi", "Python", 7000000)

    print(worker1.info())
    print(worker1.work())
    
    print(programmer1.info())
    print(programmer1.work())
    
