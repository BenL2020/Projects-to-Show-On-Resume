#processing code for specifically the website

#functions for making the dictionaries
#deletes all the elements in one dict from another dict
def dict_cutter(x, y):
    #converts the first array into a list, leaving out all elements which are also in the second array
    x_list = [letter for letter in x if letter not in y]
    #converts it back into an array
    x_dict = {*x_list}
    return x_dict
#dictionary merger for the sound catagories
#makes a new array that is a copy of the first array with the second array attached to that one
def dict_merger(x, y):
    z = x.copy()
    z.update(y)
    return z

#dictionaries of all the different catagories of sounds
consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
alveolar_sounds = {"t", "n", "l", "s", "d", "z"} #also the th's and ts
nonalveolar_sounds = dict_cutter(consonants, alveolar_sounds)
post_alveolar_sounds = {"j"} #there are more but I don't have a way to add them yet
velar_sounds = {"k", "g"} #same here
affricate_sounds = {"j"} #'j' makes two sounds in english, one is a post-alveolar sound and the is an affricate
nonaffricate_sounds = dict_cutter(consonants, affricate_sounds) #all consonants that are not affricates
gliding_sounds = {"r", "l"} #focusing on liquid gliding for now
fricative_sounds = {"v", "f", "z", "s", "j", "h"} #there are more
vowelization_sounds = {"l", "r"} #not going to use the same as gliding sounds in case I add to gliding
palatal_sounds = {"y"}
palatoalveolar_sounds = {"j"} #there are more like "ch", "sh", and "zh"
labial_sounds = {"p", "b", "m", "w", "f", "v"}
nonlabial_sounds = dict_cutter(consonants, labial_sounds)
nasal_sounds = {"m", "n"} #also ng


#figures out if it wants CVC or all
def step1(first_word, CVC_list, klist):
    if first_word == "CVC":
        first_word = CVC_list
    else: first_word = klist
    return first_word

def step2(second_word):
    if len(second_word) == 1:
        second_word = {second_word}
    if second_word == "backing":
        second_word = alveolar_sounds
    if second_word == "alveolarization":
        second_word = nonalveolar_sounds
    if second_word == "fronting":
        second_word = dict_merger(velar_sounds, post_alveolar_sounds)
    if second_word == "stopping":
        second_word = dict_merger(affricate_sounds, fricative_sounds)
    if second_word == "affrication":
        second_word = nonaffricate_sounds
    if second_word == "deaffrication":
        second_word = affricate_sounds
    if second_word == "gliding":
        second_word = gliding_sounds
    if second_word == "depalatalization":
        second_word = dict_merger(palatal_sounds, palatoalveolar_sounds)
    if second_word == "vowelization":
        second_word = vowelization_sounds
    if second_word == "labialization":
        second_word = nonlabial_sounds
    if second_word == "denasalization":
        second_word = nasal_sounds
    return second_word

def write_up(process):
    return process[0]
