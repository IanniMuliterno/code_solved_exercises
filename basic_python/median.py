#sort vector
#find center
#if len can be divided by 2 get the 2 central values else get central value only
x = [5,4,1,6,7]


def median(vec):
    sorted_vec = sorted(vec)
    n = len(vec)

    if(n%2 == 0):
        locate = int(n/2) - 1
        center = [sorted_vec[i] for i in [locate,(locate+1)]]
        return(sum(center)/2)
    
    else:
        locate = int((n - 1)/2)
        return(sorted_vec[locate])    

print(median(x))