#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016/3/10

@author: weiliang1216
'''
import random
from time import ctime

def twenty_four_calc(filename="24_data.txt"): 
    fi = open(filename)
    fo = open("24_data_output.txt",'w')
    count = 0
    while True:
        line = fi.readline()
        count = count+1
        #if count%100==0:
        #    print str(count) + ".",
        #if count%1000==0:
        #    print ""
        if line:
            line = line.strip()
            strv = line.split(" ")
            iv = []
            # Traslate J,Q,K,A to 11,12,13,1
            for i in range(len(strv)):
                if strv[i]=='J':
                    tmp = 11
                elif strv[i]=='Q':
                    tmp = 12
                elif strv[i]=='K':
                    tmp = 13
                elif strv[i]=='A':
                    tmp = 1
                else:
                    tmp = int(strv[i])
                iv.append(tmp)
            # 
            V=[[iv,[],[],[],[]]]
            out=[]
            #print "===" + line
            fo.write("==="+line+"\n")
            while True:
                if V==[]:
                    break
                V,out = itercalc(V,out)
            if len(out)==0:
                #print "Impossible"
                fo.write("Impossible\n")
            else:
                for i in range(len(out)):
                    #print out[i]
                    fo.write(str(out[i][0])[1:-1])
                    fo.write("\n")
            fo.write("\n")
        else:
            break        
    fi.close()
    fo.close()

'''
B struct: [[compute element],[next element],[expression],[direction for compute],[direction for expression]
out is an array
iterate logic: 
if [compute element]>2 then
subtract first/last element put it in B stack, and tell direction[0,-1] for compute/expression
if [compute element]=2 then
compute element 1 and element 2
if [compute element]=1 then
    if no next element then output
    if have next element then put the next element to compute element
'''
def itercalc(B=[],out=[]):
    if len(B)==0:
        return B,out
    elif len(B)>0:
        T = B[0]
        del B[0]
        #then calc first element end del first element till no element
        if len(T[0])>2:
            Q1 = T[1][:]
            Q2 = T[1][:]
            Q1.insert(0,T[0][-1])
            Q2.insert(0,T[0][0])
            R1 = T[3][:]
            R1.insert(0,-1)
            R2 = T[3][:]
            R2.insert(0,0)
            M = [T[0][:-1],Q1,[],R1,R1]
            N = [T[0][1:],Q2,[],R2,R2]
            B.append(M) 
            B.append(N)
            return B,out
        elif len(T[0])==2:
            if len(T[2])<=0:
                H = [[T[0][0]+T[0][1]],T[1],["(" + str(T[0][0]) + "+" + str(T[0][1]) + ")"],T[3],T[4]]
                B.append(H)
                H = [[T[0][0]-T[0][1]],T[1],["(" + str(T[0][0]) + "-" + str(T[0][1]) + ")"],T[3],T[4]]
                B.append(H)
                H = [[T[0][0]*T[0][1]],T[1],["(" + str(T[0][0]) + "*" + str(T[0][1]) + ")"],T[3],T[4]]
                B.append(H)
                if T[0][1]!=0 and T[0][0]%T[0][1]==0:
                    H = [[T[0][0]/T[0][1]],T[1],["(" + str(T[0][0]) + "/" + str(T[0][1]) + ")"],T[3],T[4]]
                    B.append(H)
                return B,out
            else:
                if T[4][0]==-1:
                    H = [[T[0][0]+T[0][1]],T[1],["(" + str(T[2][0]) + "+" + str(T[0][1]) + ")"],T[3],T[4][1:]]
                    B.append(H)
                    H = [[T[0][0]-T[0][1]],T[1],["(" + str(T[2][0]) + "-" + str(T[0][1]) + ")"],T[3],T[4][1:]]
                    B.append(H)
                    H = [[T[0][0]*T[0][1]],T[1],["(" + str(T[2][0]) + "*" + str(T[0][1]) + ")"],T[3],T[4][1:]]
                    B.append(H)
                    if T[0][1]!=0 and T[0][0]%T[0][1]==0:
                        H = [[T[0][0]/T[0][1]],T[1],["(" + str(T[2][0]) + "/" + str(T[0][1]) + ")"],T[3],T[4][1:]]
                        B.append(H)
                    return B,out
                elif T[4][0]==0:
                    H = [[T[0][0]+T[0][1]],T[1],["(" + str(T[0][0]) + "+" + str(T[2][0]) + ")"],T[3],T[4][1:]]
                    B.append(H)
                    H = [[T[0][0]-T[0][1]],T[1],["(" + str(T[0][0]) + "-" + str(T[2][0]) + ")"],T[3],T[4][1:]]
                    B.append(H)
                    H = [[T[0][0]*T[0][1]],T[1],["(" + str(T[0][0]) + "*" + str(T[2][0]) + ")"],T[3],T[4][1:]]
                    B.append(H)
                    if T[0][1]!=0 and T[0][0]%T[0][1]==0:
                        H = [[T[0][0]/T[0][1]],T[1],["(" + str(T[0][0]) + "/" + str(T[2][0]) + ")"],T[3],T[4][1:]]
                        B.append(H)
                    return B,out
        elif len(T[0])==1:
            if len(T[1])==0:
                if T[0][0]==24:
                    #print T
                    out.append(T[2])
                return B,out
            elif len(T[1])>0:
                if(T[3][0]==-1):
                    T[0].append(T[1][0])
                    P = [T[0],T[1][1:],T[2],T[3][1:],T[4]]
                elif(T[3][0]==0):
                    T[0].insert(0,T[1][0])
                    P = [T[0],T[1][1:],T[2],T[3][1:],T[4]]
                else:
                    print "error"
                B.append(P)
                return B,out
        else:
            print"expection!"
        return B,out
    else:
        print "expection!"
        return B,out

# Design the source data
def design_source(filename="24_data.txt"):
    fo = open(filename,'w')
    dd = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    for i in range(5000):
        fo.write(dd[random.randint(0,12)] + " " + dd[random.randint(0,12)] + " "  + dd[random.randint(0,12)] +  " "  + dd[random.randint(0,12)] + "\n")
    
print "start time %s" %ctime()
#design_source()
twenty_four_calc()
print "\nend time %s" %ctime()