import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            "Baroque counterpoint",
            "Classical sonata form",
            "Romantic period harmonies",
            "Jazz improvisation"
        ]
        mathematical_models = [
            "Markov chains",
            "Fractals",
            "Cellular automata",
            "Neural networks"
        ]
        constraints = [
            "Must include a golden ratio-based structure",
            "Must incorporate microtonal intervals",
            "Must feature polyrhythmic patterns",
            "Must use only prime number harmonics"
        ]
        example_elements = [
            "Bach-style four-part harmony",
            "Mozart-style melodic development",
            "Debussy-inspired whole-tone scales",
            "Miles Davis-inspired modal jazz progressions"
        ]
        
        tasks = [
            {
                "musical_style": random.choice(musical_styles),
                "mathematical_model": random.choice(mathematical_models),
                "constraint": random.choice(constraints),
                "example_element": random.choice(example_elements)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates original musical compositions in the style of {t['musical_style']}, using {t['mathematical_model']} for structural analysis and generation. Your system must also incorporate the following constraint: {t['constraint']}. Additionally, demonstrate how your system would analyze and generate a musical element similar to {t['example_element']}.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI composition system.
   b) Explain how you integrate music theory principles with the chosen mathematical model.
   c) Detail how your system incorporates the given musical style and constraint.
   d) Provide a high-level diagram or pseudocode representing the system's workflow (describe this textually, do not attempt to include actual diagrams).

2. Harmonic Analysis (200-250 words):
   a) Explain how your system analyzes and models harmonic structures.
   b) Describe any novel techniques used for identifying and generating harmonic progressions.
   c) Discuss how your approach captures the essence of the given musical style.
   d) Provide an example of how your system would analyze a chord progression typical of the given style.

3. Mathematical Modeling (200-250 words):
   a) Elaborate on how you implement the specified mathematical model in your system.
   b) Explain how this model contributes to the generation of musical structures.
   c) Discuss any adaptations or extensions you've made to the model for musical applications.
   d) Include a simple mathematical formula or equation that is central to your model's functioning (describe this textually).

4. Constraint Implementation (150-200 words):
   a) Describe how you incorporate the given constraint into your composition process.
   b) Explain any challenges in implementing this constraint and how you addressed them.
   c) Discuss how this constraint affects the musical output and its relationship to the chosen style.

5. Creative Process (200-250 words):
   a) Outline the steps your AI system takes to generate a musical composition.
   b) Explain how your system balances adherence to style and mathematical structure with creativity.
   c) Provide an example of how a specific musical element (similar to {t['example_element']}) might be generated using your system.

6. Evaluation Metrics (150-200 words):
   a) Propose methods to evaluate the quality and style-adherence of the generated compositions.
   b) Describe how you would compare your AI's output to human-composed music in the same style.
   c) Discuss any limitations in evaluating computer-generated music and how you might address them.

7. Ethical and Artistic Implications (150-200 words):
   a) Discuss the potential impact of AI-generated music on human composers and the music industry.
   b) Explore the artistic value of compositions created by your system.
   c) Propose guidelines for the responsible development and use of AI in music composition.

Ensure your response demonstrates a deep understanding of music theory, mathematical modeling, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining musical and mathematical rigor.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1300-1650 words. Do not use bullet points or numbered lists within sections; each section should be a cohesive paragraph or set of paragraphs."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system must generate compositions in the style of {t['musical_style']}",
            f"The system must use {t['mathematical_model']} for structural analysis and generation",
            f"The system must incorporate the constraint: {t['constraint']}",
            f"The response must include an analysis or generation example related to {t['example_element']}",
            "The response should demonstrate deep understanding of music theory, mathematical modeling, and AI",
            "The proposed system should be innovative and creatively integrate multiple disciplines",
            "The response should address all required sections with appropriate depth and clarity",
            "The response should include a textual description of a high-level diagram or pseudocode",
            "The response should include a textual description of a mathematical formula or equation",
            "The response should be within the specified word count range (1300-1650 words)",
            "The response should not use bullet points or numbered lists within sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
