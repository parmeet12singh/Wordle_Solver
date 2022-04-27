MAX_CHAR = 256;
 
def uniqueCharacters(string):
    n = len(string)
     
    # If length is greater than 256,
    # some characters must have
    # been repeated
    if n > MAX_CHAR:
        return False
 
    chars = [False] * MAX_CHAR
 
    for i in range(n):
        index = ord(string[i])
 
        '''
         * If the value is already True,
         string has duplicate characters,
         return False'''
        if (chars[index] == True):
            return False
 
        chars[index] = True
 
    ''' No duplicates encountered,
        return True '''
    return True

f = open('C:/Users/parmeets219/Desktop/wordbase.txt', 'r')  
# display content of the file
required_words = f.readlines()  
# close the file
f.close()

# print(required_words)
print(len(required_words))

# f = open('C:/Users/parmeets219/Desktop/required_unique_words.txt', 'r')  
# # display content of the file
# required_unique_words = f.readlines()  
# # close the file
# f.close()

# required_unique_words = []

# for i in required_words:
#     if(uniqueCharacters(i)):
#         required_unique_words.append(i)

# print(required_unique_words)

required_unique_words = list(map(lambda i: i.replace('\n',''), required_unique_words))

print(required_unique_words)

# with open('C:/Users/parmeets219/Desktop/required_unique_words.txt', 'w+') as f:
      
#     # write elements of list
#     for items in required_unique_words:
#         f.write('%s\n' %items)
      
#     print("File written successfully")
  
  
# # close the file
# f.close()