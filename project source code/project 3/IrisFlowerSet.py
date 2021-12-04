
import csv
import matplotlib.pyplot as plt
import statistics
#*******************************************************************************
def make_list(flower_name):
  sepal_length=[]
  speal_width=[]
  petal_length=[]
  petal_width=[]
  fp = open("iris.csv","r")
  reader=csv.DictReader(fp)
  for line in reader:
    if line["species"]==flower_name:
      sepal_length.append(float(line["sepal_length"]))
      speal_width.append(float(line["sepal_width"]))
      petal_length.append(float(line["petal_length"]))
      petal_width.append(float(line["petal_width"]))
  master_list=[sepal_length,speal_width,petal_length,petal_width]
  return master_list
#*******************************************************************************
def mean(flower_list):

#0:sepal length 1:sepal width 2:petal length 3:petal width
  avg_list=[0,0,0,0]
  flower_len=len(flower_list[0])

#store all sums in avg_list
  for y in range(0,4):
    for x in range(0,flower_len):
      avg_list[y]+=flower_list[y][x]

#divide all of the values
  for x in range(0,4):
      avg_list[x]/=flower_len
  return avg_list

#*******************************************************************************
def min_numbers(flower_list):
  min=[]
  for x in range(0,len(flower_list)):
    flower_list[x].sort()
  for x in range(0,len(flower_list)):
    min.append(flower_list[x][0])
  return min
#*******************************************************************************
def max_numbers(flower_list):
  max=[]
  for x in range(0,len(flower_list)):
    flower_list[x].sort()
  for x in range(0,len(flower_list)):
    max.append(flower_list[x][len(flower_list[0])-1])
  return max
#*******************************************************************************
def standard_dev(flower_list):
  std_dev=[]
  for x in range(0,len(flower_list)):
    std_dev.append(statistics.stdev(flower_list[x]))
  return std_dev
#*******************************************************************************
def prettyprint(flower_name,mean,min,max,std_dev):
    print('-'*90,"\n",flower_name,"\t\tsepal lenght:"," sepal width:",\
          " petal length:"," petal width:\n",'-'*90)
    line=" \t{:.2f}\t\t   {:.2f}\t\t     {:.2f}\t\t{:.2f}" #for formatting
    print("Mean:\t\t",line.format(mean[0],mean[1],mean[2],mean[3]))
    print("Minimum:\t",line.format(min[0],min[1],min[2],min[3]))
    print("Maximum:\t",line.format(max[0],max[1],max[2],max[3]))
    print("Standard deviation:",line.format(std_dev[0],std_dev[1],\
                                            std_dev[2],std_dev[3]))

    return

#*******************************************************************************

def make_dict(flower_name):
  sepal_length=[]
  speal_width=[]
  petal_length=[]
  petal_width=[]
  fp = open("iris.csv","r")
  reader=csv.DictReader(fp)
  for line in reader:
    if line["species"]==flower_name:
      sepal_length.append(float(line["sepal_length"]))
      speal_width.append(float(line["sepal_width"]))
      petal_length.append(float(line["petal_length"]))
      petal_width.append(float(line["petal_width"]))
  master_dict={"sepal length":sepal_length,"sepal width":speal_width,"petal length":petal_length,"petal width":petal_width}  
  return master_dict


#*******************************************************************************
def make_list2():
  sepal_length=[]
  speal_width=[]
  petal_length=[]
  petal_width=[]
  fp = open("iris.csv","r")
  reader=csv.DictReader(fp)
  for line in reader:
     sepal_length.append(float(line["sepal_length"]))
     speal_width.append(float(line["sepal_width"]))
     petal_length.append(float(line["petal_length"]))
     petal_width.append(float(line["petal_width"]))
  master_list=[sepal_length,speal_width,petal_length,petal_width]
  return master_list
#*******************************************************************************  
def prettyprint2(flower_name,flower_normalized_values):
    print('-'*101,"\n",flower_name,"\t\tsepal lenght:","\t sepal width:"," petal length:","\tpetal width:\n",'-'*100)
    line=" \t{:.2f}\t\t   {:.2f}\t\t     {:.2f}\t\t{:.2f}" #for formatting
    print("Normalized Minimum:\t",line.format(flower_normalized_values[5],flower_normalized_values[5],flower_normalized_values[5],flower_normalized_values[5]))
    print("Normalized Mean:\t",line.format(flower_normalized_values[0],flower_normalized_values[1],flower_normalized_values[2],flower_normalized_values[3]))
    print("Normalized Maximum:\t",line.format(flower_normalized_values[4],flower_normalized_values[4],flower_normalized_values[4],flower_normalized_values[4]))
    

    return
#*******************************************************************************
def normalize(flower_means,flower_min,flower_max):
  
  petal_wid_range,sepal_wid_range,petal_len_range,sepal_len_range=0.0,0.0,0.0,0.0
  #Subtracting the min from the max
  normalized_avg_list=[]
  sepal_len_range=flower_max[0]-flower_min[0]
  sepal_wid_range=flower_max[1]-flower_min[1]
  petal_len_range=flower_max[2]-flower_min[2]
  petal_wid_range=flower_max[3]-flower_min[3]
  
  a=flower_means[0]-flower_min[0]
  a/=sepal_len_range
  
  b=flower_means[1]-flower_min[1]
  b/=sepal_wid_range

  c=flower_means[2]-flower_min[2]
  c/=petal_len_range

  d=flower_means[3]-flower_min[3]
  d/=petal_wid_range
  normalized_avg_list=[a,b,c,d,1,0]
  #the min or max minus the min divided by the range will always equal zero or one so I just saved  the values at the end of the list

  return normalized_avg_list 


