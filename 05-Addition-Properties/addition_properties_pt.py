from manim import *

class AdditionProperties(Scene):
	def construct(self):
		title = Text("Propriedades da Soma")
		primeira_propriedade = Text("1. Associatividade")
		segunda_propriedade = Text("2. Cumulativa")
		terceira_propriedade = Text("3. Elemento Neutro")
		self.wait(10)

class AdditionExample(Scene):
	def construct(self):
		self.wait(10)
