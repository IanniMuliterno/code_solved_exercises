# one of the most confusing things for me, when I was a Statistician with R programming deep rooted in my heart, was to understand the concept of lambda functions. Now that I found THE way for memorizing it, I'm happy to share. Lets go

# first lets define a simple function
def double_my_number(num):
    return 2*num ;

print(double_my_number(5))

#how do I do that with lambda
#well, knowing that lambda is defined like this -> lambda <input>: <return>
double_my_number_with_lambda = lambda x: x*2
print(double_my_number_with_lambda(5))

#nice right?! defining the function in the good old <def> allows us to see clearly whats happening. Lets keep going

