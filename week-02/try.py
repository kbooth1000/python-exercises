class Contact():
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone

kyle = Contact('Kyle', 'Booth', '212-442-1373')

print kyle.phone
print kyle.first