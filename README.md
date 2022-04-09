# Battleship-Command-Line
A Python application to run Battleship on the command line, with 2 player functionalities.

The code works by printing and clearing to simulate turn changes and has functionalities to detect out of bound responses, account for the errors and then loop back for another attempt.

As soon as the function is executed, two matrices are initialized that will be the grids for the two players.

```python
#Declaring initial grids
grid_mat_pc = [['O']*10 for _ in range(10)]
grid_mat_player = [['O']*10 for _ in range(10)]
```

Then the function, _printingGrid_, is called which takes in as parameters the two grids and then displays them.

```python
#Printing starting grid
printingGrid(grid_mat_pc, grid_mat_player)
```

Along with that, instructions are also given to the players to assist them in figuring out the UI.

![image](https://user-images.githubusercontent.com/69855968/162577176-d0853771-77a8-4eb3-8a64-a68b5ee011c2.png)

The coordinates are taken in as row and column in the form of two integers with spaces in between.
They are **position based** and not **index based**, so to place a ship at the first column, you would enter 1 and not 0.

As you can see in the image below, the coordinates were entered and then the player is shown the positions of his ships.

![image](https://user-images.githubusercontent.com/69855968/162577116-bb56a2f1-310a-46ed-a399-bee3a9f951fb.png)

Once the user has entered _ok_, the program clears the screen, reprints the grid and prepares for the other player to place their ships.

Once both players have placed their ships, the program starts off the actual game with Player 1's turn.

![image](https://user-images.githubusercontent.com/69855968/162577325-43823f25-d13a-4e7c-817b-e2c4d7809e5f.png)

When the user enters the co-ordinates to attack, the program checks through the list it has made for each player to see if a ship was hit or not.

If it was hit, the player's turn would continue, otherwise it would swap to the other player.

A lot of functions go into this functionality, so going through them one by one, first when they're called in _battleshipcode.py_ and then their inner workings in _battleship_utils.py_.

First action we will take a look at is making the list for the verification of the hit.

```python
#Making lists that will store coordinates of ship parts
coordinates_list_pc = list()
coordinates_list_player = list()

#Placing ships
print("Player 1's Placing : ")
placingShips(1, grid_mat_pc, coordinates_list_pc)
```
Here you can see that the list variables are made and then the function _placingShips_ is called to fill the list with the coordinates.

_placingShips_ code explanation :

```python
#Facilitates taking user input to place the ships in the grid.
#Takes in parameters of player number, grid to modify and 
#Coordinates list to append to.    
def placingShips(player_num,grid_mat_pc,coordinates_list_pc):
    #placing ships
    print('''There are 3 types of ships :
          1) A horizontal ship of 2 lengths
          2) A vertical ship of 4 length
          3) A ship which takes up a rectangle of 3 height and 4 width
          ''')
    
    #PLACING HORIZONTAL 2 SHIP
    placed_hor2 = False
    while not placed_hor2 :
        #Taking input for the starting coordinates
        hor2_pos = input("Enter the coordinates to place the ship number 1 (horizontal with length 2) : ")
        hor2_pos_dim_list = hor2_pos.split()
        hor2_row = int(hor2_pos_dim_list[0])-1
        hor2_col = int(hor2_pos_dim_list[1])-1
        
        
        #checking for out of index errors
        try :
            x = grid_mat_pc[hor2_row][hor2_col+1]
            placed_hor2 = True
        except:
            print("Invalid Coordinates, not enough space to place it, please enter again!")
    #appending to coordinates list        
    for i in range(2):
        coordinates_list_pc.append((hor2_row,hor2_col+i))
    
    
    #PLACING VERTICAL 4 SHIP
    placed_ver4 = False
    while not placed_ver4 :
        #Taking input for the starting coordinates
        ver4_pos = input("Enter the coordinates to place the ship number 2 (vertical with length 4) : ")
        ver4_pos_dim_list = ver4_pos.split()
        ver4_row = int(ver4_pos_dim_list[0])-1
        ver4_col = int(ver4_pos_dim_list[1])-1
        
        #checking for out of index errors
        try:
            x=grid_mat_pc[ver4_row+3][ver4_col]
        except:
            print("Invalid Coordinates, not enough space to place it, please enter again!")
            
        #checking for overlapping of coordinates with previously placed ships
        flag_ver4 = False
        count_ver4 = 0
        for i in range(4):
            if (ver4_row+i,ver4_col) not in coordinates_list_pc :
                count_ver4+=1

        if count_ver4 == 4 :
            flag_ver4 = True
        
        #appending after verifying no overlap
        if flag_ver4:
            for i in range(4):
                coordinates_list_pc.append((ver4_row+i,ver4_col))
            placed_ver4=True
        else :
            print("These coordinates overlap with a previously placed ship, please enter again!")
    
    
    #PLACING RECT SHIP
    placed_rect = False
    while not placed_rect :
        #taking input for the starting coordinates
        rect_pos = input("Enter the coordinates of the top left corner of the ship number 3 (rectangle with height 3 and width 4) : ")
        rect_pos_dim_list = rect_pos.split()
        rect_row = int(rect_pos_dim_list[0])-1
        rect_col = int(rect_pos_dim_list[1])-1
        
        #checking for out of index errors
        try:
            x=grid_mat_pc[rect_row+2][rect_col+3]
        except:
            print("Invalid Coordinates, not enough space to place it, please enter again!")
            
        #checking for overlapping of coordinates with previously placed ships    
        flag_rect = False
        count_rect = 0
        for i in range(3):
            for j in range(4):
                if (rect_row+i, rect_col+j) not in coordinates_list_pc :
                    count_rect+=1
        
        if count_rect == 12 :
            flag_rect = True
            
        #appending after verifying no overlap   
        if flag_rect:
            for i in range(3):
                for j in range(4):
                    coordinates_list_pc.append((rect_row+i, rect_col+j))
            placed_rect=True
        else:
            print("These coordinates overlap with a previously placed ship, please enter again!")
```

The next and last function that is called is _attackFunc_. This function accomplishes the back and forth attacking until the game is won by one or the other player.

```python
#Function to use user input to attack a specific coordinate on the other grid.
#Takes in parameters of both players' grids and both coordinate lists.
def attackFunc(grid_mat_pc, grid_mat_player, coordinates_list_pc, coordinates_list_player):
    while len(coordinates_list_pc)!=0 and len(coordinates_list_player)!=0 :
        turn_token = 1
        print("Player 1's Turn : ")
        print("Attack their ships!")
        while turn_token == 1 :
            #Checking to see if entered coordinates are out of bounds of list index
            flag_dim_1 = False
            while not flag_dim_1 :
                #requesting user input for attack
                dim_input = input("Enter the position in the grid to attack (in the form of 'row_no col_no') :")
                
                #conerting input into row and col values
                dim_input_list = dim_input.split()
                row = int(dim_input_list[0])-1
                col = int(dim_input_list[1])-1
                
                try :
                    x=grid_mat_player[row][col]
                    flag_dim_1=True
                except:
                    print("Coordinates entered are out of bounds! Please enter again.")
            
            print("")
            
            #Verifying if the attack hit or not
            if (row,col) in coordinates_list_player :
                coordinates_list_player.remove((row,col))
                hit=True
                replaceGridElem(row, col, hit, grid_mat_player)
                printingGrid(grid_mat_pc, grid_mat_player)
            else :
                hit=False
                replaceGridElem(row, col, hit, grid_mat_player)
                printingGrid(grid_mat_pc, grid_mat_player)
                turn_token = 2
                
            if len(coordinates_list_player)==0 :
                turn_token = 0
                
        if len(coordinates_list_player)==0 :
            break
        
        print("Player 2's Turn : ")
        print("Attack their ships!")
        while turn_token == 2 :
            #Checking to see if entered coordinates are out of bounds of list index
            flag_dim_2 = False
            while not flag_dim_2 :
                #requesting user input for attack
                dim_input = input("Enter the position in the grid to attack (in the form of 'row_no col_no') :")
                
                #conerting input into row and col values
                dim_input_list = dim_input.split()
                row = int(dim_input_list[0])-1
                col = int(dim_input_list[1])-1
                
                try :
                    x=grid_mat_pc[row][col]
                    flag_dim_2=True
                except:
                    print("Coordinates entered are out of bounds! Please enter again.")
            
            
            
            print("")
            
            #Verifying if the attack hit or not
            if (row,col) in coordinates_list_pc :
                coordinates_list_pc.remove((row,col))
                hit=True
                replaceGridElem(row, col, hit, grid_mat_pc)
                printingGrid(grid_mat_pc, grid_mat_player)
            else :
                hit=False
                replaceGridElem(row, col, hit, grid_mat_pc)
                printingGrid(grid_mat_pc, grid_mat_player)
                turn_token = 1
                
            if len(coordinates_list_pc)==0 :
                turn_token = 0
                break
        if len(coordinates_list_pc)==0 :
            break
            
    if len(coordinates_list_pc) == 0 :
        
        print("Player 2 won!")
        sys.exit()
        
    else :
        print("Player 1 won!")
        sys.exit()
```

That concludes the major functions that support the application.

Some other minor functions are :

_clearConsoleSpyder()_ for clearing the Spyder console if you run it on that.
_clearConsole()_ for clearing the terminals.
















