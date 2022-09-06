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

#---------------------------------------------------------------------------------------------------------------#
#                                           SETS                                                                #
#---------------------------------------------------------------------------------------------------------------#

# Want to test the speed and ability to get distinct items of a list and set
sentence = """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
    molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
    numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
    optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
    obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
    nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
    tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
    quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos 
    sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
    recusandae alias error harum maxime adipisci amet laborum. Perspiciatis 
    minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit 
    quibusdam sed amet tempora. Sit laborum ab, eius fugit doloribus tenetur 
    fugiat, temporibus enim commodi iusto libero magni deleniti quod quam 
    consequuntur! Commodi minima excepturi repudiandae velit hic maxime
    doloremque. Quaerat provident commodi consectetur veniam similique ad 
    earum omnis ipsum saepe, voluptas, hic voluptates pariatur est explicabo 
    fugiat, dolorum eligendi quam cupiditate excepturi mollitia maiores labore 
    suscipit quas? Nulla, placeat. Voluptatem quaerat non architecto ab laudantium
    modi minima sunt esse temporibus sint culpa, recusandae aliquam numquam 
    totam ratione voluptas quod exercitationem fuga. Possimus quis earum veniam 
    quasi aliquam eligendi, placeat qui corporis!
"""
# With list
# 1) Membership
very_long_list = list(sentence)
import time
start_time = time.time()
print('!' in very_long_list)
print(f"List membership operation took {time.time() - start_time} seconds")

# 2) Get list of distinct items
start_time = time.time()
distinct_items = []
for item in very_long_list:
    if item not in distinct_items:
        distinct_items.append(item)
print(f"Amount of time to create distinct list {time.time() - start_time}")
print(f"Length of distinct list is {len(distinct_items)}")

# With set
# 1) Membership
long_set = set(sentence)
start_time = time.time()
print('!' in long_set)
print(f"Set membership operation took {time.time() - start_time} seconds")

# Creating a distinct list of items
list2 = list(sentence)
start_time = time.time()
set_from_list = set(list2)
list3 = list(set_from_list)
print(f"Amount of time to create distinct list from set is {time.time() - start_time} seconds")
print(f"Length of distinct list is {len(list3)}")