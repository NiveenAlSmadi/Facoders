
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names (grade_number):
            b=list(grade_number.keys())
            print(b)

def student_score (grade_number , students_name):
          c= list (grade_number.get(students_name))
          d=sum(c)
          print(d)

def students_count (grade_number) :
       e=list(grade_number.keys())
       print (len(e))

a= input("Choose one: students_names, student_score, students_count = ")
if a=='students_names':
     a1=input('Enter grade_number:')
     if a1=='grade_one':
        students_names(grade_one)
    elif a1=='grade_two':
        students_names(grade_two)
    elif a1=='grade_three':
        students_names(grade_three)
elif a=='student_score' :
    a2=input('Enter grade_num ,student name :')
    


elif a== 'students_count':
   a3=input('Enter grade_number :')
   students_count(a3)

world=input('Enter done or more')
if world == 'more' :
    print(a)
else:
    exit()
