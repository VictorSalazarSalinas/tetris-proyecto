from config import *
from os.path import join

class Puntos:
    def __init__(self):
        self.surface=pygame.Surface((barra_ancho,jue_alto*puntos_al-esp))

        #parametro para colocar el puntaje en su possion izq inferior der
        self.rect=self.surface.get_rect(bottomright =(ven_ancho-esp,ven_alto-esp))
        

        self.display_surface= pygame.display.get_surface()

        #fuente 
        self.font=pygame.font.Font(join('..','graficos','Russo_One.ttf'))

        #separacion
        self.al_pre_fig=self.surface.get_height()/3


        self.level=1 
        self.score=0
        self.lines=0


    def display_texto(self,pos,texto):
        texto_surface=self.font.render(f'{texto[0]}:{texto[1]}',True,'#FFFFFF')
        texto_rect= texto_surface.get_rect(center = pos)
        self.surface.blit(texto_surface,texto_rect)



    def run(self):

        self.surface.fill('#1C1C1C')

        for i,texto in enumerate([('Score',self.score),('Level',self.level),('lineas',self.lines)]):
            
            x = self.surface.get_width()/2
            y = self.al_pre_fig/2 + i * self.al_pre_fig

            self.display_texto((x,y),texto)



        #superponer la venta de juegos en la ventana original
        self.display_surface.blit(self.surface,self.rect)

        pygame.draw.rect(self.display_surface,'#FFFFFF',self.rect,2,2)