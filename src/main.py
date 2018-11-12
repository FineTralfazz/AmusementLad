from sys import argv
from gameboy import GameBoy


gameboy = GameBoy()


def main():
	with open(argv[1]) as f:
		gameboy.loadRom(f)
	gameboy.run()


if __name__ == '__main__':
	main()
		