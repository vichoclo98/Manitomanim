from manim import *

class Hola(Scene):
    def construct(self):
        texto = Text("¡Hola, Manim!")
        self.play(Write(texto))
        self.wait(2)