from mmu import MMU

class Display():
	def __init__(self, mmu):
		self._mmu = mmu


	def draw(self):
		print('Drawing!')
		self._reg_ly_set(0)
		# draw image...
		self._reg_ly_set(148)


	def _reg_ly(self):
		return self._mmu.read8(0xff44)

	def _reg_ly_set(self, value):
		return self._mmu.write8(0xff44, value)
