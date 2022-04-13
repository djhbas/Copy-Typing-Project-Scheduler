import os

def add (pid, prio, title, size):
    ''' To add projects in a .txt file '''
    file = open("projects.txt","a")
    file.write(str(pid)+" "+title+" "+str(size)+" "+str(prio)+"\n")
    file.close()
        

def input_projects():
    ''' To input project details '''
    while (True):
        pid = int(input("\n Enter project ID: "))
        if pid == 0: 
            return
        title = input ("\n Enter project title: ")
        size = int (input (" Enter no of pages: "))
        prio = int (input (" Enter priority: "))
        add (pid, prio, title, size)
        
        ex = int(input("\n 1 = YES 0 = NO\n Exit? [1/0] >> "))
        if ex == 1: 
            return

def view_projects(ch2):
    ''' To view projects from a .txt file '''
    if ch2 == 1:
        proj = []
        print("\n ---Project---")
        srch = int(input("\n Project ID: "))
        file = open("projects.txt", "r")
        found = 0
        for line in file:
            proj = (line.split())
            if int(proj[0])==srch:
                print(" Title:",proj[1])
                print(" Size:",proj[2])
                print(" Priority:",proj[3])
                found = 1
        if(found==0):
            print(" Project ID doesn't exists! Please try again.")
    elif ch2 == 2:
        print("\n ---Completed Projects---")
        if os.path.isfile("completed.txt"):
            file1 = open("completed.txt", "r")
            compl = []
            for line1 in file1:
                compl = (line1.split())
                print("\n Project ID:",compl[0])
                print(" Title:",compl[1])
                print(" Size:",compl[2])
                print(" Priority:",compl[3])
            file1.close()  
        else:
            print("\n As of now, you don't have any completed projects")
    elif ch2 == 3:
        lst = []
        print("\n ---All Projects---")
        file2 = open("projects.txt", "r")
        for line2 in file2:
            lst = (line2.split())
            print("\n Project ID:",lst[0])
            print(" Title:",lst[1])
            print(" Size:",lst[2])
            print(" Priority:",lst[3])
        file2.close()   
    elif ch2 == 4:
        return

def CreateSched():
    ''' To crea6e a schedule for projects '''
    line = []
    ID = []
    title = []
    sz = []
    prio = []
    
    file = open("projects.txt", "r")
    for lines in file:
        line = (lines.split())
            
        ID.append(line[0])
        title.append(line[1])
        sz.append(line[2])
        prio.append(line[3])
        
    file.close()
    
    if(os.path.isfile("queue.txt")):
        file = open("queue.txt", "r")
        for lines in file:
            line = (lines.split())
            
            ID.append(line[0])
            title.append(line[1])
            sz.append(line[2])
            prio.append(line[3])
        
        file.close()

    open('projects.txt', 'w').close()
    
    
    for i in range(len(ID)):   
        
        max_prio = i
        for j in range(i+1, len(ID)):
            if int(prio[max_prio]) > int(prio[j]):
                max_prio = j
            if int(prio[max_prio]) == int(prio[j]):
                if int(sz[max_prio]) < int(sz[j]):
                    max_prio = j
                
        ID[i], ID[max_prio] = ID[max_prio], ID[i]
        title[i], title[max_prio] = title[max_prio], title[i]
        sz[i], sz[max_prio] = sz[max_prio], sz[i]
        prio[i], prio[max_prio] = prio[max_prio], prio[i]
        
    file = open("queue.txt","w")
    for i in range(len(ID)):
        file.write(ID[i] + " " + title[i] + " " + sz[i] + " " + prio[i] + "\n")

    file.close()

    print("\n ---Create Schedule---\n")
    print(" Queue:\n")

    for i in range(len(ID)):
        print(" ", i + 1, ". ", ID[i], "\n", sep = '')
    

def ViewSched():
    ''' To view scheduled projects from a .txt file '''
    print("\n ---View Updated Schedule---\n")
    if(os.path.isfile("queue.txt")):
        file = open("queue.txt", "r")
        for lines in file:
            line = (lines.split())
            
            print("\n Project ID:",line[0])
            print(" Title:",line[1])
            print(" Size:",line[2])
            print(" Priority:",line[3])
        
        file.close()

    else:
        print(" No Schedule found!")
        ex = int(input(" 1 = YES 0 = NO\n Create a Schedule? [1/0] >> "))
        if ex == 1: 
            CreateSched()

def GetProj():
    ''' To get a project from a scheduled projects '''
    print("\n ---Get Project---")
    if(os.path.isfile("queue.txt")):
        pass
    else:
        print("\n No Schedule Created!")
        return

    with open('queue.txt', 'r') as fr:
        lines = fr.readlines()
         
        ptr = 1
     
        with open('queue.txt', 'w') as fw:
            for line in lines:
               
                if ptr != 1:
                    fw.write(line)
                else:
                    file = open("completed.txt","a")
                    file.write(line)
                    file.close()
                ptr += 1
        print("\n Project Successfully Dequeued!\n")
        print(" Queue:")
        
        file = open("queue.txt", "r")
        for lines in file:
            line = (lines.split())
            
            print("\n Project ID:",line[0])
            print(" Title:",line[1])
            print(" Size:",line[2])
            print(" Priority:",line[3])
        
        file.close()

def menu3():
    ''' Menu for Schedule Projects '''
    m3 = 0
    while (m3!= 3):
        print("\n ==============================")
        print("\tSchedule Projects")
        print(" ==============================")
        print(" [1] Create Schedule")
        print(" [2] View Updated Schedule")
        print(" [3] Back")
        m3 = int(input("\n Enter: "))
        if (m3 == 1):
            CreateSched()
        elif (m3 == 2):
            ViewSched()

#Main menu
while True:
    print("\n =================================")
    print("   COPY-TYPING PROJECT SCHEDULER")
    print(" =================================")
    ch = int (input ("\n [1] Input project details\n [2] View projects\n [3] Schedule projects\n [4] Get project\n [5] Exit\n\n Enter: "))
    if (ch == 1):
        input_projects()
    elif (ch == 2):
        print("\n ==============================")
        print("        View Projects")
        print(" ==============================")
        ch2 = int (input ("\n [1] One project\n [2] Completed projects\n [3] All projects\n [4] Go back\n\n Enter: "))
        view_projects(ch2)
    elif (ch == 3):
        menu3()
    elif (ch == 4):
        GetProj()
    elif (ch == 5):
        break