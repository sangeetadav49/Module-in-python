#Create a list in Python of children selected for science quiz with the following names-
l=["Arjun", "Sonakshi", "Vikram", "Sandhya", "Sonal", "Isha", "Kartik"]

#Perform the following tasks on the list in sequence-
#○ Print the whole list
print(l)

#Delete the name “Vikram” from the list
l.remove("Vikram")
print(l)
# Add the name “Jay” at the end
l.append("Jay")
print(l)
# Remove the item which is in the second position
l.pop(1)
print(l)
# Create a list num=[23,12,5,9,65,44]
num=[23,12,5,9,65,44]
print(num)

# print the length of the list
print(len(num))
# print the elements from second to fourth position using positive indexing
print(num[1:4])
# print the elements from position third to fifth using negative indexing
print(num[3:5])
# Create a list of the first 10 even numbers, add 1 to each list item and print the final list.
#l=10 even numbers, add 1 to each list item and print the final list.
l=[2,4]
l[0]=l[0]+1
l[1]=l[1]+1
print(l)
# Create a list List_1=[10,20,30,40]. Add the elements [14,15,12] using the extend function. Now sort the final list in ascending order and print it.
List_1=[10,20,30,40]
List_1.extend([14,15,12])
print(List_1)
