# -*- coding: utf-8 -*-
"""Kai_HK1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DRD2HwXdQMB01XY1taVUjET6Da7gVsYL

# **Homework**
- Data: 
- Name:

### **(1) A Phone Book**
Write a problem that allows user to store and search contact information.
Each entry of the contact information should contain the `name` and `phone`. As an example using `dict`, it would look like

`
{
  "name": "John",
  "phone": "0987-654321,
}
`
<br/><br/>
You may use a `list` of `dict` as data structure of the phone book, or if you prefer, any other suitable data container to implement the phone book.
As an example using `list` of `dict`, it would look like

`
[{
  "name": "John",
  "phone": "0987-654321,
}, {
  "name": "Andrew",
  "phone": "0912-343531,
}, {
  "name": "Catherine",
  "phone": "0956-396471,
}, ... ]
`
<br/><br/>
**Requirements**
1. Implement a function `add(name, phone)` which allows user to add an entry to the phone book.
1. Implement a function `find(name="", phone="")` which allows user to search the phone book ***either*** by "name" or "phone".
1. Implement a function `print_all()` which allows user to print the phone book. For each line, print one entry in the format of `"name / phone number"`.
"""

class Phonebook:
  def __init__(self, pb):
    self.pb = pb
    self.val_pb = pb.values() # values of pb

  def add(self, name, phone):
    self.pb["{}".format(name)] = phone # add the new dict into pb
    return self.pb

  def find(self, key):
    if key in self.pb: # key in pb.keys
      print("{}'s phone is {}".format(key, self.pb[key])) 

    elif key in self.val_pb: # key in pb.values
      pb_ = {v : k for k, v in self.pb.items()} # change keys and values position
      print("{}'s phone is {}".format(pb_[key], key))
      
    else: # if type wrong key
      print("{} is not in phone book!".format(key))

  def print_all(self):
    for i,j in self.pb.items():
      print(i, "\t/", j)

phone_book = {"John": "0987-654321", "Andrew": "0912-343531"}
pb = Phonebook(phone_book)

pb.add("Kai", "0900-000000")
pb.find("0987-654321")
pb.find("Kai")
pb.find("0987654321")
pb.print_all()

"""### **(2) Find a missing number from a list**
Use a function and write a python program to find a missing number from a list. 

Ex. `Input: [1, 2, 3, 5, 6, 7]`, `Output: 4`

"""

def miss(li):
  li.sort()
  misnum = []
  for i in range(li[-1]):
    if i+1 not in li:
      print(i+1, end = " ")

li = [1, 5, 8, 6, 9, 10, 11]
miss(li)

"""### **(3) Reverse a string**

Write a function to reverse a string.

Sample String : "abcd4567"

Expected Output : "7654dcba"
"""

def rev(string):
  print('"', end = "")
  for i in range(len(string)):
    print(string[-i-1], end = "")
  print('"', end = "")

string = "abcd467"
rev(string)

"""### **(4) Calculate the harmonic sum**
Harmonic series is inverse of a arithmetic progression. In general, the terms in a harmonic progression can be denoted as 1/a, 1/(a + d), 1/(a + 2d), 1/(a + 3d) …. 1/(a + nd). 
As Nth term of AP is given as ( a + (n – 1)d). Hence, Nth term of harmonic progression is reciprocal of Nth term of AP, which is 1/(a + (n – 1)d), where “a” is the 1st term of AP and “d” is a common difference.

Example:

![CodeCogsEqn.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALcAAAAlBAMAAADy7mXkAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARM0yInYQiatmmbtU3e/6iv2wAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAB5UlEQVRIDe2WPywDYRjGH3qOI1rMBmFglHSwcYvE2DCIhZvYkPhbBkJwEYkaGgkLE9FYxGTqbGSzWAwm8SeREEkdd9d63q+nHdqtt3zf83vf57nLm7uvBeRV1SFJS7cgClA9wuFJbehNFPr7RLgCVI+IyEkZjogIVwEUTy6Od0pjJfxnQJWx8GviqbKO5UXeMtIkiAKgeITDk/ri6wxXJnY7+StSgOrxE5SDwi+UYM0eFJYM0wsCFPT4H/eezDLkqBWAgp5K+O9U5eTKP5Z622637Wnn7hnnenbWU3uty95yNpEfkg/843Ha3av8T+7cp+BrBTnQIjz+QVHK8AFL28SAhexBUcrwXjP0gF7TG3y5xuLHj3ub4VTa3emWuxrJDQZAjwvgebTO5KVs8Tp4qTX1DyZxRGJMcMdau380mQSoxm6cc2kZ4VUmxjZrLc06UIUTWJHFqQST6BnrosMd2wVbgUEBEjJ8ZL9JtARJTf5CHxxxqwERrsdwyy2BqloMATi0qDkqw51qijqCRVwpNbQRSuQJH6WOQGHIB19H/fvfbuNk4Yb/IDSmMfa3I3jfCoOK2hfqnokAV6yrzSLHEjpuvmbrPCZjTGS4YekPoiO/DGcyn1ypmdthgJ6nWSbJJZOBq74BU4+MGZhA8tsAAAAASUVORK5CYII=)

Write a function to calculate the harmonic sum of n-1.

"""

def sum(n):
  if n == 0:
    return 0
  else:
    term = sum(n-1)
    h_sum = term + 1/n
    return h_sum

print(sum(8))