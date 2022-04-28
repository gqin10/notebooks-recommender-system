from Constraint import Constraint, String_Attribute, Number_Attribute, Boolean_Attribute, NATURE
from spec_list import brand_list, cpu_list, gpu_list
from constraint_processor import set_cpu_gpu_average


def get_user_requirements():
    user_constraint = Constraint()

    for key, attr in user_constraint.__dict__.items():
        if key == "cpu_average" or key == "gpu_average":
            continue

        priority = float(input(f"Enter {key} priority: "))
        setattr(user_constraint.get(key), "priority", priority)
        if priority > 0:
            if isinstance(attr, String_Attribute) or isinstance(attr, Boolean_Attribute):
                temp = input(f"Enter {key} option: ")
                temp = [x for x in temp.split(",")]
                if isinstance(attr, String_Attribute):
                    setattr(user_constraint.get(key), "value", temp)
                else:
                    setattr(user_constraint.get(key), "value", bool(temp))

            elif isinstance(attr, Number_Attribute):
                value = 0
                if attr.nature == NATURE.MORE:
                    value = float(input(f"Enter minimum value of {key}: "))

                elif attr.nature == NATURE.LESS:
                    value = float(input(f"Enter maximum value of {key}: "))

                elif attr.nature == NATURE.NEAR:
                    value = float(input(f"Enter value of {key}: "))

                setattr(user_constraint.get(key), "value", value)

    return set_cpu_gpu_average(user_constraint)
