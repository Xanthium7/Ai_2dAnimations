from manim import *


class NeuralNetworkExplanationNew(Scene):
    def construct(self):
        # --- Phase 1: Introduction to Neural Networks ---
        self.next_section("Introduction to Neural Networks",
                          skip_animations=False)
        title = Text("Neural Networks: The Basics", font_size=50).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        intro_text = Text(
            "Inspired by the human brain, neural networks are powerful tools in AI.",
            font_size=32,
            color=WHITE
        ).next_to(title, DOWN, buff=0.7)
        self.play(Write(intro_text))
        self.wait(2)

        # Basic Structure Overview - Labels for layers
        input_layer_label = Text("Input Layer", font_size=28, color=BLUE_B).shift(
            LEFT * 5.5).to_edge(UP, buff=1.0)
        hidden_layer_label = Text(
            "Hidden Layer", font_size=28, color=GREEN_B).to_edge(UP, buff=1.0)
        output_layer_label = Text("Output Layer", font_size=28, color=RED_B).shift(
            RIGHT * 5.5).to_edge(UP, buff=1.0)

        # Create placeholder circles for the layers (Neurons/Nodes)
        input_nodes = VGroup(*[Circle(radius=0.4, color=BLUE, fill_opacity=0.6)
                             for _ in range(3)]).arrange(DOWN, buff=0.8).shift(LEFT * 5.5)
        hidden_nodes = VGroup(*[Circle(radius=0.4, color=GREEN, fill_opacity=0.6)
                              for _ in range(4)]).arrange(DOWN, buff=0.7)
        output_nodes = VGroup(*[Circle(radius=0.4, color=RED, fill_opacity=0.6)
                              for _ in range(2)]).arrange(DOWN, buff=0.9).shift(RIGHT * 5.5)

        layer_group = VGroup(input_nodes, hidden_nodes, output_nodes)

        self.play(
            FadeOut(intro_text),
            AnimationGroup(
                FadeIn(input_nodes, shift=LEFT),
                FadeIn(hidden_nodes, shift=UP),
                FadeIn(output_nodes, shift=RIGHT),
                lag_ratio=0.3
            ),
            Write(input_layer_label),
            Write(hidden_layer_label),
            Write(output_layer_label)
        )
        self.wait(1)

        # Connect the layers (conceptual lines for Synapses)
        connections_intro = VGroup()
        for i_node in input_nodes:
            for h_node in hidden_nodes:
                line = Line(i_node.get_right(), h_node.get_left(),
                            color=YELLOW, stroke_width=2)
                connections_intro.add(line)
        for h_node in hidden_nodes:
            for o_node in output_nodes:
                line = Line(h_node.get_right(), o_node.get_left(),
                            color=YELLOW, stroke_width=2)
                connections_intro.add(line)

        self.play(Create(connections_intro, run_time=2))
        self.wait(1)

        nodes_label = Text("Nodes (Neurons)", font_size=28, color=BLUE_C).next_to(
            input_nodes[1], LEFT, buff=0.8)
        connections_label = Text("Connections (Synapses)", font_size=28, color=YELLOW_C).next_to(
            connections_intro[0], UP+LEFT*0.5, buff=0.5)

        self.play(
            FadeIn(nodes_label, shift=LEFT),
            FadeIn(connections_label, shift=UP)
        )
        self.wait(2)

        self.play(
            FadeOut(layer_group, shift=DOWN),
            FadeOut(connections_intro, shift=DOWN),
            FadeOut(nodes_label),
            FadeOut(connections_label),
            FadeOut(input_layer_label),
            FadeOut(hidden_layer_label),
            FadeOut(output_layer_label),
            FadeOut(title)
        )
        self.wait(1)

        # --- Phase 2: Creation - The Artificial Neuron ---
        self.next_section("The Artificial Neuron", skip_animations=False)
        neuron_title = Text("The Artificial Neuron", font_size=50).to_edge(UP)
        self.play(Write(neuron_title))
        self.wait(1)

        # Central neuron
        neuron = Circle(radius=1.0, color=BLUE, fill_opacity=0.3).center()
        self.play(GrowFromCenter(neuron))
        self.wait(0.5)

        # Inputs (x)
        inputs_label = Text("Inputs", font_size=32, color=YELLOW).next_to(
            neuron, LEFT * 2, buff=1.5)
        input_arrows = VGroup(*[
            Arrow(start=LEFT * 5, end=neuron.get_left(), color=WHITE, buff=0.1, tip_length=0.2) for _ in range(3)
        ]).arrange(DOWN, buff=1.2).next_to(neuron, LEFT, buff=1.0)

        input_values = VGroup()
        for i, arrow in enumerate(input_arrows):
            val = MathTex(f"x_{{{i+1}}}", color=YELLOW,
                          font_size=30).next_to(arrow.get_start(), LEFT, buff=0.2)
            input_values.add(val)

        self.play(
            AnimationGroup(
                Create(input_arrows),
                Write(input_values),
                lag_ratio=0.1
            ),
            Write(inputs_label)
        )
        self.wait(1)

        # Weights (w)
        weights_label = Text("Weights", font_size=32, color=ORANGE).next_to(
            inputs_label, DOWN, buff=1.0)
        weights = VGroup()
        for i, arrow in enumerate(input_arrows):
            w = MathTex(f"w_{{{i+1}}}", color=ORANGE,
                        font_size=30).next_to(arrow.get_center(), UP * 0.5)
            weights.add(w)

        self.play(
            FadeIn(weights, shift=UP),
            Write(weights_label)
        )
        self.wait(1)

        # Weighted Sum (Σxiwi)
        weighted_sum_text = Tex(
            r"Weighted Sum: $\Sigma x_i w_i$", font_size=36).next_to(neuron, UP, buff=0.8)
        self.play(Write(weighted_sum_text))
        self.wait(1)

        # Bias (b)
        bias_label = Text("Bias", font_size=32, color=PURPLE).next_to(
            neuron, DOWN, buff=0.8)
        bias_equation = MathTex(
            "+ b", color=PURPLE, font_size=36).next_to(weighted_sum_text, RIGHT, buff=0.5)
        self.play(
            Write(bias_label),
            FadeIn(bias_equation, shift=UP)
        )
        self.wait(1)

        # Activation Function (f)
        activation_label = Text("Activation Function", font_size=32, color=GREEN).next_to(
            neuron, RIGHT * 2, buff=1.5)
        activation_func_eq = MathTex(
            r"f(\Sigma x_i w_i + b)", font_size=36).next_to(neuron.get_right(), RIGHT, buff=0.8)
        activation_arrow = Arrow(neuron.get_right(
        ), activation_func_eq.get_left(), buff=0.1, color=WHITE, tip_length=0.2)

        self.play(
            Write(activation_label),
            GrowArrow(activation_arrow),
            Write(activation_func_eq)
        )
        self.wait(1)

        # Output (y)
        output_label = Text("Output", font_size=32, color=BLUE_C).next_to(
            activation_func_eq, RIGHT, buff=1.5)
        output_arrow = Arrow(activation_func_eq.get_right(
        ), RIGHT * 6, buff=0.1, color=WHITE, tip_length=0.2)
        output_value = MathTex("y", color=BLUE_C, font_size=36).next_to(
            output_arrow.get_end(), RIGHT, buff=0.2)

        self.play(
            Write(output_label),
            GrowArrow(output_arrow),
            Write(output_value)
        )
        self.wait(2)

        neuron_elements = VGroup(
            neuron, input_arrows, input_values, inputs_label, weights, weights_label,
            weighted_sum_text, bias_label, bias_equation, activation_label,
            activation_arrow, activation_func_eq, output_label, output_arrow, output_value
        )
        self.play(FadeOut(neuron_elements, shift=DOWN), FadeOut(neuron_title))
        self.wait(1)

        # --- Phase 3: Creation - Connecting Neurons (Layers) ---
        self.next_section("Building the Network", skip_animations=False)
        network_creation_title = Text(
            "Building the Network", font_size=50).to_edge(UP)
        self.play(Write(network_creation_title))
        self.wait(1)

        # Re-create the layered structure for illustration
        input_nodes_full = VGroup(*[Circle(radius=0.35, color=BLUE, fill_opacity=0.6)
                                  for _ in range(3)]).arrange(DOWN, buff=0.8).shift(LEFT * 5)
        hidden_nodes_full = VGroup(
            *[Circle(radius=0.35, color=GREEN, fill_opacity=0.6) for _ in range(4)]).arrange(DOWN, buff=0.7)
        output_nodes_full = VGroup(*[Circle(radius=0.35, color=RED, fill_opacity=0.6)
                                   for _ in range(2)]).arrange(DOWN, buff=0.8).shift(RIGHT * 5)

        # Labels for full network
        input_layer_label_full = Text("Input", font_size=28, color=BLUE_B).next_to(
            input_nodes_full, UP, buff=0.5)
        hidden_layer_label_full = Text("Hidden", font_size=28, color=GREEN_B).next_to(
            hidden_nodes_full, UP, buff=0.5)
        output_layer_label_full = Text("Output", font_size=28, color=RED_B).next_to(
            output_nodes_full, UP, buff=0.5)

        self.play(
            AnimationGroup(
                FadeIn(input_nodes_full, shift=LEFT),
                FadeIn(hidden_nodes_full, shift=UP),
                FadeIn(output_nodes_full, shift=RIGHT),
                lag_ratio=0.3
            ),
            Write(input_layer_label_full),
            Write(hidden_layer_label_full),
            Write(output_layer_label_full)
        )
        self.wait(1)

        # Add input value placeholders
        input_x_values = VGroup()
        for i, node in enumerate(input_nodes_full):
            x_val = MathTex(f"x_{{{i+1}}}", color=YELLOW,
                            font_size=30).next_to(node, LEFT, buff=0.3)
            input_x_values.add(x_val)
        self.play(FadeIn(input_x_values, shift=LEFT))
        self.wait(0.5)

        # Connect all layers fully (Dense connections)
        all_connections = VGroup()
        for i_node in input_nodes_full:
            for h_node in hidden_nodes_full:
                line = Line(i_node.get_right(), h_node.get_left(),
                            color=YELLOW, stroke_width=1.5)
                all_connections.add(line)
        for h_node in hidden_nodes_full:
            for o_node in output_nodes_full:
                line = Line(h_node.get_right(), o_node.get_left(),
                            color=YELLOW, stroke_width=1.5)
                all_connections.add(line)

        self.play(Create(all_connections, run_time=2.5))
        self.wait(1)

        connection_explainer = Text("Each connection has a modifiable 'weight'.", font_size=32).next_to(
            network_creation_title, DOWN, buff=0.5)
        self.play(Write(connection_explainer))
        self.wait(2)
        self.play(FadeOut(connection_explainer))

        # --- Phase 4: Functioning - Forward Propagation ---
        self.next_section("Forward Propagation", skip_animations=False)
        forward_prop_title = Text(
            "Functioning: Forward Propagation", font_size=50).to_edge(UP)
        self.play(Transform(network_creation_title, forward_prop_title))
        self.wait(1)

        data_flow_text = Text("Data flows from input to output, activating neurons layer by layer.",
                              font_size=32).next_to(forward_prop_title, DOWN, buff=0.5)
        self.play(Write(data_flow_text))
        self.wait(1)

        # Simulate input values entering the network
        input_data = [0.7, 0.3, 0.9]  # Example values
        actual_input_values = VGroup()
        for i, node in enumerate(input_nodes_full):
            val_mobj = MathTex(f"{input_data[i]}", color=WHITE, font_size=30).next_to(
                node, LEFT, buff=0.3)
            actual_input_values.add(val_mobj)

        self.play(
            # Replace generic x_i with actual values
            ReplacementTransform(input_x_values, actual_input_values),
            run_time=1
        )
        self.wait(0.5)

        # Animate data flowing from Input to Hidden Layer
        hidden_activations_mobj = VGroup()
        for h_idx, h_node in enumerate(hidden_nodes_full):
            # For each hidden node, gather inputs from all input nodes
            animations_for_h_node = []
            for i_idx, i_node in enumerate(input_nodes_full):
                # Find the specific connection line
                connection_line = Line(i_node.get_right(), h_node.get_left())

                # Create a temporary 'data packet' to animate along the line
                val_to_pass = actual_input_values[i_idx].copy().move_to(
                    i_node.get_center())
                animations_for_h_node.append(
                    Succession(
                        FadeIn(val_to_pass, scale=0.5),
                        MoveAlongPath(val_to_pass, connection_line,
                                      run_time=0.5, rate_func=linear),
                        FadeOut(val_to_pass, scale=0.5)
                    )
                )

            # Play all inputs reaching this hidden node, then activate it
            self.play(
                AnimationGroup(*animations_for_h_node, lag_ratio=0.1),
                Indicate(h_node, color=WHITE, scale_factor=1.1)
            )

            # Show the activation value appearing at the hidden node
            hidden_node_activation_val = MathTex(
                f"a_{{{h_idx+1}}}", color=GREEN_C, font_size=30).move_to(h_node.get_center())
            hidden_activations_mobj.add(hidden_node_activation_val)
            self.play(FadeIn(hidden_node_activation_val, scale=0.5))
            self.wait(0.2)

        # Remove input values after they've propagated
        self.play(FadeOut(actual_input_values, shift=LEFT))
        self.wait(0.5)

        # Animate data flowing from Hidden to Output Layer
        output_predictions_mobj = VGroup()
        for o_idx, o_node in enumerate(output_nodes_full):
            # For each output node, gather inputs from all hidden nodes
            animations_for_o_node = []
            for h_idx, h_node in enumerate(hidden_nodes_full):
                connection_line = Line(h_node.get_right(), o_node.get_left())
                val_to_pass = hidden_activations_mobj[h_idx].copy().move_to(
                    h_node.get_center())
                animations_for_o_node.append(
                    Succession(
                        FadeIn(val_to_pass, scale=0.5),
                        MoveAlongPath(val_to_pass, connection_line,
                                      run_time=0.5, rate_func=linear),
                        FadeOut(val_to_pass, scale=0.5)
                    )
                )

            # Play all inputs reaching this output node, then activate it
            self.play(
                AnimationGroup(*animations_for_o_node, lag_ratio=0.1),
                Indicate(o_node, color=WHITE, scale_factor=1.1)
            )

            # Show the activation value appearing at the output node (the prediction)
            output_node_prediction_val = MathTex(
                f"y_{{pred_{{{o_idx+1}}}}}", color=RED_C, font_size=30).move_to(o_node.get_center())
            output_predictions_mobj.add(output_node_prediction_val)
            self.play(FadeIn(output_node_prediction_val, scale=0.5))
            self.wait(0.2)

        # Remove hidden values
        self.play(FadeOut(hidden_activations_mobj, shift=LEFT))
        self.wait(1)

        final_output_label = Text("Final Output (Prediction)", font_size=32).next_to(
            output_nodes_full, RIGHT, buff=1.0)
        self.play(Write(final_output_label))
        self.wait(2)

        # Clean up for next phase
        self.play(
            FadeOut(data_flow_text),
            FadeOut(final_output_label),
            FadeOut(output_predictions_mobj),
            FadeOut(all_connections),
            FadeOut(input_nodes_full),
            FadeOut(hidden_nodes_full),
            FadeOut(output_nodes_full),
            FadeOut(input_layer_label_full),
            FadeOut(hidden_layer_label_full),
            FadeOut(output_layer_label_full),
            FadeOut(network_creation_title)
        )
        self.wait(1)

        # --- Phase 5: Functioning - Learning (Brief concept of Backpropagation) ---
        self.next_section("Learning: Backpropagation", skip_animations=False)
        learning_title = Text("Learning: Backpropagation",
                              font_size=50).to_edge(UP)
        self.play(Write(learning_title))
        self.wait(1)

        learning_intro_text = Text(
            "Networks learn by adjusting weights based on the difference between predicted and true outputs.",
            font_size=32
        ).next_to(learning_title, DOWN, buff=0.5)
        self.play(Write(learning_intro_text))
        self.wait(2)

        # Re-introduce a simplified network for learning concept
        simplified_input = Circle(
            radius=0.5, color=BLUE, fill_opacity=0.6).shift(LEFT * 4)
        simplified_hidden = Circle(
            radius=0.5, color=GREEN, fill_opacity=0.6).center()
        simplified_output = Circle(
            radius=0.5, color=RED, fill_opacity=0.6).shift(RIGHT * 4)

        conn1 = Line(simplified_input.get_right(),
                     simplified_hidden.get_left(), color=YELLOW, stroke_width=3)
        conn2 = Line(simplified_hidden.get_right(),
                     simplified_output.get_left(), color=YELLOW, stroke_width=3)

        simplified_network = VGroup(
            simplified_input, simplified_hidden, simplified_output, conn1, conn2)
        self.play(
            FadeOut(learning_intro_text),
            FadeIn(simplified_network)
        )
        self.wait(0.5)

        # Predicted and True Output
        predicted_output_val = MathTex("y_{pred}", color=RED_C, font_size=40).next_to(
            simplified_output, RIGHT, buff=0.8)
        true_output_val = MathTex("y_{true}", color=WHITE, font_size=40).next_to(
            predicted_output_val, DOWN, buff=0.8)

        self.play(
            FadeIn(predicted_output_val, shift=RIGHT),
            FadeIn(true_output_val, shift=RIGHT)
        )
        self.wait(1)

        error_label = Text("Error = Prediction - True",
                           font_size=32).next_to(true_output_val, DOWN, buff=1.0)
        error_arrow_to_text = Arrow(predicted_output_val.get_corner(
            DR), error_label.get_left(), color=BLUE_C, buff=0.1)
        self.play(
            Write(error_label),
            GrowArrow(error_arrow_to_text)
        )
        self.wait(1.5)

        # Backpropagation concept: error flows backward
        backprop_arrow1 = Arrow(error_label.get_top(), conn2.get_center(
        ), color=RED, buff=0.1, max_stroke_width_to_length_ratio=4)
        backprop_arrow2 = Arrow(conn2.get_center(), conn1.get_center(
        ), color=RED, buff=0.1, max_stroke_width_to_length_ratio=4)

        adjust_weights_text = Text(
            "Error is used to adjust weights (w) and biases (b).", font_size=32).to_edge(DOWN, buff=0.5)

        self.play(
            Transform(error_arrow_to_text, backprop_arrow1),
            Indicate(conn2, scale_factor=1.2)
        )
        self.wait(0.5)
        self.play(
            Create(backprop_arrow2),
            Indicate(conn1, scale_factor=1.2),
            Write(adjust_weights_text)
        )
        self.wait(2)

        self.play(
            FadeOut(simplified_network),
            FadeOut(predicted_output_val),
            FadeOut(true_output_val),
            FadeOut(error_label),
            FadeOut(error_arrow_to_text),  # Transformed arrow
            FadeOut(backprop_arrow2),
            FadeOut(adjust_weights_text),
            FadeOut(learning_title)
        )
        self.wait(1)

        # --- Conclusion ---
        self.next_section("Conclusion", skip_animations=False)
        conclusion_text = Text(
            "Neural networks learn from data to make predictions or decisions.",
            font_size=40,
            color=WHITE
        ).center()

        conclusion_text2 = Text(
            "They are the foundation of many modern AI applications!",
            font_size=36,
            color=BLUE_A
        ).next_to(conclusion_text, DOWN, buff=0.8)

        self.play(Write(conclusion_text))
        self.wait(2)
        self.play(Write(conclusion_text2))
        self.wait(3)

        self.play(FadeOut(conclusion_text, conclusion_text2))
        self.wait(1)
