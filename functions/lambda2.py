number=[200,500,300]

#map works with predefined functions as well as lambda function
out1=map(str,number)
out=map(lambda i:i/10,number)

#out and out1 are lazy objects
print(set(out))
print(list(out1))