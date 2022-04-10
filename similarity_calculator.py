from Notebook import String_Attribute, Number_Attribute

def compute_similarity(constraint, item_list):
    for key, attr in constraint.__dict__.items():
        if isinstance(attr, str) or attr.priority <= 0:
            pass

        if isinstance(attr, String_Attribute) and attr.value != "":
            # process string constraint
            pass

        elif isinstance(attr, Number_Attribute) and (attr.min_value > 0 or attr.max_value > 0):
            # process number constraint
            pass
