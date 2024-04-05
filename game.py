#import pygame module
import pygame

#main_function
def main():

    #initialize game module
    pygame.init()

    #create a screen. dimensions: 240 x 180
    screen = pygame.display.set_mode((240,180))

    #variable to control the main loop
    running = True

    #main loop
    while running:

        #events (gets events from the main queue)
        for event in pygame.event.get():

            #when the user quits,
            if event.type == pygame.QUIT:
                #the running variable stops.
                running = False

#run the main fucntion only if this module is executed
if __name__ == "__main__":
    #call the main function
    main()