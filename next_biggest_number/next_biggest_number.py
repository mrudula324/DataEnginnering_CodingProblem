#!/usr/bin/python3
import sys
from itertools import permutations
import time

def main():
    next_biggest_number(sys.argv[1])


# Function to find the next largest numbers by rearranging the digits:
def next_biggest_number(num):
  
  num=str(num)                        # converting to str from num
  num_list=[]                         # Empty list to convert string of num to list
  
  for x in num:                       # Loop to convert num values to list
    num_list.append(x)
  
  for n in range(len(num_list)+1):    # Loop to increment values from tens place to max place value.
    if n>=2:
      part2=num[-n:]
      part1=num[:-n]
      
      perm_list=[]                    # Empty list to capture permutation values
      perm = permutations(part2)      # Creating permulations with the digits and appending to perm_list
      for i in list(perm):
        st="".join(i)
        perm_list.append(st)

      for li in sorted(perm_list):    # Iterating over perm_list and checking condition
        next_num = part1 + li
        if num == max(perm_list):
          return (int(-1))
        elif (part1+li) > num:
          return int(next_num)


if __name__ == "__main__":
    main()

from next_biggest_number import next_biggest_number
def test_simple_cases():
# assert(next_biggest_number(12))
   assert(next_biggest_number(123) == 132)
   # assert(next_biggest_number(67809) == 67890)