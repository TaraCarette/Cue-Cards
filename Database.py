import os
from PIL import Image
import pathlib
import random

# data is image or string, word is what it means
# directory is where we want to save
# dataType is boolean, 0 for pic, 1 for txt
def save(dataType, data, word, directory):
    # database folder - all folders for category (anatomy, mandarin, etc)
    if not os.path.exists("Databases"):
        os.mkdir("Databases")
    if not os.path.exists("Databases/" + directory):
        directory = "Databases/" + directory
        os.mkdir(directory)
    else:
        directory = "Databases/" + directory
    # make 2 folders in directory if not already there
    # definition folder and data folder
    if not os.path.exists(directory + "/Data"):
        os.mkdir(directory + "/Data")
        # if data folder doesn't exist, set number = 0
        number = "0"
    # if data folder already exists, get most recent number
    else:
        numFile = open(directory + "/number.txt","r")
        number = numFile.read()
        numFile.close();
        intNumber = int(number) + 1
        number = str(intNumber)
    if not os.path.exists(directory + "/Word"):
        os.mkdir(directory + "/Word")
    # inside data, pic folder and data folder
    if not os.path.exists(directory + "/Data/Pic"):
        os.mkdir(directory + "/Data/Pic")
    if not os.path.exists(directory + "/Data/Text"):
        os.mkdir(directory + "/Data/Text")
    # check if data is text or pic
    # save in diff folders
    if dataType == "0": # pic
        # if pic save as jpg
        # NUM_pic.jpg
        data.save(directory + "/Data/Pic/" + number + "_pic", "PNG")
    elif dataType == "1": # text
        # if text save as txt file
        # txtNUM.jpg
        file = open(directory + "/Data/Text/" + number + "_text.txt", "w")
        file.write(data)
        file.close()
    else:
        print ("You did not give a valid dataType. 0 = pic, 1 = string")
    
    # in data folder, save word as number_(0/1).txt
    numFile = open(directory + "/Word/" + number + "_" + dataType + ".txt", "w")
    numFile.write(word)
    numFile.close()
    # save last number
    file = open(directory + "/number.txt", "w")
    file.write(number)
    file.close()

# only returns file locations of word, data and dataType
def get(directory):
    # find word in Word/
    # split at _ and find number in 1st number
    # find dataType
    # return word file and corresponding file
    file = open(directory + "/number.txt","r")
    maxNum = file.read()
    maxNum = int(maxNum)
    num = random.randint(0, maxNum)
    num = str(num)
    #directory = "Databases/" + directory
    # find out if word is connected to pic or text
    
    if os.path.isfile(directory + "/Word/" + num + "_0.txt"): # pic
        fileWord = open(directory + "/Word/" + num + "_0.txt","r")
        word = fileWord.read()
        fileWord.close()
        fileData = open(directory + "/Data/Pic/" + num + "_pic.png")
        data = fileData.read()
        fileData.close()
        # return word location and data location
        array = [word,data]
        return (array)
    elif os.path.isfile(directory + "/Word/" + num + "_1.txt"): # text
        fileWord = open(directory + "/Word/" + num + "_1.txt","r")
        word = fileWord.read()
        fileWord.close()
        fileData = open(directory + "/Data/Text/" + num + "_text.txt")
        data = fileData.read()
        fileData.close()
        # return word location and data location
        array = [word,data]
        return (array)        
    else:
        print ("You screwed up")
global category
category = "Anatomy"
def call():
    #dataType = "1" # text
    #data = "Rhomboids, Levator scapula"
    #word = "Downwards rotation"
    #directory = "Anatomy"
    #save(dataType, data, word, directory)
    directory = "Databases/" + category
    print(directory)
    if os.path.isdir(directory):
        array = get(directory)
        return array
    #print("Word at " + array[0])
    #print("Data at " + array[1])

def getters(temp):
    category = temp 
#call("Anatomy")
    
