from Notebook import Notebook


def get_requirements():
    user_constraint = Notebook()

    user_constraint.brand.priority = input("Enter brand priority: ")
    if float(user_constraint.brand.priority) > 0:
        user_constraint.brand.value = input("Enter brand option: ")

    user_constraint.cpu.priority = input("Enter CPU priority: ")
    if float(user_constraint.cpu.priority) > 0:
        user_constraint.cpu.value = input("Enter CPU option: ")

    user_constraint.gpu.priority = input("Enter GPU priority")
    if float(user_constraint.gpu.priority) > 0:
        user_constraint.gpu.value = input("Enter CPU option: ")

    user_constraint.ram.priority = input("Enter RAM priority: ")
    if float(user_constraint.ram.priority) > 0:
        user_constraint.ram.min_value = input("Enter minimum RAM (GB): ")
        user_constraint.ram.max_value = input("Enter maximum RAM (GB): ")

    user_constraint.storage.priority = input("Enter storage priority: ")
    if float(user_constraint.storage.priority) > 0:
        user_constraint.storage.min_value = input("Enter minimum storage (GB): ")
        user_constraint.storage.max_value = input("Enter maximum storage (GB): ")

    user_constraint.screen_size.priority = input("Enter screen size priority: ")
    if float(user_constraint.screen_size.priority) > 0:
        user_constraint.screen_size.min_value = input("Enter minimum screen size (inches): ")
        user_constraint.screen_size.max_value = input("Enter maximum screen size (inches): ")

    user_constraint.weight.priority = input("Enter weight priority: ")
    if float(user_constraint.weight.priority) > 0:
        user_constraint.weight.min_value = input("Enter minimum weight (kg): ")
        user_constraint.weight.max_value = input("Enter maximum weight(kg): ")

    user_constraint.price.priority = input("Enter price priority: ")
    if float(user_constraint.price.priority) > 0:
        user_constraint.price.min_value = input("Enter minimum price (RM): ")
        user_constraint.price.max_value = input("Enter maximum price (RM): ")

    return user_constraint


if __name__ == "__main__":
    print("Refer to notebook-spec-option.md for the available options")

    user_constraint = get_requirements()

    """
    user_constraint.brand.value = "HP"
    user_constraint.brand.priority = 1 
    
    user_constraint.cpu.value = "i3"
    user_constraint.cpu.priority = 1
    
    user_constraint.gpu.value = "rtx"
    user_constraint.gpu.priority = 1
    
    user_constraint.ram.min_value = 8
    user_constraint.ram.max_value = 16
    user_constraint.ram.priority = 2 
    
    user_constraint.storage.min_value = 256
    user_constraint.storage.max_value = 512
    user_constraint.storage.priority = 3 
    
    user_constraint.screen_size.min_value = 13
    user_constraint.screen_size.max_value = 15
    user_constraint.screen_size.priority = 1 
    
    user_constraint.weight.min_value = 1.5
    user_constraint.weight.max_value = 3
    user_constraint.screen_size.priority = 1 
    
    user_constraint.price.min_value = 1000
    user_constraint.price.max_value = 5000
    user_constraint.screen_size.priority = 1 
    """
