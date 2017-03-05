from vector import Vector

class Cube:
	"""Provides iteration over vectors in a d-dimensional cuboid with a given side length.
	
	Args:
		dimension - dimension of ambient space
		side_length - length of one side
	"""
	
	def __init__(self, dimension, side_length):
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
					
if __name__ == '__main__':
	c = Cube(2, 5)
	
	for p in zip(c,c):
		print(p)