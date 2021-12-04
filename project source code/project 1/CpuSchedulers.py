#Functions and their definitions************************************************

#This function adds burst time for the currently running que
def add_burst_time(curQue):
  burst_time_dic[curQue[len(curQue)-1]]+=1

#This function adds wait time for all the processes waiting in the ready que
#while a process is running
def add_wait_time(readyList):
  for y in readyList:
    wait_time_dic[y[len(y)-1]]+=1

#This function tells a process at what time it should return from io burst to
#ready que
def manage_waiting_times(waitList,readyList,io_time_dic,x):
  identifier=''
  counter=len(waitList)
  for index,u in enumerate(waitList):
    identifier=u[len(u)-2]
    u[0]-=1
    if  u[len(u)-1]==x:
      ioDone=waitList.pop(index)
      ioDone.pop(0)
      ioDone.pop(len(ioDone)-1)
      
      if choice!='3':
          ready_que.append(ioDone)
      else:
          queue1.append(ioDone)

    counter-=1
  identifier=''
  
  #in the case that one or more processes have the same return time that they don't get skipped
  while counter>0:
    for index,u in enumerate(waitList):
      identifier=u[len(u)-2]
      if  u[len(u)-1]==x:
        ioDone=waitList.pop(index)
        ioDone.pop(0)
        ioDone.pop(len(ioDone)-1)
        if choice!='3':
          ready_que.append(ioDone)
        else:
          queue1.append(ioDone)
      counter-=1
  
  return
#prints out context switch
def contextprint(globalClock,readyList,waitList,running,choice):
  print('-'*50)
  print('\nTotal time',globalClock)
  
  if len(running)>0:
    print('running process\tburst time',)
    print(running[len(running)-1],'\t\t',running[0])
  else:
    print('Nothing is running')
  
  if choice=='3':
    if len(queue1)>0:
      print('\nqueue 1\tburst time')
      for process in queue1:
        print(process[len(process)-1],'\t\t',process[0])
    else:
      print('\nqueue 1 is empty')
    
    if len(queue2)>0:
      print('\nqueue 2\tburst time')
      for process in queue2:
        print(process[len(process)-1],'\t\t',process[0])
    else:
      print('\nqueue 2 is empty')
  

  if len(readyList)>0:
     print('\nReady queue\tburst time')
     for process in readyList:
       print(process[len(process)-1],'\t\t',process[0])
  else:
      print('\nReady queue is empty')

  if len(waitList)>0:
    print('\nWaiting queue\tio burst time')
    for process in waitList:
      print(process[len(process)-2],'\t\t',process[0])
  else:
    print('\nWaiting queue is empty')
  print('-'*50,'\n')
  
  return




#*************************************MAIN PROGRAM******************************

