from slogger import SLogger
import argparse
from PIL import Image
from mazelib import Maze
from mazelib.generate.Prims import Prims
logger = SLogger()
args = argparse.ArgumentParser()
args.add_argument("-w", "--w", type=int, default=0)
args.add_argument("-d", "--hi", type=int, default=0)
args.add_argument("-n", "--name", type=str, default="")
args = args.parse_args()
(w, h, name) = (args.w, args.hi, args.name)
if w == 0 or h == 0 or name == "":
	(w, h, name) = (int(input("w:")), int(input("h:")), input("name:"))
logger.info("Creating maze...")
m = Maze()
logger.info("done!")
m.generator = Prims(w, h)
logger.info("Generating maze...")
m.generate()
logger.info("done!")
logger.info("saving maze...")
maze = str(m)
mazelist = maze.split("\n")
#for x in mazelist:
#	mazelist[x] = mazelist[x].replace("\n", "")
img = Image.new("RGB", (len(mazelist), len(mazelist[0])), color=(255, 255, 255))
for x in range(img.size[0]):
	for y in range(img.size[1]):
		pixel = mazelist[x][y]
		if pixel == "#":
			img.putpixel((x, y), (0, 0, 0))
img.save(name+".png", "PNG")
logger.info("done!")
logger.info("END")
