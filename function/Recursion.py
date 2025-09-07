


# def recursion(n):
#     if n==0:           # base  case to stop the recursion
#        return;
#     print(n);
#     recursion(n-1);


# n = 5
# recursion(n);

 
# def naturalNumSum(n):
#     if n==0:           # base  case to stop the recursion
#        return 0;
#     return n + naturalNumSum(n-1);

# print(naturalNumSum(5));  


def printelem(nlist,indx=0):
    if indx==len(nlist):
        return 1
    print(nlist[indx]) 
    return printelem(nlist , indx+1);


list = [1,2,3,4,5]
printelem(list)
    # print(list[i])

