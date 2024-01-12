# Faca um programa em Python que abra e reproduza o audio de um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.play()
pygame.event.wait