from manim import *

class BasicText(Scene):
	def construct(self):
		quadratic_formula = MathTex(
			"ax^2+bx+c=0","\\Leftrightarrow","x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}"
		)
		self.play(Write(quadratic_formula))
		self.wait(4)
