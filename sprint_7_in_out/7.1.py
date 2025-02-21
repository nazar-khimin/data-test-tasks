import json
from typing import Union, Set, List

def find_unique_values(json_content: Union[dict, list], search_key:str) -> Set[str]:
    values = set()
    if isinstance(json_content, dict):
        if search_key in json_content:
            value = json_content[search_key]
            if isinstance(value, list):
                values.update(value)
            else:
                values.add(value)
        for sub_item in json_content.values():
            if isinstance(sub_item, (dict, list)):
                values.update(find_unique_values(sub_item, search_key))
    else:
        if isinstance(json_content, list):
            for item_with_list_value in json_content:
                values.update(find_unique_values(item_with_list_value, search_key))
    return values


def find(file: str, key: str) -> List[str]:
    with open(file, 'r') as f:
        data = json.load(f)

    values = find_unique_values(data, key)
    return list(values)


# print(find("1.json", "password"))
print(find("7_1/3.json", "password"))
