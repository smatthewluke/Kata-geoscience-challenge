# geoscience kata workspace - see https://kata.geosci.ai/

import requests
from IPython.display import Markdown
from itertools import pairwise

url = 'https://kata.geosci.ai/challenge/sequence' # challenge = 'sequence'

r = requests.get(url)
Markdown(r.text)

#1. What is the total thickess in metres of sandstone (`S`)? Each sample represents one metre.
#2. How many sandstone beds are there? A bed is a contiguous group of one lithology, so `MMFFF` is 2 beds, one of `M` and one of `F`.
#3. How many times does the most common *upwards* bed transition occur? Do not include transitions from a lithology to itself.



# Preparation for the challenges, incl. set-up

my_key = "testing"
params = {'key': my_key}
r = requests.get(url, params)
rock_sequence = r.text # rock_squence is a string of beds, such as 'MFSS'

# question 1: What is the total thickess in metres of sandstone (`S`)? Each sample represents one metre.
rock_library = {bed:rock_sequence.count(bed) for bed in rock_sequence}
sandstone_thickness = rock_library['S']
#print(sandstone_thickness) # answer

# solution submission
params = {'key': my_key,   # <--- must be the same key as before
          'question': 1,   # <--- which question you're answering
          'answer': sandstone_thickness,  # <--- your answer to that question
          }
r = requests.get(url, params)
r.text

# question 2: How many sandstone beds are there? A bed is a contiguous group of one lithology, so `MMFFF` is 2 beds, one of `M` and one of `F`.
previous_bed = ''
sandstone_beds = 0

for bed in rock_sequence:
    if bed == 'S' and previous_bed != 'S':
        previous_bed = 'S'
        sandstone_beds += 1
    elif bed != 'S':
        previous_bed = bed
# print(sandstone_beds) # answer

# solution submission

params = {'key': my_key,   # <--- must be the same key as before
          'question': 2,   # <--- which question you're answering
          'answer': sandstone_beds,  # <--- your answer to that question
          }
r = requests.get(url, params)
r.text

# question 3: How many times does the most common *upwards* bed transition occur? Do not include transitions from a lithology to itself.
#rock_library = {first_bed,second_bed:rock_sequence.count(first_bed,second_bed) for (first_bed, second_bed) in pairwise(rock_sequence) if first_bed != second_bed}

transition_dict = {}
test = pairwise(rock_sequence)
for first_bed, second_bed in test:
    if first_bed != second_bed:
        if (first_bed + second_bed) in transition_dict:
            transition_dict[(first_bed + second_bed)] += 1
        else:
            transition_dict[(first_bed + second_bed)] = 1

most_common_transition = (max(transition_dict.values())) # answer

# solution submission

params = {'key': my_key,   # <--- must be the same key as before
          'question': 3,   # <--- which question you're answering
          'answer': most_common_transition,  # <--- your answer to that question
          }
r = requests.get(url, params)
r.text

# finished!


