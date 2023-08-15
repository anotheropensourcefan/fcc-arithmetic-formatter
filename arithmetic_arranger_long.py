import re

# first version where I use too many loops

max_digits = 4
max_problems = 5
between = "    "

class Problem:
  def __init__(self, left, operator, right):
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


def arithmetic_arranger_long(problems):

  if len(problems) > max_problems:
    return "Error: Too many problems."

  problems_list = []

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

    problems_list.append(pb)

  arranged_problems = ""

  # left
  for problem in problems_list:
    space = problem['length'] - problem["len_left"]
    arranged_problems += " " * space + problem['left'] + between
  arranged_problems += "\n"

  # operator + right
  for problem in problems_list:
    arranged_problems += problem['operator']
    space = problem['length'] - 1 - problem['len_right']
    arranged_problems += " " * space + problem['right'] + between
  arranged_problems += "\n"

  # dashes
  for problem in problems_list:
    arranged_problems += "-" * problem['length'] + between

  return arranged_problems
