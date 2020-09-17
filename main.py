# Author: Shubhang Srikoti svs6959@psu.edu
# Collaborator: Geng Niu gjn5124@psu.edu
# Collaborator: Max Skeen - mls6984@psu.edu
# Collaborator: Ananya Ashwinikumar ava6290@psu.edu
# Section: 4
# Breakout Room: 7

def sum_n(num):
  if num >= 1:
    return num + sum_n(num - 1)
  else:
    return 0
  
def print_n(string, num):
  if num >= 1:
    print(string)
    print_n(string, num - 1)

def run(): 
  num = input("Enter an int: ")
  print(f"Sum is {sum_n(int(num))}.")

  num1 = input("Enter an int: ")
  string = input("Enter a string :")
  print_n(string, int(num1))

if __name__ == "__main__":
  run()