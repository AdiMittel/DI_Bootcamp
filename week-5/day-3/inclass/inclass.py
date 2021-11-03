class Person:
    def __init__(self, fname,lname, age):
      self.first_name = fname
      self.last_name = lname
      self.age = age
    
    def __str__(self):
        return (self.first_name +' '+ self.last_name).title()
    def __repr__(self):
        return f'person object: {str(self)}'
    def __call__(self):
        return f'check me out i was called'
    def __gt__(self,other):
        if isinstance(other,int):
            return self.age > other
        elif isinstance(other,float):
            return self.age > other
        elif isinstance(other,Person):
            return self.age > other.age
        else:
            raise Exception('this operation is not supported, we only compare people to person,int or float')
        # return len(str(self)) > len(str(other))

p1 = Person('Toby','Toboscus',35)
p2 = Person('CJ','Craigg',45)
p3 = Person('The','Doctor',890)
print(p1)
print(p2)
print(p3)