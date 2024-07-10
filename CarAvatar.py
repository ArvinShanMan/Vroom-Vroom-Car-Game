import pygame

def create_car_image():

    pygame.init()

    car_width, car_height = 50, 60
    car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)  # Using SRCALPHA for transparency

    # Fill the car with a transparent color
    car_surface.fill((0, 0, 0, 0))  

    # Draw the car (a simple rectangle with windows)
    pygame.draw.rect(car_surface, (0, 0, 255), (0, 0, car_width, car_height))  # Car body
    pygame.draw.rect(car_surface, (255, 255, 255), (10, 10, 10, 10))  # Left window
    pygame.draw.rect(car_surface, (255, 255, 255), (30, 10, 10, 10))  # Right window

    # Save the car surface to an image file
    pygame.image.save(car_surface, 'Racecar.png')

    # Quit Pygame
    pygame.quit()
    

if __name__ == "__main__":
    create_car_image()