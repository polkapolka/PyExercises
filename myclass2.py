class MyClass:
  name = "NoName"
  age = 0
  friends = mynames()
  
class mynames():
  names = []
  
  def add(self, newname):
    self.names.append(newname)

def Main():
  p01 = myclass()
  p01.name = "Sarah"
  p01.age = 34
  p01.friends.add("John")
  p01.friends.add("Jack")

  print("My name is " + p01.name + "and I am " + str(p01.age) + ". My friends are " + str(p01.friends.names))

if __name__ == '__main__':
	Main()
