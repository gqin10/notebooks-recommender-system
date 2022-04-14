from Notebook import String_Attribute, Number_Attribute

def average(a, b):
    return (a+b)/2

def compute_similarity(constraint, item_list):
    #assign 0 to each item's similarity
    item_list["similarity"] = [0 for i in range((item_list.shape)[0])]

    for key, attr in constraint.__dict__.items():
        if isinstance(attr, str) or attr.priority <= 0:
            continue

        if isinstance(attr, String_Attribute) and attr.value != "":
            # process string constraint
            pass

        elif isinstance(attr, Number_Attribute) and (attr.min_value > 0 or attr.max_value > 0):
            # process number constraint
            s = attr.priority * (average(attr.min_value, attr.max_value) * item_list[key].astype(float))
            item_list["similarity"] = item_list["similarity"] + s

    print(item_list)
