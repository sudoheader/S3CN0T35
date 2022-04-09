# Python

* Strings: 
	> *Use single-quotes for string literals, e.g. 'my-identifier', but use double-quotes for strings that are likely to contain single-quote characters as part of the string itself (such as error messages, or any strings containing natural language), e.g. "You've got an error!".*
* Math: Addition `+`, Subtraction `-`, Multiplication `*`, Division`/`, Modulus `%`, Exponentiation `**`, Floor Division `//`
	* Use PEMDAS for order of operation.
* Variables and Methods: `.upper()`,`.lower()`, `.title()`, `int()`, `str()`,`len()` 
	* int (1) difference between float (1.0)
* Functions: define functions with `def`
* Lists: If you have a list like `fruit = ["apples", "oranges", "grapes"]` you can get the last index of the list with `fruit[-1]`
	* `fruit.append("bananas")`: add to end of list. In this case "bananas" will be added
	* `fruit.pop()`: remove from end of list. "bananas" will be removed.
	* `fruit.pop(0)`: remove item at index 0. Removes "apples" from "fruit"
* Tuples: are immutable once they are defined. Usage with `()` like `grades = ("a", "b", "c", "d", "f")`
---
### Importing modules
`import sys` : to import system functions and parameters
`sys.version` : print out system version
`from datetime import datetime as dt`: import with alias

---
### Advanced Strings
```python 
sentence = "This is a sentence"
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
```

`.split()`: split sentence into a list
`' '.join()`: join list into a sentence
`.strip()`: strip whitespace

```python
movie = "The Matrix"
print("My favorite movie is {}.".format(movie))
```

### Dictionaries
```python
#Dictionaries - key/value pairs {}
drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} # drink is key, price is value
print(drinks)
employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] # add new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) # add new key:value pair

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
```

