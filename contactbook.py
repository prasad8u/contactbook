contact={}

def displaycontact():
    print("name\t\t contact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


        
while True:
    choice=int(input("enter no"))
    if choice==1:
        name=input("enter the contact name :")
        phone=input("enter mobile no :")
        contact[name]=phone
    elif choice==2:
        searchname=input("enter contact name")
        if searchname in contact:
            print(searchname,"'s contact number is",contact[searchname])
        else:
            print("name is not found in contact book")
    elif choice==3:
        if not contact:
   
           print("empty contact book")
        else:
             displaycontact()       
   
    elif choice==4:
        editcontact=input("enter the contact to be edited")
        if editcontact in contact:
            phone=input("enter mobile number :")
            contact[editcontact]=phone
            print("update content")
            displaycontact()
        else:
            print("name is not found in contact book")
    elif choice==5:
        delcontact=input("enter the contact to be deleted :")
        if delcontact in contact:
            confirm=input("do you want to delete this contact :")
            if confirm=='y' or confirm=='Y':
                contact.pop(delcontact)
                displaycontact()
        else:
            print("name is not found in contact number")
    else:
        break
