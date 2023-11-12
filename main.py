import pyglet

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False

import pyglet.gl as gl

class Window(pyglet.window.Window):
    def_init_(self, **args):
        super(Window, self)._init_(**args)
        
    def on_draw(self):
        gl.glClearColor(1.0, 0.5, 1.0, 1.0)
        self.clear()
        
    def on_resize(self, width, height):
        print("resize %d * %d" % (width, height))

class Game:
    def_init(self)
        self.config = gl.Config(major_version = 3)
        self.window = Window(config = self.config, width = 800, height = 600, caption "Minecraft Python", resizeable= True, vsync = False)
    def run(self):
        pyglet.app.run()
        
    
    
if _name_ == "_main_":
    game = Game()
    game.run()