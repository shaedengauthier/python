from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
def init():
	mc = Minecraft.create("10.183.4.122", 4711)
	x, y, z = mc.player.getPos()
	return mc
	
def main():
	mc = init()
	mc.player.setPos(0, -53, -20)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x+4, y+3, z+2, x-4, y-9, z-2, 246)
	mc.setBlocks(x+5, y+3, z+2, x-5, y-9, z-2, 246)
	mc.setBlocks(x+4, y+3, z+3, x-4, y-9, z-3, 246)
	mc.setBlocks(x+3, y+3, z+4, x-3, y-9, z-3, 246)
	mc.setBlocks(x+5, y+3, z+2, x-5, y-9, z-2, 246)
	mc.setBlocks(x+6, y+4, z+2, x-6, y-9, z-2, 246)
	mc.setBlocks(x+5, y+4, z+3, x-5, y-9, z-3, 246)
	mc.setBlocks(x+7, y+5, z+2, x-7, y-9, z-2, 246)
	mc.setBlocks(x+6, y+5, z+3, x-6, y-9, z-3, 246)
main()
def chest():
	mc = init()
	mc.player.setPos(0, 45-93, -20)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x+5, y, z+3, x-5, y, z-3, 246)
	mc.setBlocks(x+6, y, z+2, x-6, y, z-2, 246)
	mc.setBlocks(x+7, y, z+1, x-7, y, z-1, 246)
chest()
def chest2():
	mc = init()
	mc.player.setPos(0, 45-93, -20)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x+5, y, z+4, x-5, y, z-3, 246)
	
chest2()
def chest3():
	mc = init()
	mc.player.setPos(0, 46-93, -20)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x+5, y+2, z+5, x-5, y, z-3, 246)
	mc.setBlocks(x+6, y+2, z+4, x-6, y, z-3, 246)
	mc.setBlocks(x+7, y+2, z+3, x-7, y, z-2, 246)
	mc.setBlocks(x+8, y+2, z+2, x-8, y, z-1, 246)
chest3()
def chest4():
	mc = init()
	mc.player.setPos(0, 49-93, -20)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x+5, y, z+4, x-5, y, z-3, 246)
	mc.setBlocks(x+5, y, z+3, x-5, y, z-3, 246)
	mc.setBlocks(x+6, y, z+3, x-6, y, z-2, 246)
	mc.setBlocks(x+7, y, z+2, x-7, y, z-1, 246)
chest4()
def abbs():
	mc = init()
	x = -2 
	y = 32-93
	z = -15
	while True:
		for spunky in range(2):
			mc.setBlocks(x+1, (y+3)+spunky, z, x, y+spunky, z, 246)
			mc.setBlocks(x+4, (y+3)+spunky, z, x+3, y+spunky, z, 246)
			mc.setBlocks(x+1, (y+7)+spunky, z, x, y+5+spunky, z, 246)
			mc.setBlocks(x+4, (y+7)+spunky, z, x+3, y+5+spunky, z, 246)
			mc.setBlocks(x+1, (y+10)+spunky, z, x, y+9+spunky, z, 246)
			mc.setBlocks(x+4, (y+10)+spunky, z, x+3, y+9+spunky, z, 246)
			sleep(1)
			mc.setBlocks(x+4, (y+10)+spunky, z, x, y+spunky, z, 0)
def arm1():
	mc = init()
	mc.player.setPos(9, 47-93, -19)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+3, z-1, (x)*blah, y, z+2, 246)
arm1()	
def arm11():
	mc = init()
	mc.player.setPos(9, 48-93, -19)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x-2)*blah, y+1, z, (x+3)*blah, y, z+1, 246)
arm11()
def arm12():
	mc = init()
	mc.player.setPos(10, 46-93, -18)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+3, z-1, (x)*blah, y, z+2, 246)
arm12()	
def arm13():
	mc = init()
	mc.player.setPos(11, 45-93, -17)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+3, z-1, (x)*blah, y-2, z+2, 246)
arm13()	
def arm13():
	mc = init()
	mc.player.setPos(11, 43-93, -16)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+3, z-1, (x)*blah, y-2, z+2, 246)
arm13()	
def arm14():
	mc = init()
	mc.player.setPos(11, 40-93, -15)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+3, z-1, (x)*blah, y, z+2, 246)
arm14()
def arm15():
	mc = init()
	mc.player.setPos(11, 38-93, -7)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+3, z-13, (x)*blah, y, z, 246)
arm15()
def arm16():
	mc = init()
	mc.player.setPos(13, 39-93, -6)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+2)*blah, y+3, z, (x-3)*blah, y-2, z, 49)
		mc.setBlocks((x+1)*blah, y+2, z, (x-2)*blah, y-1, z, 0)
arm16()
def arm17():
	mc = init()
	mc.player.setPos(13, 39-93, -5)
	x, y, z = mc.player.getPos()
	for blah in range (-1, 2, 2):
		mc.setBlocks((x+3)*blah, y+4, z, (x-4)*blah, y-3, z, 49)
		mc.setBlocks((x+2)*blah, y+3, z, (x-3)*blah, y-2, z, 0)
arm17()
if __name__ == "__main__":
	abbs()

"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
