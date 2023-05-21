import csv
def create():
    with open("details.csv", "w", newline="") as obj:
        fobj = csv.writer(obj)
        fobj.writerow(['Roll', 'Name', 'Total_marks'])
        while True:
            roll = int(input("Enter Roll No :"))
            name = input("Enter Name :")
            total = int(input("Enter Total Marks :"))
            record = [roll, name, total]
            fobj.writerow(record)
            ch = int(input("1-Enter more \n 2- Exit\n Enter your choice :"))
            if ch == 2:
                break
def display():
    with open("details.csv", "r") as obj:
        fobj = csv.reader(obj)
        for i in fobj:
            print(i)

def search():
    with open("details.csv", "r") as obj:
        fobj = csv.reader(obj)
        next(fobj)
        for i in fobj:
            marks = int(i[2])
            if marks >= 50:
                print(i)

# create()
# display()
search()