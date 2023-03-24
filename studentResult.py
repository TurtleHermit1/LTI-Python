num=int(input())

passed=dict()
failed=dict()
studentMarks=0


for i in range(num):
    studentMarks=int(input())
    if studentMarks>=40:
        passed[i+1] = studentMarks
    else:
        failed[i+1] = studentMarks


if(len(passed)==0):
    print("All are failed")
elif(len(failed)==0):
    print("All are passed")
else:
    print("Students who Failed in Final Exam\n")
    for x,y in failed.items():        
        print(f"Roll No: {x} - Mark: {y}\n")

    print("Students who passed in Final Exam\n")
    for x,y in passed.items():
        print(f"Roll No: {x} - Mark: {y}\n")







