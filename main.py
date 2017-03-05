from itertools import product

from vector import Vector
from polytope import Polytope

class Examples:
	"""Generate polytopes inside a cube with a specified number of vertices."""
	
	def __init__(self, cube, vertex_count):
		self.cube = cube
		self.vertex_count = vertex_count
	
	def __iter__(self):
		for polytope in product(*([self.cube]*self.vertex_count)):
			yield Polytope(tuple(polytope))

class Admissibility:
	"""A callable object that tests whether a polytope is "admissible"."""
	
	def __init__(self, dimension, magnitude, threshold):
		ranges = [range(-magnitude, magnitude)]*(dimension-1)
		self.no_improvement_vectors = [Vector(coords + (1,)) for coords in product(*ranges)]
		
		ranges.append(range(2, magnitude))
		self.improvement_vectors = [Vector(coords) for coords in product(*ranges)]
	
		self.threshold = threshold
		
	def __call__(self, polytope):
		for v in self.no_improvement_vectors:
			if polytope.width(v) < self.threshold:
				return False
		
		for v in self.improvement_vectors:
			if polytope.width(v) < self.threshold:
				return True
		
		return False
			
if __name__ == '__main__':
	from cube import Cube
	
	dimension = 4
	threshold = 3  # aka "l"
	magnitude = 10
	vertex_count = 5
	
	cube = Cube(dimension, threshold)
	examples = Examples(cube, vertex_count)
	
	is_admissible = Admissibility(dimension, magnitude, threshold)
	
	
	for polytope in examples:
		if is_admissible(polytope):
			print(str(polytope))
	