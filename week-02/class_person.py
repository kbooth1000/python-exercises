class Person(object):
    def __init__(self, first, email, phone):
        self.first = first
        self.email = email
        self.phone = phone
        self.friends = []
        self.greetings = 0
        self.unique_greetings = 0
        self.greeted_people = []

    def greet(self, other_person):
        self.greetings += 1
        self.greeted_people.append(other_person)
        if other_person in self.greeted_people:
            self.unique_greetings += 1
            print 'unique greeting for %s: %d (%s)' % (self.first, self.unique_greetings, other_person.first)
        else:
            print 'Hello %s, I am %s' % (other_person.first, self.first)
            print '****',self.greeted_people

    def greeting_count(self):
        print '%s has greeted someone %d times.' % (self.first, self.greetings)

    def num_unique_people_greeted(self):
        print '%s has greeted %d different people.' % (self.first, self.unique_greetings)

    def print_contact_info(self):
        print '%s\'s email is: %s; %s\'s phone number is: %s' % (self.first, self.email, self.first, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)
        print '%s\'s friend-list now includes: %s' % (self.first, self.friends[0].first)

    def num_friends(self):
        self.friend_num = len(self.friends)
        return 'Number of friends %s has: %d' % (self.first, self.friend_num)
    def __repr__(self):
        return '%s, %s, %s' % (self.first,self.email,self.phone,)

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
lena = Person('Lena', 'lena@gmail.com', '404-334-6925')

jordan = Person('Jordan','jordan@aol.com','495-586-3456')

# print '%s, %s' % (sonny.first, sonny.email)
# print '%s, %s' % (jordan.first, jordan.email)

# print jordan.print_contact_info()

sonny.greet(lena)
jordan.greet(lena)
sonny.greet(jordan)
lena.greet(sonny)

sonny.add_friend(jordan)
print sonny.num_friends()
sonny.greeting_count()
jordan.greeting_count()
lena.greeting_count()

print sonny
print jordan

print
sonny.num_unique_people_greeted()