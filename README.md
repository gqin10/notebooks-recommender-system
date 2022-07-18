# Notebooks Recommender System
A constraint-based recommender system for notebooks

# Start the Project
1. Clone or download this repository
2. Install python packages listed in requirements.txt with PyPI
```
pip install -r requirements.txt
```

# Constraint-based Recommender System
1. Open demo_user.ipynb
2. import the following code
```python
from constraint_based_recommender_system import *
```
3. define a constraint-based recommender system problem
```python
constraintRS = ConstraintRS()
```
4. add constraints to the problem
```python
constraintRS.add_constraint(Constraint(attribute_value, specification_value, attribute_priority))
```
**attribute_value**: the name of attribute (refer to attribute value table in demo_user.ipynb)

**specification_value**: the specification/constraint of the attribute (refer to specification values table in demo_user.ipynb)

**attribute_priority**: the priority of the attribute (any positive numbers)
5. obtain items or suggestions to edit constraints
```python
constraintRS.get_items()
```