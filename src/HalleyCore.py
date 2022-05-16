#######

"""
    !Proyect started by Raxabi

    Noob Project, Version Alpha 0.1.0

    Contributors = [
        Raxabi,
    ] 
"""

#######

# Dependencies
import math
import random
import time

class HalleyEncrypt:
    def __init__(self):
        pass
    
    def easy_Method(original_string, salt, version):
        if version == 1:
            splitedString = list(original_string)
            return original_string ^ salt
        elif version == 2:
            return original_string + salt

    def Crypt_by_Time(original_string, salt):
        # This function Encrypt a string considering the left time until the Halley Comet will be see in the Earth
        pass
    
    """
        generate_Random_Key will get any parsed argument or anything argument
        if an argument was parsed the function will order randomly a basic operation with that arguments
        else anything argument was parsed (pass)
    """
    def generate_Random_Key(*args: float or int):
        # If the function will be called without arguments, will generate a random hash
        if args.count == 0:
            random.seed()
            i = random.random()
            final_random = math.sqrt(i)
            return final_random
        elif args.count == 4:
            index_arguments = args[0]*args[3]**args[2]-index_arguments*args[1]

            get_square_of_index = math.sqrt(index_arguments^index_arguments)
            
            get_string_of_square = list(int(get_square_of_index).__str__())
            
            get_string_length_of_string_square = len(get_string_of_square)
            
            final_mix = get_string_length_of_string_square

            return final_mix