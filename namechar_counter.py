while True:
 name = input("State his name please: ")
 name2 = input("State her name please: ")
 
 print(f"{name} lenght is {len(name)}")
 print(f"{name2} lenght is {len(name2)}")

 is_continue = input("Try again? Y/N: ")

 while is_continue == False:
    if is_continue == "Y" or is_continue == "y":
     continue
    elif is_continue == "N" or is_continue == "N":
     break
    else:
     print("Error")