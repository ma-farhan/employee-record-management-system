import mysql.connector

myc = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fari",
    database="db5"
)


def add(n, a, s):
    obj = myc.cursor()
    sql = "insert into users (name,age,salary) values (%s,%s,%s)"
    val = (name, age, salary)
    obj.execute(sql, val)
    myc.commit()
    print("Employee Added Successfully")


def edit(n, a, s, i):
    obj = myc.cursor()
    sql = "update users SET name=%s,age=%s,salary=%s where id=%s"
    val = (name, age, salary, id)
    obj.execute(sql, val)
    myc.commit()
    print("Employee Information Updated Successfully!")


def list():
    obj = myc.cursor()
    sql = "SELECT name,age,salary from users"
    obj.execute(sql)
    result = obj.fetchall()
    print(result)


def delete(n):
    obj = myc.cursor()
    sql = "delete from users where name=%s"
    val = (name,)
    obj.execute(sql, val)
    myc.commit()
    print("Employee Deleted Successfully!")


print("Employee Record Management System")
while True:
    print("=======================================")
    print("Menu")
    print("Please select your input")
    print("1.List")
    print("2.Add")
    print("3.Edit")
    print("4.Delete")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        list()
    elif choice == 2:
        name = input("Enter employee name : ")
        age = input("Enter employee age : ")
        salary = input("Enter employee salary : ")
        add(name, age, salary)
    elif choice == 3:
        id = input("Enter employee id to edit: ")
        name = input("Enter employee's new name : ")
        age = input("Enter employee's new age : ")
        salary = input("Enter employee's new salary : ")
        edit(name, age, salary, id)
    elif choice == 4:
        name = input("Enter name to Delete : ")
        delete(name, )
    elif choice == 5:
        quit()
    else:
        print("Invalid Choice !")
