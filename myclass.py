class myclass:
  number = 0
  name = "NoName"
  
def Main():
  me = myclass()
  me.number = 342
  me.name = "Steve"
  
  friend = myclass()
  friend.number = 53
  friend.name = "Heather"
  
  empty = myclass()
  
  print( "Name: " + me.name + ", Favorite Number: " str(me.number) )
  print( "Name: " + friend.name + ", Favorite Number: " str(friend.number) )
  print( "Name: " + empty.name + ", Favorite Number: " str(empty.number) )

if __name__ = "__main__":
  Main()
