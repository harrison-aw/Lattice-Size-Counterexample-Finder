class Vector(object):
	"""Object to represent n-dimensional points.
	
	Vectors are treated as immutable objects with certain operations defined.
	
	Args:
		coordinates - tuple of numbers
	"""
	
	variables = ('x', 'y', 'z', 'w')
	
	def __init__(self, coordinates):
	
		self.coordinates = coordinates
		
	def __repr__(self):
		return 'Vector(%s)' % repr(self.coordinates)
		
	def __str__(self):
		return repr(self.coordinates)
		
	def __add__(self, other):
		"""Return the sum of two vectors."""
	
		return Vector(tuple(x + y for x, y in zip(self.coordinates, other.coordinates)))
	
	def __mul__(self, other):
		"""Return the dot product of two vectors."""
	
		return sum(x * y for x, y in zip(self.coordinates, other.coordinates))
		
	
	def __eq__(self, other):
		return self.coordinates == other.coordinates
	
	def __ne__(self, other):

		return self.coordinates != other.coordinates
	
	def __len__(self):
		"""Return number of coordinates."""
		
		return len(self.coordinates)
		
	def __getitem__(self, k):
		"""Return the k-th coordinate (zero-indexed)."""
		
		return self.coordinate[key]
	
	@property
	def x(self):
		"""Return the first coordinate."""
		
		return self.coordinates[0]
	
	@property
	def y(self):
		"""Return the second coordinate."""
		
		return self.coordinates[1]
	
	@property
	def z(self):
		"""Return the third coordinate."""
		
		return self.coordinates[2]
	
	@property
	def w(self):
		"""Return the fourth coordinate."""
		
		return self.coordinates[3]
	
	@property
	def dimension(self):
		"""Return the number of coordinates of the vector."""
		
		return len(self.coordinates)
	
	def delta_notation(self):
		"""Return the string of the vector in Delta notation."""
		
		if self.dimension <= len(Vector.variables):
			variables = Vector.variables
		else:
			variables = tuple('x_' + str(i) for i in range(self.dimension))
		
		notation = ''
		
		for i in range(len(self.coordinates)):
			c = self.coordinates[i]
			
			if c != 0:
				if c > 0:
					notation += '+'
					
				if c == 1:
					notation += variables[i]
				elif c == -1:
					notation += '-' + variables[i]
				else:
					notation += str(c) + variables[i]
		
		if notation[0] == '+':
			return 'Delta(' + notation[1:] + ')'
		
		return 'Delta(' + notation + ')'

if __name__ == '__main__':
	v1 = Vector((1, 1))
	v2 = Vector((-1, 2))
	v3 = Vector((0, 0))
	v4 = Vector((1, 0))
	
	print("Initialize and Represent: Vector((1, 1)) = %s" % repr(v1))
	print("String: (1, 1) == %s" % str(v1))
	print("Dimension: 2 = %d" % v1.dimension)
	print("Add: Vector((0, 3)) = %s" % repr(v1+v2))
	print("Dot Product: 1 = %s" % repr(v1*v2))
	print("Delta Notation: %s" % v2.delta_notation())
		