#*******************************************************************************
def sum_stats():
  flower_list=make_list2()
  flower_means=mean(flower_list)
  flower_min=min_numbers(flower_list)
  flower_max=max_numbers(flower_list)
  flower_normalized_values=normalize(flower_means,flower_min,flower_max)
  prettyprint2("All flowers",flower_normalized_values)
  return
#*******************************************************************************




  
#main program
print("Summary Statistics\n")
versicolor=make_list("versicolor")
versicolor_means=mean(versicolor)
versicolor_min=min_numbers(versicolor)
versicolor_max=max_numbers(versicolor)
versicolor_std_dev=standard_dev(versicolor)
prettyprint("vesicolor",versicolor_means,versicolor_min,versicolor_max,versicolor_std_dev)



virginica=make_list("virginica")
virginica_means=mean(virginica)
virginica_min=min_numbers(virginica)
virginica_max=max_numbers(virginica)
virginica_std_dev=standard_dev(virginica)
prettyprint("virginica",virginica_means,virginica_min,virginica_max,virginica_std_dev)



setosa=make_list("setosa")
setosa_means=mean(setosa)
setosa_min=min_numbers(setosa)
setosa_max=max_numbers(setosa)
setosa_std_dev=standard_dev(setosa)
prettyprint("setosa",setosa_means,setosa_min,setosa_max,setosa_std_dev)

print("\n"*10,"Normalized section\n")
sum_stats()

print("\n"*10,"Plotting section\n")
versicolor=make_dict("versicolor")
virginica=make_dict("virginica")
setosa=make_dict("setosa")

plt.title("Iris species flower comparision")
plt.xlabel("Sepal width")
plt.ylabel("Sepal lenght")

plt.scatter(versicolor["sepal length"],versicolor["sepal width"],label="Versicolor")
plt.scatter(virginica["sepal length"],virginica["sepal width"],label="Virginica")
plt.scatter(setosa["sepal length"],setosa["sepal width"],label="Setosa")
plt.legend()
plt.show()



plt.title("Iris species flower comparision")
plt.xlabel("Petal width")
plt.ylabel("Petal lenght")

plt.scatter(versicolor["petal length"],versicolor["petal width"],label="Versicolor")
plt.scatter(virginica["petal length"],virginica["petal width"],label="Virginica")
plt.scatter(setosa["petal length"],setosa["petal width"],label="Setosa")
plt.legend()
plt.show()

def mean_dict(flower_list,flower_name):

#0:sepal length 1:sepal width 2:petal length 3:petal width
  avg_list=[0,0,0,0]
  flower_len=len(flower_list[0])

#store all sums in avg_list
  for y in range(0,4):
    for x in range(0,flower_len):
      avg_list[y]+=flower_list[y][x]

#divide all of the values
  for x in range(0,4):
      avg_list[x]/=flower_len
  avg_dict={"petal length":float(avg_list[2]),"petal width":float(avg_list[3]),"species":flower_name}
  return avg_dict

def take_a_guess(flower_name,guess_list,setosa_mean,versicolor_means,virginica_means):#take_a_guess("setosa",setosa,)
    counter=len(guess_list[0])
    #import list intended for guessing as guess list
    #import all of the averages to break into categories 
    #a counter for accuracy for all that are correct 
    print('-'*90,"\nThis guess list is for",flower_name,"\n")
    for x in range(0,50):
      if  guess_list[2][x]<=(setosa_mean["petal length"]+.3) and guess_list[2][x]>=(setosa_mean["petal length"]-.3) or guess_list[3][x]<=(setosa_mean["petal width"]+.1) and guess_list[3][x]>=(setosa_mean["petal width"]-.1):
            
            if flower_name!=setosa_mean["species"] and counter>0:
              counter-=1
              
      elif guess_list[2][x]<=(versicolor_means["petal length"]+1) and guess_list[2][x]>=(versicolor_means["petal length"]-1) and guess_list[3][x]<=(versicolor_means["petal width"]+.6) and guess_list[3][x]>=(versicolor_means["petal width"]-.6):
           
           if flower_name!=versicolor_means["species"] and counter>0:
              counter-=1
              
      elif guess_list[2][x]<=(virginica_means["petal length"]+2.5) and guess_list[2][x]>=(virginica_means["petal length"]-1) and guess_list[3][x]<=(virginica_means["petal width"]+.6) and guess_list[3][x]>=(virginica_means["petal width"]-.5):
          
          if flower_name!=virginica_means["species"] and counter>0:
              counter=-1
              
      else:
        
        if counter > 0:
          counter-=1

    print("This was",(counter/50)*100,"percent accurate\n",'-'*90)
      
    






#first step get data from file
versicolor=make_list("versicolor")
virginica=make_list("virginica")
setosa=make_list("setosa")


#second step get averages from list
setosa_means=mean_dict(setosa,"setosa")
versicolor_means=mean_dict(versicolor,"versicolor")
virginica_means=mean_dict(virginica,"virginica")





#third step read list again

take_a_guess(setosa_means["species"],setosa,setosa_means,versicolor_means,virginica_means)
take_a_guess(versicolor_means["species"],versicolor,setosa_means,versicolor_means,virginica_means)
take_a_guess(virginica_means["species"],virginica,setosa_means,versicolor_means,virginica_means)
