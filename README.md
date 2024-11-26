
# Interactive Bedtime Story Generator

Welcome to the **Interactive Bedtime Story Generator** project! This Python-based tool uses OpenAI's language models to craft engaging, age-appropriate bedtime stories for children aged 5–10. It offers a guided storytelling experience where users can choose key story elements and provide feedback to customize the narrative.

---

## Requirements

Before running the code, ensure you have the following installed:

```plaintext
openai>=1.0.0
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/nicolelyu021/Story-Generator-Prompt.git
    cd interactive-story-generator
    ```

2. Set up your OpenAI API key:

- Open the `main.py` file and replace `"YOUR_API_KEY_HERE"` with your OpenAI API key.
- Alternatively, you can securely set your API key as an environment variable in your terminal:

    ```bash
    export OPENAI_API_KEY='your-api-key'
    ```

3. Run the script:

    ```bash
    python main.py
    ```

4. Follow the prompts to create a magical bedtime story!

---

## TL;DR

This project is an **Interactive Bedtime Story Generator** designed to create engaging and age-appropriate stories for children aged 5–10 using OpenAI's language model. It allows users to interactively select story elements like characters, settings, and magical abilities, while also providing feedback to shape the narrative.

### Key features include:
- **Incremental Story Updates**: Tracks the story's state to incorporate user feedback without regenerating the entire narrative.
- **Safety and Quality Control**: Ensures all generated content is child-safe and appropriate.
- **Dynamic Interaction**: Responds to user confusion or irrelevant inputs with tailored clarifications and examples.

The project was developed step-by-step, addressing challenges like ambiguous input, maintaining narrative consistency, and creating a personalized user experience. Future enhancements could include emotion detection, user profiles, and advanced content safety mechanisms.

---

## How It Works

### Storytelling Process
The tool uses a six-step storytelling process:
1. **Brainstorming**: Users choose story elements like the main character, setting, and magical ability.
2. **Planning**: Matches user input to a specific theme and generates a cohesive story outline.
3. **Drafting**: Generates a segment of the story, maintaining consistency with previous parts.
4. **Revising**: Adapts and updates the story based on user feedback.
5. **Editing**: Ensures safety, quality, and clarity in the narrative.
6. **Publishing**: Displays the completed story or returns to revising based on feedback.

### Interaction Highlights
- Responds dynamically to user feedback or confusion.
- Generates age-appropriate language and themes.
- Uses predefined examples for characters, settings, and abilities to guide storytelling.

---

## How This Project Was Developed

This project was developed with a focus on solving an open-ended and ambiguous prompt engineering challenge. Below is a breakdown of the steps taken to approach and build the solution:

### 1. Understanding the Problem
- The assignment required creating an interactive bedtime story generator appropriate for children aged 5–10. The brief left significant room for interpretation.
- **Key Questions Considered**:
  - What makes a story engaging for this age group?
  - How can user feedback shape the storytelling experience?
  - What safeguards are necessary to ensure age-appropriate and safe content?

### 2. Brainstorming and Planning
- Identified the storytelling process as a series of phases: brainstorming, planning, drafting, revising, editing, and publishing.
- Decided to break the problem into smaller components:
  - Gathering user input for the main character, setting, and magical abilities.
  - Generating story segments incrementally.
  - Addressing issues like confusion or irrelevant inputs.

### 3. Iterative Development
- **Prototype Creation**: Built a framework for generating complete stories and iteratively improved interaction handling.
- **Challenges and Solutions**:
  - **Challenge**: User feedback required regenerating the entire story instead of modifying it incrementally.
    - **Solution**: Introduced a `StoryContext` class to maintain and update the story state incrementally.
  - **Challenge**: Responding to irrelevant inputs or confusion during brainstorming.
    - **Solution**: Designed confusion detection based on common phrases and added predefined responses.
  - **Challenge**: Ensuring story consistency while allowing flexibility in user choices.
    - **Solution**: Randomized story themes and provided specific examples for each segment.

### 4. Ensuring Content Safety and Quality
- Added advanced prompt structures to enforce safety.
- Designed age-appropriate story guidelines to ensure suitability for children.

### 5. Refining the Interaction
- Improved the user experience with:
  - Dynamic prompts for selecting characters, settings, and abilities.
  - Incremental updates based on user feedback.
- Enabled flexible, personalized storytelling through clear and engaging interaction design.

---

## Future Enhancements
If I had more than 2-3 hours to spend on this project, I would ...

### 1. **Improved Input Understanding**
- **Objective**: Better handle ambiguous or irrelevant user inputs during brainstorming.
- **Implementation**:
  - Detect confusion or unrelated inputs and respond with clarifying prompts.
  - Rephrase or simplify confusing story segments based on user feedback.
- **Impact**: Enhances engagement by ensuring clarity and understanding throughout the interaction.

### 2. **Enhanced Story Generation Consistency**
- **Objective**: Ensure a cohesive narrative while maintaining flexibility for user choices.
- **Implementation**:
  - Provide more predefined examples for each story segment to ensure consistency.
  - Use theme-based storytelling strategies with tailored guidelines for different genres (e.g., adventure, mystery, fantasy).
- **Impact**: Improves the quality and flow of generated stories, creating a more immersive experience.

### 3. **Content Safety and Quality Control**
- **Objective**: Maintain a safe and child-friendly narrative environment.
- **Implementation**:
  - Use advanced prompt structures to filter inappropriate content and themes.
  - Introduce stricter guidelines for handling sensitive topics while maintaining creative flexibility.
- **Impact**: Builds trust in the tool and ensures it meets parental and educator expectations.

---

## Contribution

Feel free to fork this repository and submit pull requests. Contributions are welcome to expand features, improve story quality, or enhance user interactions.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
