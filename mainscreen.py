import pygame
import time
pygame.font.init()


class Screen:
    def __init__(self, screen_w, screen_h, font, fontcolor):
        self.screen = pygame.Surface((screen_w, screen_h))
        self.dateScreen = pygame.Surface((screen_w/2, screen_h/10))
        self.timeScreen = pygame.Surface((screen_w/2, screen_h/10))

        self.font = pygame.font.SysFont(font, screen_w/12)
        self.fontcolor = fontcolor

    def clear_screen(self):
        self.screen.fill((0, 0, 0))
        self.dateScreen.fill((0, 255, 145))
        self.timeScreen.fill((255, 255, 0))

    def update_time_screen(self):
        """returns current time in H:M:S format"""
        current_time = time.localtime()
        hours = str(current_time[3])
        minutes = str(current_time[4])
        seconds = str(current_time[5])
        if len(minutes) == 1:
            minutes = "0"+minutes
        if len(seconds) == 1:
            seconds = "0"+seconds
        return self.font.render(hours+":"+minutes+":"+seconds, True, self.fontcolor)

    def update_date_screen(self):
        """returns current date in string in 'D M Y' format"""
        month_name = {
            1: "Stycznia",
            2: "Lutego",
            3: "Marca",
            4: "Kwietnia",
            5: "Maja",
            6: "Czerwca",
            7: "Lipca",
            8: "Sierpnia",
            9: "Września",
            10: "Października",
            11: "Listopada",
            12: "Grudnia",
        }

        current_time = time.localtime()
        year = str(current_time[0])
        month = month_name[current_time[1]]
        day = str(current_time[2])
        return self.font.render(day+" "+month+""+year, True, self.fontcolor)

    def draw(self):
        """rgreg"""
        # CLEAR THE SCREENS
        self.screen.fill((155, 0, 0))
        self.timeScreen.fill((100, 0, 100))
        #self.dateScreen.fill((0, 155, 0))
        # blit time screen
        #self.timeScreen.blit(self.update_time_screen(), (0, 0))
        # blit date screen
        #self.dateScreen.blit(self.update_date_screen(), (0, 0))

        # BLIT EVERYTHING ONTO MAIN SCREEN
        self.screen.blit(self.timeScreen, (0, 0))
        #self.screen.blit(self.dateScreen, (0, self.timeScreen.get_height()))
