import os
import sys
import math
from decimal import Decimal
from HalleyCore import HalleyEncrypt

x = HalleyEncrypt.generate_Random_Key(30, 50, 60, 100)

index_arguments = 20*40**100-70*50

second_index_argumets = 40/40**50+100*14

get_square_of_index = int(index_arguments^second_index_argumets)

get_string_of_square = list(int(get_square_of_index).__str__())
            
get_string_length_of_string_square = len(get_string_of_square)
            
final_mix = math.sqrt(get_string_length_of_string_square)

print(get_square_of_index)