# This is where I try out what i learnt from the orientation as i process information

#---------------------------------------------------------------------------------------------------------------#
#                                           DEFAULTDICT                                                         #
#---------------------------------------------------------------------------------------------------------------#
# Trying out defaultdict to see if there is a big difference that comes when trying to count the number of words
# in a sentence

sentence = """This is a very long winded sentence. I don't think it has to be this long but honestly
              who is going to stop me! I could go on forever but honestly in getting bored! That's it
              I've ended now! Now I'm serious I've stopped typing! Ok"""

# Method 1 : Using KeyError to tell that there is a missing value and adding it
method1_dict = dict()
for word in sentence:
    try:
        method1_dict[word] += 1
    except KeyError:
        method1_dict[word] = 1
print(method1_dict)

# Method 2: Using a default dict to simplify the process
from collections import defaultdict, Counter
method2_dict = defaultdict(int) # Makes default value for a word 0
for word in sentence:
    method2_dict[word] += 1
print(method2_dict)
print(f"Is method1_dict and method2_dict equal: {method1_dict == method2_dict}")
# MY VERDICT: IF THE DICT BEING EMPTY ALWAYS RESULTS IN YOU ADDING AN ENTRY TO THE DICT WITH THAT KEY IT
# IS EASIER AND LESS ERROR PRONE TO USE DEFAULTDICT


#---------------------------------------------------------------------------------------------------------------#
#                                       COUNTERS                                                                #
#---------------------------------------------------------------------------------------------------------------#
# Counters provide a very easy way to solve our word counting issue
counts = Counter(sentence)
print(counts.most_common(5))