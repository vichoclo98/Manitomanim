La forma de compilar una animación hola.py es con el comando:
    uv run manim -pql scenes/hola.py Hola
Esto se hace en la terminal de VSCode y genera el archivo Hola.mp4 en media/videos
La palabra Hola al final del comando debe calzar con la línea de código "class Hola(Scene):"
Basta crear las distintas animaciones en el archivo hola.py, ya que las distintas animaciones se llaman desde los distintos class "Palabra"(Scene)
# Habría que ver si hay algún motivo para separar en distintos archivos.
El código viene como

class Chao(Scene):
    def construct(self):
        texto = Text("¡Chao, Manito!")
        self.play(Write(texto))
        self.wait(2)

la segunda línea debe ir sí o sí (al parecer se puede modificar self por otra palabra)