print("""
-----------------------------------------------------------------------
               STUDENT PROGRESS TACKER SYSTEM
-----------------------------------------------------------------------
      """)

Name=input("enter student name:")
Class=input("enter student class:")
Roll_no=input("enter student roll no:")
count=0
sub=[]
num=1
while True:
    if num==1:
        n=int(input("enter number of subjects:"))
        marks=[]
        # Collect marks for each subject
        for i in range(n):
            marks.append(int(input(f"enter marks of subject{i+1}:")))
        # Calculate total
        total=0
        for i in range(n):
            total=total+marks[i]
        # Calculate average
        avg=total/n
        # Grade calculation
        grade=""
        if avg>=90 and avg<=100:
            grade="A"
        elif avg>=75 and avg<=89:
            grade="B"
        elif avg>=50 and avg<=74:
            grade="C"
        elif avg>=35 and avg<=49:
            grade="D"
        else:
            grade="F"

        # Count subjects with marks less than 35
        for i in range(n):
            if marks[i]<35:
                count+=1
                sub.append(i)

        # Determine result based on grade and count
        result=""
        if grade=="F" or count!=0:
            result="FAIL"
        else:
            result="PASS"


        num=2
        continue

    elif num==2:
        print("""
-----------------------------------------------------------------------
                  STUDENT PROGRESS REPORT
-----------------------------------------------------------------------
              """)
        print(f"Name  :- {Name}")
        print(f"Class :- {Class}")
        print(f"Roll no :- {Roll_no}")
        print(f"Total marks :- {total}")
        print(f"Average marks :- {avg}")
        print(f"Grade :- {grade}")
        print(f"Result :- {result}")
        #Failed subjects
        print("-----------------------------------------------------------------------")

        if count==0:
            print("ALL CLEAR 👍")
        else:
            print(f"Number of subjects failed are {count}")
            count=0
            for i in range(len(sub)):
                print(f"Subject {sub[i]+1} is failed with marks {marks[sub[i]]}")


        print("""-----------------------------------------------------------------------""")
        print("""
              What do you want to do next
                   1.Enter marks again
                   2.View report again
                   3.Exit
              """)
    num=int(input("Enter Your Choice :"))
    if num==3:
        print("Exiting the program. Goodbye!")
        break
