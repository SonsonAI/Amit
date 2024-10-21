import os
class TextFileReader:
    def __init__(self,file_path): #intial function where the path should be received
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.data = file.read()
            print(self.data)
    def count_lines(self):        #function to count lines in the txt file
        with open(self.file_path, 'r') as file:
            file = file.readlines()
            print("Number of lines: ",len(self.data))
    def count_words(self):        #Count number of words in file
        with open(self.file_path,'r') as file:
            file = file.read().split(" ")
            print("Number of words: ",len(self.data))
    def count_characters(self):    #Count number of characters
        with open(self.file_path,"r") as file:
            file = file.read()
            print("Number of characters: ",len(self.data))
    def unique_words_counter(self):
        with open(self.file_path,'r') as file:
            list1 = file.read().split(" ")
            unique_words = set(list1)
            counts = {word: 0 for word in unique_words}
            for i in unique_words:
                for j in list1:
                    if i == j:
                        counts[i] += 1
            print(counts)
         
FilePath = input("Enter File Path: ")
Filepath = FilePath.replace("\\","/") # this line corrects the path destination
x = TextFileReader(FilePath) #File Path must be added as an argument to display and read it
x.count_lines()
x.count_words()
x.count_characters()
x.unique_words_counter()