import json
# import jsonschema
# from jsonschema import validate
import csv


class DepartmentName(Exception):
    pass


class InvalidInstanceError(Exception):
    pass


def user_with_department(csv_file, user_json, departament_json):
    users = read_json_file(user_json)
    validate_json(users, user_schema)
    departments = read_json_file(departament_json)
    validate_json(departments, department_schema)

    output_dic = []
    for user in users:
        dept_name = next((dep["name"] for dep in departments if user["department_id"] == dep["id"]), None)
        if not dept_name:
            raise DepartmentName(f"Department with id {user["department_id"]} doesn't exists")

        output_dic.append({"name": user["name"], "department": dept_name})

    write_to_csv(csv_file, output_dic)


def write_to_csv(file_name, data):
    with open(file_name, "w", newline="") as file:
        headers = ["name", "department"]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return list(json.load(f))


def validate_json(data, scheme):
    try:
        validate(data, scheme)
        pass
    except Exception:
        raise InvalidInstanceError(f"Error in {scheme["title"]} schema")


user_schema = {
    'title': 'user',
    "properties": {
        "id", "name", "department_id"
    }
}

department_schema = {
    'title': 'department',
    "properties": {"id", "name"}
}


def validate(data, schema):

    for item in data:
        missing_keys = schema['properties'] - item.keys()
        if missing_keys:
            raise Exception(f"Missed key {missing_keys}")

try:
    user_with_department("7_3/user_department.csv", "7_3/user_without_dep.json", "7_3/department.json")
except DepartmentName as e:
    print(str(e))
