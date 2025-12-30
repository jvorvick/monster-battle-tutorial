from settings import *

class UI:
    def __init__(self, monster):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster

        # control
        self.general_options = ['attack', 'heal', 'switch', 'escape', 'foo', 'bar']
        self.index = {'col': 0, 'row': 0}
        self.state = 'general'

        self.attack_options = monster.abilities

    def input(self):
        keys = pygame.key.get_just_pressed()
        self.index['row'] = (self.index['row'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % 2
        self.index['col'] = (self.index['col'] + int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])) % 2
        if keys[pygame.K_SPACE]:
            self.state = self.general_options[self.index['col'] + self.index['row'] * 2]

    def general(self, options, cols, rows):
        # bg
        rect = pygame.FRect(self.left + 40, self.top + 60,100 * cols,100 * rows)
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        # menu
        for col in range(cols):
            for row in range(rows):
                x = rect.left + rect.width / 4 + (rect.width / 2) * col
                y = rect.top + rect.height / 4 + (rect.height / 2) * row
                i = col + cols * row
                color = COLORS['gray'] if col == self.index['col'] and row == self.index['row'] else COLORS['black']

                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_frect(center = (x,y))
                self.display_surface.blit(text_surf, text_rect)

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case 'general':
                length = len(self.general_options)
                if not length % 2:
                    col = length // 2
                    row = col - 1
                else:
                    col = length // 2
                    row = length - row
                print(col, row)
                self.general(self.general_options, col, row)
            case 'attack': self.general(self.attack_options, 2, 2)