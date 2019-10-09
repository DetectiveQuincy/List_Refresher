#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenny.coons
#
# Created:     07/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Lists
words = ["cheeseburger", "Guacamole", "Jack Doff"] #sets words in a list
numbers = [69, 420] #sets numbers in a list
print(words)  #Prints the words from the words list
print(numbers) #prints the numbers in the numbers list
print(numbers, words) #prints the words and numbers from their respective lists

item_list = ["you chose cheeseburger", "you chose Guacamole", "you chose Jack Doff"] #sets code for a function
print(item_list)
print(item_list[0])
print(item_list[1])
print(item_list[2])




blank_inventory = []  #sets an empty inventory
new_item = input("name a thing")  #Allows the user to input an item into the blank list
blank_inventory.append(new_item) #user item added to list
print (blank_inventory)  #Prints the list with the user added item to it


inventory == [69, "pinch", "taxi Driver", 420] #Sets Items in the list
item_remove = input("what would you like to remove")  #User chooses item it wants removed
inventory.remove = (item_remove) #removes item

#Functions
def list_choice():     #Function for a list in which the user can select an option of 3 items
    choice = input("what item would you like")
    if choice == "cheeseburger":
        print(item_list[0])
    elif choice == "guacamole":
        print(item_list[1])
    elif choice == "Jack Doff":
        print("Jack Doff")



#Main Code

list_choice() #runs the function





