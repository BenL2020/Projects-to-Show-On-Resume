# Code for my website version of target word selector code
# Ben Lambright

from flask import Flask, request
# functions and variables to import
from Final_Product import klist_creator, CVC_list_creator, allfound, backing, fronting, gliding, stopping, vowelization, affrication, deaffrication
from Final_Product import alveolarization, depalatalization, labializaiton, denasalization
from processing import step1, step2, write_up

#essential variables
klist = klist_creator()
clean_klist = ", ".join(klist)
CVC_list = CVC_list_creator()
backing_writeup = write_up(backing)
fronting_writeup = write_up(fronting)
gliding_writeup = write_up(gliding)
stopping_writeup = write_up(stopping)
vowelization_writeup = write_up(vowelization)
affrication_writeup = write_up(affrication)
deaffrication_writeup = write_up(deaffrication)
alveolarization_writeup = write_up(alveolarization)
depalatalization_writeup = write_up(depalatalization)
labializaiton_writeup = write_up(labializaiton)
denasalization_writeup = write_up(denasalization)

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        word1 = None
        word2 = None
        word3 = None
        word4 = None
        try:
            word1 = str(request.form["word1"])
        except:
            errors += "<p>{!r} is not a string, please type in one of the recommended words.</p>\n".format(request.form["word1"])
        try:
            word2 = str(request.form["word2"])
        except:
            errors += "<p>{!r} is not a string, please type in one of the recommended words.</p>\n".format(request.form["word2"])
        try:
            word3 = str(request.form["word3"])
        except:
            errors += "<p>{!r} is not a string, please type in one of the recommended words.</p>\n".format(request.form["word3"])
        try:
            word4 = str(request.form["word4"])
        except:
            errors += "<p>{!r} is not a string, please type in one of the recommended words.</p>\n".format(request.form["word4"])
        if word1 is not None and word2 is not None and word3 is not None and word4 == "":
            first_word = step1(word1, CVC_list, klist)
            second_word = step2(word2)
            third_word = word3
            allfound_list = allfound(first_word, second_word, third_word)
            allfounds = " ".join(allfound_list)
            return '''
                <html>
                    <body style="background-color:  #ffebcc; padding-right: 30px; padding-left: 30px;">
                        <p>You selected {word1}, {word2}, and {third_word}.</p>
                        <p style="text-align: center; font-size: 125%;">Here are the target words I found:</p>
                        <div style="border: 2px solid black; margin: 25px 200px; background-color:  white;">
                            <p style="text-align: center; font-size: 110%;">{allfounds}</p>
                        </div>
                        <p style="margin: 50px 0px">Not seeing any target words? There are some selections that my program just can't generate target words for. Try a
                        different combination or typing in consonants instead.</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(word1=word1, word2=word2, first_word=first_word, second_word=second_word, third_word=third_word,
            allfounds=allfounds)
        if word1 is not None and word3 is not None and word4 is not None and word2 is not None:
            first_word = step1(word1, CVC_list, klist)
            word4 = word4.lower()
            second_word = step2(word4)
            third_word = word3
            allfound_list = allfound(first_word, second_word, third_word)
            allfounds = " ".join(allfound_list)
            return '''
                <html>
                    <body style="background-color:  #ffebcc; padding-right: 30px; padding-left: 30px;">
                        <p>You selected {word1}, {word4}, and {third_word}.</p>
                        <p style="text-align: center; font-size: 125%;">Here are the target words I found:</p>
                        <div style="border: 2px solid black; margin: 25px 200px; background-color:  white;">
                            <p style="text-align: center; font-size: 110%;">{allfounds}</p>
                        </div>
                        <p style="margin: 50px 0px">Not seeing any target words? Check spelling and capitalization, you should have typed in one of the bolded options
                        exactly as it was written. Of course, there are some selections that my program just can't generate target words for.</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(word1=word1, word4=word4, first_word=first_word, second_word=second_word, third_word=third_word,
            allfounds=allfounds)

    return '''
        <html>
            <body style="background-color:  #ffebcc;">
                {errors}
                <head>
                    <title>Target Word Selector</title>
                    <link rel="stylesheet" href="base.css">
                </head>
                <div style="border: 2px dotted black; background-color: powderblue;">
                <h1>Target Word Selector</h1>
                <h1 style="font-size: 100%;">By Ben Lambright<h1>
                </div>
                <div style="text-align: center; padding-right: 200px; padding-left: 200px;">
                    <p class="intro">Table of Contents</p>
                    <p style="line-height: 75%;"><a href="#background">About this website</a></p>
                    <p style="line-height: 75%;"><a href="#generate">Generate target words here!</a></p>
                    <p style="line-height: 75%;"><a href="#processes">More info on phonological processes</a></p>
                    <p style="line-height: 75%;"><a href="#future">Future work</a></p>
                    <p style="line-height: 75%;"><a href="#list">List of possible target words</a></p>
                    <p class="spacing">---</p>
                    <p class="intro"  id="background">About this website<p>
                    <p>Last year, I wrote a computer program that helps speech-language pathologists (SLPs) prepare therapy sessions for
                    children with speech disorders. It provides "target words" that people can practice pronouncing that are drawn from a list
                    of words appropriate for early-elementary school students. I turned my target word selector program into a website (creating
                    it from scratch) so that anyone can use it. For example, if you select CVC, type in f, and select beginning of the word,
                    the target words returned will be for, fan, fat, fed, fib, fig, fin, fit, fog, and fun.</p>
                <p class="spacing">---</p>
                    <p class="intro" id="generate">Generate your target words!</p>
                    <form method="post" action=".">
                        <p>Please select either all possible words or CVC words, which are words that start and
                        end with a consonant and only have a single vowel in the middle like "cat". CVC stands for consonant-vowel-consonant.</p>
                        <select name="word1">
                            <option></option>
                            <option value="CVC">CVC</option>
                            <option value="all">all possible words</option>
                        </select>
                        <p>Please select a phonological process.</p>
                        <select name="word2">
                            <option></option>
                            <option value="backing">backing</option>
                            <option value="fronting">fronting</option>
                            <option value="gliding">gliding</option>
                            <option value="stopping">stopping</option>
                            <option value="vowelization">vowelization</option>
                            <option value="affrication">affrication</option>
                            <option value="deaffrication">deaffrication</option>
                            <option value="alveolarization">alveolarization</option>
                            <option value="depalatalization">depalatalization</option>
                            <option value="labializaiton">labializaiton</option>
                            <option value="denasalization">denasalization</option>
                        </select>
                        <p>Alternatively, you can type in a single consonant, like <strong>f</strong>, to search for target words with that
                        consonant.</p>
                        <p><input name="word4" /></p>
                        <p>Please select either beginning, end, or anywhere in the word in order to search for the target sounds in a specific
                        part of the word</p>
                        <select name="word3">
                            <option></option>
                            <option value="beginning">beginning of the word</option>
                            <option value="end">end of the word</option>
                            <option value="anywhere">anywhere in the word</option>
                        </select>
                        <p><input type="submit" value="Click here to generate your target words!"/></p>
                    </form>
                <p class="spacing">---</p>
                    <p class="intro" id="processes">More on the phonological processes:</p>
                    <p>Phonological processes are the types of speech sound errors of speech disorders that my program focuses on.</p>
                    <p>{backing_writeup}</p>
                    <p>{fronting_writeup}</p>
                    <p>{gliding_writeup}</p>
                    <p>{stopping_writeup}</p>
                    <p>{vowelization_writeup}</p>
                    <p>{affrication_writeup}</p>
                    <p>{deaffrication_writeup}</p>
                    <p>{alveolarization_writeup}</p>
                    <p>{depalatalization_writeup}</p>
                    <p>{labializaiton_writeup}</p>
                    <p>{denasalization_writeup}</p>
                <p class="spacing">---</p>
                    <p class="intro" id="future">Hopes for the future</p>
                    <p>As opposed to just searching for words that have the target sound at the beginning, end, or anywhere in the word, I also
                    want to be able to search for the target sound in the middle of the word and in the beginning, middle and end of a
                    syllable.</p>
                    <p>In addition to searching for individual consonants, I would like to be able to search for consonant blends and digraphs.
                    Consonant blends are when two ore more consonants make sounds together like "sl" and "br." Digraphs are when two or more consonats
                    make a singular sound together, like "sh" or "tch"</p>
                    <p>I'd like to find minimal pairs for the target words. Minimal pairs are pairs of words that are identical in every
                    way other than one speech sound, like "thing" and "sing"</p>
                    <p>For those who are still too young to read, I'd like to add images corresponding to target words.</p>
                    <p>I also need to fix the fact that my program always considers the letter y a consonant. I need to find a way for the code to
                    distinguish between the consonant and vowel y.</p>
                <p class="spacing">---</p>
                    <p class="intro" id="list">This is the list I search for target words from</p>
                    <p>{clean_klist}</p>
                    <p>I compiled my list from the recommendations of speech-language pathologists that I interviewed, largely taking the words from
                    the Dolch and Fry sight word lists</p>
                </div>
            </body>
        </html>
    '''.format(errors=errors, backing_writeup=backing_writeup, fronting_writeup=fronting_writeup, gliding_writeup=gliding_writeup,
    stopping_writeup=stopping_writeup, vowelization_writeup=vowelization_writeup, affrication_writeup=affrication_writeup,
    deaffrication_writeup=deaffrication_writeup, alveolarization_writeup=alveolarization_writeup, depalatalization_writeup=depalatalization_writeup,
    labializaiton_writeup=labializaiton_writeup, denasalization_writeup=denasalization_writeup, clean_klist=clean_klist)
