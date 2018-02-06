class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print '%s, %s, %s' % (self.make, self.model, self.year)
    
highlander = Vehicle('Toyota','Highlander','2007')
highlander.print_info()