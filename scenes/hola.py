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
        #Seteo del color de fondo
        self.camera.background_color = ManimColor("#012121")
        #colocar el cuadrículado de fondo, quitar en versión final
        #ax = NumberPlane(y_range=[-1, 7], background_line_style={"stroke_opacity": 0.4})
        #variable temp
        t=ValueTracker(0)
        #ecuación de balance energético
        eqtext=MathTex(r"\Delta E=0")
        eqtext.to_corner(UL) #deja en superior izquierda del cuadro original, si no calza es por config.frame_width
        #elementos fijos
        piso=Square(side_length=20.0, color=ManimColor("#7A8A02")).set_fill(ManimColor("#7A8A02"),opacity=1).shift(14*DOWN)
        mesa=Rectangle(color=ManimColor("#FF8F44"), height=0.8, width=6).move_to([-7,0,0]).set_fill(ManimColor("#FF8F44"),opacity=1)
        mesa1=Rectangle(color=ManimColor("#FF8F44"), height=3.9, width=0.5).move_to([-8.8,-2.1,0]).set_fill(ManimColor("#FF8F44"),opacity=1)
        mesa2=Rectangle(color=ManimColor("#FF8F44"), height=3.9, width=0.5).move_to([-4.8,-2.1,0]).set_fill(ManimColor("#FF8F44"),opacity=1)
        polea=Circle(radius=0.5,color=("#449BFF")).move_to([-3.5,0.5,0]).set_fill(ManimColor("#449BFF"),opacity=1)
        soporte=Triangle(color=ManimColor("#1F211F")).scale(0.6).rotate(70*DEGREES).move_to([-4,0.1,0]).set_fill(ManimColor("#FF8F44"),opacity=1)
        #cronómetro                                                                      
        unidad=MathTex(r"[\text{s}]")
        unidad.to_corner(UR) #esto crear la unidad de medida y la ubica en la esquina superior (UP) derecha (RIGHT)
        temptext=Variable(
            t.get_value(), MathTex(r"t"), num_decimal_places = 2
        ).add_updater(lambda y: y.next_to(unidad, LEFT))
        temptext.add_updater(lambda q: q.tracker.set_value(t.get_value()))
        bloquehor = always_redraw(
                 lambda: Square(side_length=1, color=GREEN).move_to([0.5*t.get_value()**2-8,0.8,0]).set_fill(ManimColor("#88FF44"), opacity=1)
        )
        cuerda1 =always_redraw(
                         lambda: Line(start=[-3.5,1,0], end=[0.5*t.get_value()**2-7.5,1,0], color=BLUE, buff=0)
                )
        bloquever = always_redraw(
                         lambda: Square(side_length=1, color=RED).move_to([-3,-1-0.5*t.get_value()**2,0]).set_fill(ManimColor("#FF7644"), opacity=1)
                )
        cuerdav =always_redraw(
                                 lambda: Line(start=[-3,0.5,0], end=[-3,-0.5-0.5*t.get_value()**2,0], color=BLUE, buff=0)
                        )
        desptext=MathTex(r"\vec{D}").add_updater(lambda y: y.move_to([t.get_value()-4.8,1.5*t.get_value()-0.5*t.get_value()**2-4.3,0]))
        self.add(mesa,mesa1,mesa2,polea,soporte,bloquehor,cuerda1,eqtext,temptext,unidad,piso,bloquever,cuerdav)
        self.play(
                    t.animate.set_value(2.3), #define a que valor se cambia t
                    run_time=2, #cuantos segundos dura la animación, vale 1 si se omite la línea
                    rate_func=linear #velocidad de cambio constante, puede hacerse un ida y vuelta, animación suave (por defecto), etc.
                )
        self.wait()

