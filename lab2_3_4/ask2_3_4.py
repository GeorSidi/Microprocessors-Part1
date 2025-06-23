import itertools as t
import signalprobs as pr

################lab3#################
####stis procces 8elo gia olaes tis pilles kai na kano pili XNOR

class myclass:
    def __init__(self,type,inputs,output):
        self.type=type
        self.inputs = inputs
        self.output = output

signaltable=[1 , 1,  0 ,  0  ,0 , 0] #a,b,c,d,e,f
gates =     ["a","b","c","d","e","f"]
b=[0.5,0.5,0.5]
c=[0.4488,0.4488,0.4488]
#validgates=["NOT", "AND", "OR", "XOR", "NAND", "NOR", "XNOR"]

########code for part 1#############
def proccess(E):
    if(E.type=="AND"):
        signaltable[E.output - 1]=pr.spAND([signaltable[E.inputs[0]-1] , signaltable[E.inputs[1]-1]])
    elif(E.type=="NOT"):
        signaltable[E.output - 1]=pr.spNOT(signaltable[E.inputs[0]-1])
    elif(E.type=="XOR"):
        signaltable[E.output - 1]=pr.spXOR([signaltable[E.inputs[0]-1] , signaltable[E.inputs[1]-1]]) 

def firstpart(Elementstable):
    a=list(t.product([0, 1], repeat=3))
    print("previous lab truth table: ")
    pr.check2()
    print("current lab truth table: ")
    for j in a:
        signaltable[0:3]=j
        for i in Elementstable:
            proccess(i)
        print(f"for inputs abc: {signaltable[0:3]} is def: {signaltable[3:len(signaltable)]}")

    signaltable[0:3]=b
    print(f"for previous with inputs {b} : {pr.circuit(b)}")
    for i in signaltable[0:3]:
        for i in Elementstable:
            proccess(i)
    print(f"for current with inputs abc: {signaltable[0:3]} is def: {signaltable[3:len(signaltable)]}")

    signaltable[0:3]=c
    print(f"for previous with inputs {c} : {pr.circuit(c)}")
    for i in signaltable[0:3]:
        for i in Elementstable:
            proccess(i)
    print(f"for current with inputs abc: {signaltable[0:3]} is def: {signaltable[3:len(signaltable)]}")

#######code for part2##########
signaltable2=[]
def part_two():
    top_inputs=[]  ################
    Elementstable=[]
    gatesoffile=[]
    inputs=[]
    outputs=[]

    file = open("C:\\Users\\geo3\\Desktop\\micro_epeksergastes\\lab.txt", "r")
    firstline=True
    for line in file:
        splited_line=line.split()
        if firstline and splited_line[0]=="top_inputs" :
            top_inputs=splited_line[1:]
            inputs=top_inputs
            print("we have top level inputs")
        else:
            gatesoffile.append(splited_line)
            
            for i in splited_line[2:]:
                if i not in inputs+outputs:
                    inputs.append(i)
            
            if splited_line[1] not in inputs+outputs:
                outputs.append(splited_line[1])      
        firstline=False
##########create element table#################
    Elementstable=part_two_create_elementtable(inputs+outputs,gatesoffile)
##############the process############################
    N=len(inputs) ## the N of inputs signals
    secondpart(Elementstable,inputs+outputs,N)

def part_two_create_elementtable(inoutputs,gatesoffile):
    Elementstable=[]
    for i in gatesoffile:
        indexs_of_inputs=[]
        for j in i[2:]:
            indexs_of_inputs.append(inoutputs.index(j))
        print(i[0],indexs_of_inputs,inoutputs.index(i[1]))
        Elementstable.append(myclass(i[0],indexs_of_inputs,inoutputs.index(i[1])))
    return Elementstable

def secondpart(Elementstable2,gates2,N):
    global signaltable2
    if N<6:
        print("Sorted: ")
        for i in Elementstable2:
            print(i.type,i.output,i.inputs)
        a=list(t.product([0, 1], repeat=N))
        for i in gates2:
            signaltable2.append(1)
        for j in a:
            signaltable2[0:N]=j
            for i in Elementstable2:
                proccess2(i)
            print(f"for inputs {gates2[0:N]}: {signaltable2[0:N]} is {gates2[N:]}: {signaltable2[N:len(signaltable2)]}")   
        if N==3:
            signaltable2[0:N]=[0.5,0.5,0.5]
            for i in Elementstable2:
                proccess2(i)
            print(f"for inputs {gates2[0:N]}: {signaltable2[0:N]} is {gates2[N:]}: {signaltable2[N:len(signaltable2)]}")
            signaltable2[0:N]=[0.4488,0.4488,0.4488]
            for i in Elementstable2:
                    proccess2(i)
            print(f"for inputs {gates2[0:N]}: {signaltable2[0:N]} is {gates2[N:]}: {signaltable2[N:len(signaltable2)]}")
    else:
        print("sad")

