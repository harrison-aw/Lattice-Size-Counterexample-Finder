class DimensionError(Exception):
	def __init__(self, expected, found):
		self.expected = expected
		self.found = found
	
	def __repr__(self):
		return "Expected object of dimension %d, but found object of dimension %d" % (self.expected, self.found)
		

class Vector(object):
	def __init__(self, coordinates):
		"""Initialize object attributes.
		
		Vectors are treated as immutable objects with certain operations
		defined.
		
		Args:
			coordinates - a tuple of numbers
		"""
		
		object.__init__(self)
		
		self.coordinates = coordinates
		
	def __repr__(self):
		return "Vector(%s)" % repr(self.coordinates)
		
	def __str__(self):
		return repr(self.coordinates)
	
	def __add__(self, other):
		"""Return the sum of two vectors."""
	
		if self.dimension() == other.dimension():
			return Vector(tuple(x + y for x, y in zip(self.coordinates, other.coordinates)))
		else:
			raise DimensionError(self.dimension(), other.dimension())
	
	def __mul__(self, other):
		"""Return the dot product of two vectors."""
		
		if self.dimension() == other.dimension():
			return sum(x * y for x, y in zip(self.coordinates, other.coordinates))
		else:
			raise DimensionError(self.dimension(), other.dimension())
		
	def dimension(self):
		return len(self.coordinates)
	
	def __eq__(self, other):
		return self.coordinates == other.coordinates
	
	def __ne__(self, other):
		return self.coordinates != other.coordinates

class Polytope(object):
	def __init__(self, vertices):
		"""Initialize polytope.
		
		Args:
			vertices - non-empty tuple of Vectors of homogeneous dimension
		"""
		object.__init__(self)
		
		self.vertices = tuple(vertices)
	
	def __repr__(self):
		return "Polytope(%s)" % repr(self.vertices)
	
	def __str__(self):
		return "conv(%s)" % ", ".join(str(v) for v in self.vertices)
	
	def width(self, direction):
		"""Return the width of the polytope in the direction given."""
		
		values = [direction * v for v in self.vertices]
		return max(values) - min(values)
	
	def dimension(self):
		return self.vertices[0].dimension()

class Cube(object):
	def __init__(self, dimension, side_length):
		object.__init__(self)
		
		self.dimension = dimension
		self.side_length = side_length
	
	def __iter__(self):
		d = self.dimension
		l = self.side_length
		
		max_sum = d*l
		
		point = [0] * d
		
		while True:
			yield Vector(tuple(point))
			
			if sum(point) == max_sum:
				break
			
			for i in range(d):
				if point[i] < l:
					point[i] += 1
					break
				else:
					point[i] = 0

