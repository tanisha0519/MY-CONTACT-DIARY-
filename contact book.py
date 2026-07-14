contacts = {}
while True:
    print(" MY CONTACT DIARY")
    print("1:Add contact")
    print("2:View contact")
    print("3:Edit contact")
    print("4:Search contact")
    print("5:Del contact")
    print("6:Exit")
    choice=input("Enter your choice (1-6): ")
    if choice == "1":
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        contacts[name]=phone
        print("Contact succesfully added!!!...")
    elif choice == "2":
            name=input("Enter name to view:")
            if name in contacts:
                print("Contact succesfully matched!!!...")
                print("Name :", name)
                print("Phone:", contacts[name])
    elif choice =="3":
        name=input("Enter name to edit:")
        if name in contacts:
            phone=input("Enter the edited number: ")
            contacts[name]=phone
            print("Contact editted successfully!")
        else:
            print("Contact not matched!!!...")
    elif choice == "4":
        name=input("Enter name to search: ")
        if name in contacts:
            print("Contact succesfully matched!!!...")
            print("Name :", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not matched!")
    elif choice == "5":
        name=input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not matched!")
    elif choice == "6":
        print("Thank you for using!!!...")
        break
    else:
        print("OOPS!! please try again...")