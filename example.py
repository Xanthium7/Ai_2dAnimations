from manim import *


class SetTheoryEquation(Scene):
    def construct(self):
        # --- Constants and Mobjects Setup ---
        # Define custom colors for better visual distinction
        COLOR_A_REGION = BLUE_A
        COLOR_B_REGION = RED_B
        # This color visually represents the intersection when both A and B contribute to it,
        # indicating it's "double-counted" conceptually before correction.
        COLOR_INTERSECTION_DOUBLE_COUNTED = PURPLE_D
        # This color represents the final union region, where the intersection is counted once.
        COLOR_UNION_FINAL = GREEN_D

        # Display the main equation at the top of the screen
        equation_tex = Tex(
            r"$A \cup B = A + B - A \cap B$").to_edge(UP).scale(1.2)
        self.play(Write(equation_tex))
        # Create two overlapping circles for the Venn Diagram outlines
        self.wait(0.5)
        circle_A_outline = Circle(radius=2, color=WHITE).shift(LEFT * 1)
        circle_B_outline = Circle(radius=2, color=WHITE).shift(RIGHT * 1)

        # Labels for Set A and Set B
        label_A = Text("A").next_to(circle_A_outline, UL)
        label_B = Text("B").next_to(circle_B_outline, UR)

        # Animate the drawing of the circles and the appearance of their labels
        self.play(
            Create(circle_A_outline),
            Create(circle_B_outline),
            FadeIn(label_A, label_B)
        )
        self.wait(1)

        # Group the permanent Venn diagram elements (outlines + labels) for easy manipulation
        venn_diagram_elements = VGroup(
            circle_A_outline, circle_B_outline, label_A, label_B)

        # Define the distinct regions of the Venn diagram using boolean operations on the circles.
        # These are initially just conceptual polygons, not yet filled or added to the scene.
        a_only_polygon = Difference(circle_A_outline, circle_B_outline)
        b_only_polygon = Difference(circle_B_outline, circle_A_outline)
        intersection_polygon = Intersection(circle_A_outline, circle_B_outline)

        # --- Animation Sequence: Explaining Each Set Theory Concept ---

        # 1. Explain Set A
        # Highlight 'A' from the equation's 'A + B' part (index 4 in the Tex object) and its label
        self.play(Indicate(equation_tex.submobjects[0][4]), Indicate(label_A))

        # Create a VGroup to represent Set A's filled region (A_only part + intersection part)
        fill_a_visual = VGroup(
            a_only_polygon.copy().set_fill(COLOR_A_REGION, opacity=0.8),
            intersection_polygon.copy().set_fill(COLOR_A_REGION, opacity=0.8)
        )
        self.play(FadeIn(fill_a_visual))  # Animate the filling of Set A

        # Add a textual caption for Set A
        a_label_caption = Text("This is Set A").next_to(
            venn_diagram_elements, DOWN).set_color(COLOR_A_REGION)
        self.play(FadeIn(a_label_caption))
        self.wait(1.5)
        self.play(FadeOut(fill_a_visual), FadeOut(
            a_label_caption))  # Clear Set A's filling

        # 2. Explain Set B
        # Highlight 'B' from the equation's 'A + B' part (index 6 in the Tex object) and its label
        self.play(Indicate(equation_tex.submobjects[0][6]), Indicate(label_B))

        # Create a VGroup to represent Set B's filled region
        fill_b_visual = VGroup(
            b_only_polygon.copy().set_fill(COLOR_B_REGION, opacity=0.8),
            intersection_polygon.copy().set_fill(COLOR_B_REGION, opacity=0.8)
        )
        self.play(FadeIn(fill_b_visual))  # Animate the filling of Set B

        # Add a textual caption for Set B
        b_label_caption = Text("This is Set B").next_to(
            venn_diagram_elements, DOWN).set_color(COLOR_B_REGION)
        self.play(FadeIn(b_label_caption))
        self.wait(1.5)
        self.play(FadeOut(fill_b_visual), FadeOut(
            b_label_caption))  # Clear Set B's filling

        # 3. Explain A ∩ B (Intersection)
        # Highlight 'A \cap B' in the equation (indices 8 to 10 in the Tex object)
        self.play(Indicate(equation_tex.submobjects[0][8:11]))

        # Create and show the filled region for the Intersection
        fill_intersection_visual = intersection_polygon.copy().set_fill(
            COLOR_INTERSECTION_DOUBLE_COUNTED, opacity=0.8)
        self.play(FadeIn(fill_intersection_visual))

        # Add a textual caption for the Intersection
        intersection_caption = Text("This is A ∩ B (Intersection)").next_to(
            venn_diagram_elements, DOWN).set_color(COLOR_INTERSECTION_DOUBLE_COUNTED)
        self.play(Write(intersection_caption))
        self.wait(2)
        self.play(FadeOut(fill_intersection_visual), FadeOut(
            intersection_caption))  # Clear Intersection's filling

        # 4. Explain A ∪ B (Union)
        # Highlight 'A \cup B' in the equation (indices 0 to 2 in the Tex object)
        self.play(Indicate(equation_tex.submobjects[0][0:3]))

        # Create and show the filled region for the Union
        fill_union_visual = VGroup(
            a_only_polygon.copy().set_fill(COLOR_UNION_FINAL, opacity=0.8),
            b_only_polygon.copy().set_fill(COLOR_UNION_FINAL, opacity=0.8),
            intersection_polygon.copy().set_fill(COLOR_UNION_FINAL, opacity=0.8)
        )
        self.play(FadeIn(fill_union_visual))

        # Add a textual caption for the Union
        union_caption = Text("This is A ∪ B (Union)").next_to(
            venn_diagram_elements, DOWN).set_color(COLOR_UNION_FINAL)
        self.play(Write(union_caption))
        self.wait(2)
        self.play(FadeOut(fill_union_visual), FadeOut(
            union_caption))  # Clear Union's filling

        # --- Animation Sequence: Demonstrating the Equation A ∪ B = A + B - A ∩ B ---

        # Shrink equation slightly to make room for captions during demonstration
        self.play(equation_tex.animate.scale(0.8).to_edge(UP))

        # 5.1. Start with 'A' (part of A + B)
        # Highlight 'A' in the equation to show focus
        self.play(
            Indicate(equation_tex.submobjects[0][4]),
            equation_tex.submobjects[0][4].animate.set_color(YELLOW)
        )

        # Show A's region filled. Store these filled mobjects for later transformations.
        current_fill_a_only = a_only_polygon.copy().set_fill(COLOR_A_REGION, opacity=0.8)
        current_fill_intersection_from_a = intersection_polygon.copy().set_fill(
            COLOR_A_REGION, opacity=0.8)
        self.play(FadeIn(current_fill_a_only), FadeIn(
            current_fill_intersection_from_a))
        self.wait(1)

        # 5.2. Add 'B' (part of A + B)
        # Highlight '+ B' in the equation
        self.play(
            # Highlight '+' and 'B'
            Indicate(equation_tex.submobjects[0][5:7]),
            equation_tex.submobjects[0][5:7].animate.set_color(YELLOW)
        )

        # Show B's region filled.
        # For the intersection, transform its color to indicate it's now double-counted
        # (visually, it becomes a mix of A's and B's colors).
        current_fill_b_only = b_only_polygon.copy().set_fill(COLOR_B_REGION, opacity=0.8)
        target_fill_intersection_double = intersection_polygon.copy().set_fill(
            COLOR_INTERSECTION_DOUBLE_COUNTED, opacity=0.8)

        self.play(
            FadeIn(current_fill_b_only),
            # Transforms the previous intersection fill
            Transform(current_fill_intersection_from_a,
                      target_fill_intersection_double)
        )

        # Group the currently visible filled regions to represent the A+B visual state
        current_a_plus_b_regions = VGroup(
            current_fill_a_only, current_fill_b_only, current_fill_intersection_from_a)

        # Explain that the intersection is now double-counted
        double_count_explanation = Text("A + B: Intersection (A ∩ B) is counted twice!").scale(
            0.7).next_to(venn_diagram_elements, DOWN).set_color(RED)
        self.play(Write(double_count_explanation), Flash(
            current_fill_intersection_from_a.get_center()))
        self.wait(2)
        self.play(FadeOut(double_count_explanation))

        # Reset color of the A+B part in the equation
        self.play(
            equation_tex.submobjects[0][4].animate.set_color(WHITE),  # A
            equation_tex.submobjects[0][5:7].animate.set_color(WHITE)  # +B
        )

        # 5.3. Subtract 'A ∩ B'
        # Highlight '- A \cap B' in the equation
        self.play(
            Indicate(equation_tex.submobjects[0][7:]),  # From '-' to 'B'
            equation_tex.submobjects[0][7:].animate.set_color(YELLOW)
        )
        self.wait(0.5)

        # Explain the subtraction
        subtract_explanation = Text("Subtract A ∩ B to correct double counting!").scale(
            0.7).next_to(venn_diagram_elements, DOWN)
        self.play(Write(subtract_explanation))

        # Transform the intersection region's fill color back to a single-counted union color,
        # effectively "removing" the second count.
        target_fill_intersection_union_color = intersection_polygon.copy().set_fill(
            COLOR_UNION_FINAL, opacity=0.8)

        self.play(Transform(current_fill_intersection_from_a,
                  target_fill_intersection_union_color))
        self.wait(1.5)
        self.play(FadeOut(subtract_explanation))
        # Reset color of the -A intersect B part in the equation
        self.play(equation_tex.submobjects[0][7:].animate.set_color(WHITE))

        # 5.4. Result: 'A ∪ B'
        # Highlight 'A \cup B' on the left side of the equation
        self.play(
            Indicate(equation_tex.submobjects[0][0:3]),
            equation_tex.submobjects[0][0:3].animate.set_color(YELLOW)
        )
        self.wait(0.5)

        # For visual consistency, transform the A_only and B_only parts to the union color
        final_a_only_union_color = a_only_polygon.copy().set_fill(
            COLOR_UNION_FINAL, opacity=0.8)
        final_b_only_union_color = b_only_polygon.copy().set_fill(
            COLOR_UNION_FINAL, opacity=0.8)

        self.play(
            Transform(current_fill_a_only, final_a_only_union_color),
            Transform(current_fill_b_only, final_b_only_union_color)
        )

        # Display the final result text
        final_result_text = Text("Result: A ∪ B").scale(0.7).next_to(
            venn_diagram_elements, DOWN).set_color(GREEN)
        self.play(Write(final_result_text), Flash(
            current_a_plus_b_regions.get_center()))
        self.wait(3)  # Long wait to emphasize the final state

        # --- Cleanup ---
        # Fade out all remaining mobjects from the scene
        self.play(
            FadeOut(current_a_plus_b_regions),  # All filled regions
            FadeOut(venn_diagram_elements),     # Outlines and labels
            FadeOut(equation_tex),
            FadeOut(final_result_text)
        )
        self.wait(1)  # Final pause before scene ends
