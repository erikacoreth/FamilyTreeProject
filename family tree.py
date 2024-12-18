class Node:
    def __init__(self, child):
        self.child = child
        self.left = None
        self.right = None
        self.parent = None

    def add_child(self, child, direction):
        #check if the direction is valid
        if direction not in ['L', 'R']:
            return False, "Invalid direction. Use 'L' for left or 'R' for right."

        #add to the left or right as specified
        if direction == 'L':
            if self.left is not None:
                return False, "Left child already exists."
            self.left = Node(child)
            self.left.parent = self
        elif direction == 'R':
            if self.right is not None:
                return False, "Right child already exists."
            self.right = Node(child)
            self.right.parent = self

        return True, f"{child} added to {direction}-child of {self.child}."

    def find_node(self, name):
        #check if the current node matches the name
        if self.child == name:
            return self
        #search in the left subtree
        if self.left:
            found = self.left.find_node(name)
            if found:
                return found

        #search in the right subtree
        if self.right:
            return self.right.find_node(name)

        return None #if not found in any subtree, return None

    def print_tree(self, level=0):
        if self is None:
            return #base case: if the node is none, stop

        #print the current node with indentation
        print("  " * level + str(self.child))
        #print the current node with indentation based on its depth

        #Recur for left and right children
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)

class Main:
    def __init__(self):
        self.root = None #root node starts as none


    def menu(self):
        while True:
            #check if the root node exists
            if self.root is None:
                print("===Menu===")
                print("1) Add Root Creature: ")
                print("0) Exit: ")
                choice = input("--Enter choice: ")

                if choice == '1':
                    name = input("--Enter the name of the root creature: ")
                    self.root = Node(name)
                    print(f"{name} added as root creature.")
                elif choice == '0':
                    print("Exiting program")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 0.")
            else:
                #Full menu now that root creature is selected
                print("===Menu===")
                print("1) Add Child Creature: ")
                print("2) Print Tree: ")
                print("3) Find Creature: ")
                print("0) Exit: ")
                choice = input("--Enter choice: ")

                if choice == '1':
                    parent_name = input("--Enter the name of the parent creature: ")
                    direction = input("--Enter direction (L or R): ")
                    child_name = input("--Enter the name of the child creature: ")

                    #find the parent node
                    parent_node = self.root.find_node(parent_name)
                    if parent_node:
                        success = parent_node.add_child(child_name, direction)
                        if success:
                            print(f"{child_name} added to {parent_name} as {direction}-child.")
                        else:
                            print(f"Couldn't add {child_name} to {parent_name}.")
                    else:
                        print(f"Parent creature '{parent_name}' not found.")

                elif choice == '2':
                    print("===Creature Tree===")
                    if self.root:
                        self.root.print_tree() #print whole tree
                    else:
                        print("The tree is empty.")
                elif choice == '3':
                    creature_name = input("--Enter the name of the creature to search for: ")
                    node = self.root.find_node(creature_name)
                    if node:
                        # Start with the chosen creature
                        print(f"{creature_name}", end="")
                        # Traverse the ancestors
                        current = node
                        while current.parent:
                            print(f" is descended from {current.parent.child}", end="")
                            current = current.parent
                        # End the statement with a period
                        print(".")
                    else:
                        print(f"Creature '{creature_name}' not found.")
                elif choice == '0':
                    print("Exiting program")
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_program = Main()
    main_program.menu()










