from manim import *

class BasicShapes(Scene):
	def construct(self):
		# Create a circle and square
		circle = Circle()  # Create a circle
		square = Square(color=BLUE, fill_opacity=1)  # Create a square
		
		# Position the square to the right of the circle
		square.next_to(circle, RIGHT)
		
		# Create a text object
		text = Text("Hello, Manim!")
		
		# Position the text below the circle and square
		text.next_to(circle, DOWN)

		# Add the shapes and text to the scene
		self.play(Create(circle), Create(square), Write(text))
		self.wait(2)  # Wait for 2 seconds

		self.play(square.animate.shift(LEFT))
		self.play(square.animate.set_fill(ORANGE))
		self.play(square.animate.scale(0.3))
		self.play(square.animate.rotate(0.4))

		self.wait(2)  # Wait for 2 seconds
