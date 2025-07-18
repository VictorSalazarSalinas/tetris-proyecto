from config import *
from pygame.image import load
from os import path



class P_piezas:
    def __init__(self):

        self.surface=pygame.Surface((barra_ancho,jue_alto*barra_poral))

        #parametro para colocar el puntaje en su possion izq inferior der
        self.rect=self.surface.get_rect(topright=(ven_ancho-esp,esp))
        

        self.display_surface= pygame.display.get_surface()




        #figuras
        
        self.fig_surper={fig: load(path.join('..','graficos',f'{fig}.png')).convert_alpha() for fig in TETROMINOS.keys()}
        print(self.fig_surper)

        self.al_pre_fig=self.surface.get_height()/3




    def display_piezas(self,formas):
        for i,forma in enumerate(formas):
            forma_super= self.fig_surper[forma]
            x = self.surface.get_width()/2
            y = self.al_pre_fig/2 + i * self.al_pre_fig
            centrar = forma_super.get_rect(center=(x,y))
            self.surface.blit(forma_super,centrar)



    def run(self,sig_fig):
        self.surface.fill('#1C1C1C')

        self.display_piezas(sig_fig)

        
        #superponer la venta de juegos en la ventana original
        self.display_surface.blit(self.surface,self.rect)

        pygame.draw.rect(self.display_surface,'#FFFFFF',self.rect,2,2)