burst_time_dic={'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
io_time_dic={'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
wait_time_dic={'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
started_dict={'P1':0,'P2':0,'P3':0,'P4':0,'P5':0,'P6':0,'P7':0,'P8':0}
#Variable initlization 
P1=[5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 5,'P1']
P2=[4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8,'P2']
P3=[8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6,'P3']
P4=[3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3,'P4']
P5=[16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4,'P5']
P6=[11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8,'P6']
P7=[14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10,'P7']
P8=[4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6,'P8']
started=[]
waiting_que=[]
ready_que=[P1,P2,P3,P4,P5,P6,P7,P8]
x=0
cpu_burst=0
que=''
counter=0

choice=input("Enter your choice by number\n1. fcfs\n2. sjf\n3. mlfq\n")

#---------------------------------------------------------------------------------------SJF AND FCFS ONLY----------------------------------------------------------------------

while len(waiting_que)>=1  or  len(ready_que)>=1 or len(que)>=1 and choice!=3:
  
  #This function gets called when all other ques are empty except waiting que
  if len(waiting_que)>=1 and len(ready_que)==0 and len(que)<1:
    manage_waiting_times(waiting_que,ready_que,io_time_dic,x)
    x+=1
#*****************************************************************************  
  #Adds item from the ready que if a cpu burst is not occuring and the
  #Ready que has a process waiting
  if len(ready_que)>=1 and cpu_burst==0:
     
    #fcfs
    #will chose the process at the top of the queue
    if choice=='1':
      que=ready_que.pop(0)   
    
    #sjf
    # will choose the process with the shortest time to be pushed from the ready queue
    elif choice=='2':
      min=1000
      for z in range(0,len(ready_que)):
        if ready_que[z][0]<min:
          min=ready_que[z][0]
          index=z
      que=ready_que.pop(index)
       
    else:
      break
    
    
    
    #This adds the response time if the process has never been started before 
    if que[len(que)-1] not in started:
      print(que[len(que)-1],'started at',x)
      started.append(que[len(que)-1])
      started_dict[que[len(que)-1]]+=x
      
      
    #sets the time for the when process will finish and prints the context switch 
    cpu_time=que[0]
    cpu_time+=x
    cpu_burst=1
    contextprint(x,ready_que,waiting_que,que,choice)
    

    
  #Cpu burst occuring***********************************************************
  elif cpu_burst==1:    
    
    #If there are processes waiting to come back in the io this updates them
    if len(waiting_que)>=1:
      manage_waiting_times(waiting_que,ready_que,io_time_dic,x)
    #These add burst time to the running process and wait time to the other processes
    #Also the global clock ,x, gets updates and one is taken off the process time
    add_burst_time(que)
    add_wait_time(ready_que)
    que[0]-=1
    x+=1
    
    #When cpu time is finally equal to the global clock if the process is not finished
    #then it goes to the waiting list otherwise the process is finished 
    
    if x==cpu_time :
      #updates process list
      que.pop(0)
      
      #finished
      if len(que)==1:
        print('*'*50,'\n',que[0],'has finished','\n','*'*50)
        que.clear()
        cpu_burst=0
      
      #not finished
      else:
        cpu_burst=0
        io_time_dic[que[len(que)-1]]+=que[0]
        que.append(que[0]+x)
        waiting_que.append(que)
        que=''


#-----------------------------------------------------------------------------MULTI LEVEL FEEDBACK QUEUE----------------------------------------------------------------------------------
#because multi level feedback queue requires more queues additional initalizations are needed
if choice=='3':
  ready_que=[]
  started=[]
  waiting_que=[]
  fin=[]
  queue1=[P1,P2,P3,P4,P5,P6,P7,P8]
  queue2=[]
  fcfs=q1=q2=0
  que=''
  q=5

  while len(waiting_que)>=1 or len(queue1)>=1 or len(queue2)>=1 or len(que)>=1 or len(ready_que)>=1:
    
    #calls if everything is in the waiting que and nothing is in the other queues
    if len(waiting_que)>=1 and len(queue1)==0 and len(queue2)==0 and len(ready_que)==0 and que=='':
      manage_waiting_times(waiting_que,ready_que,io_time_dic,x)
      x+=1

    #checks if the highest priority que has a process waiting to be added 
    if cpu_burst!=1 and len(queue1)>0:
      
      #gets first process from queue 1
      que=queue1.pop(0)   
      contextprint(x,ready_que,waiting_que,que,choice)
      
      #adds starting time to unstarted processes
      if que[len(que)-1] not in started:
        started.append(que[len(que)-1])
        started_dict[que[len(que)-1]]+=x
        
        
      #sets cpu burst time and various flags
      cpu_time=que[0]
      cpu_time+=x
      cpu_burst=1
      q1=1
      q2=0
      fcfs=0

    #checks if the second highest priority que has a process waiting to be addded 
    elif cpu_burst!=1 and len(queue2)>0 and len(queue1)==0:
        
        que=queue2.pop(0)   
        contextprint(x,ready_que,waiting_que,que,choice)
        
        #sets cpu time and various flags
        cpu_time=que[0]
        cpu_time+=x
        cpu_burst=1
        q2=1
        q1=0
        fcfs=0
    
    #checks if the lowest priority que has a process waiting to be addded 
    elif cpu_burst!=1 and len(queue2)==0 and len(queue1)==0 and len(ready_que)>0:
        
        que=ready_que.pop(0)   
        contextprint(x,ready_que,waiting_que,que,choice)

        #sets cpu time and various flags
        cpu_time=que[0]
        cpu_time+=x
        cpu_burst=1        
        q1=0
        q2=0

#Cpu burst occuring***********************************************************
    elif cpu_burst==1:    
      
    
      #Time quatum is set based off the flags set during context switch
      if q1==1:
        q=5
      elif q2==1:
        q=10
      else:
        fcfs=1
      #------------

      #manages io waiting times 
      if len(waiting_que)>=1:
        manage_waiting_times(waiting_que,ready_que,io_time_dic,x)
      x+=1
      counter+=1
      add_burst_time(que)
      
      #adds waiting times to each queue
      if len(queue1)>0:
        add_wait_time(queue1)
      
      if len(queue2)>0:
        add_wait_time(queue2)
        
      if len(ready_que)>0:
        add_wait_time(ready_que)
      
      que[0]-=1
      
    #*****************************************************************************

      if fcfs!=1 and x!=cpu_time and counter==q: 
        #in this case the cpu time is larger than q which can be 5 or 10
        #sets cpu burst to zero 
        counter=0             
        cpu_burst=0
        
        
        
        
        #append to second lowest priority queue if q==5
        if q==5:
          queue2.append(que)
        #append to lowest priority queue if q==10
        elif q==10:
          ready_que.append(que)
      
        que=''
        cpu_burst=0 
        q1=q2=0
    #*****************************************************************************

      elif fcfs!=1 and x==cpu_time and counter<=q: 
      #The time is met within the 5 or 10 and the process is added to the waiting que or finishes
            
        counter=0 
        que.pop(0) 
        
        if len(que)==1:
          print('*'*50,'\n',que[0],'has finished','\n','*'*50)
          que.clear()
          cpu_burst=0
        
        elif len(que)>0:
          cpu_burst=0
          io_time_dic[que[len(que)-1]]+=que[0]
          que.append(que[0]+x)
          waiting_que.append(que)
        que=''

    #*****************************************************************************
      #first come first serve the process will finish regardless of remaning length
      #process will either finish or go to waiting queue
      elif fcfs==1:
        counter=0
        
        if x==cpu_time:
          que.pop(0)
        
          if len(que)==1:
            print('*'*50,'\n',que[0],'has finished','\n','*'*50)
            que.clear()
            cpu_burst=0
          
          elif len(que)>0:
            cpu_burst=0
            io_time_dic[que[len(que)-1]]+=que[0]
            que.append(que[0]+x)
            waiting_que.append(que)
            
          que=''


#Summary statistics*************************************************************
#This will print out and caculate the required statistics as mentioned in the 
#assignment document
try:
  print("\n\n\nThe total time for all eight processes to finsh was:\t",x,'\n')

  avg=0
  plist=['P1','P2','P3','P4','P5','P6','P7','P8']

  for z in burst_time_dic.values():
    avg+=z
  print('\nThe cpu utalization was %',avg/x*100)
  print('\nTurn around time\tWaiting time\tResponse Time')
  rep_avg=0
  wait_avg=0
  tr_avg=0
  for y in plist:
    avg=0
    p_tr=io_time_dic[y]+burst_time_dic[y]+wait_time_dic[y]
    avg+=p_tr
    tr_avg+=avg
    rep_avg+=started_dict[y]
    wait_avg+=wait_time_dic[y]
    print('\n',y,'\n',p_tr,'\t\t\t',wait_time_dic[y],'\t\t',started_dict[y],'\t\t\t',)
  print('\n\nThe average wait time\t',wait_avg/8,'\nThe average turnaround time\t',tr_avg/8,'\nThe average response time\t',rep_avg/8)
except ZeroDivisionError:
  print('Invalid entry program exiting')