# 🎬 Manimations - AI-Powered 2D Animation Framework

An intelligent AI framework that generates high-quality, educational 2D animations using the Manim library. Transform your ideas into stunning visual explanations with the power of AI and mathematical animation.

## ✨ Features

- 🤖 **AI-Powered Animation Generation**: Convert natural language descriptions into executable Manim code
- 📚 **Educational Focus**: Optimized for creating clear, pedagogical animations
- 🎨 **Multiple AI Providers**: Support for Google Gemini and Groq APIs
- 🔧 **Clean Code Generation**: Produces well-structured, commented, and maintainable Manim code
- 🎯 **Lumi Assistant**: Specialized AI assistant designed for Manim animation expertise

## 🚀 Quick Start

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

### Running Example Animations

The project includes example animations to get you started:

```bash
# Run the Venn diagram example
manim example.py VennDiagramUnion -pql
manim example.py VennDiagramIntersection -pql
manim example.py VennDiagramDifference -pql
```

### Using the AI Assistant

#### With Google Gemini

```python
from ai.GEMINI.app import generate_animation

# Describe your animation idea
prompt = "Create an animation showing the Pythagorean theorem with a right triangle"

# Generate Manim code
animation_code = generate_animation(prompt)
```

#### With Groq (Coming Soon)

The framework is designed to support multiple AI providers. Groq integration is in development.

### Creating Custom Animations

1. **Describe your animation**: Write a clear description of what you want to animate
2. **Generate code**: Use the AI assistant to convert your description into Manim code
3. **Render**: Run the generated code with Manim to create your video

## 🏗️ Project Structure

```
manimations/
├── ai/                          # AI provider integrations
│   ├── GEMINI/                  # Google Gemini integration
│   │   ├── app.py              # Main Gemini application
│   │   └── response.txt        # Sample responses
│   └── GROQ/                   # Groq integration (planned)
├── prompts/                     # System instructions and prompts
│   └── SystemInstruction.md    # Lumi AI assistant instructions
├── media/                       # Generated animation outputs
├── example.py                   # Example Venn diagram animations
├── main.py                      # Main application entry point
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## 🎯 About Lumi

Lumi is the specialized AI assistant at the heart of this framework. Designed specifically for Manim animations, Lumi:

- **Understands Animation Concepts**: Interprets educational and conceptual animation requests
- **Generates Clean Code**: Produces syntactically correct, well-commented Manim code
- **Focuses on Education**: Emphasizes clarity and pedagogical effectiveness
- **Uses Native Capabilities**: Only uses Manim's built-in features, no external dependencies

## 📝 Example Prompts

Here are some example prompts you can use with the AI assistant:

- "Create an animation showing how quadratic equations are solved step by step"
- "Animate the concept of limits in calculus with a function approaching a point"
- "Show the relationship between sine and cosine functions on the unit circle"
- "Demonstrate how binary search works with a sorted array"
- "Visualize the process of matrix multiplication"

## 🛠️ Development

### Running in Development Mode

```bash
# Install development dependencies
pip install -e .

# Run tests (when available)
python -m pytest

# Format code
black .
```

### Adding New AI Providers

1. Create a new directory in `ai/`
2. Implement the provider interface
3. Update the main application to support the new provider

## 📚 Dependencies

### Core Dependencies
- **manim**: Mathematical animation engine
- **python-dotenv**: Environment variable management
- **google-generativeai**: Google Gemini API client

### Development Dependencies
- Various supporting libraries for AI integration and video processing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines

1. Follow the existing code style
2. Add comments for complex animation logic
3. Test your animations before submitting
4. Update documentation as needed

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