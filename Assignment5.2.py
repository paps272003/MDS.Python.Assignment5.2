subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for sub in range(len(subjects)):
    for ver in range(len(verbs)):
        for obj in range(len(objects)):
            sent='%s %s %s' %(subjects[sub],verbs[ver],objects[obj])
            print(sent)	