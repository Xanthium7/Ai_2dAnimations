# 🎓 Lumi - AI-Powered Educational Animation Framework

Transform complex concepts into crystal-clear visual explanations. Lumi is an intelligent AI framework designed specifically for educators, students, and content creators who want to make learning more engaging through dynamic, mathematically-precise animations powered by Manim.

# Working


https://github.com/user-attachments/assets/91f67642-ff29-4a02-9929-4e39547e42f8




## 🎯 Why Choose Lumi for Education?

### 📚 **Perfect for Educators**
- **Explain Complex Concepts**: Break down difficult mathematical, scientific, and technical concepts into digestible visual steps
- **Engage Students**: Transform static textbook diagrams into dynamic, interactive learning experiences
- **Save Time**: Generate professional-quality educational animations in minutes, not hours
- **Curriculum Support**: Covers mathematics, physics, computer science, and more

### 👩‍🎓 **Ideal for Students**
- **Visual Learning**: See abstract concepts come to life through precise mathematical animations
- **Study Aid**: Create custom visualizations to reinforce understanding
- **Project Work**: Generate impressive educational presentations and demonstrations
- **Research Visualization**: Illustrate complex research findings and theoretical concepts

### 🧠 **Learning Enhancement**
- **Conceptual Clarity**: Step-by-step visual breakdowns that make "aha!" moments happen
- **Retention Boost**: Visual learning increases comprehension and memory retention by up to 65%
- **Universal Access**: Make complex topics accessible to diverse learning styles
- **Interactive Understanding**: See how changing parameters affects outcomes in real-time

## 🚀 Quick Start for Educators

### Prerequisites

- Python 3.11 or higher
- FFmpeg (for video rendering)
- A valid API key for Google Gemini or Groq

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd manimations
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using uv:
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Test the installation**
   ```bash
   python main.py
   ```

## 📖 Usage

## 📖 Educational Applications

### Mathematics Education
- **Algebra**: Visualize equation solving, function transformations, and polynomial behavior
- **Geometry**: Animate geometric proofs, transformations, and spatial relationships
- **Calculus**: Show limits, derivatives, integrals, and infinite series convergence
- **Statistics**: Demonstrate probability distributions, central limit theorem, and hypothesis testing

### Science Visualization
- **Physics**: Illustrate wave mechanics, electromagnetic fields, orbital dynamics, and thermodynamics
- **Chemistry**: Animate molecular interactions, reaction mechanisms, and phase transitions
- **Biology**: Visualize cellular processes, genetic algorithms, and evolutionary concepts
- **Earth Science**: Show geological processes, climate patterns, and astronomical phenomena

### Computer Science Education
- **Algorithms**: Demonstrate sorting, searching, graph traversal, and optimization algorithms
- **Data Structures**: Visualize trees, graphs, hash tables, and dynamic data manipulation
- **Machine Learning**: Show neural networks, training processes, and decision boundaries
- **Programming Concepts**: Illustrate recursion, object-oriented principles, and computational complexity

### Teaching Examples

The project includes educational animation examples to get you started:

```bash
# Run mathematical visualization examples
manim example.py VennDiagramUnion -pql
manim example.py VennDiagramIntersection -pql
manim example.py VennDiagramDifference -pql

# Earth's seasons educational animation
manim new_example.py EarthSeasonsAnimation -pql
```

### Using the AI Teaching Assistant

#### With Google Gemini

```python
from ai.GEMINI.app import generate_animation

# Describe your educational concept
prompt = "Create an animation showing how the Pythagorean theorem works with a visual proof"

# Generate educational Manim code
animation_code = generate_animation(prompt)
```

#### With Groq (Coming Soon)

The framework is designed to support multiple AI providers. Groq integration is in development.

### Creating Educational Content

1. **Identify Learning Objective**: Define what concept you want students to understand
2. **Describe the Visualization**: Write a clear description of how to illustrate the concept
3. **Generate Animation**: Use the AI assistant to convert your description into Manim code
4. **Customize for Your Class**: Adjust parameters, colors, and timing to fit your teaching style
5. **Share with Students**: Render and distribute videos or use in presentations

