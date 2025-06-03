from manim import *

# Constants
EARTH_ORBIT_RADIUS = 3.5
EARTH_RADIUS = 0.4
AXIAL_TILT = 23.5 * DEGREES  # 23.5 degrees in radians


class Scene1_IntroductionToOrbital(Scene):
    def construct(self):
        # Sun at center
        sun = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        # Earth's orbital path (Ellipse approximated as Circle for simplicity)
        sun_label = Text("The Sun", color=WHITE).next_to(sun, DOWN, buff=0.3)
        orbit = Circle(radius=EARTH_ORBIT_RADIUS, color=WHITE,
                       stroke_opacity=0.5)
        orbit_label = Text("Earth's Orbit", color=WHITE).next_to(
            orbit, UP, buff=0.3)

        # Earth at starting point (to the right of Sun)
        earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        earth.shift(RIGHT * EARTH_ORBIT_RADIUS)
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

        # Animate Earth revolving once around orbit
        self.play(
            MoveAlongPath(earth, orbit, rate_func=linear, run_time=4),
            MoveAlongPath(earth_label, orbit, rate_func=linear, run_time=4),
        )
        self.wait(1)


class Scene2_EarthAxialTilt(Scene):
    def construct(self):
        # Zoom in: Represent Earth larger
        earth = Circle(radius=1.0, color=BLUE, fill_opacity=1.0)
        axis = Line(
            -UP * 1.2, DOWN * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=ORIGIN)
        tilt_arc = Arc(
            start_angle=PI / 2 - AXIAL_TILT,
            angle=AXIAL_TILT,
            radius=1.0,
            color=WHITE
        )
        angle_label = MathTex("23.5^\\circ", color=WHITE).next_to(
            tilt_arc, UP, buff=0.1)
        axis_label = Text("Earth's Axis", color=WHITE).next_to(
            axis.get_end(), UP, buff=0.1)

        # Show Earth
        self.play(FadeIn(earth))
        self.wait(0.3)

        # Show axis tilted
        self.play(Create(axis), FadeIn(axis_label))
        self.wait(0.3)

        # Show tilt arc and angle
        self.play(Create(tilt_arc), Write(angle_label))
        self.wait(0.5)

        # Rotate Earth on its axis (but keep tilt direction fixed in space)
        self.play(Rotate(earth, angle=2 * PI, about_point=ORIGIN,
                  run_time=3, rate_func=linear))
        self.wait(0.5)
        self.play(FadeOut(earth), FadeOut(axis), FadeOut(
            axis_label), FadeOut(tilt_arc), FadeOut(angle_label))


