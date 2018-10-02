from collections.abc import Mapping,MutableMapping

a = {
    "bob1":{"company":"com1","department":"depart1"},
    "bob2":{"company":"com2","department":"depart2"},
    "bob3":{"company":"com3","department":"depart3"},
    "bob4":{"company":"com4","department":"depart4"}
    }

# new_dict = a.copy()
import copy
new_dict = copy.deepcopy(a)
new_dict["bob1"]["company"]="com0"
print(id(a["bob1"]))
print(id(new_dict["bob1"]))
pass