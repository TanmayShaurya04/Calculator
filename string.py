print("He said,\"I want to eat an apple\"")
print('He said ," I want to eat an apple"')
#both ill do same work 

#to access the characters of string 
name="Tanmay"
print(name[0]) #T
print(name[1]) #a
print(name[2]) #n
print(name[3]) #m
print(name[4]) #a
print(name[5]) #y
#name[6] # this will give an error because there is no index 6 in the string   

for character in name:
    print(character)


    #string slicing

name1="Tanmay,Yukti,Tanisha"
print(name1[7:12])
print(len(name1)) # this will give the length of the string
print(len(name1[7:12])) # this will give the length of the sliced string
print(name1[:6]) # this will give the first 6 characters of the string
print(name1[13:]) # this will give the characters from index 13 to the end of the string
print(name1[:]) # this will give the entire string
print(name1[1:-4]) # this will give the characters from index 1 to the index -4 (which is the 4th last character of the string)

nm="Harry"
print(nm[-4:-2])