## 🏗️ Project Structure for Educators

```
manimations/
├── ai/                          # AI-powered educational content generation
│   ├── GEMINI/                  # Google Gemini integration for concept explanation
│   │   ├── app.py              # Main educational content generator
│   │   └── response.txt        # Sample educational responses
│   └── GROQ/                   # Additional AI provider (planned)
├── prompts/                     # Educational prompt templates and instructions
│   ├── SystemInstruction.md    # Lumi educational AI assistant instructions
│   └── userFilterPrompt.md     # Enhanced prompt system for 2D/3D capabilities
├── media/                       # Your generated educational videos and assets
├── example.py                   # Mathematical visualization examples (Venn diagrams)
├── new_example.py              # Science education example (Earth's seasons)
├── main.py                      # Main application entry point
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Project configuration
└── README.md                   # This educational guide
```

## 🎯 About Lumi - Your AI Teaching Assistant

Lumi is the specialized educational AI assistant designed specifically for creating impactful learning experiences. Lumi excels at:

- **Educational Focus**: Understands pedagogical principles and learning objectives
- **Concept Visualization**: Transforms abstract ideas into concrete visual representations
- **Student-Centered Design**: Creates animations that enhance comprehension and engagement
- **Curriculum Alignment**: Generates content that supports standard educational frameworks
- **Accessibility**: Makes complex topics approachable for diverse learning styles
- **Scientifically Accurate**: Ensures mathematical and scientific precision in all visualizations

## 📝 Educational Prompt Examples

Transform your teaching ideas into stunning visual explanations with these example prompts:

### Mathematics & Physics
- "Create an animation showing how quadratic equations are solved step by step with visual transformations"
- "Animate the concept of limits in calculus with a function approaching a point, showing epsilon-delta definition"
- "Show the relationship between sine and cosine functions on the unit circle with rotating radius"
- "Visualize how waves interfere constructively and destructively with amplitude demonstrations"
- "Demonstrate orbital mechanics showing how gravitational force creates elliptical orbits"

### Computer Science & Algorithms
- "Demonstrate how binary search works with a sorted array, highlighting the elimination process"
- "Visualize the process of matrix multiplication with color-coded calculations"
- "Show how a binary tree is constructed and traversed step by step"
- "Animate Dijkstra's shortest path algorithm on a weighted graph"
- "Illustrate how neural networks learn through backpropagation"

### Biology & Chemistry
- "Animate DNA replication showing helicase unwinding and polymerase synthesis"
- "Visualize how enzymes work with substrate binding and product formation"
- "Show cellular respiration process from glucose to ATP production"
- "Demonstrate molecular orbital formation in chemical bonding"

### Educational Scenarios
- "Create a concept map animation showing the relationships between geometric theorems"
- "Animate the historical development of the periodic table with element discoveries"
- "Show how statistical distributions change with different parameters"

## 🛠️ Development & Educational Customization

### Customizing for Your Classroom

```bash
# Install development dependencies for educational customization
pip install -e .

# Test educational animations
python -m pytest

# Format and organize educational content
black .
```

### Creating Subject-Specific Content

1. Create subject-specific animation libraries in `subjects/`
2. Develop curriculum-aligned prompt templates
3. Build assessment-integrated visualizations
4. Create interactive educational experiences

## 📚 Dependencies

### Core Educational Dependencies
- **manim**: Mathematical animation engine for precise educational visualizations
- **python-dotenv**: Environment configuration for educational AI models
- **google-generativeai**: Google Gemini API for intelligent educational content generation

### Educational Enhancement Libraries
- Supporting tools for curriculum integration, assessment alignment, and learning analytics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Manim Community](https://github.com/ManimCommunity/manim) for the amazing animation library
- AI providers (Google Gemini, Groq) for powering the intelligent code generation
- The open-source community for inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Review the Manim documentation
3. Create a new issue with a detailed description

---

**Happy Animating!** 🎬✨
