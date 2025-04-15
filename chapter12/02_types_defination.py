from typing import List,Tuple,Dict,Union
n : int = 5
name : str = "harsh"
def sum(a: int, b: int) -> int:
    return a+b
print(sum(2,5))

numbers: List[int] = [1,2,3,4,5]

data: Tuple[str, int] = ("Harsh", 18)

scores: Dict[str, int] = {"Harsh": 95, "Rahul": 98}

indentify: Union[int, str] = "AD1243"
# indentify = 12345

print(numbers)
print(data)
print(scores)
print(indentify)