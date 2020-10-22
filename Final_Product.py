#THIS IS THE OFFICIAL, FINAL DRAFT OF MY PROTOTYPE

#Benjamin Lambright
#search program for target words for phonological processes
#This file should include all the functions necessary to run my complete program for June

#first wrote some functions to manipulate and create my complete lists of words

#making sure no repeats in a given list
def list_cleaner(list):
    #puts in every word in the list so long as the word is not in the list so far
    list = [word for num, word in enumerate(list) if word not in list[:num]]
    return list

#creation of klist and CVC_list
#klist
def klist_creator():
    #all this pulls out the list from a text file I made of the list exported from google drive
    with open("/Users/ben/KindergartenWords.txt", "r") as w:
        klist = w.read().split()
    #the first word in the list is a bit of code, not an actual word so I deleted it
    klist.pop(0)
    #use the same code as in my list_cleaner function
    klist = [word for num, word in enumerate(klist) if word not in klist[:num]]
    return klist
klist = klist_creator()

# bring in the other lists
def cv_klist_creator():
    #for each letter of each word of klist, a copy of klist is made where each vowel is replaced with V and if it is
    #not a vowel, it is replaced with C
    cv_klist = [''.join(('V' if letter in {'a', 'e', 'i', 'o', "u"} else 'C') for letter in word) for word in klist]
    return cv_klist
cv_klist = cv_klist_creator()

def CVC_list_creator():
    #for every word in klist, if it corresponds to CVC in cv_klist, it is put into CVC_list
    CVC_list = [word for word in klist if cv_klist[klist.index(word)] == "CVC"]
    return CVC_list
CVC_list = CVC_list_creator()

#dictionary merger for the sound catagories
#makes a new array that is a copy of the first array with the second array attached to that one
def dict_merger(x, y):
    z = x.copy()
    z.update(y)
    return z

#deletes all the elements in one dict from another dict
def dict_cutter(x, y):
    #converts the first array into a list, leaving out all elements which are also in the second array
    x_list = [letter for letter in x if letter not in y]
    #converts it back into an array
    x_dict = {*x_list}
    return x_dict

#the following are the sounds, phonological processes, and a function to present them

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

#explanations of each phonological process
#function to make them. When using this, but * before the list to split the two elements of it
def bio(process, source):
    print(process)
    print("from this source: " + source)
    print()
    return

#lists to put into the function
backing = ["Backing is when alveolar sounds, including /t/, /n/, /l/, /s/, /d/, are replaced with velar "
          "sounds like /k/ and /g/", "https://i.pinimg.com/originals/c8/b9/d5/c8b9d5de9c880a5cf053f1d5284f02bd.png"]
fronting = ["Fronting is when velar and post-alveolar sounds, including /k/, /g/, /j/, are replaced with "
          "alveolar sounds like /t/ and /s/", "https://www.sltinfo.com/phon101-fronting/"]
gliding = ["Gliding is when sounds like /r/ and /l/ are replaced with sounds like /y/ and /w/",
           "https://www.sltinfo.com/phon101-gliding/"]
# IPA would actually have it be /j/, not /y/, but that takes more explaining for now
stopping = ["Stopping is when the air flow in affricates and fricatives like /h/ and /z/ are stopped "
            "with consonants like /t/ and /d/", "https://www.sltinfo.com/phon101-stopping/"]
vowelization = ["Vowelization is when /l/ or /r/ sounds are replaced with a vowel.",
                "https://i.pinimg.com/originals/c8/b9/d5/c8b9d5de9c880a5cf053f1d5284f02bd.png"]
affrication = ["Affrication is when a nonaffricate sound (any consonant that is not an affricate) is replaced with an "
               "affricate like /j/",
               "https://i.pinimg.com/originals/c8/b9/d5/c8b9d5de9c880a5cf053f1d5284f02bd.png"]
deaffrication = ["Deaffrication is when an affricate, like /j/, is replaced with a fricative or stop like /d/ or /h/",
                 "https://i.pinimg.com/originals/c8/b9/d5/c8b9d5de9c880a5cf053f1d5284f02bd.png"]
alveolarization = ["Alveolarization is when an alveolar sound like /n/ or /s/ replaces a nonalveolar sound, which is "
                   "any consonant which is not an alveolar sound.",
                   "https://www.home-speech-home.com/phonological-processes.html"]
depalatalization = ["Depalatalization is when a palatal sound like /y/ or a palato-alveolar sound like /j/ are replaced"
                    " with a fricative or stop like /s/ or /d/",
                    "https://www.home-speech-home.com/phonological-processes.html"]
labializaiton = ["Labialization is when nonlabial sounds, normally alveolar sounds like /t/ and /s/, are replaced with"
                 " labial sounds like /p/ and /w/", "https://www.sltinfo.com/phon101-labialization/"]
denasalization = ["Denasalization is when nasal sounds like /m/ and /n/ are replaced with nonnasal sounds like /t/ or /d/",
                  "https://www.sltinfo.com/phon101-denasalization/"]
#make sure to also list it in all_proesses

all_processes = [backing, fronting, gliding, stopping, vowelization, affrication, deaffrication, alveolarization,
                 depalatalization, labializaiton, denasalization]

#from here on I write the function for search. I build it inside out, starting with the inner parts of the function
#and moving on to the bigger and bigger parts like a matryoshka doll