class Scene3_SummerSolstice(Scene):
    def construct(self):
        # Sun
        sun = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun_label = Text("The Sun", color=WHITE).to_corner(UL)        # Orbit
        orbit = Circle(radius=EARTH_ORBIT_RADIUS, color=WHITE,
                       stroke_opacity=0.5)
        self.add(sun, sun_label, orbit)

        # Earth at top of orbit (June Solstice)
        earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        earth.move_to(UP * EARTH_ORBIT_RADIUS)
        # Tilt axis pointing toward Sun (north end tilted toward sun)
        axis = Line(
            earth.get_center() + UP * EARTH_RADIUS * 1.2,
            earth.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth.get_center())

        # Sunlight rays from below (toward Earth)
        sunlight = VGroup()
        for i in range(-3, 4):
            ray = Line(
                start=DOWN * 6 + RIGHT * i * 0.5,
                end=earth.get_center() + RIGHT * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            sunlight.add(ray)

        # Labels
        nh_summer = Text("Northern Hemisphere: Summer",
                         color=WHITE).to_edge(LEFT).shift(UP * 2)
        sh_winter = Text("Southern Hemisphere: Winter",
                         color=WHITE).to_edge(LEFT).shift(DOWN * 2)
        solstice_label = Text("June Solstice", color=WHITE).to_edge(DOWN)

        # Animate Earth moving into position (from right quadrant)
        start_earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        start_earth.move_to(RIGHT * EARTH_ORBIT_RADIUS)
        earth_label = Text("Earth", color=WHITE).next_to(
            start_earth, UP, buff=0.1)
        self.play(FadeIn(start_earth), FadeIn(earth_label))
        self.wait(0.3)
        self.play(
            MoveAlongPath(start_earth, orbit, rate_func=linear, run_time=2),
            MoveAlongPath(earth_label, orbit, rate_func=linear, run_time=2),
        )
        self.remove(start_earth, earth_label)

        # Add final Earth & axis
        self.play(FadeIn(earth), Create(axis))
        self.wait(0.3)

        # Sunlight appears, highlighting northern hemisphere
        self.play(Create(sunlight))
        self.wait(0.3)

        # Labels appear
        self.play(FadeIn(nh_summer), FadeIn(sh_winter), Write(solstice_label))
        self.wait(1)


class Scene4_WinterSolstice(Scene):
    def construct(self):
        # Sun and orbit
        sun = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit = Circle(radius=EARTH_ORBIT_RADIUS,
                       color=WHITE, stroke_opacity=0.5)
        self.add(sun, sun_label, orbit)

        # Earth at bottom (December Solstice)
        earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        earth.move_to(DOWN * EARTH_ORBIT_RADIUS)
        # Tilt axis pointing away (Northern tilted away)
        axis = Line(
            earth.get_center() + UP * EARTH_RADIUS * 1.2,
            earth.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(-AXIAL_TILT, about_point=earth.get_center())

        # Sunlight rays from above
        sunlight = VGroup()
        for i in range(-3, 4):
            ray = Line(
                start=UP * 6 + RIGHT * i * 0.5,
                end=earth.get_center() + RIGHT * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            sunlight.add(ray)

        # Labels
        nh_winter = Text("Northern Hemisphere: Winter",
                         color=WHITE).to_edge(LEFT).shift(UP * 2)
        sh_summer = Text("Southern Hemisphere: Summer",
                         color=WHITE).to_edge(LEFT).shift(DOWN * 2)
        solstice_label = Text("December Solstice", color=WHITE).to_edge(DOWN)

        # Animate Earth moving from top to bottom
        start_earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        start_earth.move_to(UP * EARTH_ORBIT_RADIUS)
        earth_label = Text("Earth", color=WHITE).next_to(
            start_earth, UP, buff=0.1)
        self.play(FadeIn(start_earth), FadeIn(earth_label))
        self.wait(0.3)
        self.play(
            MoveAlongPath(start_earth, orbit, rate_func=linear, run_time=2),
            MoveAlongPath(earth_label, orbit, rate_func=linear, run_time=2),
        )
        self.remove(start_earth, earth_label)

        # Show final Earth & axis
        self.play(FadeIn(earth), Create(axis))
        self.wait(0.3)

        # Sunlight appears, highlighting southern hemisphere
        self.play(Create(sunlight))
        self.wait(0.3)

        # Labels appear
        self.play(FadeIn(nh_winter), FadeIn(sh_summer), Write(solstice_label))
        self.wait(1)


class Scene5_Equinoxes(Scene):
    def construct(self):
        # Sun and orbit
        sun = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit = Circle(radius=EARTH_ORBIT_RADIUS,
                       color=WHITE, stroke_opacity=0.5)
        self.add(sun, sun_label, orbit)

        # Earth at March Equinox (left)
        earth_march = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        earth_march.move_to(LEFT * EARTH_ORBIT_RADIUS)
        axis_march = Line(
            earth_march.get_center() + UP * EARTH_RADIUS * 1.2,
            earth_march.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth_march.get_center())

        # Earth at September Equinox (right)
        earth_sept = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        earth_sept.move_to(RIGHT * EARTH_ORBIT_RADIUS)
        axis_sept = Line(
            earth_sept.get_center() + UP * EARTH_RADIUS * 1.2,
            earth_sept.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth_sept.get_center())

        # Sunlight rays hitting equally (horizontal)
        sunlight_equal = VGroup()
        for i in range(-3, 4):
            ray = Line(
                start=RIGHT * 6 + UP * i * 0.5,
                end=earth_march.get_center() + RIGHT * 0.1 + UP * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            sunlight_equal.add(ray)

        # Labels
        march_label = Text("March Equinox", color=WHITE).to_edge(
            DOWN).shift(LEFT * 1.5)
        sept_label = Text("September Equinox", color=WHITE).to_edge(
            DOWN).shift(RIGHT * 1.5)

        # Animate Earth moving from December position (down) to March (left)
        start_earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        start_earth.move_to(DOWN * EARTH_ORBIT_RADIUS)
        earth_label = Text("Earth", color=WHITE).next_to(
            start_earth, DOWN, buff=0.1)
        self.play(FadeIn(start_earth), FadeIn(earth_label))
        self.wait(0.3)
        self.play(
            MoveAlongPath(start_earth, orbit, rate_func=linear, run_time=2.5),
            MoveAlongPath(earth_label, orbit, rate_func=linear, run_time=2.5),
        )
        self.remove(start_earth, earth_label)

        # Show March Earth, axis, sunlight, label
        self.play(FadeIn(earth_march), Create(axis_march))
        self.wait(0.3)
        self.play(Create(sunlight_equal))
        self.wait(0.3)
        self.play(Write(march_label))
        self.wait(1)

        # Transform to September: move Earth & axis, adjust sunlight, label
        self.play(FadeOut(earth_march), FadeOut(axis_march),
                  FadeOut(sunlight_equal), FadeOut(march_label))

        # Move from left to right
        self.play(
            MoveAlongPath(earth_sept, orbit, rate_func=linear, run_time=3),
        )
        self.play(FadeIn(earth_sept), Create(axis_sept))
        self.wait(0.3)

        # Sunlight equally from left side
        sunlight_equal2 = VGroup()
        for i in range(-3, 4):
            ray = Line(
                start=LEFT * 6 + UP * i * 0.5,
                end=earth_sept.get_center() + LEFT * 0.1 + UP * i * 0.1,
                color=YELLOW_A,
                stroke_width=2
            )
            sunlight_equal2.add(ray)

        self.play(Create(sunlight_equal2))
        self.wait(0.3)
        self.play(Write(sept_label))
        self.wait(1)


class Scene6_FullAnnualCycle(Scene):
    def construct(self):
        # Sun and orbit
        sun = Circle(radius=1.0, color=YELLOW, fill_opacity=1.0)
        sun_label = Text("The Sun", color=WHITE).to_corner(UL)
        orbit = Circle(radius=EARTH_ORBIT_RADIUS,
                       color=WHITE, stroke_opacity=0.5)
        self.add(sun, sun_label, orbit)

        # Earth with axis (initial at right)
        earth = Circle(radius=EARTH_RADIUS, color=BLUE, fill_opacity=1.0)
        earth.move_to(RIGHT * EARTH_ORBIT_RADIUS)
        axis = always_redraw(lambda: Line(
            earth.get_center() + UP * EARTH_RADIUS * 1.2,
            earth.get_center() + DOWN * EARTH_RADIUS * 1.2,
            color=RED
        ).rotate(AXIAL_TILT, about_point=earth.get_center()))

        # Group Earth & axis so they move together
        earth_and_axis = VGroup(earth, axis)

        # Sunlight highlight: a semi-transparent circle sector representing illuminated half
        illuminated = always_redraw(lambda: Dot(
            fill_color=YELLOW_A,
            radius=EARTH_RADIUS * 1.05,
            fill_opacity=0.4
        ).move_to(earth.get_center()))

        # Season labels positions around orbit
        summer_label = Text("Summer", color=WHITE).scale(
            0.6).move_to(UP * (EARTH_ORBIT_RADIUS + 0.7))
        autumn_label = Text("Fall", color=WHITE).scale(
            0.6).move_to(LEFT * (EARTH_ORBIT_RADIUS + 0.7))
        winter_label = Text("Winter", color=WHITE).scale(
            0.6).move_to(DOWN * (EARTH_ORBIT_RADIUS + 0.7))
        spring_label = Text("Spring", color=WHITE).scale(
            0.6).move_to(RIGHT * (EARTH_ORBIT_RADIUS + 0.7))

        # Add Earth & axis initially
        # Animate full revolution with continuous tilt and sunlight emphasis
        self.add(earth_and_axis)

        def update_sunlight(mob, dt):
            # Determine vector from Sun to Earth center
            direction = normalize(earth.get_center() -
                                  sun.get_center())
            # Create half illumination by shifting the Dot slightly toward Sun
            mob.move_to(earth.get_center() + direction * 0.01)

        illuminated.add_updater(update_sunlight)
        self.add(illuminated)

        # Add season labels (fade in/out during animation)
        self.play(
            FadeIn(summer_label),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(FadeOut(summer_label))

        # Animation: Earth moves around orbit once (8 seconds)
        self.play(
            MoveAlongPath(earth_and_axis, orbit, rate_func=linear, run_time=8),
        )

        # Sequentially display season labels approximately at quarter points
        self.play(FadeIn(autumn_label), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(autumn_label))

        self.play(FadeIn(winter_label), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(winter_label))

        self.play(FadeIn(spring_label), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(spring_label))

        # Conclude with summary text
        summary = Text("Earth's Revolution + Axial Tilt = Seasons",
                       color=WHITE).scale(0.7)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)
