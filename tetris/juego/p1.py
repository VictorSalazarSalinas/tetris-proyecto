import arcade

filas=20
columnas=10

ancho=30
alto=30

margen=1

ven_ancho = (ancho + margen) * columnas + margen
ven_alto = (alto + margen) * filas + margen

ven_titulo = "tetris"

piezas=[    
            #cruz
            [[0, 1, ],
            [1, 1, 1]],

            #vib izq
            [[1, 1, 0],
            [0, 1, 1]],

            #vib der
            [[0, 1, 1],
            [1, 1, 0]],

            #cuadrado
            [[1, 1],
            [1, 1]],

            #palo
            [[1, 1, 1, 1]],

            #l izq
            [[1, 0, 0],
            [1, 1, 1]],

            #l der
            [[0, 0, 1],
            [1, 1, 1]],

                        ]

movimiento=1 



class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AMAZON

        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    

   


def main():
    
    window = arcade.Window(ven_ancho ,ven_alto, ven_titulo)

    
    game = GameView()

    
    window.show_view(game)

    
    arcade.run()



if __name__ == "__main__":
    main()