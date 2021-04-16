# create new shopping list called shopping)list
# create function called add_to_list that declares param named item
# add the item to list 

shopping_list = []

def show_help():
    print("What should we pick up at the store")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW_LIST' to see all items on the list. 
Enter 'HELP' for this help.
""")

    
def add_to_list(item):
    shopping_list.append(item)
    # notify user that item was added, state number of items
    print("Added: List has {} items".format(len(shopping_list)))
    
          
# define function show_list that prints out all items in list
def show_list():
    print("Here's your shoppig list:")
    for item in shopping_list:
          print(item)
    # enable the show command to list, don't forget to add to help
    # don't forget to run it
          

show_help()
while True:
    new_item = input("> ")
        
        
    if new_item =='DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item =='SHOW_LIST':
        show_list()
        continue
         
        
    # call add to list
    add_to_list(new_item)

    
show_list()
