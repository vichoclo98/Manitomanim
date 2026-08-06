from manim import *

class Chao(Scene):
    def construct(self):
        texto = Text("¡Chao, Manito!")
        self.play(Write(texto))
        self.wait(2)

class Prueba(Scene):
    def construct(self):
        texto = Text("Prueba uno")
        self.play(Write(texto))
        self.wait(2)