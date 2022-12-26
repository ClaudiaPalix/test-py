#coding loops assignment
#to print positive values in a list

def pos_list(input_list):
    out_list = []
    for i in input_list:
        if i >= 0:
            out_list.append(i)
    print(out_list)     

list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]

pos_list(list1)
pos_list(list2)
