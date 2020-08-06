import os
path="C:\\GOworkSpace\\src\\revision\\templates"
for d,s,f in os.walk(path) :
    if len(f) != 0 :
        print(d)
        for eachFile in f :
            print(os.path.join(d,eachFile))
        print()
