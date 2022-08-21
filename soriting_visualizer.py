from decimal import MIN_EMIN
from lib2to3.pygram import python_grammar
from ssl import DER_cert_to_PEM_cert
from this import d
from time import CLOCK_UPTIME, sleep
from turtle import heading, width
import pygame
import math 
import random  #module that generates the random number as required
pygame.init()  # helps to initialize all the pygame modules 

# if something is used from the global scope that can not be imported into the other files used 
#hence use class , to all the stuff in the class , that can be used to store all the global values 

class DrawInFormation :
    BLACK = 0 ,0 , 0
    WHITE = 255 ,255,255
    GREEN = 0 , 255 , 0
    RED = 255 , 0 ,0 
    GREY = 128 , 128, 128 
    BACKGROUND_COLOR = WHITE 
    FONT = pygame.font.SysFont('comicsans' , 30 )
    LARGE_FONT = pygame.font.SysFont('comicsans' , 40 )
    SIDE_PAD = 100 # 50 from left and 50 from right
    TOP_PAD = 150 # pixels is the unit 
    GRADIENTS = [
        (128 , 128 , 128 ),
        (160 , 160 , 160 ),
        (192 , 192 , 192 )
    ]
    # these are the colors that are used for various bars , histograms  etc 


    def__init__(self ,width , height ,lst  )
    self.width = width
    self.height = height
    self.window = pygame.display.set_mode((width , height))
    pygame.display.set_caption("Sorting algorithm visualizer ")
    self.set_list (lst)
    def set_list (self , lst ):
        self.lst = lst 
        self.max_value = max(lst )
        self.min_value = min (lst)
        #padding in the left and right hand side 
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        # this tells me the total area that I have to divide the area into the number of space I have 
        # we wan this all to be dynamic , so the range 
        self.block_height = math.floor((self.height - self.TOP_PAD )  / (self.max_val - self.min_value)) # divide tells us the number of value in that range 
        self.start_x = self.SIDE_PAD  // 2 

        # generate astarting list 
        def draw (draw_info, algo_name , ascending  ):
            draw_info.window .fill (draw_info.BACKGROUND_COLOR ) # .fill fills the entire screen with a same color to get rid of any of the prv color on the screen , then I clear all the things and then redraw 
            tile  = draw_info.LARGER_FONT.render ("f {algo_name}-{'Ascending' if ascending else 'Descending'}" ,1, draw_info.GREEN )
            draw_info.window.blit (controls , (draw_info.width/2 -controls.get_width()/2, 35 )) # .blit transfers the content from one screen to the another 

            controls = draw_info.FONT.render ("R - Rest | SOACE - Start sorting | A -Ascending | D- descending" ,1, draw_info.BLACK )
            draw_info.window.blit (controls , (draw_info.width/2 -controls.get_width()/2, 45 )) # .blit transfers the content from one screen to the another 
        
            sorting = draw_info.FONT.render ("I - Insertion sort | B -Bubble sort " ,1, draw_info.BLACK )   # we made it 35 bcoz it it thaat down  from the top paragraph             draw_info.window.blit (sorting , (draw_info.width/2 -sorting .get_width()/2, 35 )) # .blit transfers the content from one screen to the another 
            draw_info.window.blit (controls , (draw_info.width/2 -controls.get_width()/2, 75 )) # .blit transfers the content from one screen to the another 

            draw_list(draw_info)
            pygame.display.update() #.update inserts the specific item into the directry 

        def draw_list ( draw_info , color_position ={} , clear_bg = False ):
            #complicated , look at all the element accoding to that element , then draw all the rectangles in diff colors 
            lst = draw_info.lst 
            if  clear_bg :
                clear_bg = ( draw_info .SIDE_PAD//2 , draw_info.TOP_PAD , draw_info.width -draw_info.SIDE_PAD , draw_info.height -draw_info.TOP_PAD)

            pygame .draw . rect = ( draw_info.window , draw_info.BACKGROUND_COLOR , clear_rect)
            for i , val in enumerate(lst):
                #enmurates will give the i value and the value at the index at that list 
                x = draw_info.start_x + i * draw_info.block_width
                y = draw_info.height - ( val - draw_info.min_val) * draw_info.block_height  # draw_info.min_val equalizes it to zero that is the base 
                color = draw_info.GRADIENTS [i%3] # give colors in the range of the three different color , only to see the difference 
                if i in color_position:
                    color = color_position[i]
                pygame.draw.rect (draw_info.window , color ,(x,y,draw_info.block_width , draw_info.height)) # draw.rect()  is a fucntion that draws a rectangle into a screen 
            
            if clear_bg :
                pygame.display.update() # update as we deleted only that portion nd drew a new list histogram 
        def generate_starting_list  ( n , min_val , max_val):
            for _ in range (n) :
                val = random.randint (min_val , max_val) 
                lst.append(val)


            return lst 
        
        def bubble_sort (draw_info ,ascending = True ):
            lst = draw_info.lst 
            for i in range (len(lst)-1):
                for j in range (len(lst )-1):
                    num1 = lst [j]
                    num2 = lst[j+1]
                    if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                        lst[j] ,lst[j+1 ] = lst [j+1 ] ,lst [j]  # this swaps the the two elements in one line 
                        draw_list(draw_info  {j: draw_info.GREEN , j+1 : draw_info.RED}, True )  # assigning different color to the elements that are swapped # true clears the background to show us the live swapping 
                        yield True  # call this fun for each time of swap nd yield control back where it is called , pasuess the execution dn stroes the current state of the fun and then runs the fun from where it is stored last time 
            return lst
        def insertition_sort ( draw_info , ascending = True ):
            lst = draw_info.lst 
            for i in range (1 , len (lst )):
                current = lst [i]
                while True :
                    ascending_sort = i > 0 and lst [i-1]  > current and ascending
                    descending_sort = i > 0 and lst [i-1] < current and not ascending
                    
                    if not ascending_sort and not descending_sort:
                        break 
                    lst[i] = lst [ i-1]
                    i = i -1 
                    lst [i] = current 
                    draw_list ( draw_info , {i: draw_info.GREEN , i-1 :draw_info.RED}, True )
                    yield True 
                return lst 
        def  main ():
            run = True 
            clock  = pygame.time.Clock ()
            n =50
            min_val = 0
            max_val =100
            lst = generate_starting_list(n, min_val , max_val)
            draw_info =DrawInFormation (800 , 600 , lst )
            sorting = False
            ascending = True 
            sorting_algorithm = bubble_sort
            sorting_algo_name = "BUBBLE SORT"
            sorting_algorithm_generator = sorting_algorithm( draw_info , ascending)
            while run : # keeps the display runnning in the scrren else it would end suddely , it keeps the screen on , whne the soritn g alogorithm is going no 
                clock.tick(120) # fps , max no of time it can run in a second 
                if sorting :
                    try :
                        next(sorting_algorithm_generator)
                    except StopIteration:
                        sorting = False 
                else :
                    draw(draw_info , sorting_algo_name , ascending)
                draw(draw_info)
                pygame.display.update()  # we can see it on the display 
                # no need to calculate the actual height , bcoz the extra height is below the screen 
                for event in pygame.event.get():
                    # gives the referance of all the things that occured in the last event 
                    if event.type == pygame.QUIT: # this closes window when the cross of the code is clicked 
                        run = False
                    if event.type != pygame.KEYDOWN:   # the type funciton returns 
                        continue # so for not pressing any eydown we are gona continue 
                    if event.key == pygame.K_r : # no pygame bcoz we only needs it to see only at the previous event  # when u hit the SPACE button keybaord the new list is generated 
                        lst = generate_starting_list(n , min_val , max_val )
                        draw_info.set_list(lst) # a new list is generated , in the sequenee
                        sorting = False 
                    elif event.key == pygame.K_SPACE  and sorting == False : # no pygame bcoz we only needs it to see only at the previous event  # when u hit the SPACE button keybaord the new list is generated 
                        sorting = True 
                    elif event.key == pygame.K_a and not sorting :
                        ascending = True 
                    elif event.key == pygame.K_d and not sorting :
                        descending = False 
                    
                    # that's how you will all the 10 sorting algorithm into the code 
                    elif event.key == pygame.K_i and not sorting :
                        sorting_algorithm = insertition_sort
                        sorting_algo_name = "INSERTITION SORT "
                    elif event.key == pygame.K_b and not sorting :
                        sorting_algo_name = "BUBBLE SORT "
                        sorting_algorithm = bubble_sort 
                    
                pygame.quit()

        if __name__ == "__main__":
            main ()

# CONCEPT OF GENERATOR 


