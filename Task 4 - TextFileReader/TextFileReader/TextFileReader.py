import os
class TextFileReader:
    def __init__(self,file_path):           #intial function where the path should be received
        with open(file_path, 'r') as file:
            self.data = file.read()
            print(self.data)
    def count_lines(self,file_path):        #function to count lines in the txt file
        with open(file_path, 'r') as file:
            self.data = file.readlines()
            print("Number of lines: ",len(self.data))
    def count_words(self,file_path):        #Count number of words in file
        with open(file_path,'r') as file:
            self.data = file.read().split(" ")
            print("Number of words: ",len(self.data))
    def count_characters(self,file_path):    #Count number of characters
        with open(file_path,"r") as file:
            self.data = file.read()
            print("Number of characters: ",len(self.data))
         
FilePath = input("Enter File Path: ")
Filepath = FilePath.replace("\\","/") # this line corrects the path destination
x = TextFileReader(FilePath) #File Path must be added as an argument to display and read it
x.count_lines(FilePath)
x.count_words(FilePath)
x.count_characters(FilePath)