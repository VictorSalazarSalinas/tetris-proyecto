from config import *
from sys import exit
from os.path import join
from game import Game
from puntos import Puntos
from p_piezas import P_piezas

#elige un valor random de una lista
from random import choice


class Main:
    
    def __init__(self): 
        #crear instancia de juego
        pygame.init()
       #crear ventana 
        self.display_surface=pygame.display.set_mode((ven_ancho,ven_alto))
        #Crear timer (reloj)
        self.clock = pygame.time.Clock()

        #titulo
        pygame.display.set_caption('tetris')

        #pre render d e3 figuras
        self.sig_figs=[choice(list(TETROMINOS.keys())) for forma in range(3)]
        print(self.sig_figs)


        #cachitos de la pantalla
        self.game=Game(self.get_sig_fig,self.update_puntos)
        self.puntos=Puntos()
        self.p_piezas=P_piezas()


        # audio 
        self.music = pygame.mixer.Sound(join('..','sonido','music.wav'))
        self.music.set_volume(0.05)
        self.music.play(-1)

    def update_puntos(self,lines,puntos,level):
        self.puntos.level=level 
        self.puntos.score=puntos
        self.puntos.lines=lines


    def get_sig_fig(self):
        sig_fig=self.sig_figs.pop(0)
        self.sig_figs.append(choice(list(TETROMINOS.keys())))
        return sig_fig
    

    #metoda para que se corra siempre
    def run(self):
        while True:
            #if para comprobar siempre el cierre de la vnetana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #matar el programa
                    exit()

            #mostrar en pantalla
                        #ventana color
            self.display_surface.fill('#1C1C1C')


            self.game.run()
            self.puntos.run()
            self.p_piezas.run(self.sig_figs)

            
            #fps
            pygame.display.update()
            self.clock.tick()



if __name__ == '__main__':
    main=Main()
    #correr el programa
    main.run()
