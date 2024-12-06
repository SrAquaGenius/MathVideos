from manim import *
from manim.utils.rate_functions import ease_in_out_sine

SMALL_PADD = 2
SMALL2_PADD = 4
MEDDIUM_PADD = 6
BIG_PADD = 11

class AdditionProperties(Scene):
	def customPlay(self, *animations, run_time=1.5, rate_func=ease_in_out_sine, **kwargs):
		self.play(*animations, run_time=run_time, rate_func=rate_func, **kwargs)


	def construct(self):
		title = Text("Addition Properties").to_edge(UP)
		first_property = Text("1. Associative")
		second_property = Text("2. Commutative")
		third_property = Text("3. Null Element")

		properties = [first_property, second_property, third_property]
		properties_group = VGroup(*properties)

		self.createMenu(title, properties_group)
		self.wait(2)
		self.associativeProperty(title, properties)
		self.bringMenuBack(title, properties_group)
		self.wait(2)
		self.commutativeProperty(title, properties)
		self.bringMenuBack(title, properties_group)
		self.wait(2)
		self.nullElementProperty(title, properties)
		self.bringMenuBack(title, properties_group)
		self.wait(2)
		return

	# ------------------------- Associative Property --------------------------
	def associativeProperty(scene, title, properties):
		# Select only the Associative property title
		scene.customPlay(
			title.animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[0].animate.to_edge(UP),
			properties[1].animate.to_edge(DOWN).shift(DOWN * SMALL_PADD),
			properties[2].animate.to_edge(DOWN).shift(DOWN * (SMALL_PADD +0.7))
		)

		canonical = MathTex("a + (b + c)", "=", "(a + b) + c").shift(UP/2)
		example = MathTex("1 + (2 + 3)", "=", "(1 + 2) + 3").shift(DOWN/2)

		scene.customPlay(Write(canonical))
		scene.wait(2)
		scene.customPlay(Write(example))
		scene.wait(4)

		# Removing everything in screen
		scene.customPlay(
			properties[0].animate.shift(RIGHT * BIG_PADD),
			canonical.animate.shift(RIGHT * BIG_PADD),
			example.animate.shift(RIGHT * BIG_PADD)
		)
		return

	# ------------------------- Commutative Property --------------------------
	def commutativeProperty(scene, title, properties):
		scene.customPlay(
			title.animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[0].animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[1].animate.to_edge(UP),
			properties[2].animate.to_edge(DOWN).shift(DOWN * SMALL_PADD)
		)

		canonical = MathTex("a + b", "=", "b + a").shift(UP/2)
		example = MathTex("1 + 2", "=", "2 + 1").shift(DOWN/2)

		scene.customPlay(Write(canonical))
		scene.wait(2)
		scene.customPlay(Write(example))
		scene.wait(4)

		# Removing everything in screen
		scene.customPlay(
			properties[1].animate.shift(RIGHT * BIG_PADD),
			canonical.animate.shift(RIGHT * BIG_PADD),
			example.animate.shift(RIGHT * BIG_PADD)
		)
		return

	# ------------------------- Null Element Property -------------------------
	def nullElementProperty(scene, title, properties):
		scene.customPlay(
			title.animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[0].animate.to_edge(UP).shift(UP * (SMALL_PADD + 0.7)),
			properties[1].animate.to_edge(UP).shift(UP * SMALL_PADD),
			properties[2].animate.to_edge(UP)
		)

		canonical = MathTex("If\;", "a + b", "=", "a", ",\;so\;", "b = 0")
		null_element = Tex("Addition null element is 0")
		example = MathTex("1 + 0", "=", "1")

		lines = [canonical, null_element, example]
		lines_group = VGroup(*lines)

		lines_group.arrange(DOWN, buff=0.5)
		scene.play(Write(lines_group), run_time=4)
		scene.wait(4)

		# Removing everything in screen
		scene.customPlay(
			properties[2].animate.shift(RIGHT * BIG_PADD),
			lines_group.animate.shift(RIGHT * BIG_PADD)
		)
		return

	# ---------------------------- Menu Functions -----------------------------
	def createMenu(scene, title, properties):
		properties.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
		scene.play(Write(title), run_time=2)
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
