import random as r

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
li_len = len(li)
li_dic = {}

if li_len % 3 == 0:
    
    r.shuffle(li)
    
    group_num = 1
    
    for i in range(0, li_len, 3):
        li_dic[group_num] = li[i:i+3]
        group_num += 1

    print(li_dic)

else:
    print("Not Work")
