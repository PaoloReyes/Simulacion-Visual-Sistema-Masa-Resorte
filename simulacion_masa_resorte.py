from manim import *
import math

class Sim(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        c1 = 0.085
        c2 = 0.000278293773100543
        lamb = 0.4*10.5
        omega = 7.35*10.5
        f = lambda t : ((c1*math.e**(-lamb*t)*np.cos(np.sqrt(omega**2-lamb**2)*t)+ c2*math.e**(-lamb*t)*np.sin(np.sqrt(omega**2-lamb**2)*t))+0.13)*8

        axes = Axes(x_range=[0, 10], y_range=[0, 0.3, 0.1], x_length=20, y_length=0.5, tips=False)
        sin = lambda t : np.sin(10*t)
        s = axes.plot(sin, color=PURPLE).scale(0.3).rotate(np.pi/2)
        mass = Square(side_length=1.5, color=RED, fill_opacity=1).shift(3.5*UP)
        cont = Rectangle(width=3.5, height=6, color=BLACK, fill_color=BLUE, fill_opacity=0.4).shift(UP)
        cont.z_index=5
        self.add(cont, s)
        self.play(s.animate.shift(3*DOWN), mass.animate.shift(3*DOWN), rate_func=f, run_time=11)