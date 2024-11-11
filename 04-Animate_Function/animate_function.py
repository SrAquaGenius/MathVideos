from manim import *

class AnimateFunction(Scene):
	def construct(self):
		# Setting up the axes
		axes = Axes(
			x_range=[-10, 10.3, 1],
			y_range=[-1.5, 1.5, 1],
			x_length=10,
			axis_config={"color": GREEN},
			x_axis_config={
				"numbers_to_include": np.arange(-10, 10.01, 2),
				"numbers_with_elongated_ticks": np.arange(-10,10.01, 2),
			},
			tips=False,
		)
		axes_labels = axes.get_axis_labels()

		# Value tracker for the moving dot
		t = ValueTracker(-10)

		# Define the function to plot
		def func(x):
			return np.sin(x)

		# Plotting the function
		func_graph = axes.plot(func, color=BLUE)

		# Initial point and dot on the function graph
		dot = Dot().move_to(axes.c2p(t.get_value(), func(t.get_value())))
		dot.add_updater(lambda d: d.move_to(axes.c2p(t.get_value(), func(t.get_value()))))

		# Add dynamic coordinates for the dot
		x_label = always_redraw(lambda: MathTex(f"x = {t.get_value():.2f}")
								.next_to(dot, DOWN, buff=0.3))
		y_label = always_redraw(lambda: MathTex(f"y = {func(t.get_value()):.2f}")
								.next_to(dot, LEFT, buff=0.3))

		# Path trace for the dot's movement
		path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=4)

		# Vertical and horizontal lines from dot to axes
		h_line = always_redraw(lambda: axes.get_horizontal_line(dot.get_bottom(), color=GRAY))
		v_line = always_redraw(lambda: axes.get_vertical_line(dot.get_left(), color=GRAY))

		# Add all elements to the scene
		self.add(axes, axes_labels, func_graph, dot, x_label, y_label, path, h_line, v_line)

		# Animate the dot moving along the function
		self.play(t.animate.set_value(10), run_time=8, rate_func=linear)

		self.wait(2)
