import struct

class MMU():
	def __init__(self):
		self._ram = bytearray(0xf0000)


	def loadRom(self, romFile):
		print('Loading ROM...')
		addr = 0
		byte = romFile.read(1)
		while byte:
			self._ram[addr] = byte
			addr += 1
			byte = romFile.read(1)
		print('Read ' + str(addr) + ' bytes')


	def read8(self, addr):
		return self._ram[addr]


	def read8_signed(self, addr):
		value = self._ram[addr]
		if value > 127:
			value -= 256
		return value


	def read16(self, addr):
		return struct.unpack('<H', self._ram[addr:addr+2])[0]


	def write8(self, addr, value):
		self._ram[addr] = value