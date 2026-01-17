# Create and iterate through a tuple
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Using for loop with tuple
print("Fruits in the tuple:")
for fruit in fruits:
    print(fruit)

# Using enumerate with tuple
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Accessing tuple elements
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])