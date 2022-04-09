from battleship_utils import *

#Declaring initial grids
grid_mat_pc = [['O']*10 for _ in range(10)]
grid_mat_player = [['O']*10 for _ in range(10)]

#Printing starting grid
printingGrid(grid_mat_pc, grid_mat_player)
print('''The upper grid is Player 1's and the bottom grid is Player 2's''')
print("")

#Making lists that will store coordinates of ship parts
coordinates_list_pc = list()
coordinates_list_player = list()

#Placing ships
print("Player 1's Placing : ")
placingShips(1, grid_mat_pc, coordinates_list_pc)

#Printing grid with ship positions highlighted to show the user
for i in coordinates_list_pc :
    replaceGridElem(i[0], i[1], True, grid_mat_pc)
printingGrid(grid_mat_pc, grid_mat_player)
print("Please check your grid for the location of your ships.")
checkToMoveOn()

#Resetting the grids to default
grid_mat_pc = [['O']*10 for _ in range(10)]

print("Player 2's Placing : ")
placingShips(2, grid_mat_player, coordinates_list_player)

#Printing grid with ship positions highlighted to show the user
for i in coordinates_list_player :
    replaceGridElem(i[0], i[1], True, grid_mat_player)
printingGrid(grid_mat_pc, grid_mat_player)
print("Please check your grid for the location of your ships.")
checkToMoveOn()

#Resetting the grids to default
grid_mat_player = [['O']*10 for _ in range(10)]

#Calling the function to facilitate attacking until one or the other user has won.
attackFunc(grid_mat_pc, grid_mat_player, coordinates_list_pc, coordinates_list_player)




