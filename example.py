from manim import *
# from manim.mobject.geometry.geometric_shapes import Gear


class ClientServerAPI(Scene):
    def construct(self):
        # CLIENT (Computer)
        client_box = RoundedRectangle(
            corner_radius=0.2, width=2, height=1.2, color=BLUE_B, fill_opacity=0.7)
        client_screen = Rectangle(width=1.4, height=0.7, color=WHITE, fill_opacity=0.9).move_to(
            client_box.get_center() + UP*0.1)
        client_base = Rectangle(width=0.8, height=0.15, color=GREY_B, fill_opacity=0.8).next_to(
            client_box, DOWN, buff=0.05)
        client_label = Text("Client", font_size=28).next_to(
            client_box, DOWN, buff=0.3)
        client_group = VGroup(client_box, client_screen,
                              client_base, client_label).move_to(LEFT*4)

        # SERVER (DB Cylinder)
        server_cylinder = Cylinder(
            radius=0.7, height=1.2, direction=OUT, color=GREEN_B, fill_opacity=0.8)
        server_label = Text("Server", font_size=28).next_to(
            server_cylinder, DOWN, buff=0.3)
        server_group = VGroup(server_cylinder, server_label).move_to(RIGHT*0.5)

        # API (Box with cogs and screws)
        api_box = RoundedRectangle(
            corner_radius=0.15, width=2, height=1.2, color=YELLOW_B, fill_opacity=0.7)
        # Gear is not available in standard Manim, using Circle as placeholder
        cog1 = Circle(radius=0.25, color=GREY_B, fill_opacity=1).move_to(
            api_box.get_center() + LEFT*0.4 + UP*0.2)
        cog2 = Circle(radius=0.18, color=GREY_B, fill_opacity=1).move_to(
            api_box.get_center() + RIGHT*0.3 + DOWN*0.2)
        screw1 = Dot(color=GREY_B).scale(1.2).move_to(
            api_box.get_corner(UL) + DOWN*0.15 + RIGHT*0.15)
        screw2 = Dot(color=GREY_B).scale(1.2).move_to(
            api_box.get_corner(UR) + DOWN*0.15 + LEFT*0.15)
        screw3 = Dot(color=GREY_B).scale(1.2).move_to(
            api_box.get_corner(DL) + UP*0.15 + RIGHT*0.15)
        screw4 = Dot(color=GREY_B).scale(1.2).move_to(
            api_box.get_corner(DR) + UP*0.15 + LEFT*0.15)
        api_label = Text("API", font_size=28).next_to(api_box, DOWN, buff=0.3)
        api_group = VGroup(api_box, cog1, cog2, screw1, screw2,
                           screw3, screw4, api_label).move_to(RIGHT*4)

        # Arrows
        arrow1 = Arrow(client_group.get_right(),
                       server_group.get_left(), buff=0.2, color=BLUE_B)
        arrow2 = Arrow(server_group.get_right(),
                       api_group.get_left(), buff=0.2, color=GREEN_B)
        arrow3 = Arrow(api_group.get_left(), server_group.get_right(),
                       buff=0.2, color=YELLOW_B).flip()
        arrow4 = Arrow(server_group.get_left(),
                       client_group.get_right(), buff=0.2, color=PURPLE_B).flip()

        # Labels for arrows
        label1 = Text("Request", font_size=22, color=BLUE_B).next_to(
            arrow1, UP, buff=0.1)
        label2 = Text("Query", font_size=22, color=GREEN_B).next_to(
            arrow2, UP, buff=0.1)
        label3 = Text("Response", font_size=22, color=YELLOW_B).next_to(
            arrow3, DOWN, buff=0.1)
        label4 = Text("Result", font_size=22, color=PURPLE_B).next_to(
            arrow4, DOWN, buff=0.1)

        # Animation sequence
        self.play(FadeIn(client_group), FadeIn(
            server_group), FadeIn(api_group))
        self.wait(0.5)
        self.play(GrowArrow(arrow1), FadeIn(label1))
        self.wait(0.3)
        self.play(GrowArrow(arrow2), FadeIn(label2))
        self.wait(0.3)
        self.play(GrowArrow(arrow3), FadeIn(label3))
        self.wait(0.3)
        self.play(GrowArrow(arrow4), FadeIn(label4))
        self.wait(0.5)

        # Animate cogs spinning for extravagance
        self.play(Rotate(cog1, angle=2*PI),
                  Rotate(cog2, angle=-2*PI), run_time=2)
        self.wait(1)

        # Highlight flow
        for arrow, color in zip([arrow1, arrow2, arrow3, arrow4], [BLUE_B, GREEN_B, YELLOW_B, PURPLE_B]):
            self.play(Indicate(arrow, color=color), run_time=0.5)
        self.wait(1)

# Note: You need to provide a cog SVG at "Mobject/cog.svg" or replace with manim's built-in cogs if available.
