##crud
##
##create
##get 
##update 
##delete

class Student:
    
    count=1
    data={}
    def __init__(self):
        self.id=Student.count
        print('creating student.....')
        try:
            self.name=str(input('enter student name:'))
            self.age=int(input('enter student age:'))
        except Exception as e:
            print('error is:',e)
        else:
            Student.data[self.id] = {'id': self.id, 'name': self.name, 'age': self.age}
            Student.count+=1
            print('student createed successfully.....')
            print()
            #print(Student.data)
    
    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\n"
        
    @staticmethod
    def get_student(i):
        if i in Student.data:
            print(f'fetching details of student id {i} from database....')
            print(f'id : {Student.data[i]["id"]}')
            print(f'name : {Student.data[i]["name"]}')
            print(f'age : {Student.data[i]["age"]}')
        else:
            print('id not found')
       
    @staticmethod
    def get_data():
        print(f'fetching all student data from database....')
        for i,j in Student.data.items():
            print(f"id : {j['id']}")
            print(f"name : {j['name']}")
            print(f"age : {j['age']}")
            print()
            print()

    @staticmethod
    def update_student(i):
        if i in Student.data:
            print('this is your previous data')
            Student.get_student(i)
            update=int(input('''press 1 to edit name
    press 2 to edit age
    pres 3 to edit all'''))
            if update==1:
                n=input('enter new name:')
                Student.data[i]['name']=n
                print('name updated successfully in database.....')
                Student.get_student(i)
            elif update==2:
                a=int(input('enter new age:'))
                Student.data[i]['age']=a
                print('name updated successfully in database.....')
                Student.get_student(i)
            elif update==3:
                n=input('enter new name:')
                a=int(input('enter new age:'))
                Student.data[i]['name']=n
                Student.data[i]['age']=a
                print('data updated successfully in database.....')
                Student.get_student(i)
        else:
            print('id not found')
            
    @staticmethod
    def delete_student(i):
        if i in Student.data:
            print(f"deleting student with id {i} and name {Student.data[i]['name']}")
            del Student.data[i]
            print(Student.data)
        else:
            print('id not found')

            
s1=Student()
##print(s1)
##s2=Student()
##Student.get_student(3)
##Student.update_student(1)
##Student.get_data()
##Student.delete_student(1)
##   
