import re

# new version where I remove 17% lines of code

max_digits = 4
max_problems = 5
between = "    "

class Problem:
  def __init__(self, left: str, operator: str, right: str):
    self.left = left
    self.operator = operator
    self.right = right

  @property
  def len_left(self) -> int:
    return len(self.left)
  @property
  def len_right(self) -> int:
    return len(self.right)
  @property
  def lenght(self) -> int:
    return max(self.len_left, self.len_right) + 2


def arithmetic_arranger(problems):

  if len(problems) > max_problems:
    return "Error: Too many problems."

  top = ""
  bottom = ""
  lines = ""
  for problem in problems:

    looking_good = re.search('(\S+)\s*([+-/*])\s*(\S+)', problem)
    if not looking_good:
      return "Error: Doesn't look good"

    operator = re.search('[+-]', problem).group()
    if not operator:
      return "Error: Operator must be '+' or '-'."

    left = re.search('^(?=\s*)[0-9]+', problem).group()
    right = re.search('[0-9]+(?=\s*)$', problem).group()
    if not left or not right:
      return "Error: Numbers must only contain digits."

    # Creating from class
    pb = Problem(left, operator, right)
    
    if pb.len_left > max_digits or pb.len_right > max_digits:
      return "Error: Numbers cannot be more than four digits."

    top += (pb.lenght - pb.len_left) * " " + pb.left + between
    bottom += pb.operator + (pb.lenght - 1 - pb.len_right) * " " + pb.right + between
    lines += "-" * pb.lenght + between

  arranged = top + "\n" + bottom + "\n" + lines
  
  return arranged
