# Exercise 6.6 Longest in Collection

The exercise template comes with the class `SimpleCollection` that's familiar from previous exercises. Implement the method `def longest()` for the class, which returns the longest string of the collection. If the collection is empty, the method should return a `None` reference.

```python
j = SimpleCollection("characters")
print("Longest: " + str(j.longest()))

j.add("magneto")
j.add("mystique")
j.add("phoenix")

print("Longest: " + str(j.longest()))
```

```plaintext
Longest: None
Longest: mystique
```
