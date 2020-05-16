
#opens file in read mode 
file_object  = open("output.txt", 'r') 
file_object2  = open("output.txt", 'r+') 
#checks if file is in read mode
if file_object.mode=='r':
    contents=file_object.read()
    print ("Text Decryption: "+contents)
    file_object2.truncate(0)
   

file_object.close()
file_object2.close()
