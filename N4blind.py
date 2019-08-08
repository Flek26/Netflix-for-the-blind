#! /usr/bin/python3

#Flek's Netflix Show reccomender for the Blind. 
'''
    Based off of the category you wish to brwose (or all),
    It will randomly pick a show / movie for you that 
    are available from Netflix with Audio Description tracks.
    
    Plan to have voice control / tts to make it easy to use. 
    
    Available generes are:

    Action | Comedy | Documentary | Drama | Horror | Kids & Family | Sci-Fi & Fantasy | Thriller | Other
'''
import pyttsx
def main():

    engine = pyttsx.init()
    engine.say('Good morning.')
    engine.runAndWait()

if __name__ == '__main__':
    main()
