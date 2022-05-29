import copy
import numpy as np
def solution(minterm):
    vks = 0;

    answer = []
    combi = []
    minterm2 = []

    for i in range(2, len(minterm)):
        minterm2.append(my_b(minterm[i], minterm[0]))
    cnt = 0

    check_v2 = [minterm[i] for i in range(2, len(minterm))]

    while (vks == 0):
        # print(cnt,len(minterm2),minterm[0])
        cnt += 1
        vks = 1
        check = [0 for i in range(len(minterm2))]
        minterm3 = []

        check_v = [0 for i in range(len(check_v2))]
        check_v3 = []

        for i in range(len(minterm2) - 1):
            for j in range(i + 1, len(minterm2)):
                ch2 = 0
                ch3 = 0
                for k in range(minterm[0]):
                    if (minterm2[i][k] == minterm2[j][k]):
                        ch2 = ch2 + 1
                    else:
                        ch3 = k
                if (ch2 == minterm[0] - 1):
                    vks = 0
                    check[i] = 1
                    check[j] = 1

                    check_v[i] = 1
                    check_v[j] = 1

                    n = []
                    if (cnt == 1):
                        n.append(check_v2[i])
                        n.append(check_v2[j])
                    else:
                        n2 = check_v2[i]
                        n2.extend(check_v2[j])
                        for k in n2: n.append(k)
                    m = minterm2[j][:]
                    m[ch3] = '-'

                    if (m not in minterm3):
                        minterm3.append(m)
                        check_v3.append(n)
                        # print(i,j,minterm2[i],minterm2[j],minterm3[len(minterm3)-1],check_v3)

        for i in range(len(check)):
            if (check[i] == 0):
                s = ""
                for j in minterm2[i]:
                    if (j == '-'):
                        s += '2'
                    else:
                        s += j
                answer.append(s)
                # print(answer[len(answer)-1])

        for i in range(len(check_v)):
            if (check_v[i] == 0):
                combi.append(check_v2[i])
                # print(combi)

        minterm2 = copy.deepcopy(minterm3)
        check_v2 = copy.deepcopy(check_v3)

    answer2 = []
    answer3 = []
    for i in range(2, len(minterm)):
        cc = 0
        cc2 = 0
        for j in range(len(combi)):
            if (str(type(combi[j])) == "<class 'list'>" and (minterm[i] in combi[j])):
                cc = cc + 1
                cc2 = j
            elif (str(type(combi[j])) == "<class 'int'>" and minterm[i] == combi[j]):
                cc = cc + 1
                cc2 = j
        if (cc == 1 and (combi[cc2] not in answer2)):
            answer2.append(combi[cc2])
            answer3.append(answer[cc2])

    # print(answer)
    answer.sort()
    answer3.sort()
    for i in range(len(answer)):
        answer[i] = answer[i].replace('2', '-')
    for i in range(len(answer3)):
        answer3[i] = answer3[i].replace('2', '-')

    # print("PI list : ", combi)
    #print(answer2, answer3)
    answer.append("EPI")
    answer.extend(answer3)
    print(answer)
    print()

    return combi


def my_b(n, m):
    li = []
    for i in range(m):
        q = int(n / 2)
        r = int(n % 2)
        if n != 0:
            if (r == 0):
                li.insert(0, '0')
            else:
                li.insert(0, '1')
            n = n / 2
        else:
            li.insert(0, '0')
    return li


def column_dominance(PI_list2):
    pp=[]
    for i in range(0, len(minterm)):
        cc = 0
        cc2 = 0
        for j in range(len(PI_list)):
            if (minterm[i] in PI_list[j] and check[minterm[i]]==1):
                cc = cc + 1
                cc2 = j
        if(cc==1):
            print("column_dominance : ", minterm[i],"in PI_"+str(cc2),":",PI_list[cc2])
            for j in range(len(PI_list[cc2])):
                check[PI_list[cc2][j]]=0

            for n in range(len(PI_list[cc2])):
                for m in range(len(PI_list)):
                    if(m==cc2): continue
                    if(PI_list[cc2][n] in PI_list2[m]): PI_list2[m].remove(PI_list[cc2][n])
            pp.append(cc2)
    pp2=[]
    for i in range(len(PI_list2)):
        if(i not in pp):
            pp2.append(PI_list2[i])
        else: pp2.append([])

    # print(pp2)
    return pp2


