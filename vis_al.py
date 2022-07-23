from calendar import c
from msilib.schema import Font
import pygame
import random

height_window = 600


pygame.init()

Screen = pygame.display.set_mode((900, height_window))

pygame.display.set_caption('Hello World')

sort = False
color = [(255,0,0), (0,255,0)]
green = 0
running = True
clock = pygame.time.Clock()

size = 10
width_block = 300 // size
arr = [random.randint(2, 100) for i in range(size)]
arr2 = []
Sort = False

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            num1 = arr[j]
            num2 = arr[j+1]
            if num1 > num2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                return arr, j

def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1    
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            array[j + 1] = key
            return array, j

def texts():
    FONT = pygame.font.SysFont('ariel', 50)
    FONT2 = pygame.font.SysFont('ariel', 24)

    head = FONT.render("Algo Visualizer", 1, (255, 255, 255))
    body = FONT2.render("Press I - For using Insertion Sort", 1, (255, 255, 255))
    body_2 = FONT2.render("Press B - For using Bubble Sort", 1, (255, 255, 255))
    line3 = FONT2.render("Press R - For Reseting Array", 1, (255, 255, 255))

    Screen.blit(head, (20, 20))
    Screen.blit(body, (25, 82))
    Screen.blit(body_2, (25, 110))
    Screen.blit(line3, (25, 550))


while running:
    Screen.fill((0, 0, 0))
    texts()

    for i, val in enumerate(arr):
        if i == green or i == green +1:
            pygame.draw.rect(Screen, color[1], pygame.Rect((width_block + 1) * i + 350, 80, width_block, (5 * val)))
        else:
            pygame.draw.rect(Screen, color[0], pygame.Rect((width_block + 1) * i + 350, 80, (width_block), (5 * val)))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i and sort == False:
                arr2, green = insertion_sort(arr)
                arr = arr2
            if event.key == pygame.K_b and sort == False:
                arr2, green = bubble_sort(arr)
                arr = arr2
            if event.key == pygame.K_r:
                arr = [random.randint(2, 100) for i in range(size)]
                green = 0
                sort = False


            if sorted(arr) == arr:
                sort = True
                
        
    pygame.display.update()

