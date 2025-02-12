import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'cultures': ['Japanese', 'Scandinavian', 'Moroccan'],
                'time_period': '50 years',
                'architectural_elements': ['facades', 'interior spaces', 'urban planning']
            },
            '2': {
                'cultures': ['Brazilian', 'Indian', 'Australian Aboriginal'],
                'time_period': '100 years',
                'architectural_elements': ['sustainable materials', 'communal spaces', 'integration with nature']
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the evolution of aesthetic preferences across different cultures, then apply it to predict and generate future trends in architectural design. Focus on the following cultures: {', '.join(t['cultures'])}. Your system should predict trends over the next {t['time_period']} and focus on these architectural elements: {', '.join(t['architectural_elements'])}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling cultural aesthetic evolution.
   b) Explain how your system integrates knowledge from cultural anthropology, cognitive science, and architectural design.
   c) Detail how the system processes historical and contemporary data on aesthetic preferences.
   d) Discuss any novel algorithms or techniques used in your design.

2. Cultural Aesthetic Evolution Model (250-300 words):
   a) Explain the mechanisms your system uses to model the evolution of aesthetic preferences.
   b) Describe how your model accounts for cultural exchange and global influences.
   c) Discuss how your system handles the emergence and propagation of new aesthetic trends.

3. Application to Architectural Design (250-300 words):
   a) Describe how you would apply your system to predict future trends in architectural design for the specified cultures.
   b) Explain how your system incorporates the given architectural elements into its predictions.
   c) Provide an example of a potential future trend for each culture, explaining how it evolved from current aesthetics.

4. AI-Generated Design Concepts (200-250 words):
   a) Describe how your system would generate new architectural design concepts based on predicted aesthetic trends.
   b) Provide a brief description of one AI-generated design concept for each culture, highlighting how it reflects the evolved aesthetic preferences.
   c) Explain how your system ensures that generated designs are both innovative and culturally appropriate.

5. Evaluation and Validation (200-250 words):
   a) Propose a method to evaluate the accuracy and cultural sensitivity of your system's predictions and generated designs.
   b) Describe how you would validate your model against real-world data and expert opinions.
   c) Discuss potential biases in your system and how you would address them.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss the potential impact of AI-predicted and AI-generated architectural designs on cultural identity and diversity.
   b) Explore the ethical considerations of using AI to influence aesthetic trends and architectural practices.
   c) Propose guidelines for responsible development and use of such AI systems in creative and cultural domains.

7. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your proposed system.
   b) Suggest potential improvements or extensions to address these limitations.
   c) Propose a research direction that could further advance our understanding of cultural aesthetic evolution and its application in design fields.

Ensure your response demonstrates a deep understanding of cultural anthropology, cognitive science, architectural design, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cultural anthropology, cognitive science, architectural design, and artificial intelligence.",
            "The proposed AI system architecture is well-designed and incorporates novel approaches to modeling cultural aesthetic evolution.",
            "The application to architectural design is thoughtful and provides plausible future trends for each specified culture.",
            "The AI-generated design concepts are innovative yet culturally appropriate.",
            "The evaluation and validation methods are well-reasoned and address potential biases.",
            "The discussion of ethical and societal implications is insightful and proposes meaningful guidelines.",
            "The limitations and future directions are clearly identified and suggest valuable areas for further research.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
