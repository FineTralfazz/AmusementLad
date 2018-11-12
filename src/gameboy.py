from time import time
from mmu import MMU
from cpu import CPU
from display import Display

class GameBoy():
	def __init__(self):
		self._mmu = MMU()
		self._display = Display(self._mmu)
		self._cpu = CPU(self._mmu, self._display)


	def loadRom(self, romFile):
		self._mmu.loadRom(romFile)


	def run(self):
		print('Running...')
		start_time = time()
		instruction_count = 0

		try:
			while True:
				self._cpu.tick()
				instruction_count += 1
		except KeyboardInterrupt:
			exec_time = time() - start_time
			print('\nExecuted ' + str(instruction_count) + ' instructions in ' + str(exec_time) + ' seconds')
			instructions_per_second = instruction_count / exec_time
			print('(' + str(instructions_per_second) + '/sec)')
		