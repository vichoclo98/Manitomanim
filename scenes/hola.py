from manim import *
config.frame_width = 20 #se puede regular para hacer zoom, mantiene aspect ratio
#uv run manim -pql scenes/hola.py Lanzamiento
class Lanzamiento(Scene):
    def construct(self):
        self.camera.background_color = ManimColor("#012121")
        t=ValueTracker(0)
        eqtext=MathTex(r"\vec{D}=\vec{v}_0\cdot t+\frac{1}{2}\vec{g}\cdot t^2")
        eqtext.to_corner(UL) #deja en superior izquierda del cuadro original, si no calza es por config.frame_width
        piso=Square(side_length=20.0, color=ManimColor("#7A8A02")).set_fill(ManimColor("#7A8A02"),opacity=1).shift(14*DOWN)
        unidad=MathTex(r"[\text{s}]")
        unidad.to_corner(UR) #esto crear la unidad de medida y la ubica en la esquina superior (UP) derecha (RIGHT)
        temptext=Variable(
            t.get_value(), MathTex(r"t"), num_decimal_places = 2
        ).add_updater(lambda y: y.next_to(unidad, LEFT))
        temptext.add_updater(lambda q: q.tracker.set_value(t.get_value()))
        circle = always_redraw(
                 lambda: Circle(radius=0.15, color=GREEN).move_to([2*t.get_value()-5,3*t.get_value()-1*t.get_value()**2-4,0]).set_fill(ManimColor("#88FF44"), opacity=1)  # set the color and transparency
        )
        puntofalso= always_redraw(
                 lambda: Dot(radius=0).move_to([t.get_value()-5,1.5*t.get_value()-4,0])
        )
        velocidad =always_redraw(
                 lambda: Arrow(start=[-5,-4,0], end=[2*t.get_value()-5,3*t.get_value()-4,0], color=BLUE, buff=0)
        )
        aceleración =always_redraw(
                         lambda: Arrow(start=[2*t.get_value()-5,3*t.get_value()-4.0,0], end=[2*t.get_value()-5,3*t.get_value()-(t.get_value()**2)-4.0,0], color=RED,buff=0)
                )
        #distancia =always_redraw(
        #                         lambda: Arrow(start=[-4,-3,0], end=[2*t.get_value()-4,3*t.get_value()-1*t.get_value()**2-3,0], color=WHITE)
        #                )
        distancia1 = Arrow(start=[-5,-4,0], end=[-3.5,-2.3124,0], color=WHITE, buff=0)
        distancia2 = Arrow(start=[-5,-4,0], end=[-0.5,-2.3125,0], color=WHITE, buff=0)
        trazo=TracedPath(circle.get_center)
        velotext=MathTex(r"\vec{v}_0\cdot t",color=BLUE).add_updater(lambda m: m.next_to(puntofalso, LEFT))
        acetext=MathTex(r"\frac{1}{2}\vec{g}\cdot t^2",color=RED).add_updater(lambda x: x.next_to(aceleración, RIGHT))
        desptext=MathTex(r"\vec{D}").add_updater(lambda y: y.move_to([t.get_value()-4.8,1.5*t.get_value()-0.5*t.get_value()**2-4.3,0]))
        self.add(trazo,puntofalso,eqtext,temptext,unidad,piso)
        self.play(FadeIn(circle))
        self.add(velocidad,aceleración,velotext,acetext)
        self.play(
	        t.animate.set_value(0.75), #define a que valor se cambia t
	        run_time=2, #cuantos segundos dura la animación, vale 1 si se omite la línea
	        rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
        )
        self.play(Write(distancia1),FadeIn(desptext))
        self.wait()
        self.play(FadeOut(distancia1),FadeOut(desptext))
        self.play(
                    t.animate.set_value(2.25), #define a que valor se cambia t
                    run_time=4, #cuantos segundos dura la animación, vale 1 si se omite la línea
                    rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
                )
        self.play(Write(distancia2),FadeIn(desptext))
        self.wait()
        self.play(FadeOut(distancia2),FadeOut(desptext))
        self.play(
                    t.animate.set_value(2.99), #define a que valor se cambia t
                    run_time=2, #cuantos segundos dura la animación, vale 1 si se omite la línea
                    rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
                )
        self.wait()
