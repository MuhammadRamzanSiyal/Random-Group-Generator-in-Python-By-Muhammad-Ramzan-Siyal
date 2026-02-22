import random as r

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
li_len = len(li)
li_dic = {}

if li_len % 3 == 0:
    
    group_num = 1
    
    while li:
        li_temp = []
        
        for _ in range(3):
            li_rand = r.choice(li)
            li_temp.append(li_rand)
            li.remove(li_rand)
        
        li_dic[group_num] = li_temp
        group_num += 1
    
    print(li_dic)

else:
    print("Code Not Work")
