from tkinter import*
import tkinter as tk
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import warnings
warnings.filterwarnings('ignore')
class IMS():
    def LinearRegressions(self):
        data = pd.read_csv(r"D:/AMIT/Amit/MachineLearningGUI/Salary_Data.csv") # real
        X = data.iloc[:,:-1]
        y = data.iloc[:,1]
        X_train , X_test , y_train , y_test = train_test_split(X,y,train_size=0.8,random_state = 10)
        my_model = LinearRegression()
        my_model.fit(X_train,y_train)
        y_pred = my_model.predict(X_test)
        mse = mean_squared_error(y_test,y_pred)
        rsq = r2_score(y_test,y_pred)
        print('mean squared error :',mse)
        print('r square :',rsq)
        print('Intercept of the model:',my_model.intercept_)
        print('Coefficient of the line:',my_model.coef_)
        y_hat = 9357 * 7 +  26089 
        print(y_hat)
        x=int(self.entryRegression.get())
        y_hat = 9357 * x +  26089 
        self.resultRegressionLabel.config(text=f"Expected Salary: {y_hat}")
        self.resultRegressionLabel.pack(side="bottom")
        
    def __init__(self, window):
        self.window = window
        self.window.geometry("1350x700+0+0")
        self.window.title("Machine Learning")
        self.window.config(background ="white")

        frame = Frame(self.window,bg="#d9d4d4",highlightbackground="black", highlightthickness=1)
        frame.place(x= 0 , y=75)
        frameButtons = Frame(self.window,width=400, height=120)
        frameButtons.place(relx=0.5, rely=0.2, anchor="center")
        frameButtons.pack_propagate(False)
        mainTitle = Label(self.window, text="AMIT Projects", font=("Raleway",40,"bold"), bg="#01468a", fg="white",
                        highlightbackground='white',highlightthickness=2,pady= 30).place(x= 0, y =0,relwidth=1,relheight=0.05,height = 50)
        self.regressionLabel = Label(frame, text="Linear Regression" , font = ("Raleway",20,'bold'), bg="#d9d4d4",fg="black").pack(side="top")
        self.EntryLabel = Label(frameButtons,text="Enter Years: ",font= ('Raleway',10,'bold')).pack(side="top")
        self.entryRegression = Entry(frameButtons)
        self.entryRegression.config(font=('Raleway',10),width= 20,bg="#f2f0f0")
        self.entryRegression.pack()
        self.entrybutton = Button(frameButtons,text="submit",command=self.LinearRegressions).pack(side="top")
        self.resultRegressionLabel = Label(frameButtons,font=('Arial Rounded MT',20),fg="#00ff22")
        label1 = Label(frame, text="Project 1" , font = ("Raleway",20,'bold'), bg="#d9d4d4",fg="black",pady=10).pack(side="top")
        label2 = Label(frame, text="Project 2" , font = ("Raleway",20,'bold'), bg="#d9d4d4",fg="black",pady=10).pack(side="top")
        label3 = Label(frame, text="Project 3" , font = ("Raleway",20,'bold'), bg="#d9d4d4",fg="black",pady=10).pack(side="top")
        label4 = Label(frame, text="Project 4" , font = ("Raleway",20,'bold'), bg="#d9d4d4",fg="black",pady=10).pack(side="top")
        label5 = Label(frame, text="Project 5" , font = ("Raleway",20,'bold'), bg="#d9d4d4",fg="black",pady=10).pack(side="top")

if __name__ == "__main__":
    window = Tk()
    obj = IMS(window)
    window.mainloop()