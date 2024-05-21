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

#lambda inside a list?
power_lambda = lambda x: x*x
lambda_in_list_1 = [power_lambda(x) for x in range(10)]
#function_in_list_2 = [x*x for x in range(10)] #the output is the same as above

print(lambda_in_list_1)
#print(function_in_list_2)

#Example of Lambda for Encoder and Decoder:
#Let's say you have a simple encoding scheme where each character is shifted by a certain number of places in the alphabet.
import string

# create a dictionary mapping each character to its shifted value
shift = 3
alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#lets check how we're doing, shall we?
print(shifted_alphabet)

encoder = dict(zip(alphabet,shifted_alphabet))

#lambda functions for encoding and decoding
encode = lambda text:  ''.join(encoder.get(char,char) for char in text)
decode = lambda text: ''.join(shifted_alphabet.get(char,char) for char in text)