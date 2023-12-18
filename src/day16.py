# Day 16 of the 2023 Advent of Code
class Beam():
    def __init__(self,x,y,dirX,dirY):
        self.x = x
        self.y = y
        self.dirX = dirX
        self.dirY = dirY

def matchCross(a,crossed_list):
    for b in crossed_list:
        if a.x == b.x and a.y == b.y and a.dirX == b.dirX and a.dirY == b.dirY: return True
    else: return False

def energizeMatrix(initial_beam):
    energize_matrix = []
    for i in range(len(map_matrix)): energize_matrix.append([0]*len(map_matrix[0]))
    beam_count = 1
    beam_dict = {0: initial_beam}
    crossed_list = []
    while beam_dict:
        add_dict = {}
        del_list = []
        for i in beam_dict:
            if matchCross(beam_dict[i],crossed_list) or not (beam_dict[i].x in range(len(map_matrix)) and beam_dict[i].y in range(len(map_matrix[0]))):
                del_list.append(i)
                continue
            energize_matrix[beam_dict[i].x][beam_dict[i].y] = 1
            crossed_list.append(Beam(beam_dict[i].x,beam_dict[i].y,beam_dict[i].dirX,beam_dict[i].dirY))
            if map_matrix[beam_dict[i].x][beam_dict[i].y] == "-" and beam_dict[i].dirY == 0:
                del_list.append(i)
                add_dict[beam_count] = Beam(beam_dict[i].x,beam_dict[i].y,0,1)
                add_dict[beam_count+1] = Beam(beam_dict[i].x,beam_dict[i].y,0,-1)
                beam_count += 2
            elif map_matrix[beam_dict[i].x][beam_dict[i].y] == "|" and beam_dict[i].dirX == 0:
                del_list.append(i)
                add_dict[beam_count] = Beam(beam_dict[i].x,beam_dict[i].y,1,0)
                add_dict[beam_count+1] = Beam(beam_dict[i].x,beam_dict[i].y,-1,0)
                beam_count += 2
            elif map_matrix[beam_dict[i].x][beam_dict[i].y] == "/":
                aux = beam_dict[i].dirX
                beam_dict[i].dirX = -beam_dict[i].dirY
                beam_dict[i].dirY = -aux
            elif map_matrix[beam_dict[i].x][beam_dict[i].y] == "\\":
                aux = beam_dict[i].dirX
                beam_dict[i].dirX = beam_dict[i].dirY
                beam_dict[i].dirY = aux
            beam_dict[i].x += beam_dict[i].dirX
            beam_dict[i].y += beam_dict[i].dirY
        for i in del_list: del beam_dict[i]
        for i in add_dict: beam_dict[i] = add_dict[i]
    return sum(sum(x) for x in energize_matrix)

# Read input file
with open("../include/input16.inc","r") as map_file:
    map_matrix = list(map(lambda a: a.strip(),map_file.readlines()))

########################### Part 1 ###########################
print("Part 1: %s"%energizeMatrix(Beam(0,0,0,1)))

########################### Part 2 ###########################
res_list = []
for x in range(len(map_matrix[0])): res_list.append(energizeMatrix(Beam(0,x,1,0)))
for x in range(len(map_matrix[0])): res_list.append(energizeMatrix(Beam(len(map_matrix)-1,x,-1,0)))
for x in range(len(map_matrix)): res_list.append(energizeMatrix(Beam(x,0,0,1)))
for x in range(len(map_matrix)): res_list.append(energizeMatrix(Beam(x,len(map_matrix[0])-1,0,-1)))
print("Part 2: %s"%max(res_list))