#uv run manim -pql scenes/hola.py FzasConsGPT
class FzasConsGPT(Scene):
    def construct(self):

        # --------------------------------------------------
        # 1. CONFIGURACIÓN GENERAL
        # --------------------------------------------------

        self.camera.background_color = "#071B24"

        AZUL = "#449BFF"
        NARANJA = "#FF984F"
        VERDE = "#A5E65A"
        ROJO = "#FF684F"
        BLANCO = "#F2F5F7"
        GRIS = "#8CA3AD"

        t = ValueTracker(0)

        # Cuadrícula de fondo
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            background_line_style={
                "stroke_color": "#45616B",
                "stroke_opacity": 0.18,
                "stroke_width": 1
            },
            axis_config={"stroke_opacity": 0}
        )

        self.add(grid)

        # --------------------------------------------------
        # 2. TÍTULO Y ECUACIÓN
        # --------------------------------------------------

        titulo = Text(
            "SISTEMA DE BLOQUES Y POLEA",
            font_size=28,
            color=BLANCO,
            weight=BOLD
        ).to_corner(UL).shift(DOWN * 0.25 + RIGHT * 0.2)

        eqtext = MathTex(
            r"\Delta E = 0",
            color=VERDE,
            font_size=38
        ).next_to(titulo, DOWN, aligned_edge=LEFT)

        self.play(
            FadeIn(titulo, shift=DOWN),
            Write(eqtext),
            run_time=1.5
        )

        # --------------------------------------------------
        # 3. ESTRUCTURA MECÁNICA
        # --------------------------------------------------

        # Piso
        piso = Line(
            [-9, -3, 0],
            [9, -3, 0],
            color=GRIS,
            stroke_width=5
        )

        # Mesa
        mesa = Rectangle(
            width=6,
            height=0.35,
            color=NARANJA,
            fill_color=NARANJA,
            fill_opacity=1
        ).move_to([-7, 0, 0])

        pata1 = Rectangle(
            width=0.35,
            height=2.85,
            color=NARANJA,
            fill_color=NARANJA,
            fill_opacity=1
        ).move_to([-8.8, -1.6, 0])

        pata2 = Rectangle(
            width=0.35,
            height=2.85,
            color=NARANJA,
            fill_color=NARANJA,
            fill_opacity=1
        ).move_to([-5.2, -1.6, 0])

        # Soporte de la polea
        soporte = Polygon(
            [-4.15, 0.15, 0],
            [-3.55, 0.15, 0],
            [-3.85, 0.85, 0],
            color=NARANJA,
            fill_color=NARANJA,
            fill_opacity=1
        )

        # Polea
        polea = Circle(
            radius=0.5,
            color=AZUL,
            stroke_width=5,
            fill_color="#173D5C",
            fill_opacity=1
        ).move_to([-3.5, 0.5, 0])

        eje = Dot(
            [-3.5, 0.5, 0],
            radius=0.09,
            color=BLANCO
        )

        estructura = VGroup(
            piso, mesa, pata1, pata2, soporte, polea, eje
        )

        self.play(
            FadeIn(estructura),
            run_time=1.5
        )

        # --------------------------------------------------
        # 4. BLOQUES
        # --------------------------------------------------

        # Bloque horizontal
        bloquehor = always_redraw(
            lambda: Square(
                side_length=1,
                color=VERDE,
                stroke_width=3,
                fill_color="#355D2B",
                fill_opacity=1
            ).move_to([
                0.5 * t.get_value()**2 - 8,
                0.8,
                0
            ])
        )

        # Bloque vertical
        bloquever = always_redraw(
            lambda: Square(
                side_length=1,
                color=ROJO,
                stroke_width=3,
                fill_color="#71392F",
                fill_opacity=1
            ).move_to([
                -3,
                -1 - 0.5 * t.get_value()**2,
                0
            ])
        )

        # Etiquetas de los bloques
        etiqueta_h = MathTex("m_1", color=BLANCO).scale(0.7)
        etiqueta_h.add_updater(
            lambda m: m.move_to(bloquehor.get_center())
        )

        etiqueta_v = MathTex("m_2", color=BLANCO).scale(0.7)
        etiqueta_v.add_updater(
            lambda m: m.move_to(bloquever.get_center())
        )

        # --------------------------------------------------
        # 5. CUERDAS
        # --------------------------------------------------

        cuerda1 = always_redraw(
            lambda: Line(
                [-3.5, 1, 0],
                [
                    0.5 * t.get_value()**2 - 7.5,
                    1,
                    0
                ],
                color=BLANCO,
                stroke_width=3
            )
        )

        cuerda2 = always_redraw(
            lambda: Line(
                [-3, 0.5, 0],
                [
                    -3,
                    -0.5 - 0.5 * t.get_value()**2,
                    0
                ],
                color=BLANCO,
                stroke_width=3
            )
        )

        # --------------------------------------------------
        # 6. VECTOR DE DESPLAZAMIENTO
        # --------------------------------------------------

        desplazamiento = always_redraw(
            lambda: Arrow(
                start=[-7.8, 1.6, 0],
                end=[
                    0.5 * t.get_value()**2 - 7.8,
                    1.6,
                    0
                ],
                buff=0,
                color=VERDE,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.15
            )
        )

        etiqueta_d = MathTex(
            r"\vec{d}",
            color=VERDE
        ).scale(0.8).add_updater(
            lambda m: m.next_to(desplazamiento, UP, buff=0.1)
        )

        # --------------------------------------------------
        # 7. CRONÓMETRO
        # --------------------------------------------------

        unidad = MathTex(
            r"\text{s}",
            color=BLANCO
        ).scale(0.8).to_corner(UR).shift(
            DOWN * 0.4 + LEFT * 0.25
        )

        reloj = Variable(
            t.get_value(),
            MathTex("t"),
            num_decimal_places=2,
            color=BLANCO
        )

        reloj.add_updater(
            lambda m: m.tracker.set_value(t.get_value())
        )

        reloj.scale(0.9)
        reloj.next_to(unidad, LEFT, buff=0.15)

        # --------------------------------------------------
        # 8. INCORPORAR ELEMENTOS
        # --------------------------------------------------

        self.play(
            Create(cuerda1),
            Create(cuerda2),
            FadeIn(bloquehor),
            FadeIn(bloquever),
            run_time=1.5
        )

        self.play(
            FadeIn(etiqueta_h),
            FadeIn(etiqueta_v),
            FadeIn(reloj),
            FadeIn(unidad),
            run_time=1
        )

        self.play(
            GrowArrow(desplazamiento),
            FadeIn(etiqueta_d),
            run_time=1
        )

        # --------------------------------------------------
        # 9. ANIMACIÓN PRINCIPAL
        # --------------------------------------------------

        self.play(
            t.animate.set_value(2.3),
            run_time=5,
            rate_func=linear
        )

        self.wait(2)
