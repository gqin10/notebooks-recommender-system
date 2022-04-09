from Notebook import Notebook

if __name__ == "__main__":
    print("Refer to notebook-spec-option.md for the available options")

    user_constraint = Notebook()

    user_constraint.brand = ""
    user_constraint.cpu = ""
    user_constraint.ram = ""
    user_constraint.storage = ""
    user_constraint.screen_size = ""
    user_constraint.weight = ""
    user_constraint.price = ""

    """
    user_constraint.brand = input("Select brand: ") 
    user_constraint.cpu = input("Select cpu: ")
    user_constraint.ram = input("Enter range of RAM: ") 
    user_constraint.storage = input("Enter range of storage: ") 
    user_constraint.screen_size = input("Enter range of screen size: ") 
    user_constraint.weight = input("Enter range of weight: ") 
    user_constraint.price = input("Enter range of price") 
    """