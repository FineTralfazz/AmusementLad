import struct


class UnimplementedInstructionException(Exception):
	pass


class CPU():
	def __init__(self, mmu, display):
		self._mmu = mmu
		self._display = display
		self._cycles = 0
		self._interrupts_enabled = True
		self._registers = {
			'A': 0x01,
			'F': 0xb0,
			'B': 0,
			'C': 0x13,
			'D': 0,
			'E': 0xd8,
			'H': 0x01,
			'L': 0x4d,
			'SP': 0xfffe,
			'PC': 0x100
		}
		self._instructions = [
			self._ins_0x0,
			self._ins_0x1,
			self._ins_0x2,
			self._ins_0x3,
			self._ins_0x4,
			self._ins_0x5,
			self._ins_0x6,
			self._ins_0x7,
			self._ins_0x8,
			self._ins_0x9,
			self._ins_0xa,
			self._ins_0xb,
			self._ins_0xc,
			self._ins_0xd,
			self._ins_0xe,
			self._ins_0xf,
			self._ins_0x10,
			self._ins_0x11,
			self._ins_0x12,
			self._ins_0x13,
			self._ins_0x14,
			self._ins_0x15,
			self._ins_0x16,
			self._ins_0x17,
			self._ins_0x18,
			self._ins_0x19,
			self._ins_0x1a,
			self._ins_0x1b,
			self._ins_0x1c,
			self._ins_0x1d,
			self._ins_0x1e,
			self._ins_0x1f,
			self._ins_0x20,
			self._ins_0x21,
			self._ins_0x22,
			self._ins_0x23,
			self._ins_0x24,
			self._ins_0x25,
			self._ins_0x26,
			self._ins_0x27,
			self._ins_0x28,
			self._ins_0x29,
			self._ins_0x2a,
			self._ins_0x2b,
			self._ins_0x2c,
			self._ins_0x2d,
			self._ins_0x2e,
			self._ins_0x2f,
			self._ins_0x30,
			self._ins_0x31,
			self._ins_0x32,
			self._ins_0x33,
			self._ins_0x34,
			self._ins_0x35,
			self._ins_0x36,
			self._ins_0x37,
			self._ins_0x38,
			self._ins_0x39,
			self._ins_0x3a,
			self._ins_0x3b,
			self._ins_0x3c,
			self._ins_0x3d,
			self._ins_0x3e,
			self._ins_0x3f,
			self._ins_0x40,
			self._ins_0x41,
			self._ins_0x42,
			self._ins_0x43,
			self._ins_0x44,
			self._ins_0x45,
			self._ins_0x46,
			self._ins_0x47,
			self._ins_0x48,
			self._ins_0x49,
			self._ins_0x4a,
			self._ins_0x4b,
			self._ins_0x4c,
			self._ins_0x4d,
			self._ins_0x4e,
			self._ins_0x4f,
			self._ins_0x50,
			self._ins_0x51,
			self._ins_0x52,
			self._ins_0x53,
			self._ins_0x54,
			self._ins_0x55,
			self._ins_0x56,
			self._ins_0x57,
			self._ins_0x58,
			self._ins_0x59,
			self._ins_0x5a,
			self._ins_0x5b,
			self._ins_0x5c,
			self._ins_0x5d,
			self._ins_0x5e,
			self._ins_0x5f,
			self._ins_0x60,
			self._ins_0x61,
			self._ins_0x62,
			self._ins_0x63,
			self._ins_0x64,
			self._ins_0x65,
			self._ins_0x66,
			self._ins_0x67,
			self._ins_0x68,
			self._ins_0x69,
			self._ins_0x6a,
			self._ins_0x6b,
			self._ins_0x6c,
			self._ins_0x6d,
			self._ins_0x6e,
			self._ins_0x6f,
			self._ins_0x70,
			self._ins_0x71,
			self._ins_0x72,
			self._ins_0x73,
			self._ins_0x74,
			self._ins_0x75,
			self._ins_0x76,
			self._ins_0x77,
			self._ins_0x78,
			self._ins_0x79,
			self._ins_0x7a,
			self._ins_0x7b,
			self._ins_0x7c,
			self._ins_0x7d,
			self._ins_0x7e,
			self._ins_0x7f,
			self._ins_0x80,
			self._ins_0x81,
			self._ins_0x82,
			self._ins_0x83,
			self._ins_0x84,
			self._ins_0x85,
			self._ins_0x86,
			self._ins_0x87,
			self._ins_0x88,
			self._ins_0x89,
			self._ins_0x8a,
			self._ins_0x8b,
			self._ins_0x8c,
			self._ins_0x8d,
			self._ins_0x8e,
			self._ins_0x8f,
			self._ins_0x90,
			self._ins_0x91,
			self._ins_0x92,
			self._ins_0x93,
			self._ins_0x94,
			self._ins_0x95,
			self._ins_0x96,
			self._ins_0x97,
			self._ins_0x98,
			self._ins_0x99,
			self._ins_0x9a,
			self._ins_0x9b,
			self._ins_0x9c,
			self._ins_0x9d,
			self._ins_0x9e,
			self._ins_0x9f,
			self._ins_0xa0,
			self._ins_0xa1,
			self._ins_0xa2,
			self._ins_0xa3,
			self._ins_0xa4,
			self._ins_0xa5,
			self._ins_0xa6,
			self._ins_0xa7,
			self._ins_0xa8,
			self._ins_0xa9,
			self._ins_0xaa,
			self._ins_0xab,
			self._ins_0xac,
			self._ins_0xad,
			self._ins_0xae,
			self._ins_0xaf,
			self._ins_0xb0,
			self._ins_0xb1,
			self._ins_0xb2,
			self._ins_0xb3,
			self._ins_0xb4,
			self._ins_0xb5,
			self._ins_0xb6,
			self._ins_0xb7,
			self._ins_0xb8,
			self._ins_0xb9,
			self._ins_0xba,
			self._ins_0xbb,
			self._ins_0xbc,
			self._ins_0xbd,
			self._ins_0xbe,
			self._ins_0xbf,
			self._ins_0xc0,
			self._ins_0xc1,
			self._ins_0xc2,
			self._ins_0xc3,
			self._ins_0xc4,
			self._ins_0xc5,
			self._ins_0xc6,
			self._ins_0xc7,
			self._ins_0xc8,
			self._ins_0xc9,
			self._ins_0xca,
			self._ins_0xcb,
			self._ins_0xcc,
			self._ins_0xcd,
			self._ins_0xce,
			self._ins_0xcf,
			self._ins_0xd0,
			self._ins_0xd1,
			self._ins_0xd2,
			self._ins_0xd3,
			self._ins_0xd4,
			self._ins_0xd5,
			self._ins_0xd6,
			self._ins_0xd7,
			self._ins_0xd8,
			self._ins_0xd9,
			self._ins_0xda,
			self._ins_0xdb,
			self._ins_0xdc,
			self._ins_0xdd,
			self._ins_0xde,
			self._ins_0xdf,
			self._ins_0xe0,
			self._ins_0xe1,
			self._ins_0xe2,
			self._ins_0xe3,
			self._ins_0xe4,
			self._ins_0xe5,
			self._ins_0xe6,
			self._ins_0xe7,
			self._ins_0xe8,
			self._ins_0xe9,
			self._ins_0xea,
			self._ins_0xeb,
			self._ins_0xec,
			self._ins_0xed,
			self._ins_0xee,
			self._ins_0xef,
			self._ins_0xf0,
			self._ins_0xf1,
			self._ins_0xf2,
			self._ins_0xf3,
			self._ins_0xf4,
			self._ins_0xf5,
			self._ins_0xf6,
			self._ins_0xf7,
			self._ins_0xf8,
			self._ins_0xf9,
			self._ins_0xfa,
			self._ins_0xfb,
			self._ins_0xfc,
			self._ins_0xfd,
			self._ins_0xfe,
			self._ins_0xff
		]

	###	
	# Register access functions
	###

	def _pc(self):
		return self._registers['PC']


	def _pc_set(self, addr):
		self._registers['PC'] = addr

	
	def _pc_inc(self):
		self._pc_set(self._pc() + 1)


	def _bc(self):
		return (self._registers['B'] << 4) + self._registers['C']


	def _bc_set(self, value):
		self._registers['B'] = value >> 4
		self._registers['C'] = value & 0xffff


	def _de(self):
		return (self._registers['D'] << 4) + self._registers['E']


	def _de_set(self, value):
		self._registers['D'] = value >> 4
		self._registers['E'] = value & 0xffff


	def _hl(self):
		return (self._registers['H'] << 4) + self._registers['L']


	def _hl_set(self, value):
		self._registers['H'] = value >> 4
		self._registers['L'] = value & 0xffff


	def _flag(self, flag):
		value = self._registers['F']
		if flag == 'Z':
			return (value & 128) != 0
		elif flag == 'N':
			return (value & 64) != 0
		elif flag == 'H':
			return (value & 32) != 0
		elif flag == 'C':
			return (value & 32) != 0

	
	def _flag_set(self, flag, set_1):
		if set_1:
			if flag == 'Z':
				self._registers['F'] = self._registers['F'] | 128
			elif flag == 'N':
				self._registers['F'] = self._registers['F'] | 64
			elif flag == 'H':
				self._registers['F'] = self._registers['F'] | 32
			elif flag == 'C':
				self._registers['F'] = self._registers['F'] | 16
		else:
			if flag == 'Z':
				self._registers['F'] = self._registers['F'] & 127
			elif flag == 'N':
				self._registers['F'] = self._registers['F'] & 191
			elif flag == 'H':
				self._registers['F'] = self._registers['F'] & 223
			elif flag == 'C':
				self._registers['F'] = self._registers['F'] & 239


	def _pop_ins_8(self):
		result = self._mmu.read8(self._pc())
		self._pc_inc()
		return result


	def _pop_ins_8_signed(self):
		result = self._mmu.read8_signed(self._pc())
		self._pc_inc()
		return result


	def _pop_ins_16(self):
		result = self._mmu.read16(self._pc())
		self._pc_inc()
		self._pc_inc()
		return result


	def tick(self):
		addr = self._pc()
		instruction = self._pop_ins_8()
		print('Executing ' + hex(instruction) + ' @ ' + hex(addr))
		try:
			self._instructions[instruction]()
			if self._cycles > 70150:
				self._display.draw()
				self._cycles = 0
		except UnimplementedInstructionException:
			print('Unimplemented instruction ' + hex(instruction))
			exit()


	###
	# Meta instructions called by others
	###

	def _meta_push(self, value):
		self._registers['SP'] -= 1
		self._mmu.write8(self._registers['SP'], value)


	def _meta_pop(self):
		value = self._mmu.read8(self._registers['SP'])
		self._registers['SP'] += 1
		return valueS


	def _meta_rst(self, offset):
		self._cycles += 32
		part1 = self._registers['SP'] >> 8
		part2 = self._registers['SP'] & 0xff
		self._meta_push(part1)
		self._meta_push(part2)
		self._registers['PC'] = offset


	def _meta_dec(self, register):
		if self._registers[register] == 0:
			self._registers[register] = 0xff
		else:
			self._registers[register] -= 1
		self._flag_set('Z', self._registers[register] == 0)
		self._flag_set('N', True)


	def _meta_dec16(self, getter, setter):
		if getter() == 0:
			setter(0xffff)
		else:
			setter(getter() - 1)
		self._flag_set('Z', getter() == 0)
		self._flag_set('N', True)


	def _meta_inc(self, register):
		if self._registers[register] == 0xff:
			self._registers[register] = 0
		else:
			self._registers[register] += 1
		self._flag_set('Z', self._registers[register] == 0)
		self._flag_set('N', True)


	def _meta_call(self, addr):
		part1 = self._registers['SP'] >> 8
		part2 = self._registers['SP'] & 0xff
		self._meta_push(part1)
		self._meta_push(part2)
		self._registers['PC'] = addr


	def _meta_ld_r_r(self, dst, src):
		self._registers[dst] = self._registers[src]


	def _meta_or(self, dst, src):
		self._registers[dst] = self._registers[dst] | self._registers[src]
		# print(self._registers[dst])
		self._flag_set('Z', self._registers[dst] == 0)
		self._flag_set('N', False)
		self._flag_set('H', False)
		self._flag_set('C', False)

	###
	# Instruction handlers
	###

	def _ins_0x0(self):
		self._cycles += 4
		pass


	# LD BC, d16
	def _ins_0x1(self):
		self._cycles += 12
		self._bc_set(self._pop_ins_16())


	def _ins_0x2(self):
		raise UnimplementedInstructionException


	# INC BC
	def _ins_0x3(self):
		self._cycles += 8
		self._bc_set(self._bc() + 1)


	def _ins_0x4(self):
		raise UnimplementedInstructionException


	# DEC B
	def _ins_0x5(self):
		self._cycles += 4
		self._meta_dec('B')
		

	# LD B, d8
	def _ins_0x6(self):
		self._cycles += 8
		self._registers['B'] = self._pop_ins_8()

	def _ins_0x7(self):
		raise UnimplementedInstructionException

	def _ins_0x8(self):
		raise UnimplementedInstructionException

	def _ins_0x9(self):
		raise UnimplementedInstructionException

	def _ins_0xa(self):
		raise UnimplementedInstructionException


	# DEC BC
	def _ins_0xb(self):
		self._cycles += 8
		self._meta_dec16(self._bc, self._bc_set)


	# INC C
	def _ins_0xc(self):
		self._cycles += 4
		self._meta_inc('C')


	# DEC C
	def _ins_0xd(self):
		self._cycles += 4
		self._meta_dec('C')
		print('C', self._registers['C'])


	# LD C, d8
	def _ins_0xe(self):
		self._cycles += 8
		self._registers['C'] = self._pop_ins_8()


	# RRCA
	def _ins_0xf(self):
		dropped_bit = ((self._registers['A'] << 7) & 0xff) >> 7
		self._registers['A'] == self._registers['A'] >> 1
		self._flag_set('Z', self._registers['A'] == 0)
		self._flag_set('N', False)
		self._flag_set('H', False)
		self._flag_set('C', dropped_bit == 1)


	# STOP 0
	def _ins_0x10(self):
		raise UnimplementedInstructionException


	# LD DE, d16
	def _ins_0x11(self):
		self._cycles += 12
		self._DE_set(self._pop_ins_16())


	def _ins_0x12(self):
		raise UnimplementedInstructionException


	# INC DE
	def _ins_0x13(self):
		self._cycles += 8
		self._de_set(self._de() + 1)


	# INC D
	def _ins_0x14(self):
		self._cycles += 4
		self._registers['D'] += 1
		self._flag_set('Z', self._registers['D'] == 0)
		self._flag_set('N', False)


	# DEC D
	def _ins_0x15(self):
		self._cycles += 4
		self._registers['D'] -= 1
		self._flag_set('Z', self._registers['D'] == 0)
		self._flag_set('N', True)


	def _ins_0x16(self):
		raise UnimplementedInstructionException

	def _ins_0x17(self):
		raise UnimplementedInstructionException

	def _ins_0x18(self):
		raise UnimplementedInstructionException

	def _ins_0x19(self):
		raise UnimplementedInstructionException

	def _ins_0x1a(self):
		raise UnimplementedInstructionException

	def _ins_0x1b(self):
		raise UnimplementedInstructionException

	def _ins_0x1c(self):
		raise UnimplementedInstructionException


	# DEC E
	def _ins_0x1d(self):
		self._cycles += 4
		self._registers['E'] -= 1
		self._flag_set('Z', self._registers['E'] == 0)
		self._flag_set('N', True)


	# LD E, d8
	def _ins_0x1e(self):
		self._cycles += 8
		self._registers['E'] = self._pop_ins_8()


	# RRA
	# I don't understand how this is different from RRCA...
	def _ins_0x1f(self):
		dropped_bit = ((self._registers['A'] << 7) & 0xff) >> 7
		self._registers['A'] == self._registers['A'] >> 1
		self._flag_set('Z', self._registers['A'] == 0)
		self._flag_set('N', False)
		self._flag_set('H', False)
		self._flag_set('C', dropped_bit == 1)


	# JR NZ, r8
	def _ins_0x20(self):
		self._cycles += 8 # Some docs say it could also be 12? Hmm
		addr = self._pc() + self._pop_ins_8_signed() + 1
		if not self._flag('Z'):
			self._pc_set(addr)


	# LD HL, d16
	def _ins_0x21(self):
		self._cycles += 12
		self._hl_set(self._pop_ins_16())


	def _ins_0x22(self):
		raise UnimplementedInstructionException


	# INC HL
	def _ins_0x23(self):
		self._cycles += 8
		self._hl_set(self._hl() + 1)


	def _ins_0x24(self):
		raise UnimplementedInstructionException


	# DEC H
	def _ins_0x25(self):
		self._cycles += 4
		self._registers['H'] -= 1
		self._flag_set('Z', self._registers['H'] == 0)
		self._flag_set('N', True)


	def _ins_0x26(self):
		raise UnimplementedInstructionException

	def _ins_0x27(self):
		raise UnimplementedInstructionException

	def _ins_0x28(self):
		raise UnimplementedInstructionException

	def _ins_0x29(self):
		raise UnimplementedInstructionException


	# LD A, (HL+)
	def _ins_0x2a(self):
		self._cycles += 8
		addr = self._hl()
		self._registers['A'] = self._mmu.read8(addr)
		self._hl_set(self._hl() + 1)


	def _ins_0x2b(self):
		raise UnimplementedInstructionException

	def _ins_0x2c(self):
		raise UnimplementedInstructionException


	# DEC L
	def _ins_0x2d(self):
		self._cycles += 4
		self._registers['L'] -= 1
		self._flag_set('Z', self._registers['L'] == 0)
		self._flag_set('N', True)


	# LD L, d8
	def _ins_0x2e(self):
		self._cycles += 8
		self._registers['L'] = self._pop_ins_8()


	def _ins_0x2f(self):
		raise UnimplementedInstructionException

	def _ins_0x30(self):
		raise UnimplementedInstructionException


	# LD SP, d16
	def _ins_0x31(self):
		self._cycles += 12
		self._registers['SP'] = self._pop_ins_16()


	# LD (HL-), A (and some other mnemonics for some reason?)
	def _ins_0x32(self):
		self._cycles += 8
		addr = self._hl()
		value = self._registers['A']
		self._mmu.write8(addr, value)


	# INC SP
	def _ins_0x33(self):
		self._cycles += 8
		self._sp_set(self._sp() + 1)


	def _ins_0x34(self):
		raise UnimplementedInstructionException

	def _ins_0x35(self):
		raise UnimplementedInstructionException


	# LD (HL), d8
	def _ins_0x36(self):
		self._cycles += 12
		self._mmu.write8(self._hl(), self._pop_ins_8())


	def _ins_0x37(self):
		raise UnimplementedInstructionException

	def _ins_0x38(self):
		raise UnimplementedInstructionException

	def _ins_0x39(self):
		raise UnimplementedInstructionException

	def _ins_0x3a(self):
		raise UnimplementedInstructionException

	def _ins_0x3b(self):
		raise UnimplementedInstructionException

	def _ins_0x3c(self):
		raise UnimplementedInstructionException


	# DEC A
	def _ins_0x3d(self):
		self._cycles += 4
		self._registers['A'] -= 1
		self._flag_set('Z', self._registers['A'] == 0)
		self._flag_set('N', True)


	# LD A, d8
	def _ins_0x3e(self):
		self._cycles += 8
		self._registers['A'] = self._pop_ins_8()


	def _ins_0x3f(self):
		raise UnimplementedInstructionException


	# LD B, B
	def _ins_0x40(self):
		self._cycles += 4


	def _ins_0x41(self):
		raise UnimplementedInstructionException

	def _ins_0x42(self):
		raise UnimplementedInstructionException

	def _ins_0x43(self):
		raise UnimplementedInstructionException

	def _ins_0x44(self):
		raise UnimplementedInstructionException

	def _ins_0x45(self):
		raise UnimplementedInstructionException

	def _ins_0x46(self):
		raise UnimplementedInstructionException

	def _ins_0x47(self):
		raise UnimplementedInstructionException

	def _ins_0x48(self):
		raise UnimplementedInstructionException

	def _ins_0x49(self):
		raise UnimplementedInstructionException

	def _ins_0x4a(self):
		raise UnimplementedInstructionException

	def _ins_0x4b(self):
		raise UnimplementedInstructionException

	def _ins_0x4c(self):
		raise UnimplementedInstructionException

	def _ins_0x4d(self):
		raise UnimplementedInstructionException

	def _ins_0x4e(self):
		raise UnimplementedInstructionException

	def _ins_0x4f(self):
		raise UnimplementedInstructionException

	def _ins_0x50(self):
		raise UnimplementedInstructionException

	def _ins_0x51(self):
		raise UnimplementedInstructionException

	def _ins_0x52(self):
		raise UnimplementedInstructionException

	def _ins_0x53(self):
		raise UnimplementedInstructionException

	def _ins_0x54(self):
		raise UnimplementedInstructionException

	def _ins_0x55(self):
		raise UnimplementedInstructionException

	def _ins_0x56(self):
		raise UnimplementedInstructionException

	def _ins_0x57(self):
		raise UnimplementedInstructionException

	def _ins_0x58(self):
		raise UnimplementedInstructionException

	def _ins_0x59(self):
		raise UnimplementedInstructionException

	def _ins_0x5a(self):
		raise UnimplementedInstructionException

	def _ins_0x5b(self):
		raise UnimplementedInstructionException

	def _ins_0x5c(self):
		raise UnimplementedInstructionException

	def _ins_0x5d(self):
		raise UnimplementedInstructionException

	def _ins_0x5e(self):
		raise UnimplementedInstructionException

	def _ins_0x5f(self):
		raise UnimplementedInstructionException

	def _ins_0x60(self):
		raise UnimplementedInstructionException

	def _ins_0x61(self):
		raise UnimplementedInstructionException

	def _ins_0x62(self):
		raise UnimplementedInstructionException

	def _ins_0x63(self):
		raise UnimplementedInstructionException

	def _ins_0x64(self):
		raise UnimplementedInstructionException

	def _ins_0x65(self):
		raise UnimplementedInstructionException

	def _ins_0x66(self):
		raise UnimplementedInstructionException

	def _ins_0x67(self):
		raise UnimplementedInstructionException

	def _ins_0x68(self):
		raise UnimplementedInstructionException

	def _ins_0x69(self):
		raise UnimplementedInstructionException

	def _ins_0x6a(self):
		raise UnimplementedInstructionException

	def _ins_0x6b(self):
		raise UnimplementedInstructionException

	def _ins_0x6c(self):
		raise UnimplementedInstructionException

	def _ins_0x6d(self):
		raise UnimplementedInstructionException

	def _ins_0x6e(self):
		raise UnimplementedInstructionException

	def _ins_0x6f(self):
		raise UnimplementedInstructionException

	def _ins_0x70(self):
		raise UnimplementedInstructionException


	# LD (HL), C
	def _ins_0x71(self):
		self._cycles += 8
		addr = self._hl()
		value = self._registers['C']
		self._mmu.write8(addr, value)
		

	def _ins_0x72(self):
		raise UnimplementedInstructionException

	def _ins_0x73(self):
		raise UnimplementedInstructionException

	def _ins_0x74(self):
		raise UnimplementedInstructionException

	def _ins_0x75(self):
		raise UnimplementedInstructionException

	def _ins_0x76(self):
		raise UnimplementedInstructionException

	def _ins_0x77(self):
		raise UnimplementedInstructionException


	# LD A, B
	def _ins_0x78(self):
		self._meta_ld_r_r('A', 'B')


	def _ins_0x79(self):
		raise UnimplementedInstructionException

	def _ins_0x7a(self):
		self._cycles += 4
		self._registers['A'] = self._registers['D']

	def _ins_0x7b(self):
		raise UnimplementedInstructionException

	def _ins_0x7c(self):
		raise UnimplementedInstructionException

	def _ins_0x7d(self):
		raise UnimplementedInstructionException

	def _ins_0x7e(self):
		raise UnimplementedInstructionException

	def _ins_0x7f(self):
		raise UnimplementedInstructionException

	def _ins_0x80(self):
		raise UnimplementedInstructionException

	def _ins_0x81(self):
		raise UnimplementedInstructionException

	def _ins_0x82(self):
		raise UnimplementedInstructionException

	def _ins_0x83(self):
		raise UnimplementedInstructionException

	def _ins_0x84(self):
		raise UnimplementedInstructionException

	def _ins_0x85(self):
		raise UnimplementedInstructionException

	def _ins_0x86(self):
		raise UnimplementedInstructionException

	def _ins_0x87(self):
		raise UnimplementedInstructionException

	def _ins_0x88(self):
		raise UnimplementedInstructionException


	# ADC A, C
	def _ins_0x89(self):
		self._cycles += 4
		self._registers['A'] += self._registers['C']
		self._flag_set('Z', self._registers['A'] == 0)
		self._flag_set('N', False)
		# TODO carry flags...


	def _ins_0x8a(self):
		raise UnimplementedInstructionException

	def _ins_0x8b(self):
		raise UnimplementedInstructionException

	def _ins_0x8c(self):
		raise UnimplementedInstructionException

	def _ins_0x8d(self):
		raise UnimplementedInstructionException

	def _ins_0x8e(self):
		raise UnimplementedInstructionException

	def _ins_0x8f(self):
		raise UnimplementedInstructionException

	def _ins_0x90(self):
		raise UnimplementedInstructionException

	def _ins_0x91(self):
		raise UnimplementedInstructionException

	def _ins_0x92(self):
		raise UnimplementedInstructionException

	def _ins_0x93(self):
		raise UnimplementedInstructionException


	# SUB H
	def _ins_0x94(self):
		self._cycles += 4
		self._registers['A'] -= self._registers['H']
		self._flag_set('Z', self._registers['A'] == 0)
		self._flag_set('N', True)
		# TODO set other flags

	def _ins_0x95(self):
		raise UnimplementedInstructionException

	def _ins_0x96(self):
		raise UnimplementedInstructionException

	def _ins_0x97(self):
		raise UnimplementedInstructionException

	def _ins_0x98(self):
		raise UnimplementedInstructionException

	def _ins_0x99(self):
		raise UnimplementedInstructionException

	def _ins_0x9a(self):
		raise UnimplementedInstructionException

	def _ins_0x9b(self):
		raise UnimplementedInstructionException

	def _ins_0x9c(self):
		raise UnimplementedInstructionException

	def _ins_0x9d(self):
		raise UnimplementedInstructionException

	def _ins_0x9e(self):
		raise UnimplementedInstructionException

	def _ins_0x9f(self):
		raise UnimplementedInstructionException

	def _ins_0xa0(self):
		raise UnimplementedInstructionException

	def _ins_0xa1(self):
		raise UnimplementedInstructionException

	def _ins_0xa2(self):
		raise UnimplementedInstructionException

	def _ins_0xa3(self):
		raise UnimplementedInstructionException

	def _ins_0xa4(self):
		raise UnimplementedInstructionException

	def _ins_0xa5(self):
		raise UnimplementedInstructionException

	def _ins_0xa6(self):
		raise UnimplementedInstructionException

	def _ins_0xa7(self):
		raise UnimplementedInstructionException

	def _ins_0xa8(self):
		raise UnimplementedInstructionException

	def _ins_0xa9(self):
		raise UnimplementedInstructionException

	def _ins_0xaa(self):
		raise UnimplementedInstructionException

	def _ins_0xab(self):
		raise UnimplementedInstructionException

	def _ins_0xac(self):
		raise UnimplementedInstructionException

	def _ins_0xad(self):
		raise UnimplementedInstructionException

	def _ins_0xae(self):
		raise UnimplementedInstructionException

	def _ins_0xaf(self):
		self._cycles += 4
		self._registers['A'] = 0

	def _ins_0xb0(self):
		raise UnimplementedInstructionException


	# OR C
	def _ins_0xb1(self):
		self._cycles += 4
		self._meta_or('A', 'C')


	def _ins_0xb2(self):
		raise UnimplementedInstructionException

	def _ins_0xb3(self):
		raise UnimplementedInstructionException

	def _ins_0xb4(self):
		raise UnimplementedInstructionException

	def _ins_0xb5(self):
		raise UnimplementedInstructionException

	def _ins_0xb6(self):
		raise UnimplementedInstructionException

	def _ins_0xb7(self):
		raise UnimplementedInstructionException

	def _ins_0xb8(self):
		raise UnimplementedInstructionException

	def _ins_0xb9(self):
		raise UnimplementedInstructionException

	def _ins_0xba(self):
		raise UnimplementedInstructionException

	def _ins_0xbb(self):
		raise UnimplementedInstructionException

	def _ins_0xbc(self):
		raise UnimplementedInstructionException

	def _ins_0xbd(self):
		raise UnimplementedInstructionException

	def _ins_0xbe(self):
		raise UnimplementedInstructionException

	def _ins_0xbf(self):
		raise UnimplementedInstructionException

	def _ins_0xc0(self):
		raise UnimplementedInstructionException

	def _ins_0xc1(self):
		raise UnimplementedInstructionException

	def _ins_0xc2(self):
		raise UnimplementedInstructionException

	def _ins_0xc3(self):
		self._cycles += 16
		addr = self._pop_ins_16()
		self._pc_set(addr)

	def _ins_0xc4(self):
		raise UnimplementedInstructionException

	def _ins_0xc5(self):
		raise UnimplementedInstructionException

	def _ins_0xc6(self):
		raise UnimplementedInstructionException

	def _ins_0xc7(self):
		raise UnimplementedInstructionException

	def _ins_0xc8(self):
		raise UnimplementedInstructionException


	def _ins_0xc9(self):
		raise UnimplementedInstructionException


	def _ins_0xca(self):
		raise UnimplementedInstructionException

	def _ins_0xcb(self):
		raise UnimplementedInstructionException

	def _ins_0xcc(self):
		raise UnimplementedInstructionException


	# CALL a16
	def _ins_0xcd(self):
		self._cycles += 24 # 12?
		self._meta_call(self._pop_ins_16())


	def _ins_0xce(self):
		raise UnimplementedInstructionException

	def _ins_0xcf(self):
		raise UnimplementedInstructionException

	def _ins_0xd0(self):
		raise UnimplementedInstructionException

	def _ins_0xd1(self):
		raise UnimplementedInstructionException

	def _ins_0xd2(self):
		raise UnimplementedInstructionException

	def _ins_0xd3(self):
		raise UnimplementedInstructionException

	def _ins_0xd4(self):
		raise UnimplementedInstructionException

	def _ins_0xd5(self):
		raise UnimplementedInstructionException

	def _ins_0xd6(self):
		raise UnimplementedInstructionException

	def _ins_0xd7(self):
		raise UnimplementedInstructionException

	def _ins_0xd8(self):
		raise UnimplementedInstructionException

	def _ins_0xd9(self):
		raise UnimplementedInstructionException

	def _ins_0xda(self):
		raise UnimplementedInstructionException

	def _ins_0xdb(self):
		raise UnimplementedInstructionException

	def _ins_0xdc(self):
		raise UnimplementedInstructionException

	def _ins_0xdd(self):
		raise UnimplementedInstructionException

	def _ins_0xde(self):
		raise UnimplementedInstructionException


	# RST 18H
	def _ins_0xdf(self):
		self._meta_rst(0x18)


	# LDH (a8), A
	def _ins_0xe0(self):
		self._cycles += 12
		addr = 0xff00 + self._pop_ins_8()
		print(self._registers['A'])
		self._mmu.write8(addr, self._registers['A'])


	def _ins_0xe1(self):
		raise UnimplementedInstructionException


	# LD (C), A
	def _ins_0xe2(self):
		self._cycles += 8
		self._mmu.write8(self._registers['C'], self._registers['A'])


	def _ins_0xe3(self):
		raise UnimplementedInstructionException

	def _ins_0xe4(self):
		raise UnimplementedInstructionException

	def _ins_0xe5(self):
		raise UnimplementedInstructionException

	def _ins_0xe6(self):
		raise UnimplementedInstructionException

	def _ins_0xe7(self):
		raise UnimplementedInstructionException

	def _ins_0xe8(self):
		raise UnimplementedInstructionException

	def _ins_0xe9(self):
		raise UnimplementedInstructionException


	# LD (a16), A
	def _ins_0xea(self):
		self._cycles += 16
		self._mmu.write8(self._pop_ins_16(), self._registers['A'])


	def _ins_0xeb(self):
		raise UnimplementedInstructionException

	def _ins_0xec(self):
		raise UnimplementedInstructionException

	def _ins_0xed(self):
		raise UnimplementedInstructionException

	def _ins_0xee(self):
		raise UnimplementedInstructionException

	def _ins_0xef(self):
		raise UnimplementedInstructionException


	# LDH A, (a8)
	def _ins_0xf0(self):
		addr = 0xff00 + self._pop_ins_8()
		self._registers['A'] = self._mmu.read8(addr)


	def _ins_0xf1(self):
		raise UnimplementedInstructionException

	def _ins_0xf2(self):
		raise UnimplementedInstructionException


	# DI
	def _ins_0xf3(self):
		self._cycles += 4
		self._interrupts_enabled = False


	def _ins_0xf4(self):
		raise UnimplementedInstructionException

	def _ins_0xf5(self):
		raise UnimplementedInstructionException

	def _ins_0xf6(self):
		raise UnimplementedInstructionException

	def _ins_0xf7(self):
		raise UnimplementedInstructionException

	def _ins_0xf8(self):
		raise UnimplementedInstructionException

	def _ins_0xf9(self):
		raise UnimplementedInstructionException

	def _ins_0xfa(self):
		raise UnimplementedInstructionException

	def _ins_0xfb(self):
		raise UnimplementedInstructionException

	def _ins_0xfc(self):
		raise UnimplementedInstructionException

	def _ins_0xfd(self):
		raise UnimplementedInstructionException

	# CP d8
	def _ins_0xfe(self):
		self._cycles += 8
		reg_a = self._registers['A']
		arg = self._pop_ins_8()
		self._flag_set('Z', reg_a == arg)
		self._flag_set('N', True)
		# TODO figure out what H is
		self._flag_set('C', reg_a < arg)


	# RST 38H
	def _ins_0xff(self):
		raise UnimplementedInstructionException
		self._meta_rst(0x38)