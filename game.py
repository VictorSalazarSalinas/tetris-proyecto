from config import *
#elige un valor random de una lista
from random import choice
from sys import exit
from timer import Timer
from os.path import join

class Game:
    def __init__(self,get_sig_fig,update_puntos):
        #crear otra superficie
        self.surface=pygame.Surface((jue_ancho,jue_alto))

        self.display_surface=pygame.display.get_surface()

        self.rect=self.surface.get_rect(topleft=(esp,esp))

        self.sprites=pygame.sprite.Group()


        #
        self.get_sig_fig = get_sig_fig

        self.update_puntos=update_puntos


        #esto es para hacer que las lineas tengan transparencia
        self.lineas_surface=self.surface.copy()
        self.lineas_surface.fill((0,255,0))
        self.lineas_surface.set_colorkey((0,255,0))
        self.lineas_surface.set_alpha(120)



        #generar pieza tetromino
        self.alma_ca = [[0 for x in range(columnas)] for y in range(filas) ] 
        self.tetromino=Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.create_new_tetromino,
            self.alma_ca)





        #timer
        self.down_speed= 700
        self.down_speed_vel=100
        self.down_press=False

        self.timers ={
            'v move': Timer(self.down_speed,True,self.move_down),
            'h move': Timer(200),
            'rotar': Timer(200)

        }

        self.timers['v move'].activate()

        #puntos
        self.cuenta_level=1 
        self.cuenta_score=0
        self.cuenta_lines=0


        # audio
        self.landing_sound = pygame.mixer.Sound(join('..','sonido', 'landing.wav'))
        self.landing_sound.set_volume(0.1)

    def calcular_puntos(self,num_lineas):
        self.cuenta_lines+= num_lineas
        

        self.cuenta_score+= puntos_data[num_lineas]*self.cuenta_level
        

        if self.cuenta_lines/10>self.cuenta_level:
            self.cuenta_level+=1
            self.down_speed *= 0.75
            self.down_speed_vel = self.down_speed * 0.3
            self.timers['v move'].duration = self.down_speed

        self.update_puntos(self.cuenta_lines,self.cuenta_score,self.cuenta_level)


    def timer_update(self):
        for timer in self.timers.values():
            timer.update()



    def check_game_over(self):
        for block in self.tetromino.blocks:
            if block.pos.y < 0:
                exit()

    def create_new_tetromino(self):
        self.landing_sound.play()
        self.check_game_over()
        self.com_fin()
        self.tetromino=Tetromino(
            self.get_sig_fig(),
            self.sprites,
            self.create_new_tetromino,
            self.alma_ca)

    def move_down(self):
        self.tetromino.move_down()

        #generar la lineas 
    
    def cuadrilla(self):
         for col in range(1,columnas):
            x=col*celda
            pygame.draw.line(self.lineas_surface,'#FFFFFF',(x,0),(x,self.surface.get_height()),1)

         for fi in range(1,filas):
            y=fi*celda
            pygame.draw.line(self.lineas_surface,'#FFFFFF',(0,y),(self.surface.get_width(),y),1)   
         


         self.surface.blit(self.lineas_surface,(0,0))


    def input(self):
        keys =pygame.key.get_pressed()



        if not self.timers['h move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_hori(-1)
                self.timers['h move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_hori(1)
                self.timers['h move'].activate()

        if not self.timers['rotar'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotar()
                self.timers['rotar'].activate()


        if not self.down_press and keys[pygame.K_DOWN]:
            self.down_press=True
            self.timers['v move'].duration = self.down_speed_vel
            self.timers['v move'].time = pygame.time.get_ticks() 
            print('press')

        if self.down_press and not keys[pygame.K_DOWN]:
            self.down_press=False
            self.timers['v move'].duration = self.down_speed
            self.timers['v move'].time = pygame.time.get_ticks() 
            print('relese')

    
    def com_fin(self):
        #obtener logica
        bor_filas=[]
        for i,fila in enumerate(self.alma_ca):
            if all(fila):
                bor_filas.append(i)

        #comprobaion ara borrar filas
        if bor_filas:
            for bor_fila in bor_filas:

                for block in self.alma_ca[bor_fila]:
                    #.kill mata todos los sprites
                    block.kill()

                #mover abajo
                for fila in self.alma_ca:
                    for block in fila:
                        if block and block.pos.y < bor_fila:
                            block.pos.y += 1

            self.alma_ca = [[0 for x in range(columnas)] for y in range(filas)]
            for block in self.sprites:
                self.alma_ca[int(block.pos.y)][int(block.pos.x)]=block

            #update puntos
            self.calcular_puntos(len(bor_filas))


    def run(self):


        #update
        self.input()
        self.timer_update()
        self.sprites.update()

        #di
        self.surface.fill('#1C1C1C')

        self.sprites.draw(self.surface)


        #superponer 
        self.cuadrilla()
        self.display_surface.blit(self.surface,(esp,esp))

        pygame.draw.rect(self.display_surface,'#FFFFFF',self.rect,2,2)


class Tetromino:
    def __init__(self,forma,group, create_new_tetromino,alma_ca):
        self.forma = forma

        self.block_pos=TETROMINOS[forma]['forma']

        self.color=TETROMINOS[forma]['color']

        self.create_new_tetromino = create_new_tetromino

        self.alma_ca = alma_ca

        self.blocks=[Bloque(group,pos,self.color) for pos in self.block_pos]

        
    


    #colisiones

    def move_hori_coli(self,blocks,amo):
        #crear pieza asi la izq o der para saber si se sale del rango
        colis_list=[block.hori_coli(int(block.pos.x + amo),self.alma_ca) for block in self.blocks]

        return True if any(colis_list) else False


    def move_veri_coli(self,blocks,amo):
        colis_list=[block.veri_coli(int(block.pos.y + amo),self.alma_ca) for block in self.blocks]
        return True if any(colis_list) else False

    #move
    def move_hori(self,tec):
        if not self.move_hori_coli(self.blocks,tec):
            
            for block in self.blocks:
                block.pos.x+=tec



    def move_down(self):
        if not self.move_veri_coli(self.blocks,1):
            for block in self.blocks:
                block.pos.y+=1
        else:
            for block in self.blocks:
                self.alma_ca[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()

            #for filas in self.alma_ca:
            #   print(filas)

    def rotar(self):
        if self.forma != 'O':
            #pivote 0,0
            pivote_pos =self.blocks[0].pos

            #nuevas posisciones
            new_blposis=[block.rotar(pivote_pos) for block in self.blocks]


            #colisiones
            for pos in new_blposis:

                #horizontal
                if pos.x <0 or pos.x>=columnas:
                    return

                #otras piezas

                if self.alma_ca[int(pos.y)][int(pos.x)]:
                    return


                #vertical
                if pos.y > filas:
                    return

                



            #cargar posiciones
            for i,block in enumerate(self.blocks):
                block.pos = new_blposis[i]




class Bloque(pygame.sprite.Sprite):

    def __init__(self,group,pos,color):


        super().__init__(group)

        self.image=pygame.Surface((celda,celda))
        self.image.fill(color)

        #posicion
        self.pos=pygame.Vector2(pos) + pygame.Vector2(columnas//2,-1)

        x=self.pos.x*celda
        y=self.pos.y*celda
        self.rect=self.image.get_rect(topleft=(x,y))

    def rotar(self,pivote_pos):
        distancia=self.pos - pivote_pos

        rotado=distancia.rotate(90)
        new_pos=pivote_pos + rotado
        return new_pos


    def veri_coli(self,y,alma_ca):
        if y>=filas:
            return True
        if y>=0 and alma_ca[y][int(self.pos.x)]:
            return True

    def hori_coli(self,x,alma_ca):
        #verificar si entre las columnas
        if not 0<=x < columnas:
            return True
        if alma_ca[int(self.pos.y)][x]:
            return True

    def update(self):
        
        self.rect.topleft=self.pos*celda