#prints the new list of target words
def list_printer(found):
    print()
    print("Here is a list of suggested target words!")
    #makes sure that the brackets and quotes aren't put into the list printed
    print(', '.join(found))

#actually searches the list for what's given
#allfound searches for all of a particular sound group
def allfound(list, sound_list, locus):
    #locus is the location given for where to search in the list
    if locus == "end":
        #makes a list of all the words which end with a letter in the sound_list
        allfound = [word for word in list for letter in word if word[-1] == letter in sound_list]
        allfound = list_cleaner(allfound)
        return list_printer(allfound)
    if locus == "begining":
        #makes a list of all the words which start with a letter in the sound_list
        allfound = [word for word in list for letter in word if word[0] == letter in sound_list]
        allfound = list_cleaner(allfound)
        return list_printer(allfound)
    else:
        #makes a list of all the words which have a letter in the sound_list
        allfound = [word for word in list for letter in word if letter in sound_list]
        allfound = list_cleaner(allfound)
        return list_printer(allfound)
#allfound(klist, alveolar_sounds, "kjsndf")

#xfound searches for a particular sound in a group
def xfound(list, sound, locus):
    if locus == "end":
        #makes a list of all the words which have a particular sound at the end of the word in a given list
        xfound = [word for word in list if word[-1] == sound]
        xfound = list_cleaner(xfound)
        return list_printer(xfound)
    if locus == "begining":
        #makes a list of all the words which have a particular sound at the begining of the word in a given list
        xfound = [word for word in list if word[0] == sound]
        xfound = list_cleaner(xfound)
        return list_printer(xfound)
    else:
        #makes a list of all the words which have a particular sound anywhere in a word in a given list
        xfound = [word for word in list for letter in word if letter == sound]
        xfound = list_cleaner(xfound)
        return list_printer(xfound)
#xfound(CVC_list, "begining", "s")

#finds which letter to search for and directs it to x and allfound
def search_letter(sound_list):
    #first ask the user if they want to search for CVC or all words
    print("Would you like to search for specifically CVC words? Type all, CVC"
                    ", or neither (make sure CVC is in all caps)")
    list = input("type here: ")
    #then ask the user if they want to search for sounds at the begining, end, or anywhere in the word
    print("Would you like to search for when these sounds are at the begining of a word, the end,"
                    " or anywhere. Type begining, end, anywhere")
    locus = input("type here: ")
    if list == "all":
        # finds which letter they are tyring to search for
        #asks the user which sound they want to search for
        print("Which backing sound would you like to search for? Type " + (', '.join(sound_list)) + ", or all or none")
        sound = input("type here: ")
        if sound == "all":
            # just prints all words with target sounds in the klist
            return allfound(klist, sound_list, locus)
        if sound == "none":
            return print("ending search...")
        else:
            # prints the specific sound which the user selected
            return xfound(klist, sound, locus)
    if list == "CVC":
        #does the same thing as the if statement above only using the CVC_list
        print("Which sound would you like to search for? Type " + (', '.join(sound_list)) + " or, all or none")
        sound = input("type here: ")
        if sound == "all":
            return allfound(CVC_list, sound_list, locus)
        if sound == "none":
            return print("ending search...")
        else:
            # prints the specific sound which the user selected
            return xfound(CVC_list, sound, locus)
    else:
        return print("I will hopefully find other forms of this list   ")
#search_letter(alveolar_sounds)

#complete search
def phonological_search():
    #user first types in the phonological process they would like to search for
    print("Which phonological process are the target words meant for?")
    process = input("type here: ")
    #makes the input case insensitive
    process = process.lower()
    #all of these take the input and if it is equal to a process I have, I return its bio
    # and then search for it using the search_letter function
    if process == "backing":
        bio(*backing)
        return search_letter(alveolar_sounds)
    if process == "fronting":
        bio(*fronting)
        return search_letter(dict_merger(velar_sounds, post_alveolar_sounds))
    if process == "gliding":
        bio(*gliding)
        return search_letter(gliding_sounds)
    if process == "stopping":
        bio(*stopping)
        return search_letter(dict_merger(affricate_sounds, fricative_sounds))
    if process == "vowelization":
        bio(*vowelization)
        return search_letter(vowelization_sounds)
    if process == "affrication":
        bio(*affrication)
        return search_letter(nonaffricate_sounds)
    if process == "deaffrication":
        bio(*deaffrication)
        return search_letter(affricate_sounds)
    if process == "alveolarization":
        bio(*alveolarization)
        return search_letter(nonalveolar_sounds)
    if process == "depalatalization":
        bio(*depalatalization)
        return search_letter(dict_merger(palatal_sounds, palatoalveolar_sounds))
    if process == "labialization":
        bio(*labializaiton)
        return search_letter(nonlabial_sounds)
    if process == "denasalization":
        bio(*denasalization)
        return search_letter(nasal_sounds)
    else:
        return print("Cannot find this phonological process. Make sure you spelt it correctly.")
#phonological_search()

#demonstration of my program
def demonstration():
    print("Hello class! Here is list of all of the phonological processes you can see a demonstration of!")
    print()
    #prints the bios of all of the processes I have
    for process in all_processes:
        bio(*process)
    input("Press any key to start the search!")
    print()
    #then I actually run the program to search for phonological processes
    phonological_search()
    return
demonstration()