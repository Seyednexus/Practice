import numpy as np
Units=0
average=0
total_score=0
name=input("name=")
lessons=int(input("number of lessons"))
report_card1= np.zeros((lessons, 3), dtype=object)
for lesson in range (0,lessons):
    print("lessons=",lesson+1)
    report_card1[lesson,0]=input("name of lesson")
    report_card1[lesson,1]=input("number of units")
    report_card1[lesson,2]=input("score")
    total_score=total_score+int(report_card1[lesson,2])*int(report_card1[lesson,1])
    Units=Units+int(report_card1[lesson,1])
average=total_score/Units
print(name)
print(report_card1)
print("adjusted=",average)