# IB - *args **Kwargs Notes

#args
def hello(name, *args):
    print(args)
    for first in args:
        print(f"Hello {first} {name}!")

hello("LaRose", "Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake")

hello("Kringle", "Kris")

#kwargs
def clean(data, decimals =0, **kwargs):
    if not kwargs.get("data"):
        return "There is no Data"

    if kwargs.get("type") == "str":
        return kwargs.get("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int(data)
    elif kwargs.get("type") == "float":
        if kwargs.get("decimals"):
            decimals = kwargs.get('decimals')
        return round(float(data), 2)
    elif kwargs.get("type") == "list":
        return str(f"{x}, " for x in kwargs.get("data"))
    elif kwargs.get("type") == "bool":
        return f"{data}"
        
    
print(clean(type="float", data="3.1415", decimals=3))
print(clean(data="utah", type="str"))
print(clean())

"""
Positional argument: a value matched to a parameter by its position in the call. The first value goes to the first parameter, the second to the second, and so on.
Keyword argument: a value passed by name (greeting="Hi"), so the order doesn't matter
Default parameter: a parameter with a value already set in the definition (greeting="Hello"). It is used if the caller doesn't provide one.
*args: lets a function accept any number of positional arguments. Python collects the extra values into a tuple.
**kwargs: lets a function accept any number of keyword arguments. Python collects them into a dictionary.
The names args and kwargs are just a convention. What matters is the * and **.
Order matters: when a function uses several kinds, parameters go in this order: regular parameters, default parameters, *args, then **kwargs"""