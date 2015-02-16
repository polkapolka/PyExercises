class vector2D:
  x = 0.0
  y = 0.0
  
  def Set(self, X, Y):
    self.X = X
    self.y = Y
  
def Main():
  vec = vector2D()
  vec.Set(5,6)
  print("X: " + str(vec.X) + ", Y: " + str(vec.y))

if __name__ == "__main__":
  Main()
  
  
