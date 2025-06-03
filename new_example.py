from manim import *

# Constants
EARTH_ORBIT_RADIUS = 3.5
EARTH_RADIUS = 0.4
AXIAL_TILT = 23.5 * DEGREES  # 23.5 degrees in radians


class EarthSeasonsAnimation(Scene):
    def construct(self):
        # --------------------
        # Scene 1: Introduction to Earth's Orbit
        # --------------------
        # Sun at center
        sun = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun_label = Text("The Sun", color=WHITE).next_to(sun, DOWN, buff=0.3)

        # Earth's orbital path
        orbit = Circle(radius=EARTH_ORBIT_RADIUS,
                       color=WHITE, stroke_opacity=0.5)

        orbit_label = Text("Earth's Orbit", color=WHITE).next_to(
            orbit, UP, buff=0.3)

        # Earth at starting point (right of Sun)
        earth = Circle(radius=EARTH_RADIUS, color=BLUE,
                       fill_opacity=1.0).shift(RIGHT * EARTH_ORBIT_RADIUS)
        earth_label = Text("Earth", color=WHITE).next_to(earth, DOWN, buff=0.2)

        # Draw orbit
        self.play(Create(orbit), FadeIn(orbit_label))
        self.wait(0.5)

        # Draw Sun
        self.play(FadeIn(sun), FadeIn(sun_label))
        self.wait(0.5)

        # Draw Earth and label
        self.play(FadeIn(earth), FadeIn(earth_label))
        self.wait(0.5)

        # Animate Earth revolution
        self.play(
            MoveAlongPath(earth, orbit, rate_func=linear, run_time=4),
            MoveAlongPath(earth_label, orbit, rate_func=linear, run_time=4),
        )
        self.wait(1)

        # Fade out Scene 1 elements
        self.play(
            FadeOut(earth), FadeOut(earth_label),
            FadeOut(sun), FadeOut(sun_label),
            FadeOut(orbit), FadeOut(orbit_label),
        )
        self.wait(0.5)

        # --------------------
        # Scene 2: Earth's Axial Tilt
        # --------------------
        # Zoom in on Earth (larger)
        earth2 = Circle(radius=1.0, color=BLUE, fill_opacity=1.0)
        axis = Line(-UP * 1.2, DOWN * 1.2,
                    color=RED).rotate(AXIAL_TILT, about_point=ORIGIN)
        tilt_arc = Arc(start_angle=PI / 2 - AXIAL_TILT,
                       angle=AXIAL_TILT, radius=1.0, color=WHITE)
        angle_label = MathTex("23.5^\\circ", color=WHITE).next_to(
            tilt_arc, UP, buff=0.1)
        axis_label = Text("Earth's Axis", color=WHITE).next_to(
            axis.get_end(), UP, buff=0.1)

        self.play(FadeIn(earth2))
        self.wait(0.3)
        self.play(Create(axis), FadeIn(axis_label))
        self.wait(0.3)
        self.play(Create(tilt_arc), Write(angle_label))
        self.wait(0.5)
        self.play(Rotate(earth2, angle=2 * PI,
                  about_point=ORIGIN, run_time=3, rate_func=linear))
        self.wait(0.5)

        # Fade out Scene 2 elements
        self.play(
            FadeOut(earth2), FadeOut(axis), FadeOut(axis_label),
            FadeOut(tilt_arc), FadeOut(angle_label)
        )
        self.wait(0.5)

        # --------------------
        # Scene 3: Summer Solstice (Northern Hemisphere)
        # --------------------
        # Add Sun and orbit back
        sun3 = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun3_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit3 = Circle(radius=EARTH_ORBIT_RADIUS,
                        color=WHITE, stroke_opacity=0.5)
        self.add(sun3, sun3_label, orbit3)

        # Earth moving into June position
        start_earth3 = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0).move_to(
            RIGHT * EARTH_ORBIT_RADIUS)
        earth3_label = Text("Earth", color=WHITE).next_to(
            start_earth3, UP, buff=0.1)
        self.play(FadeIn(start_earth3), FadeIn(earth3_label))
        self.wait(0.3)
        self.play(
            MoveAlongPath(start_earth3, orbit3, rate_func=linear, run_time=2),
            MoveAlongPath(earth3_label, orbit3, rate_func=linear, run_time=2),
        )
        self.remove(start_earth3, earth3_label)

        # Earth at top (June Solstice)
        earth3 = Circle(radius=EARTH_RADIUS, color=BLUE,
                        fill_opacity=1.0).move_to(UP * EARTH_ORBIT_RADIUS)
        axis3 = Line(
            earth3.get_center() + UP * EARTH_RADIUS * 1.2,
            earth3.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth3.get_center())

        # Sunlight rays from below
        sunlight3 = VGroup(*[
            Line(
                start=DOWN * 6 + RIGHT * i * 0.5,
                end=earth3.get_center() + RIGHT * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            for i in range(-3, 4)
        ])

        nh_summer = Text("Northern Hemisphere: Summer",
                         color=WHITE).to_edge(LEFT).shift(UP * 2)
        sh_winter = Text("Southern Hemisphere: Winter",
                         color=WHITE).to_edge(LEFT).shift(DOWN * 2)
        solstice_label3 = Text("June Solstice", color=WHITE).to_edge(DOWN)

        self.play(FadeIn(earth3), Create(axis3))
        self.wait(0.3)
        self.play(Create(sunlight3))
        self.wait(0.3)
        self.play(FadeIn(nh_summer), FadeIn(sh_winter), Write(solstice_label3))
        self.wait(1)

        # Fade out Scene 3 elements
        self.play(
            FadeOut(earth3), FadeOut(axis3),
            FadeOut(sunlight3),
            FadeOut(nh_summer), FadeOut(sh_winter), FadeOut(solstice_label3),
            FadeOut(sun3), FadeOut(sun3_label), FadeOut(orbit3)
        )
        self.wait(0.5)

        # --------------------
        # Scene 4: Winter Solstice (Northern Hemisphere)
        # --------------------
        sun4 = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun4_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit4 = Circle(radius=EARTH_ORBIT_RADIUS,
                        color=WHITE, stroke_opacity=0.5)
        self.add(sun4, sun4_label, orbit4)

        # Earth moves from top to bottom
        start_earth4 = Circle(radius=EARTH_RADIUS, color=BLUE,
                              fill_opacity=1.0).move_to(UP * EARTH_ORBIT_RADIUS)
        earth4_label = Text("Earth", color=WHITE).next_to(
            start_earth4, UP, buff=0.1)
        self.play(FadeIn(start_earth4), FadeIn(earth4_label))
        self.wait(0.3)
        self.play(
            MoveAlongPath(start_earth4, orbit4, rate_func=linear, run_time=2),
            MoveAlongPath(earth4_label, orbit4, rate_func=linear, run_time=2),
        )
        self.remove(start_earth4, earth4_label)

        # Earth at bottom (December Solstice)
        earth4 = Circle(radius=EARTH_RADIUS, color=BLUE,
                        fill_opacity=1.0).move_to(DOWN * EARTH_ORBIT_RADIUS)
        axis4 = Line(
            earth4.get_center() + UP * EARTH_RADIUS * 1.2,
            earth4.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(-AXIAL_TILT, about_point=earth4.get_center())

        # Sunlight rays from above
        sunlight4 = VGroup(*[
            Line(
                start=UP * 6 + RIGHT * i * 0.5,
                end=earth4.get_center() + RIGHT * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            for i in range(-3, 4)
        ])

        nh_winter = Text("Northern Hemisphere: Winter",
                         color=WHITE).to_edge(LEFT).shift(UP * 2)
        sh_summer = Text("Southern Hemisphere: Summer",
                         color=WHITE).to_edge(LEFT).shift(DOWN * 2)
        solstice_label4 = Text("December Solstice", color=WHITE).to_edge(DOWN)

        self.play(FadeIn(earth4), Create(axis4))
        self.wait(0.3)
        self.play(Create(sunlight4))
        self.wait(0.3)
        self.play(FadeIn(nh_winter), FadeIn(sh_summer), Write(solstice_label4))
        self.wait(1)

        # Fade out Scene 4 elements
        self.play(
            FadeOut(earth4), FadeOut(axis4),
            FadeOut(sunlight4),
            FadeOut(nh_winter), FadeOut(sh_summer), FadeOut(solstice_label4),
            FadeOut(sun4), FadeOut(sun4_label), FadeOut(orbit4)
        )
        self.wait(0.5)

        # --------------------
        # Scene 5: Equinoxes (Spring & Fall)
        # --------------------
        sun5 = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun5_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit5 = Circle(radius=EARTH_ORBIT_RADIUS,
                        color=WHITE, stroke_opacity=0.5)
        self.add(sun5, sun5_label, orbit5)

        # Earth moves from bottom to left (March Equinox)
        start_earth5 = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0).move_to(
            DOWN * EARTH_ORBIT_RADIUS)
        earth5_label = Text("Earth", color=WHITE).next_to(
            start_earth5, DOWN, buff=0.1)
        self.play(FadeIn(start_earth5), FadeIn(earth5_label))
        self.wait(0.3)
        self.play(
            MoveAlongPath(start_earth5, orbit5,
                          rate_func=linear, run_time=2.5),
            MoveAlongPath(earth5_label, orbit5,
                          rate_func=linear, run_time=2.5),
        )
        self.remove(start_earth5, earth5_label)

        # Earth at March Equinox (left)
        earth5 = Circle(radius=EARTH_RADIUS, color=BLUE,
                        fill_opacity=1.0).move_to(LEFT * EARTH_ORBIT_RADIUS)
        axis5 = Line(
            earth5.get_center() + UP * EARTH_RADIUS * 1.2,
            earth5.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth5.get_center())

        # Sunlight equally from right
        sunlight5 = VGroup(*[
            Line(
                start=RIGHT * 6 + UP * i * 0.5,
                end=earth5.get_center() + RIGHT * 0.1 + UP * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            for i in range(-3, 4)
        ])

        march_label = Text("March Equinox", color=WHITE).to_edge(
            DOWN).shift(LEFT * 1.5)

        self.play(FadeIn(earth5), Create(axis5))
        self.wait(0.3)
        self.play(Create(sunlight5))
        self.wait(0.3)
        self.play(Write(march_label))
        self.wait(1)

        # Fade out March Equinox elements
        self.play(
            FadeOut(earth5), FadeOut(axis5),
            FadeOut(sunlight5), FadeOut(march_label)
        )
        self.wait(0.3)

        # Earth moves from left to right (September Equinox)
        earth6 = Circle(radius=EARTH_RADIUS, color=BLUE,
                        fill_opacity=1.0).move_to(LEFT * EARTH_ORBIT_RADIUS)
        axis6 = Line(
            earth6.get_center() + UP * EARTH_RADIUS * 1.2,
            earth6.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth6.get_center())

        # Animate Earth from left to right
        self.play(
            MoveAlongPath(earth6, orbit5, rate_func=linear, run_time=3),
        )
        self.remove(earth6)

        # Earth at September Equinox (right)
        earth7 = Circle(radius=EARTH_RADIUS, color=BLUE,
                        fill_opacity=1.0).move_to(RIGHT * EARTH_ORBIT_RADIUS)
        axis7 = Line(
            earth7.get_center() + UP * EARTH_RADIUS * 1.2,
            earth7.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth7.get_center())

        # Sunlight equally from left
        sunlight6 = VGroup(*[
            Line(
                start=LEFT * 6 + UP * i * 0.5,
                end=earth7.get_center() + LEFT * 0.1 + UP * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            for i in range(-3, 4)
        ])

        sept_label = Text("September Equinox", color=WHITE).to_edge(
            DOWN).shift(RIGHT * 1.5)

        self.play(FadeIn(earth7), Create(axis7))
        self.wait(0.3)
        self.play(Create(sunlight6))
        self.wait(0.3)
        self.play(Write(sept_label))
        self.wait(1)

        # Fade out Scene 5 elements
        self.play(
            FadeOut(earth7), FadeOut(axis7),
            FadeOut(sunlight6), FadeOut(sept_label),
            FadeOut(sun5), FadeOut(sun5_label), FadeOut(orbit5)
        )
        self.wait(0.5)

        # --------------------
        # Scene 6: Full Annual Cycle
        # --------------------
        sun6 = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun6_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit6 = Circle(radius=EARTH_ORBIT_RADIUS,
                        color=WHITE, stroke_opacity=0.5)
        self.add(sun6, sun6_label, orbit6)

        # Earth with axis (initial at right)
        earth8 = Circle(radius=EARTH_RADIUS, color=BLUE,
                        fill_opacity=1.0).move_to(RIGHT * EARTH_ORBIT_RADIUS)
        axis8 = always_redraw(lambda: Line(
            earth8.get_center() + UP * EARTH_RADIUS * 1.2,
            earth8.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth8.get_center()))

        earth_and_axis8 = VGroup(earth8, axis8)

        # Sunlight highlight (semi-transparent circle indicating half lit)
        illuminated = Dot(
            fill_color=YELLOW_A,
            radius=EARTH_RADIUS * 1.05,
            fill_opacity=0.4)
        illuminated.add_updater(lambda mob, dt: mob.move_to(
            earth8.get_center() + normalize(earth8.get_center() - sun6.get_center()) * 0.01
        ))

        self.add(earth_and_axis8, illuminated)

        # Season labels
        summer_label = Text("Summer", color=WHITE).scale(
            0.6).move_to(UP * (EARTH_ORBIT_RADIUS + 0.7))
        autumn_label = Text("Fall", color=WHITE).scale(
            0.6).move_to(LEFT * (EARTH_ORBIT_RADIUS + 0.7))
        winter_label = Text("Winter", color=WHITE).scale(
            0.6).move_to(DOWN * (EARTH_ORBIT_RADIUS + 0.7))
        spring_label = Text("Spring", color=WHITE).scale(
            0.6).move_to(RIGHT * (EARTH_ORBIT_RADIUS + 0.7))

        # Show Summer label
        self.play(FadeIn(summer_label), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(summer_label))

        # Earth completes one revolution (8 seconds)
        self.play(
            MoveAlongPath(earth_and_axis8, orbit6,
                          rate_func=linear, run_time=8),
        )

        # Show Fall label
        self.play(FadeIn(autumn_label), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(autumn_label))

        # Show Winter label
        self.play(FadeIn(winter_label), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(winter_label))

        # Show Spring label
        self.play(FadeIn(spring_label), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(spring_label))

        # Summary text
        summary = Text("Earth's Revolution + Axial Tilt = Seasons",
                       color=WHITE).scale(0.7).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)
