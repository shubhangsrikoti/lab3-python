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
  print(f"sum is {sum_n(int(num))}.")

  string = input("Enter a string: ")
  print_n(string, int(num))

if __name__ == "__main__":
  run()