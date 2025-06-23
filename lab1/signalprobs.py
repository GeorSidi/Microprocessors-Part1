from timeit import repeat
import itertools as it
import random, math

def signalprobs(*args):
    inputs = list(args)
    if(len(inputs)==2):
        print(f"AND gate result for {inputs[0]} , {inputs[1]} is {sp2AND(inputs[0],inputs[1])} and Switching Activity is {swact(sp2AND(inputs[0],inputs[1]))}") 
        print(f"OR gate result for {inputs[0]} , {inputs[1]} is {sp2OR(inputs[0],inputs[1])} and Switching Activity is {swact(sp2OR(inputs[0],inputs[1]))}")
        print(f"XOR gate result for {inputs[0]} , {inputs[1]} is {sp2XOR(inputs[0],inputs[1])} and Switching Activity is {swact(sp2XOR(inputs[0],inputs[1]))}")
        print(f"NAND gate result for {inputs[0]} , {inputs[1]} is {sp2NAND(inputs[0],inputs[1])} and Switching Activity is {swact(sp2NAND(inputs[0],inputs[1]))}")
        print(f"NOR gate result for {inputs[0]} , {inputs[1]} is {sp2NOR(inputs[0],inputs[1])} and Switching Activity is {swact(sp2NOR(inputs[0],inputs[1]))}")
    elif(len(inputs)==3):
        print(f"AND gate result for {inputs[0]} , {inputs[1]} , {inputs[2]} is {sp3AND(inputs[0],inputs[1],inputs[2])} and Switching Activity is {swact(sp3AND(inputs[0],inputs[1],inputs[2]))}") 
        print(f"OR gate result for {inputs[0]} , {inputs[1]} , {inputs[2]} is {sp3OR(inputs[0],inputs[1],inputs[2])} and Switching Activity is {swact(sp3OR(inputs[0],inputs[1],inputs[2]))}")
        print(f"XOR gate result for {inputs[0]} , {inputs[1]} , {inputs[2]} is {sp3XOR(inputs[0],inputs[1],inputs[2])} and Switching Activity is {swact(sp3XOR(inputs[0],inputs[1],inputs[2]))}")
        print(f"NAND gate result for {inputs[0]} , {inputs[1]} , {inputs[2]} is {sp3NAND(inputs[0],inputs[1],inputs[2])} and Switching Activity is {swact(sp3NAND(inputs[0],inputs[1],inputs[2]))}")
        print(f"NOR gate result for {inputs[0]} , {inputs[1]} , {inputs[2]} is {sp3NOR(inputs[0],inputs[1],inputs[2])} and Switching Activity is {swact(sp3NOR(inputs[0],inputs[1],inputs[2]))}")
    else:
        print(f"AND gate result for {inputs} is {spAND(inputs)} and Switching Activity is {swact(spAND(inputs))}")
        print(f"OR gate result for {inputs} is {spOR(inputs)} and Switching Activity is {swact(spOR(inputs))}") 
        print(f"XOR gate result for {inputs} is {spXOR(inputs)} and Switching Activity is {swact(spXOR(inputs))}") 
        print(f"NAND gate result for {inputs} is {spNAND(inputs)} and Switching Activity is {swact(spNAND(inputs))}") 
        print(f"NOR gate result for {inputs} is {spNOR(inputs)} and Switching Activity is {swact(spNOR(inputs))}") 
    return 0
######### for 2 inputs #############
def sp2AND(input1sp,input2sp):
    return input1sp*input2sp
def sp2OR(input1sp,input2sp):
    return 1-(1-input1sp)*(1-input2sp)
def sp2XOR(input1sp,input2sp):
    return ((1-input1sp)*input2sp)+(input1sp*(1-input2sp))
def sp2NAND(input1sp,input2sp):
    return 1-sp2AND(input1sp,input2sp)
def sp2NOR(input1sp,input2sp):
    return 1-sp2OR(input1sp,input2sp)
######### for 3 inputs ##############
def sp3AND(input1sp,input2sp,input3sp):
    return input1sp*input2sp*input3sp
