import ask3 as lab3
import random as r
import signalprobs as pr3
import matplotlib.pyplot as plt
import numpy as np

def proccess3(Elem,signal):
    for E in Elem:
        p=[]
        for i in E.inputs:
            p.append(signal[i])
        if(E.type=="AND"):
            signal[E.output]=pr3.spAND(p)   
        if(E.type=="NOT"):
            signal[E.output]=pr3.spNOT(signal[E.inputs[0]])
        if(E.type=="OR"):
            signal[E.output]=pr3.spOR(p)
        if(E.type=="NAND"):
            signal[E.output]=pr3.spNAND(p)
        if(E.type=="NOR"):
            signal[E.output]=pr3.spNOR(p)
        if(E.type=="XOR"):
            signal[E.output]=pr3.spXOR(p)
        if(E.type=="XNOR"):
            signal[E.output]=1-pr3.spXOR(p)

    return signal    

def fourth_first_part():
    p=lab3.part_three(2)
    E=[]+p[0]
    all_gates=[]+p[1]
    
    #arxikopoiseis
    N=1000
    L=[]
    printing_y=0
    ##DIMIOYRGEIA TOY 1OY L 
    Signal_before=[]
    Signal=[]
    for i in range(len(all_gates)):
        Signal_before.append( r.randint(0, 1) )
        Signal.append( r.randint(0, 1) )
    L.append(Signal_before)
    L.append(Signal)

    L[0]=proccess3(E,L[0])  #previous 
    L[1]=proccess3(E,L[1])  #after

    all_scores=[]
    best_score=0
    N=2000

    for n in range(0,N):
        score=0 
        printing_y+=1                
        temp2=[]
        for i in range(len(all_gates)):
            temp2.append( r.randint(0, 1) )

        for w in range( 20,len(L[0]) ):
            if ( L[0][w] != L[1][w] ):
                score+=1 
        L[0]=temp2+[]
        L[0]=[]+proccess3(E,L[0]) 
        
        all_scores.append(score)        
        
        if (score>best_score):
            best_score=0+score  #bazo to klitero Signal score
    tot=0
    for i in all_scores:
        tot+=i
    print("mean: ",tot/N)
    plt.plot(all_scores)
    plt.show()

def mutation_procces(L):
    for i in range(2,len(L)):
        for j in range(len(L[i])):
            for k in range(len(L[i][j])):
                mutation=r.randint(0,100)
                if (mutation<6):
                    L[i][j][k]=1-L[i][j][k]
    return L

def calculate_gates(L,E):
    for i in L:
            i[0]=[]+proccess3(E,i[0])
            i[1]=[]+proccess3(E,i[1])
    return L

def score_finder(L):
    scores=[]
    for i in L:
        score=0
        for j in range(20,len(i[0])): #edo apo 20
            if i[0][j]!=i[1][j]:
                score+=1
        scores.append(score)
    return scores

def create_L(N_of_indi,mege8os):
    L=[]
    for i in range(N_of_indi): #mege8os individuals
        temp1=[]
        temp2=[]
        for j in range(mege8os):
            temp1.append( r.randint(0, 1) )
            temp2.append( r.randint(0, 1) )
        L.append([temp1,temp2])
    return L

def fourth_three_part(N_of_indi,N_of_generations):
    p=lab3.part_three(2)
    E=[]+p[0]
    all_gates=[]+p[1]
    
    #1st L array with all individuals Signals
    L=create_L(N_of_indi,len(all_gates))

    all_all_s=[]
    first_best=-1    #[]
    second_best=-1   #[]
    first_best_invi=-1  #index
    second_best_invi=-1 #index
    maximiz=[]

    score_of_all=[]
    for genZ in range(N_of_generations): #mege8os pli8ismoy

        #seeding
        L=calculate_gates(L,E)
        s=score_finder(L)
        #print("scores: ",s)
        score_of_all.append(s)
        #end of seeding
        
        helping_list=find_max(s) #[high1,index_high1,high2,index_high2]
        #find the bests

        if(helping_list[0] != -1):
            first_best=helping_list[0]
            first_best_invi=helping_list[1]
            parent1=L[helping_list[1]]
        
        if(helping_list[2] != -1):
            second_best=helping_list[2]
            second_best_invi=helping_list[3]
            parent2=L[helping_list[3]]
        else:
            parent2=L[0]

        L=selection_new_pop(parent1,parent2,N_of_indi)
        L=mutation_procces(L)
        #print(score_finder(L))

        maximiz.append((first_best+second_best) /2)
        tot=0
        for i in s:
            tot+=i
        
        all_all_s.append(tot/N_of_indi) #mesos oros - mean
        #print("mean: ",tot/N_of_indi)
    #plt.plot(all_all_s)
    #print(maximiz)
    ############################
    #plt.plot(maximiz)
    #plt.show()
    return(maximiz)

def find_max(scores):
    high1=-1
    index_high1=-1
    high2=-1
    index_high2=-1
    for i in scores:
        if i > high1:
            high1=i
            index_high1=scores.index(i)
    for i in scores:
        if i > high2 :
            if scores.index(i)!=index_high1:
                high2=i
                index_high2=scores.index(i)
    return [high1,index_high1,high2,index_high2]

def selection_new_pop(first_best,second_best,N_L):
    new_L=[]
    new_L.append(first_best)
    new_L.append(second_best)  
    for i in range( (N_L-2)//2 ):
        h=r.randint(0,20)
        new_L.append( [first_best[0][0:h]+second_best[0][h:],second_best[1][0:h]+first_best[1][h:]])
        new_L.append( [second_best[0][0:h]+first_best[0][h:],first_best[1][0:h]+second_best[1][h:]])
    return new_L

fourth_first_part() #return sth with all scores
final=[]

plt.show()
z=fourth_three_part(30,100)
plt.plot(z)
plt.show()
for i in range(3):
    final.append(fourth_three_part(30,100))
for i in final:
    plt.plot(i)
plt.show()
