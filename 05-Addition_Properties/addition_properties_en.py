from manim import *
from manim.utils.rate_functions import ease_in_out_sine

SMALL_PADD = 2
BIG_PADD = 11

class AdditionProperties(Scene):
	def customPlay(self, *animations, run_time=2, rate_func=ease_in_out_sine, **kwargs):
		self.play(*animations, run_time=run_time, rate_func=rate_func, **kwargs)


	def construct(self):
		title = Text("Addition Properties").to_edge(UP)
		first_property = Text("1. Associative")
		second_property = Text("2. Cumulative")
		third_property = Text("3. Null Element")

		properties = [first_property, second_property, third_property]
		properties_group = VGroup(*properties)

		self.createMenu(title, properties_group)
		self.wait(4)
		self.associativeProperty(title, properties)
		self.bringMenuBack(title, properties_group)
		self.wait(4)
		self.cumulativeProperty(title, properties)
		self.bringMenuBack(title, properties_group)
		self.wait(4)
		self.nullElementProperty(title, properties)
		self.bringMenuBack(title, properties_group)
		self.wait(4)
		return

	# ------------------------- Associative Property --------------------------
	def associativeProperty(scene, title, properties):
		# Select only the Associative property title
		scene.customPlay(
			title.animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[0].animate.to_edge(UP),
			properties[1].animate.to_edge(DOWN).shift(DOWN * SMALL_PADD),
			properties[2].animate.to_edge(DOWN).shift(DOWN * SMALL_PADD)
		)

		scene.wait(4)

		# Removing everything in screen
		scene.customPlay(properties[0].animate.shift(RIGHT * BIG_PADD))
		return

	# -------------------------- Cumulative Property --------------------------
	def cumulativeProperty(scene, title, properties):
		scene.customPlay(
			title.animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[0].animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[1].animate.to_edge(UP),
			properties[2].animate.to_edge(DOWN).shift(DOWN * SMALL_PADD)
		)

		scene.wait(4)

		# Removing everything in screen
		scene.customPlay(properties[1].animate.shift(RIGHT * BIG_PADD))
		return

	# ------------------------- Null Element Property -------------------------
	def nullElementProperty(scene, title, properties):
		scene.customPlay(
			title.animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[0].animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[1].animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[2].animate.to_edge(UP)
		)

		scene.wait(4)

		# Removing everything in screen
		scene.customPlay(properties[2].animate.shift(RIGHT * BIG_PADD))
		return

	# ---------------------------- Menu Functions -----------------------------
	def createMenu(scene, title, properties):
		properties.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
		scene.play(Write(title), run_time=2)
		scene.wait(2)
		scene.play(Write(properties), run_time=4)
		return

	def bringMenuBack(scene, title, properties):
		# Reordering elements in the far left
		title.move_to(LEFT * BIG_PADD).to_edge(UP)
		properties.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
		properties.shift(LEFT * BIG_PADD)

		# Desloacte them to the scene
		scene.customPlay(
			title.animate.shift(RIGHT * BIG_PADD),
			properties.animate.shift(RIGHT * BIG_PADD),
		)
		return