#uv run manim -pql scenes/hola.py FzasCons
class FzasCons(Scene):
    def construct(self):
        self.camera.background_color = ManimColor("#012121")
        t=ValueTracker(0)
        eqtext=MathTex(r"\Delta E=0")
        eqtext.to_corner(UL) #deja en superior izquierda del cuadro original, si no calza es por config.frame_width
        piso=Square(side_length=20.0, color=ManimColor("#7A8A02")).set_fill(ManimColor("#7A8A02"),opacity=1).shift(14*DOWN)
        unidad=MathTex(r"[\text{s}]")
        unidad.to_corner(UR) #esto crear la unidad de medida y la ubica en la esquina superior (UP) derecha (RIGHT)
        temptext=Variable(
            t.get_value(), MathTex(r"t"), num_decimal_places = 2
        ).add_updater(lambda y: y.next_to(unidad, LEFT))
        temptext.add_updater(lambda q: q.tracker.set_value(t.get_value()))
        bloquehor = always_redraw(
                 lambda: Square(side_length=1, color=GREEN).move_to([t.get_value()**2-5,4,0]).set_fill(ManimColor("#88FF44"), opacity=1)  # set the color and transparency
        )
        bloquever = always_redraw(
                         lambda: Square(side_length=1, color=RED).move_to([-4,3*t.get_value()-1*t.get_value()**2-4,0]).set_fill(ManimColor("#FF7644"), opacity=1)  # set the color and transparency
                )
        puntofalso= always_redraw(
                 lambda: Dot(radius=0).move_to([t.get_value()-5,1.5*t.get_value()-4,0])
        )
        velocidad =always_redraw(
                 lambda: Arrow(start=[-5,-4,0], end=[2*t.get_value()-5,3*t.get_value()-4,0], color=BLUE, buff=0)
        )
        aceleración =always_redraw(
                         lambda: Arrow(start=[2*t.get_value()-5,3*t.get_value()-4.0,0], end=[2*t.get_value()-5,3*t.get_value()-(t.get_value()**2)-4.0,0], color=RED,buff=0)
                )
        #distancia =always_redraw(
        #                         lambda: Arrow(start=[-4,-3,0], end=[2*t.get_value()-4,3*t.get_value()-1*t.get_value()**2-3,0], color=WHITE)
        #                )
        distancia1 = Arrow(start=[-5,-4,0], end=[-3.5,-2.3124,0], color=WHITE, buff=0)
        distancia2 = Arrow(start=[-5,-4,0], end=[-0.5,-2.3125,0], color=WHITE, buff=0)
        velotext=MathTex(r"\vec{v}_0\cdot t",color=BLUE).add_updater(lambda m: m.next_to(puntofalso, LEFT))
        acetext=MathTex(r"\frac{1}{2}\vec{g}\cdot t^2",color=RED).add_updater(lambda x: x.next_to(aceleración, RIGHT))
        desptext=MathTex(r"\vec{D}").add_updater(lambda y: y.move_to([t.get_value()-4.8,1.5*t.get_value()-0.5*t.get_value()**2-4.3,0]))
        self.add(bloquehor,puntofalso,eqtext,temptext,unidad,piso,bloquever)
        self.add(velocidad,aceleración,velotext,acetext)
        self.play(
	        t.animate.set_value(0.75), #define a que valor se cambia t
	        run_time=2, #cuantos segundos dura la animación, vale 1 si se omite la línea
	        rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
        )
        self.play(Write(distancia1),FadeIn(desptext))
        self.wait()
        self.play(FadeOut(distancia1),FadeOut(desptext))
        self.play(
                    t.animate.set_value(2.25), #define a que valor se cambia t
                    run_time=4, #cuantos segundos dura la animación, vale 1 si se omite la línea
                    rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
                )
        self.play(Write(distancia2),FadeIn(desptext))
        self.wait()
        self.play(FadeOut(distancia2),FadeOut(desptext))
        self.play(
                    t.animate.set_value(2.99), #define a que valor se cambia t
                    run_time=2, #cuantos segundos dura la animación, vale 1 si se omite la línea
                    rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
                )
        self.wait()