class Examples(object):

	w_dir = Vector((0,0,0,1))

	test_directions = (
		(1,1,1,1), (1,1,1,-1), (1,1,-1,1), (1,1,-1,-1), (1,-1,1,1), (1,-1,1,-1), (1,-1,-1,1), (1,-1,-1,-1), 
		
		(1,1,0,1), (1,1,0,-1), (1,-1,0,1), (1,-1,0,-1),
		(1,0,1,1), (1,0,1,-1), (1,0,-1,1), (1,0,-1,-1),
		(0,1,1,1), (0,1,1,-1), (0,1,-1,1), (0,1,-1,-1),
		
		(1,0,0,1), (1,0,0,-1),
		(0,1,0,1), (0,1,0,-1),
		(0,0,1,1), (0,0,1,-1)
	)
	
	test_vectors = ()
	extended_test_vectors = ()
	good_vectors = ()

	def __init__(self, side_length):
		object.__init__(self)
		
		self.l = side_length
		self.cube = Cube(4, side_length)
		
		if Examples.test_vectors == ():
			Examples.test_vectors = tuple(Vector(d) for d in Examples.test_directions)
		
		if Examples.extended_test_vectors == ():
			directions = []
			for a in range(-10, 10):
				for b in range(-10,10):
					for c in range(-10,10):
						directions.append(Vector((a,b,c,1)))
			Examples.extended_test_vectors = tuple(directions)
		
		if Examples.good_vectors == ():
			directions = []
			for a in range(-10, 10):
				for b in range(-10,10):
					for c in range(-10,10):
						for d in range(2,5):
							directions.append(Vector((a,b,c,d)))
			Examples.good_vectors = tuple(directions)
	
	def is_admissible(self, P, l):				
		if P.width(Examples.w_dir) != l:
			return False
		
		for v in Examples.extended_test_vectors:
			if P.width(v) < l:
				return False
		
		for v in Examples.good_vectors:
			if P.width(v) < l:
				return True
		
		return False
	
	def print_admissibility(self, P, l):
		if P.width(Examples.w_dir) != l:
			print(Examples.delta_string(Examples.w_dir) + " < " + str(l))
			return False
		
		for v in Examples.extended_test_vectors:
			if P.width(v) < l:
				print(Examples.delta_string(v) + " < " + str(l))
				return False
		
		admissible = False
		for v in Examples.good_vectors:
			if P.width(v) < l:
				print(Examples.delta_string(v) + " < " + str(l))
				admissible = True
		
		return admissible
	
	@staticmethod
	def delta_string(vector):
		if vector.dimension() == 4:
			return "Delta(%sx + %sy + %sz + %sw)" % tuple(str(coord) for coord in vector.coordinates)
		else:
			return ""
	
	def __iter__(self):
		w_dir = Examples.w_dir
		l = self.l
		
		for v1 in self.cube:
			for v2 in self.cube:
				for v3 in self.cube:
					for v4 in self.cube:
						if v1 == v2 or v1 == v3 or v1 == v4 or v2 == v3 or v2 == v4 or v3 == v4:
							continue
							
						P = Polytope((v1,v2,v3,v4))
						
						if P.width(w_dir) == l and self.is_admissible(P, l):
							yield P
								
		
		
		

def Test():
	print("Vector Test:")
	v1 = Vector((1, 1))
	v2 = Vector((-1, 2))
	v3 = Vector((0, 0))
	v4 = Vector((1, 0))
	print("Initialize and Represent: Vector((1, 1)) = %s" % repr(v1))
	print("String: (1, 1) == %s" % str(v1))
	print("Dimension: 2 = %d" % v1.dimension())
	print("Add: Vector((0, 3)) = %s" % repr(v1+v2))
	print("Dot Product: 1 = %s" % repr(v1*v2))
		
	print()
	
	print("Polytope Test:")
	P = Polytope((v1, v2, v3, v4))
	print("Initialize and Represent: Polytope((Vector((1, 1)), Vector((-1, 2)), Vector((0, 0)), Vector((1, 0)))) = ")
	print("                          %s" % repr(P))
	print("String: conv((1, 1), (-1, 2), (0, 0), (1, 0)) = %s" % str(P))
	print("Width: 2 = %d" % P.width(Vector((1,1))))
	
	print()
	
	c = Cube(2, 2)
	for p in c:
		print(p)

if __name__ == '__main__':
	import sys
	
	Ex = Examples(3)
	
	# P = Polytope((Vector((0,0,0,0)), Vector((3,0,2,0)), Vector((3,3,0,3)), Vector((0,3,2,0))))
	# P = Polytope((Vector((0,0,0,0)), Vector((3,3,0,0)), Vector((0,3,3,3)), Vector((3,0,3,0))))
	P = Polytope((Vector((0,0,0,0)), Vector((3,3,0,0)), Vector((3,0,2,3)), Vector((0,3,3,1))))
	Ex.print_admissibility(P, 3)
	
	# if len(sys.argv) > 1:
		# if sys.argv[1] == "test":
			# Test()
		# else:
			# print("Unknown arguments: %s " % " ".join(sys.argv[1:]))
	# else:
		# Ex = Examples(3)
		# for P in Ex:
			# print(P)
		
			
			
			