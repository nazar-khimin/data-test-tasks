class ToSmallNumberGroupError(Exception):
    pass

def check_number_group(number):
    try:
        number = int(number)
        if number > 10:
            return f"Number of your group {number} is valid"
        else:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError as e:
        return str(e)

print(check_number_group("96"))