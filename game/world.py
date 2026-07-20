import pygame
from settings import *

class World:
    def __init__(self):
        self.tiles = []
        self.npc_locations = []
        
        # Create a simple village layout
        self.create_village()
    
    def create_village(self):
        """Create simple village with grass, trees, and water"""
        # For now, we'll just create some simple static objects
        # Tiles: (x, y, width, height, color, type)
        
        # Grass background (entire screen)
        self.tiles.append({
            'x': 0, 'y': 0,
            'width': SCREEN_WIDTH, 'height': SCREEN_HEIGHT,
            'color': GRASS_COLOR, 'type': 'grass'
        })
        
        # Add some trees (obstacles)
        tree_positions = [
            (150, 150), (400, 100), (700, 200), (600, 500),
            (200, 600), (850, 450)
        ]
        for x, y in tree_positions:
            self.tiles.append({
                'x': x, 'y': y,
                'width': TILE_SIZE * 2, 'height': TILE_SIZE * 2,
                'color': TREE_COLOR, 'type': 'tree'
            })
        
        # Add a small pond
        self.tiles.append({
            'x': 400, 'y': 400,
            'width': 100, 'height': 100,
            'color': WATER_COLOR, 'type': 'water'
        })
        
        # NPC spawn locations (we'll add actual NPCs soon)
        self.npc_locations = [
            {'x': 300, 'y': 300, 'name': 'Alex'},
            {'x': 600, 'y': 300, 'name': 'Jordan'},
        ]
    
    def draw(self, screen):
        """Draw the world"""
        # Draw all tiles
        for tile in self.tiles:
            pygame.draw.rect(screen, tile['color'], 
                           (tile['x'], tile['y'], tile['width'], tile['height']))
        
        # Draw NPC locations (simple circles for now)
        for npc in self.npc_locations:
            pygame.draw.circle(screen, NPC_COLOR, (int(npc['x']), int(npc['y'])), 15)
