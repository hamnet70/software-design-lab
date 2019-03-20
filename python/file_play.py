# This is my playspace for working with files

#with open("gradebook.csv", "r") as f:
#    f_contents = f.read()
#    print(f_contents)

#with open("gradebook.csv", "r") as f:
    
#    for line in f:
#        print(line, end=" ")

#    f_contents = f.readline()
#    print(f_contents)

with open("gradebook.csv","r") as rf:
    with open("new_gradebook.csv", "w") as wf:
        for line in rf:
            wf.write(line)

            