def row_dominance():
    pp=[]
    for i in range(len(PI_list)):
        for j in range(i+1,len(PI_list)):
            union = list(set(PI_list[i]) & set(PI_list[j]))

            if(PI_list[j]==union and len(ab_PI_List[i])>=len(ab_PI_List[j]) and PI_list[j]!=[]):
                print("Row_dominance : PI",j,"< PI",i)
                PI_list[j]=[]
                pp.append(j)

            elif(PI_list[i]==union and len(ab_PI_List[i])<=len(ab_PI_List[j]) and PI_list[i]!=[]):
                print("Row_dominance : PI", i, "< PI", j)
                PI_list[i]=[]
                pp.append(i)

    pp2 = []
    for i in range(len(PI_list)):
        if (i not in pp and PI_list[i]!=[]):
            pp2.append(PI_list[i])

        else: pp2.append([])

    # print("After R_D : ",pp2)

    return pp2



def petrick(sstr):
    for i in minterm:
        if(check[i]==1):
            sstr+='('
            for j in range(len(PI_list)):
                if(i in PI_list[j]):
                    sstr+="PI_"
                    sstr+=str(j)
                    sstr+=' + '
            sstr=sstr[:len(sstr)-3]
            sstr+=')'
    return sstr



def printt():
    table = [ [0 for i in range(max1+1)] for j in range(len(PI_list)) ]
    for i in range(len(PI_list)):
        for j in PI_list[i]:
            table[i][j]=1
    print("\t",end='')
    for i in minterm: print(i,end='\t')
    print()
    for i in range(len(table)):
        print("pi"+str(i),end='\t')
        for j in minterm:
            if(table[i][j]==0): print(" ",end='\t')
            else : print("V",end='\t')

        print()


# m=[4,8,2,6,8,9,10,11,14,15]
# m=[3, 6, 0,1,2,5,6,7]

# m=[4,11,0,2,5,6,7,8,10,12,13,14,15]
# m=[4,13,0,2,3,4,5,6,7,8,9,10,11,12,13]
m=[4,9,1,2,3,7,9,10,11,13,15]
PI_list = solution(m)

# PI_list=[[3,4,5,11],[4,5,6,7],[4,6,9,10],[4,5,8,9],[1,4,6,11],[1,2,6,10],[0,3,5,8],[2],[0]]
# m=[4,12,0,1,2,3,4,5,6,7,8,9,10,11]

# PI_list=[[8,10],[10,11],[12,13],[11,15],[13,15],[0,4,8,12]]
# m=[4,8,0,4,8,10,11,12,13,15]


ab_PI_List=PI_list[:]

max1=0
minterm = [m[i] for i in range(2,len(m))]

for i in range(len(PI_list)):
    if(str(type(PI_list[i])) == "<class 'int'>"):
        pi=[]
        pi.append(PI_list[i])
        PI_list[i]=pi
    if(max1<max(PI_list[i])): max1=max(PI_list[i])

check=[0 for i in range(max1+1)]
for i in minterm: check[i]=1
count = 0
for i in range(len(PI_list)):
    PI_list[i].sort()



print("SETUP")
for i in range(len(PI_list)): print("PI number ", i, " : ", PI_list[i])
print("checking : ", end='')
for i in minterm:  print(str(i) + ":", "o" if check[i] == 0 else "x", " ", end='')
print()

printt()


imsi=0

while(1):
    print("\n",count+1,"번째 실행")
    count=count+1
    imsi=1
    # for i in range(len(PI_list)): print("PI number ", i, " : ", PI_list[i])

    PI_list2 = copy.deepcopy(PI_list)

    PI_list2 = column_dominance(PI_list2)

    PI_list = copy.deepcopy(PI_list2)

    if not(np.array_equal(np.array(PI_list),np.array(PI_list2))): imsi=0
    printt()


    PI_list = row_dominance()

    if not(np.array_equal(np.array(PI_list),np.array(PI_list2))): imsi=0

    print("checking : ", end='')
    for i in minterm:  print(str(i) + ":", "o" if check[i] == 0 else "x", " ", end='')
    print()

    printt()

    if(1 not in check or imsi==1): break


if(1 in check):
    print("\nPetric")
    for i in range(len(PI_list)): print("PI number ", i, " : ", PI_list[i])
    print("Petrick method : ")
    sstr=""
    sstr = petrick(sstr)
    print(sstr)
