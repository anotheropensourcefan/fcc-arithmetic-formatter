# This entrypoint file to be used in development. Start by reading README.md
# from test_module import test_template

from arithmetic_arranger_long import arithmetic_arranger_long
from arithmetic_arranger import arithmetic_arranger

# print(arithmetic_arranger_long(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
# test_template(['-vv'])
