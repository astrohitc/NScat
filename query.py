import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from psrqpy import QueryATNF
import io
import requests
from rich import print


url="https://raw.githubusercontent.com/astrohitc/McGill-Manetar-Catalog/main/magnetar-package-data1%20-%20Sheet1.csv"
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))

#mag.loc[(mag['Period'])]

def magp():
    plt.subplot(2,2,1)
    plt.title('P-B diagram (ATNF)')
    plt.xlabel('log(P)')
    plt.ylabel('log(B)')
    plt.scatter(np.log(df['Period(atnf)'])/np.log(10), np.log(df['B(atnf)'])/np.log(10)) 
    #plt.subplot()
    plt.grid()
    
    plt.subplot(2,2,2)
    plt.title('P-B diagram (McGill)')
    plt.xlabel('log(P)')
    plt.ylabel('log(B)')
    plt.scatter(np.log(df['Period(McGill)'])/np.log(10), np.log(df['B(McGill)'])/np.log(10)) 
    #plt.subplot(212)
    plt.grid()

    plt.subplot(2,2,3)
    plt.title('P-Pdot diagram (ATNF)')
    plt.xlabel('log(P)')
    plt.ylabel('log(Pdot)')
    plt.scatter(np.log(df['Period(atnf)'])/np.log(10), np.log(df['Pdot(atnf)'])/np.log(10)) 
    #plt.subplot(212)
    plt.grid()

    plt.subplot(2,2,4)
    plt.title('P-Pdot diagram (McGill)')
    plt.xlabel('log(P)')
    plt.ylabel('log(Pdot)')
    plt.scatter(np.log(df['Period(McGill)'])/np.log(10), np.log(df['Pdot(McGill)'])/np.log(10)) 
    #plt.subplot(212)
    plt.grid()

    
    #plt.subplots_adjust(right=3)

    
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=2, 
                    top=2, 
                    wspace=0.4, 
                    hspace=0.4)

    plt.show()


def mag1():
   print("Hello! Welcome to the magnetar catalog package (or magcat)\nThis package will help you to query different parameters with respect to magnetars and help you analyze its properties through those parameters.\nWe present to you to five parameters which you will be able to query and those are:\n1)Name\n2)J-Name\n3)Spin Period\n4)Surface Magnetic Field\n5)Spin Period Derivative\n6)Characteristic Age\n7)Spin-Down Energy Rate\nIn this package you will be provided with both the radio observational values (from ATNF Pulsar Catalog; R. N. Manchester et al 2005) and the X-ray/Gamma Ray observational values (from Mcgill Magnetar Catalog (Olausen & Kaspi, 2014) for parameters like Spin Period, Spin period Derivative and Surface Magnetic Field.")
   print("The table visible below are some basic timing properties of magnetars\nTo query the table and to read further instructions, please read the [link=https://magcat.readthedocs.io/en/latest/]documentation")
   print("You can also query the P-Pdot and P-B diagrams associated with these magnetars") 
   print("These are the parameters available for querying")
   print(df.columns.tolist())
   print(df[['Name','Period(McGill)','Period(atnf)','B(McGill)','B(atnf)']])
   choice = ""
   #choice = input("What parameter would you like to query").split(",")
   if choice != "exit":
      input1=input("type s if you want to query a single parameter else type m for multiple parameters ")
   if input1=='s':
        data=pd.DataFrame()
        choice = input("What parameter would you like to query")
       #condition=input("Enter the conditions of the parameters in the same order you typed the above parameters: ").split(",")
       #print(df.loc[condition])
        if choice == 'Period':
          data=df[['Period(McGill)','Period(atnf)']]
          print(df[['Period(McGill)','Period(atnf)']])
        elif choice == 'B':
          data=df[['B(McGill)','B(atnf)']]
          print(df[['B(McGill)','B(atnf)']])
        elif choice == 'Pdot': 
          data=df[['Pdot(McGill)','Pdot(atnf)']]    
          print(df[['Pdot(McGill)','Pdot(atnf)']])
        elif choice == 'Name':
          data=df[['Name']]
          print(df[['Name','JName']])
        elif choice == 'Age':
          data=df[['Age']]
          print(df[['Age']])
        elif choice == 'Edot':
          data=df[['Edot']]
          print(df[['Edot']])
        choice=input("do you want to see the plots? if yes type y else n")
        if choice=='y':
            magp()    
        c1=input("if you want to save the table as a csv file type 'y' else type 'n' :")
        if c1=='y':
          name=input("enter the name of the file you want to save the table as: ")
          s=df[choice]
          return(data.to_csv(name))
         
   else:

    choice = input("What parameter would you like to query").split(",")
    print(df[choice])
    choice=input("do you want to see the plots? if yes type y else n")
    if choice=='y':
          magp()

    c1=input("if you want to save the table as a csv file type 'y' else type 'n' :")
    if c1=='y':
       name=input("enter the name of the file you want to save the table as: ")
       s=df[choice]
       return(s.to_csv(name))
