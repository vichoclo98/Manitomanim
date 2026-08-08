from manim import *

#uv run manim -pql scenes/hola.py Lanzamiento
class Lanzamiento(Scene):
    def construct(self):
        t=ValueTracker(0)
        eqtext=MathTex(r"\vec{d}=\vec{v}\cdot t+\frac{\vec{g}\cdot t^2}{2}").add_updater(lambda q: q.move_to([-4.5,3.3,0]))
        circle = always_redraw(
                 lambda: Circle(radius=0.15, color=GREEN).move_to([2*t.get_value()-4,3*t.get_value()-1*t.get_value()**2-3,0]).set_fill(ManimColor("#88FF44"), opacity=1)  # set the color and transparency
        )
        puntofalso= always_redraw(
                 lambda: Dot(radius=0).move_to([t.get_value()-4,1.5*t.get_value()-3,0])
        )
        velocidad =always_redraw(
                 lambda: Arrow(start=[-4,-3,0], end=[2*t.get_value()-4,3*t.get_value()-3,0], color=BLUE)
        )
        aceleración =always_redraw(
                         lambda: Arrow(start=[2*t.get_value()-4,3*t.get_value()-3,0], end=[2*t.get_value()-4,3*t.get_value()-1*t.get_value()**2-3,0], color=RED)
                )
        distancia =always_redraw(
                                 lambda: Arrow(start=[-4,-3,0], end=[2*t.get_value()-4,3*t.get_value()-1*t.get_value()**2-3,0], color=WHITE)
                        )
        trazo=TracedPath(circle.get_center)
        velotext=MathTex(r"\vec{v}\cdot t").add_updater(lambda m: m.next_to(puntofalso, LEFT))
        acetext=MathTex(r"\frac{\vec{g}\cdot t^2}{2}").add_updater(lambda x: x.next_to(aceleración, RIGHT))
        desptext=MathTex(r"\vec{d}").add_updater(lambda y: y.move_to([t.get_value()-3.8,1.5*t.get_value()-0.5*t.get_value()**2-3.3,0]))
        self.add(trazo,puntofalso,eqtext)
        self.play(FadeIn(circle))
        self.add(velocidad,aceleración,distancia,velotext,acetext,desptext)
        self.play(
	        t.animate.set_value(3), #define a que valor se cambia t
	        run_time=4, #cuantos segundos dura la animación, vale 1 si se omite la línea
	        rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
        )
        self.wait()
