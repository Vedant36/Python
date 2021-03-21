from tiled import *

class Level(Plugin):
	@classmethod
	def nameFilter(cls):
		return "Level files (*.lv)"

	@classmethod
	def shortName(cls):
		return "compact"

	@classmethod
	def write(cls, tileMap, fileName):
		with open(fileName, 'w') as fileHandle:
			for i in range(tileMap.layerCount()):
				if isTileLayerAt(tileMap, i):
					tileLayer = tileLayerAt(tileMap, i)
					for y in range(tileLayer.height()):
						tiles = []
						for x in range(tileLayer.width()):
							if tileLayer.cellAt(x, y).tile() != None:
								tiles.append(str(tileLayer.cellAt(x, y).tile().id()))
							else:
								tiles.append(str(-1))
						line = ','.join(tiles)
						if y == tileLayer.height() - 1:
							line += ';'
						else:
							line += ','
						print(line, file=fileHandle)


		return True