def sp3OR(input1sp,input2sp,input3sp):
    return 1-(1-input1sp)*(1-input2sp)*(1-input3sp)
def sp3XOR(input1sp,input2sp,input3sp):
    return (1-input1sp)*(1-input2sp)*input3sp+(1-input1sp)*input2sp*(1-input3sp)+input1sp*(1-input2sp)*(1-input3sp)+input1sp*input2sp*input3sp
def sp3NAND(input1sp,input2sp,input3sp):
    return 1-sp3AND(input1sp,input2sp,input3sp)
def sp3NOR(input1sp,input2sp,input3sp):
    return 1-sp3OR(input1sp,input2sp,input3sp)
######### for N inputs ##############
def spAND(inputs):
    k=1
    for i in inputs:
        k=i*k
    return k
def spOR(inputs):
    k=1
    for i in inputs:
        k=k*(1-i)
    return 1-k
def spXOR(inputs):
    if(len(inputs) == 2):
        return sp2XOR(inputs[0],inputs[1])
    else:
        inputs[-2]=sp2XOR(inputs[-1],inputs[-2])
        return spXOR(inputs[0:-1])
def spNAND(inputs):
    return 1-spAND(inputs)
def spNOR(inputs):
    return 1-spOR(inputs)
########### Switching Activity #############
def swact(i):
    return 2*i*(1-i)
################END###########################
def testerlab1():
    print("XOR from spXOR with inputs [0.2,0.2,0.2]: ",spXOR([0.3,0.3,0.3]))
    print("XOR from sp3XOR with inputs [0.2,0.2,0.2]: ",sp3XOR(0.3,0.3,0.3))
    print("for 2 inputs")
    signalprobs(0.5,0.5)
    print("for 3 inputs")
    signalprobs(0.5,0.5,0.5)
    print("for 4 inputs")
    signalprobs(0.5,0.5,0.5,0.5)
    print(f"Switching activity of gates output for efd=[0.7 , 0.2 ,0.45] with given probabilities are :{swact(0.7)},{swact(0.2)},{swact(0.45)}")


#####################LAB2######################
def spNOT(input):
    return 1-input

def circuit(abc):
    e=sp2AND(abc[0],abc[1])
    f=spNOT(abc[2])
    d=sp2AND(e,f)
    return ([e,f,d])

def check1(abc):
    print(f"abc: {abc} efd: {circuit(abc)} ")

def check2():
    b = list(it.product([0, 1], repeat=3))
    for i in b:
        print(f"for inputs abc: {list(i)} is efd: {circuit(i)}")

def swact2(abc):
    efd=circuit(abc)
    g=abc+efd
    sw=[]
    for i in g:
        #print(f"for {i} gate the sw is: {swact(i)}")
        sw.append(swact(i))
    return sw

def monteCarlo(times):
    for i in times:
        switch=[0,0,0]
        past=[0,0,0]
        print(f"montecarlo for N: {i}")
        for j in range(0,i+1):###
            a=random.randint(0,1)
            b=random.randint(0,1)
            c=random.randint(0,1)
            out=circuit([a,b,c])
            if(j>0):####
                if(past[2]!=out[2]):
                    switch[2]+=1
                if(past[1]!=out[1]):
                    switch[1]+=1
                if(past[0]!=out[0]):
                    switch[0]+=1
            past[2]=out[2]
            past[1]=out[1]
            past[0]=out[0]
        print(f"swe: {switch[0]/i} swf: {switch[1]/i} swd: {switch[2]/i} ")

#inputs_abc=[0.5 , 0.5 , 0.5]
#testerlab1()                                           #lab1 printing all
#print("epalithesi kiklomatos: ")
#check1(inputs_abc)                                     #erotima 2.1.1 ilopoiisi kiklomatos 
#check2()                                               #erotima 2.1.2 pinakas ali8eia            
#h=swact2(inputs_abc)                                   #erotima 2.2   switching activities
#print(f"for input a: {h[0]} b: {h[1]} c: {h[2]} the switcing activities is: e: {h[3]} f: {h[4]} d: {h[5]}")
#monteCarlo([10,100,4488,10000])                        #erotima 2.3