def proccess2(E):
    global signaltable2
    p=[]
    for i in E.inputs:
        p.append(signaltable2[i])
    if(E.type=="AND"):
        signaltable2[E.output]=pr.spAND(p)   
    if(E.type=="NOT"):
        signaltable2[E.output]=pr.spNOT(signaltable2[E.inputs[0]])
    if(E.type=="OR"):
        signaltable2[E.output]=pr.spOR(p)
    if(E.type=="NAND"):
        signaltable2[E.output]=pr.spNAND(p)
    if(E.type=="NOR"):
        signaltable2[E.output]=pr.spNOR(p)
    if(E.type=="XOR"):
        signaltable2[E.output]=pr.spXOR(p)
    if(E.type=="XNOR"):
        signaltable2[E.output]=1-pr.spXOR(p)

def isitin(E,inp,gat):
    for i in E.inputs:
        if gat[i] not in inp:
            return False 
    return True

def h(E,p_l_r): ##true ena ola ta inputs mias pilis eiani apo to proigoymeno lvl
    for i in E.inputs:
        if i not in p_l_r:
            return False    
    return True

def part_three(mode):
    top_inputs=[]  ################
    Elementstable=[]
    inputs=[]

    file = open("C:\\Users\\geo3\\Desktop\\micro_epeksergastes\\labb.txt", "r")
    firstline=True
    
    not_sorted_file=[]
    not_forsure_outputs=[]
    
    for line in file:
        splited_line=line.split()
        if firstline and splited_line[0]=="top_inputs" :
            top_inputs=splited_line[1:]
            inputs=top_inputs
            print("we have top level inputs")
        else:
            not_sorted_file.append(splited_line) 
            not_forsure_outputs.append(splited_line[1])

    if len(inputs)==0:
        for line in not_sorted_file:
            for i in line[1:]:
                if i not in not_forsure_outputs and i not in inputs:
                    inputs.append(i)
    allgates=inputs+not_forsure_outputs #ta s
    Elementstable=part_two_create_elementtable(inputs+not_forsure_outputs,not_sorted_file)
    
    ###sorting process of E ####
    Sorted_Elementstable=[]
    Not_Yet_Sorted_Elementstable=[]+Elementstable
    #1st already done at previous code
    
    #2st step

    #print(inputs)
    next_level_inputs_index=[]
    for i in Elementstable:
        if(isitin(i,inputs,allgates)):
            Sorted_Elementstable.append(i)
            next_level_inputs_index.append(i.output)

    ###### mexri edo ok ##########
    #3rd edo mporo na to balop epano   
    for i in inputs:
        next_level_inputs_index.append(allgates.index(i))
    
    while(len(Sorted_Elementstable)<(len(Elementstable))):
            
        #4th
        for i in Elementstable:
            if(h(i,next_level_inputs_index) and i not in Sorted_Elementstable):
                Sorted_Elementstable.append(i)
                next_level_inputs_index.append(i.output)

    #print("sorted: ")
    #for i in Sorted_Elementstable:
        #print(i.type,allgates[i.output],i.inputs,)
##############the process again as the 2 ############################
    N=len(inputs) ## the N of inputs signals
    if(mode==1):
        print("we are doing the 3.3")
        secondpart(Sorted_Elementstable,allgates,N)
    print("allgates: ",allgates)
    #for i in Sorted_Elementstable:
        #print(i.type,allgates[i.output],i.inputs)
    return [Sorted_Elementstable,allgates]


def testbench():
    E1=myclass("AND",[1,2],5)
    E2=myclass("NOT",[3],6)
    E3=myclass("AND",[5,6],4)
    Elementstable=[E1,E2,E3]
    ###3.1
    #firstpart(Elementstable)
    ###3.2
    #part_two() ## edo akomi to sort den iparxei 
    #3.3
    part_three(1)  ## an exo 1 eiani gia to 3.1 eno
                    ##  gia otidipote allo eiani gia alli doyeleia 
                    ## sto 3.1 kanei print stalla pla giranei Elementable      
    ## to test bench 8a trexei an kaleso to programma ask4 episis 
    ## prepei na allax8ei to arxeio apo lab se lab4 kai antoistoixa 
    ## analogame tin askisi p kanoyme  


testbench()