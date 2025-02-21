import math

class Vector:
    def __init__(self, *components):
        """Initialize a vector with any number of components."""
        self.components = tuple(components)

    def __str__(self):
        """Return a readable string representation of the vector."""
        return f"Vector{self.components}"

    def __add__(self, other):
        """Perform vector addition (element-wise)."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        new_components = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __sub__(self, other):
        """Perform vector subtraction (element-wise)."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        new_components = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*new_components)

    def __mul__(self, other):
        """Calculate the dot product if other is a vector, or perform scalar multiplication."""
        if isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for the dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*(other * a for a in self.components))
        else:
            raise TypeError("Multiplication only supports scalars or another vector.")

    def __rmul__(self, other):
        """Enable scalar multiplication from the left (e.g., 3 * v)."""
        return self * other  # Calls __mul__

    def magnitude(self):
        """Return the magnitude (length) of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        """Return the unit vector (normalized vector)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))



# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vectors
print(v1)         

# Addition
v3 = v1 + v2
print(v3)        

# Subtraction
v4 = v2 - v1
print(v4)          

# Dot product
dot_product = v1 * v2
print(dot_product)

# Scalar multiplication
v5 = 3 * v1
print(v5)          

# Magnitude
print(v1.magnitude())  

# Normalization
v_unit = v1.normalize()
print(v_unit)     