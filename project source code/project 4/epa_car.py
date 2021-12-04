import pylab
import csv
#functions

#function for creating list of highway mileage with make and model
def create_mileage_list():
#make:3,model:4,mpg:10
  epa_file=open("epadata2015.csv","r")
  mileage_list = []
  
  #To get rid of the header
  header=epa_file.readline()
  
  epa_reader = csv.reader(epa_file) 
  for line in epa_reader: 
    if 'car' in line[70]:
      mileage_list.append((line[2],line[3],int(line[10])))
  epa_file.close()
  return mileage_list
#function for plotting data from csv file
def plot(z,choice3):
  fp = open("epadata2020.csv","r")
  x,y = [],[]
  reader=csv.reader(fp)
  next(reader)
  for line in reader:
    try:
      
      line_lst = int(line[0])
      x.append(line_lst) 
      mpg=float(line[z])
      y.append(mpg)

    except ValueError:
      break
  fp.close()

  pylab.plot(x,y)
  pylab.ylabel("Highway MPG")
  pylab.xlabel("Year")
  pylab.title("EPA annual average highway MPG data")
  
  if choice3.lower()=="d":
    pylab.show()
  elif choice3.lower()=="f":
    pylab.savefig("epa_plot.png")
  return
#function for gathering the min and max 
def max_min_mileage(mileage_list, max_mileage, min_mileage):

 max_mileage_list = []
 min_mileage_list = []

 for car_tuple in mileage_list:
  if car_tuple[2] == max_mileage:
    max_mileage_list.append(car_tuple)
  if car_tuple[2] == min_mileage:
    min_mileage_list.append(car_tuple)

 return max_mileage_list, min_mileage_list

#main program
print("The main purpose of this code is to show Epa fuel consumption data and\nPlotting fuel trends over the past few years")
choice=input("Enter one to see mileage info\nEnter two for a trend plot\n")
#choice number one
if choice=="1":
    try:
      Mpg_min,Mpg_max=input("Please enter the MPG interval\n(e.g 1-10)\n").split("-")
      Mpg_min_int,Mpg_max_int=int(Mpg_min),int(Mpg_max)
    except ValueError:  
      print("You entered a incorrect value")
      Mpg_min,Mpg_max=input("Please enter the MPG interval\n(e.g 1-10)\n").split("-")
      Mpg_min_int,Mpg_max_int=int(Mpg_min),int(Mpg_max)
    
    mileage_list=create_mileage_list()
    
    max_cars,min_cars=max_min_mileage(mileage_list,Mpg_max_int,Mpg_min_int)
    print("Max vehicles","*"*80,"\n")
    for vehicles in max_cars:
      print(vehicles[0],vehicles[1])
    print("Min vehicles","*"*80,"\n")
    for vehicles in min_cars:
        print(vehicles[0],vehicles[1])
    print("\nOverall interval vehicles","*"*80,"\n")
    for cars in mileage_list:
      if cars[2]<=Mpg_max_int and cars[2]>=Mpg_min_int:
        print(cars[0].title(),cars[1])


#choice number 2 
elif choice=="2":
  choice2=input("Which measure are you interested in?\n(H)ighway MPG\n(C)ity MPG\n(O)verall MPG\n")
  if choice2.lower()=="h":
    choice3=input("Would you like to \n(D)isplay on screen \nor\nsave to (F)ile?\n")
    plot(6,choice3)

  elif choice2.lower()=="c":
    choice3=input("Would you like to \n(D)isplay on screen \nor\nsave to (F)ile?\n")
    plot(5,choice3)

  elif choice2.lower()=="o":
    choice3=input("Would you like to \n(D)isplay on screen \nor\nsave to (F)ile?\n")
    plot(4,choice3)
  else:
    print("Invalid choice exiting program")

#for invalid choice
else:
  print("Invalid choice Exiting the program")