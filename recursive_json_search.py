from test_data import *

ret_val = []
def json_search(key, input_object):
    ret_val = []
    
    if isinstance(input_object, dict):  # Iterate dictionary
        for k, v in input_object.items():  # searching key in the dict
            if k == key:
                temp = {k: v}
                ret_val.append(temp)
            if isinstance(v, dict):  # the value is another dict, so recurse
                ret_val.extend(json_search(key, v))
            elif isinstance(v, list):  # it's a list, so iterate through it
                for item in v:
                    if not isinstance(item, (str, int)):  # if item is a dict or list, recurse
                        ret_val.extend(json_search(key, item))
    
    elif isinstance(input_object, list):  # Iterate a list (some APIs return JSON in lists)
        for val in input_object:
            if not isinstance(val, (str, int)):
                ret_val.extend(json_search(key, val))
    
    return ret_val

# Example usage:
print(json_search("issueSummary", data))
