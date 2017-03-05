class Polytope:
	"""A vertex representation of a compact intersection of half spaces.
	
	Args:
		vertices - non-empty tuple of Vectors of homogeneous dimension
	"""
	
	def __init__(self, vertices):	
		self.vertices = vertices
	
	def __repr__(self):
		return "Polytope(%s)" % repr(self.vertices)
	
	def __str__(self):
		return "conv(%s)" % ", ".join(str(v) for v in self.vertices)
	
	@property
	def dimension(self):
		"""Return dimension of ambient space."""
		
		return self.vertices[0].dimension
	
	def width(self, direction):
		"""Return the width of the polytope in the direction given.
		
		Args:
			direction - a Vector instance
		"""
		
		values = [direction * v for v in self.vertices]
		return max(values) - min(values)

if __name__ == '__main__':
	from vector import Vector
	
	v1 = Vector((1, 1))
	v2 = Vector((-1, 2))
	v3 = Vector((0, 0))
	v4 = Vector((1, 0))
	
	P = Polytope((v1, v2, v3, v4))
	print("Initialize and Represent: Polytope((Vector((1, 1)), Vector((-1, 2)), Vector((0, 0)), Vector((1, 0)))) = ")
	print("                          %s" % repr(P))
	print("String: conv((1, 1), (-1, 2), (0, 0), (1, 0)) = %s" % str(P))
	print("Width: 2 = %d" % P.width(Vector((1,1))))
	