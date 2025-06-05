from manim import *


class NeuralNetworkExplanation2(MovingCameraScene):
    def construct(self):
        # --- Configuration & Aesthetics ---
        # Dark blue-grey background, similar to 3b1b
        self.camera.background_color = "#1a1a2e"
        TEXT_COLOR = WHITE
        NODE_COLOR = BLUE_C
        CONNECTION_COLOR = GREY_B
        HIGHLIGHT_COLOR = YELLOW_B
        ERROR_COLOR = RED_C
        SUCCESS_COLOR = GREEN_C
        BIAS_COLOR = ORANGE

        # Set up camera frame for potential adjustments
        self.camera.frame.set_width(config.frame_width)
        self.camera.frame.set_height(config.frame_height)

        # --- Scene 1: Introduction - Biological Inspiration ---
        title = Text("Understanding Neural Networks",
                     font_size=56, color=TEXT_COLOR)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(0.5)

        sub_title = Text("Inspired by the Human Brain",
                         font_size=36, color=BLUE_C)
        sub_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(sub_title, shift=DOWN))
        self.wait(1)

        # Simplified Neuron Visual (Dendrites, Soma, Axon, Synapse)
        soma = Circle(radius=0.8, color=NODE_COLOR, fill_opacity=0.6)
        soma_label = Text("Soma", font_size=24, color=TEXT_COLOR).next_to(
            soma, UP, buff=0.2)

        # Dendrites (inputs)
        dendrites = VGroup()
        for i in range(3):
            angle = i * 60 * DEGREES + 150 * DEGREES
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            dendrite = Line(soma.get_center(), soma.get_center() + direction * 1.5,
                            color=GREY_A, stroke_width=4)
            dendrites.add(dendrite)
        dendrites_label = Text("Dendrites (Inputs)", font_size=20, color=TEXT_COLOR).next_to(
            dendrites[1], UP+LEFT, buff=0.2)

        # Axon (output)
        axon = Line(soma.get_center(), soma.get_center() +
                    RIGHT * 2, color=GREY_A, stroke_width=4)
        axon_label = Text("Axon (Output)", font_size=20,
                          color=TEXT_COLOR).next_to(axon, RIGHT, buff=0.2)
        axon_terminal = Circle(radius=0.2, color=GREY_A,
                               fill_opacity=0.6).next_to(axon, RIGHT, buff=0)

        # Synapse (connection to next neuron)
        synapse_dot = Dot(axon_terminal.get_center() + RIGHT *
                          0.5, color=HIGHLIGHT_COLOR, radius=0.1)
        synapse_label = Text("Synapse", font_size=20, color=TEXT_COLOR).next_to(
            synapse_dot, UR, buff=0.1)

        bio_neuron = VGroup(soma, dendrites, axon, axon_terminal, synapse_dot,
                            soma_label, dendrites_label, axon_label, synapse_label)
        bio_neuron.center().shift(DOWN*0.5)

        self.play(
            Create(soma),
            FadeIn(soma_label),
            lag_ratio=0.1
        )
        self.play(
            Create(dendrites),
            FadeIn(dendrites_label),
            lag_ratio=0.1
        )
        self.play(
            Create(axon),
            Create(axon_terminal),
            FadeIn(axon_label),
            lag_ratio=0.1
        )
        self.play(
            Create(synapse_dot),
            FadeIn(synapse_label)
        )
        self.wait(2)

        # --- Transition to Artificial Neuron ---
        self.play(
            FadeOut(bio_neuron, shift=LEFT),
            FadeOut(sub_title, shift=LEFT),
            title.animate.to_edge(UP, buff=0.8)  # Keep title
        )
        self.wait(0.5)

        # --- Scene 2: The Artificial Neuron (Perceptron) ---
        new_sub_title = Text("The Artificial Neuron",
                             font_size=36, color=BLUE_C)
        new_sub_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(new_sub_title, shift=DOWN))
        self.wait(0.5)

        # Neuron components
        neuron_body = Circle(radius=0.7, color=NODE_COLOR, fill_opacity=0.8)
        neuron_label = Text("Neuron", font_size=28, color=TEXT_COLOR).move_to(
            neuron_body.get_center())

        # Inputs
        input_dots = VGroup(
            *[Dot(radius=0.15, color=HIGHLIGHT_COLOR) for _ in range(3)])
        input_dots.arrange(DOWN, buff=0.8)
        input_dots.next_to(neuron_body, LEFT, buff=3.0)

        input_labels = VGroup()
        for i, dot in enumerate(input_dots):
            label = MathTex(f"x_{{{i+1}}}", font_size=32,
                            color=TEXT_COLOR).next_to(dot, LEFT, buff=0.3)
            input_labels.add(label)

        # Weights
        weight_lines = VGroup()
        weight_labels = VGroup()
        for i, dot in enumerate(input_dots):
            line = Line(dot.get_center(), neuron_body.get_center(),
                        color=CONNECTION_COLOR, stroke_width=3)
            weight_lines.add(line)
            weight_label = MathTex(f"w_{{{i+1}}}", font_size=28, color=TEXT_COLOR).move_to(
                line.point_from_proportion(0.5)).shift(UP * 0.4)
            weight_labels.add(weight_label)

        # Bias
        bias_dot = Dot(radius=0.15, color=BIAS_COLOR).next_to(
            neuron_body, DOWN+LEFT, buff=1.5)
        bias_label = MathTex("b", font_size=32, color=TEXT_COLOR).next_to(
            bias_dot, LEFT, buff=0.3)
        bias_line = DashedLine(bias_dot.get_center(), neuron_body.get_center(),
                               color=BIAS_COLOR, stroke_width=3, dash_length=0.1)
        bias_line_label = Text("Bias", font_size=28, color=TEXT_COLOR).next_to(
            bias_line, DOWN, buff=0.4)

        # Output
        output_dot = Dot(radius=0.15, color=SUCCESS_COLOR)
        output_dot.next_to(neuron_body, RIGHT, buff=2.0)
        output_label = MathTex("y", font_size=32, color=TEXT_COLOR).next_to(
            output_dot, RIGHT, buff=0.3)
        output_line = Arrow(neuron_body.get_center(), output_dot.get_center(
        ), buff=0.1, color=CONNECTION_COLOR, stroke_width=3)

        neuron_group = VGroup(
            neuron_body, neuron_label, input_dots, input_labels, weight_lines, weight_labels,
            bias_dot, bias_label, bias_line, bias_line_label,
            output_dot, output_label, output_line
        )

        self.play(
            Create(neuron_body),
            FadeIn(neuron_label)
        )
        self.wait(0.5)

        self.play(
            LaggedStart(*[Create(dot) for dot in input_dots], lag_ratio=0.2),
            LaggedStart(*[FadeIn(label)
                        for label in input_labels], lag_ratio=0.2)
        )
        self.wait(0.5)

        self.play(
            LaggedStart(*[Create(line)
                        for line in weight_lines], lag_ratio=0.2),
            LaggedStart(*[FadeIn(label)
                        for label in weight_labels], lag_ratio=0.2)
        )
        self.wait(0.5)

        self.play(
            Create(bias_dot),
            FadeIn(bias_label),
            Create(bias_line),
            FadeIn(bias_line_label)
        )
        self.wait(1)

        # Weighted Sum Visualization
        weighted_sum_formula = MathTex(
            r"\text{Weighted Sum } Z = (x_1 w_1 + x_2 w_2 + x_3 w_3) + b",
            font_size=36, color=TEXT_COLOR
        ).next_to(neuron_group, DOWN, buff=1.0)
        # Position formula safely at the bottom
        weighted_sum_formula.to_edge(DOWN, buff=0.5)

        self.play(Write(weighted_sum_formula))
        self.wait(1)

        # Highlight calculation flow
        self.play(
            AnimationGroup(*[
                Indicate(input_labels[i], scale_factor=1.2) for i in range(3)
            ], lag_ratio=0.1, run_time=1),
            AnimationGroup(*[
                Indicate(weight_labels[i], scale_factor=1.2) for i in range(3)
            ], lag_ratio=0.1, run_time=1),
            Indicate(bias_label, scale_factor=1.2)
        )
        self.play(Flash(neuron_body, color=HIGHLIGHT_COLOR,
                  flash_radius=1.0, line_length=0.2))
        self.wait(1)

        # Activation Function
        activation_func_label = MathTex(
            r"\text{Activation Function } f(Z)",
            font_size=36, color=TEXT_COLOR
        ).next_to(weighted_sum_formula, DOWN, buff=0.5)
        # Position this carefully to avoid overlap and potentially move it
        activation_func_label.shift(LEFT*2)  # Adjust based on screen space

        self.play(
            # Remove previous formula
            FadeOut(weighted_sum_formula, shift=DOWN*0.5),
            FadeIn(activation_func_label, shift=UP*0.5)
        )

        activation_func_box = Rectangle(
            width=neuron_body.get_width() * 0.9, height=neuron_body.get_height() * 0.4,
            color=HIGHLIGHT_COLOR, fill_opacity=0.2
        ).move_to(neuron_body.get_center() + UP * neuron_body.get_height() * 0.1)  # Place subtly inside neuron
        activation_func_text = MathTex(
            "f", font_size=48, color=HIGHLIGHT_COLOR).move_to(neuron_body.get_center())

        self.play(
            Create(activation_func_box),
            FadeIn(activation_func_text)
        )
        self.wait(1)

        self.play(
            Create(output_line),
            Create(output_dot),
            FadeIn(output_label)
        )
        self.wait(1)

        # Final Neuron Output Formula
        final_output_formula = MathTex(
            r"\text{Output } y = f(Z)",
            font_size=36, color=TEXT_COLOR
        ).move_to(activation_func_label.get_center())  # Reposition to replace the previous formula

        self.play(
            FadeOut(activation_func_label, shift=DOWN*0.5),
            FadeIn(final_output_formula, shift=UP*0.5)
        )
        self.wait(2)

        # --- Transition to Network Structure ---
        self.play(
            FadeOut(new_sub_title, shift=LEFT),
            FadeOut(final_output_formula, shift=DOWN*0.5),
            FadeOut(activation_func_box),
            FadeOut(activation_func_text),
            neuron_group.animate.scale(0.6).shift(
                LEFT * config.frame_width / 4 + DOWN * 0.5),  # Move to prepare for network
            title.animate.to_edge(UP, buff=0.8)  # Ensure title stays
        )
        self.wait(0.5)

        # --- Scene 3: Building a Network - Layers ---
        network_sub_title = Text(
            "From Neuron to Network: Layers", font_size=36, color=BLUE_C)
        network_sub_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(network_sub_title, shift=DOWN))
        self.wait(0.5)

        # Define node and layer properties
        node_radius = 0.15
        layer_buff = 2.5  # Space between layers
        node_spacing = 0.7  # Space between nodes in a layer

        # Input Layer
        input_layer_nodes = VGroup(
            *[Dot(radius=node_radius, color=NODE_COLOR) for _ in range(4)])
        input_layer_nodes.arrange(DOWN, buff=node_spacing)
        input_layer_nodes.to_edge(LEFT, buff=1.5).shift(
            UP*1.0)  # Adjusted position for stability

        input_layer_label = Text("Input Layer", font_size=28, color=TEXT_COLOR)
        input_layer_label.next_to(input_layer_nodes, DOWN, buff=0.5)

        # Hidden Layer 1
        hidden_layer_1_nodes = VGroup(
            *[Dot(radius=node_radius, color=NODE_COLOR) for _ in range(5)])
        hidden_layer_1_nodes.arrange(DOWN, buff=node_spacing)
        hidden_layer_1_nodes.next_to(input_layer_nodes, RIGHT, buff=layer_buff)

        hidden_layer_1_label = Text(
            "Hidden Layer 1", font_size=28, color=TEXT_COLOR)
        hidden_layer_1_label.next_to(hidden_layer_1_nodes, DOWN, buff=0.5)

        # Output Layer
        output_layer_nodes = VGroup(
            *[Dot(radius=node_radius, color=NODE_COLOR) for _ in range(2)])
        output_layer_nodes.arrange(DOWN, buff=node_spacing)
        output_layer_nodes.next_to(
            hidden_layer_1_nodes, RIGHT, buff=layer_buff)

        output_layer_label = Text(
            "Output Layer", font_size=28, color=TEXT_COLOR)
        output_layer_label.next_to(output_layer_nodes, DOWN, buff=0.5)

        # Connections (Lines)
        connections_1_2 = VGroup()
        for in_node in input_layer_nodes:
            for hid_node in hidden_layer_1_nodes:
                connections_1_2.add(Line(in_node.get_center(), hid_node.get_center(
                ), color=CONNECTION_COLOR, stroke_width=1.5))

        connections_2_3 = VGroup()
        for hid_node in hidden_layer_1_nodes:
            for out_node in output_layer_nodes:
                connections_2_3.add(Line(hid_node.get_center(
                ), out_node.get_center(), color=CONNECTION_COLOR, stroke_width=1.5))

        # Group entire network for scaling/positioning later
        full_network = VGroup(
            input_layer_nodes, input_layer_label,
            hidden_layer_1_nodes, hidden_layer_1_label,
            output_layer_nodes, output_layer_label,
            connections_1_2, connections_2_3
        )
        full_network.center()  # Center the network
        # Move it slightly down to accommodate the title and sub-title
        full_network.shift(DOWN * 0.5)

        # Create the network layers
        self.play(
            LaggedStart(
                FadeIn(input_layer_nodes, shift=LEFT),
                FadeIn(input_layer_label, shift=DOWN),
                lag_ratio=0.2
            )
        )
        self.wait(0.5)

        self.play(
            LaggedStart(
                FadeIn(hidden_layer_1_nodes, shift=LEFT),
                FadeIn(hidden_layer_1_label, shift=DOWN),
                lag_ratio=0.2
            )
        )
        self.wait(0.5)

        self.play(
            LaggedStart(
                FadeIn(output_layer_nodes, shift=LEFT),
                FadeIn(output_layer_label, shift=DOWN),
                lag_ratio=0.2
            )
        )
        self.wait(0.5)

        # Draw connections
        self.play(Create(connections_1_2), run_time=1.5)
        self.play(Create(connections_2_3), run_time=1.5)
        self.wait(1)

        # Explain connections (weights)
        connection_explanation = Text("Each connection has a weight (w) and each neuron has a bias (b).",
                                      font_size=28, color=TEXT_COLOR)
        connection_explanation.to_edge(DOWN, buff=0.5)
        self.play(Write(connection_explanation))
        self.wait(2)

        # --- Scene 4: Functioning - Forward Propagation ---
        self.play(
            FadeOut(connection_explanation, shift=DOWN*0.5),
            FadeOut(network_sub_title, shift=LEFT)
        )
        self.wait(0.5)

        forward_prop_title = Text(
            "How Information Flows: Forward Propagation", font_size=36, color=BLUE_C)
        forward_prop_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(forward_prop_title, shift=DOWN))
        self.wait(0.5)

        # Simulate data flow
        data_in = Text("Input Data", font_size=28, color=HIGHLIGHT_COLOR).next_to(
            input_layer_nodes, LEFT, buff=0.5)
        self.play(FadeIn(data_in, shift=LEFT))
        self.wait(0.5)

        # Pulse inputs
        self.play(
            AnimationGroup(*[
                Flash(node, color=HIGHLIGHT_COLOR, flash_radius=node_radius*2) for node in input_layer_nodes
            ], lag_ratio=0.1, run_time=1)
        )

        # Animate data moving through connections and nodes
        path_segments_1 = []
        for line in connections_1_2:
            data_dot = Dot(line.get_start(),
                           color=HIGHLIGHT_COLOR, radius=node_radius*0.8)
            path_segments_1.append(MoveAlongPath(data_dot, line, run_time=0.3))
            self.add(data_dot)  # Add to scene so it's visible during movement

        self.play(
            # Lag ratio to make dots appear staggered
            AnimationGroup(*path_segments_1, lag_ratio=0.01),
            AnimationGroup(*[
                Flash(node, color=HIGHLIGHT_COLOR, flash_radius=node_radius*2) for node in hidden_layer_1_nodes
            ], lag_ratio=0.05, run_time=1)
        )
        # Remove the moving dots
        self.remove(*[p.mobject for p in path_segments_1])

        path_segments_2 = []
        for line in connections_2_3:
            data_dot = Dot(line.get_start(),
                           color=HIGHLIGHT_COLOR, radius=node_radius*0.8)
            path_segments_2.append(MoveAlongPath(data_dot, line, run_time=0.3))
            self.add(data_dot)

        self.play(
            AnimationGroup(*path_segments_2, lag_ratio=0.01),
            AnimationGroup(*[
                Flash(node, color=HIGHLIGHT_COLOR, flash_radius=node_radius*2) for node in output_layer_nodes
            ], lag_ratio=0.05, run_time=1)
        )
        self.remove(*[p.mobject for p in path_segments_2])

        final_output_text = Text("Output", font_size=28, color=SUCCESS_COLOR).next_to(
            output_layer_nodes, RIGHT, buff=0.5)
        self.play(FadeIn(final_output_text, shift=RIGHT))
        self.wait(2)

        # --- Scene 5: Learning - Backpropagation (Simplified) ---
        self.play(
            FadeOut(data_in, shift=LEFT),
            FadeOut(final_output_text, shift=RIGHT),
            FadeOut(forward_prop_title, shift=LEFT)
        )
        self.wait(0.5)

        learning_title = Text(
            "Learning from Mistakes: Backpropagation", font_size=36, color=BLUE_C)
        learning_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(learning_title, shift=DOWN))
        self.wait(0.5)

        # Explain prediction vs. actual
        predicted_output = Text("Predicted Output", font_size=28, color=HIGHLIGHT_COLOR).next_to(
            output_layer_nodes[0], UP, buff=0.5)
        actual_output = Text("Actual Output", font_size=28, color=SUCCESS_COLOR).next_to(
            output_layer_nodes[1], DOWN, buff=0.5)
        error_label = Text("Error!", font_size=36, color=ERROR_COLOR).next_to(
            output_layer_nodes, RIGHT, buff=1.0)

        self.play(
            FadeIn(predicted_output),
            FadeIn(actual_output)
        )
        self.wait(1)

        self.play(Write(error_label))
        self.play(Indicate(error_label))
        self.wait(1)

        # Show error flowing backwards
        error_arrow = CurvedArrow(
            error_label.get_center(),
            hidden_layer_1_nodes.get_center() + LEFT*1.0,
            color=ERROR_COLOR,
            stroke_width=5
        )
        error_flow_text = Text(
            "Error Signal Flowing Backwards", font_size=28, color=ERROR_COLOR)
        error_flow_text.next_to(error_arrow, DOWN, buff=0.5)
        error_flow_text.to_edge(DOWN, buff=0.5)  # Position safely

        self.play(
            Create(error_arrow),
            Write(error_flow_text)
        )
        self.wait(1)

        # Highlight connections being updated
        update_highlight_group = VGroup()
        for conn in connections_1_2:
            update_highlight_group.add(conn.copy().set_color(
                HIGHLIGHT_COLOR).set_stroke_width(5))
        for conn in connections_2_3:
            update_highlight_group.add(conn.copy().set_color(
                HIGHLIGHT_COLOR).set_stroke_width(5))

        self.play(
            LaggedStart(*[Flash(conn, color=HIGHLIGHT_COLOR, flash_radius=0.1)
                        for conn in connections_2_3], lag_ratio=0.01),
            LaggedStart(*[Flash(conn, color=HIGHLIGHT_COLOR, flash_radius=0.1)
                        for conn in connections_1_2], lag_ratio=0.01),
            run_time=2
        )

        weight_update_text = Text("Adjusting Weights and Biases", font_size=28,
                                  color=TEXT_COLOR).next_to(error_flow_text, DOWN, buff=0.5)
        # Further adjustments for text stacking
        weight_update_text.to_edge(DOWN, buff=0.1)

        self.play(Write(weight_update_text))
        self.wait(1.5)

        iteration_text = Text(
            "This process repeats for many iterations (epochs).", font_size=28, color=TEXT_COLOR)
        iteration_text.next_to(weight_update_text, DOWN, buff=0.1)
        # Position again to prevent overlap
        iteration_text.to_edge(DOWN, buff=0.1)

        self.play(Write(iteration_text))
        self.wait(2)

        # --- Scene 6: Conclusion & Applications ---
        self.play(
            FadeOut(predicted_output, shift=UP),
            FadeOut(actual_output, shift=DOWN),
            FadeOut(error_label),
            FadeOut(error_arrow),
            FadeOut(error_flow_text),
            FadeOut(weight_update_text),
            FadeOut(iteration_text),
            FadeOut(learning_title, shift=LEFT)
        )
        self.wait(0.5)

        summary_title = Text(
            "Neural Networks: Powerful & Versatile", font_size=36, color=BLUE_C)
        summary_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(summary_title, shift=DOWN))
        self.wait(0.5)

        # Applications
        applications_list = BulletedList(
            "Image Recognition (e.g., face detection)",
            "Natural Language Processing (e.g., ChatGPT)",
            "Medical Diagnosis (e.g., detecting diseases)",
            "Self-driving Cars (e.g., perception, decision-making)",
            "Recommendation Systems (e.g., Netflix, Amazon)",
            font_size=32, color=TEXT_COLOR
        )
        applications_list.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        applications_list.next_to(full_network, RIGHT, buff=1.0)
        applications_list.to_edge(RIGHT, buff=0.8).shift(
            UP*0.5)  # Position to the right, centered vertically

        self.play(
            # Fade out the network diagram as applications appear
            FadeOut(full_network),
            FadeIn(applications_list, shift=RIGHT)
        )
        self.wait(1)

        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT)
                        for item in applications_list], lag_ratio=0.5)
        )
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(summary_title),
            FadeOut(applications_list)
        )
        self.wait(1)
