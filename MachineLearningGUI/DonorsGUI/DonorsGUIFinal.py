from tkinter import *
from tkinter import messagebox
import joblib
import pickle
import pandas as pd
from tkinter import filedialog
import numpy as np

def openFile():
    global model
    try:
        # Open a file dialog to select the model file
        file_path = filedialog.askopenfilename(
            title="Trained Model Selection",
            #filetypes=("Pickle Files", "*.pkl")
        )
        if file_path:
            with open(file_path, 'rb') as file:
                model = pickle.load(file)
            messagebox.showinfo("Success", "Model loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the model: {e}")

def predict():  # This function will predict
    try:
        if 'model' not in globals():
            messagebox.showwarning("Warning", 'Please load the model')
            return
        AgeValue = float(ageEntry.get())
        if AgeValue > 100 or AgeValue < 0:
            messagebox.showwarning("Warning", 'Age value is not right')
            ageEntry.delete(0,END)
        CapitalGainEntryValue = int(CapitalGainEntry.get())
        EducationValue = float(EducationEntry.get())
        HoursValue = float(HoursEntry.get())
        # Handling Martial Input value
        MartialValue = MatrialEntry.get()
        MartialValue = MartialValue.lower()
        if MartialValue != "yes" or MartialValue !="no":
            messagebox.showwarning("Warning", 'Marital Statue is not right')
        else:    
            MartialValue = MartialValue.replace("yes", "1").replace("no", "0")
            MartialValue = int(MartialValue)
        inputs = [
            AgeValue,
            HoursValue,
            CapitalGainEntryValue,
            MartialValue,
            EducationValue
        ]
        inputs = np.array(inputs).reshape(1, -1)
        prediction = model.predict(inputs)
        prediction = str(prediction)
        prediction = prediction.replace('1', 'a Donor').replace('0', 'not a Donor')
        messagebox.showinfo("Prediction", f"The Person is a: {prediction}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear():
    ageEntry.delete(0, END)
    CapitalGainEntry.delete(0, END)
    EducationEntry.delete(0, END)
    MatrialEntry.delete(0, END)
    HoursEntry.delete(0, END)

''' Window Settings '''
window = Tk()
window.geometry("560x410")
window.title("Donor Predictor")
window.config(background="#ffffff")
window.resizable(False, False)
photo = PhotoImage(file="D:\\AMIT\\Amit\\MachineLearningGUI\\DonorsGUI\\AMITLearning.jpeg")
window.iconphoto(True, photo)

''' Frame Settings '''
frame = Frame(window, bg="#ffffff")
frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

''' App Settings '''
# App title
label = Label(frame, text="Donor Predictor", fg='green', font=('Arial', 15, 'bold'), bg='white')
label.grid(row=0, column=0, columnspan=2, sticky=W, pady=10)

# Entries
ageEntry = Entry(frame, width=30)
CapitalGainEntry = Entry(frame, width=30)
EducationEntry = Entry(frame, width=30)
MatrialEntry = Entry(frame, width=30)
HoursEntry = Entry(frame, width=30)
MatrialEntry.insert(0,"Enter Yes or No")
# Entries Labels
AgeLabel = Label(frame, text="Enter Age: ", bg='white').grid(row=1, column=0, sticky=W, pady=5)
CapitalGainLabel = Label(frame, text="Enter Capital Gain: ", bg='white').grid(row=2, column=0, sticky=W, pady=5)
EducationLabel = Label(frame, text="Enter Educational Level: ", bg='white').grid(row=3, column=0, sticky=W, pady=5)
MartialLabel = Label(frame, text="Enter Martial: ", bg='white').grid(row=4, column=0, sticky=W, pady=5)
HoursLabel = Label(frame, text="Enter Hours: ", bg='white').grid(row=5, column=0, sticky=W, pady=5)

# Entries Packing
ageEntry.grid(row=1, column=1, pady=5)
CapitalGainEntry.grid(row=2, column=1, pady=5)
EducationEntry.grid(row=3, column=1, pady=5)
MatrialEntry.grid(row=4, column=1, pady=5)
HoursEntry.grid(row=5, column=1, pady=5)

# Buttons
ButtonP = Button(frame, text='Predict', command=predict, font=('Arial', 10, 'bold'), bg='#ffe369', activebackground='white')
ButtonP.grid(row=6, column=0, pady=10, sticky=W)

ClearButton = Button(frame, text="Clear", command=clear, font=('Arial', 10, 'bold'), bg='#ffe369', activebackground='white')
ClearButton.grid(row=6, column=1, pady=10, sticky=W)

FileButtonLoader = Button(frame, text="Load Model", command=openFile, font=('Arial', 10, 'bold'), bg='#ffe369', activebackground='white')
FileButtonLoader.grid(row=7, column=0, pady=10, sticky=W)
#Mouse Events

# def clearAction(event):
#         ageEntry.delete(0, END)
#         CapitalGainEntry.delete(0, END)
#         EducationEntry.delete(0, END)
#         MatrialEntry.delete(0, END)
#         HoursEntry.delete(0, END)

# window.bind("<ButtonRelease>",clearAction)


window.mainloop()
