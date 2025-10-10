def print_data(user):
    match user:
        case ("Tom" | "Tomas" | "Tommy" | "Bulat", 37):
            print(f"{name} - default user")
        case ("Tom", age):
            print(f"Age: {age}")
        case {"name": name, "age": 22}:
            print(f"Name: {name}")
        case {"name": name, "age": age} if age < 18:
            print(f"Name: {name}  Age: {age}")
 
 
print_data(("Bulat", 37))