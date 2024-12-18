from manim import *

class BasicFunction(Scene):
	def construct(self):
		axes = Axes(
			x_range=[-15, 15.3, 1],
			y_range=[-1.5, 1.5, 1],
			x_length=10,
			axis_config={"color": GREEN},
			x_axis_config={
				# "numbers_to_include": np.arange(-10, 10.01, 2),
				"numbers_with_elongated_ticks": np.arange(-15,15.01, 2),
			},
			tips=False,
		)
		axes_labels = axes.get_axis_labels()
		sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
		cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

		sin_label = axes.get_graph_label(sin_graph, label="\\sin(x)")
		cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

		# vert_line = axes.get_vertical_line(
		# 	axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
		# )
		# line_label = axes.get_graph_label(
		# 	cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
		# )

		# plot = VGroup(axes, sin_graph, cos_graph, vert_line)
		plot = VGroup(axes, sin_graph, cos_graph)
		# labels = VGroup(axes_labels, sin_label, cos_label, line_label)
		labels = VGroup(axes_labels, sin_label, cos_label)
		self.add(plot, labels)

		self.wait(5)
