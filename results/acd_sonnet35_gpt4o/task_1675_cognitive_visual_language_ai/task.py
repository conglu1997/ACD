import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Gestalt principles of perception",
            "Cognitive load theory",
            "Dual coding theory",
            "Embodied cognition",
            "Prototype theory"
        ]
        visual_elements = [
            "Geometric shapes",
            "Color gradients",
            "Textural patterns",
            "Spatial relationships",
            "Temporal sequences"
        ]
        tasks = {
            "1": {
                "cognitive_principle": random.choice(cognitive_principles),
                "visual_element": random.choice(visual_elements)
            },
            "2": {
                "cognitive_principle": random.choice(cognitive_principles),
                "visual_element": random.choice(visual_elements)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret abstract visual languages based on cognitive principles. Your system should focus on the following:

Cognitive Principle: {t['cognitive_principle']}
Visual Element: {t['visual_element']}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and interpreting abstract visual languages.
   b) Explain how it incorporates the specified cognitive principle and visual element.
   c) Detail how the system generates visual representations and interprets their meanings.
   d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters.

2. Cognitive-Visual Mapping (200-250 words):
   a) Explain how the specified cognitive principle is mapped to visual representations.
   b) Describe how the system utilizes the given visual element in its language generation and interpretation.
   c) Discuss any novel approaches to cognitive-visual translation in your design.

3. Language Generation Process (200-250 words):
   a) Detail how your AI system generates abstract visual languages.
   b) Explain how it maintains coherence and meaning in the generated languages.
   c) Discuss how the system balances creativity and adherence to cognitive principles.

4. Interpretation Mechanism (200-250 words):
   a) Describe how your system interprets and derives meaning from the abstract visual languages it generates.
   b) Explain the algorithms or methods used for visual pattern recognition and semantic analysis.
   c) Discuss how the system handles ambiguity or multiple interpretations.

5. Output Analysis (150-200 words):
   a) Describe the expected characteristics of the visual languages produced by your system.
   b) Explain how the output reflects both the cognitive principle and the visual element.
   c) Discuss potential insights into human cognition or visual processing that could be gained from this system.

6. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your cognitive visual language AI system.
   b) Describe the methodology, including participant selection, data collection, and analysis techniques.
   c) Explain how you would measure both the visual coherence and the cognitive representation accuracy.

7. Potential Applications and Ethical Considerations (150-200 words):
   a) Suggest two potential real-world applications of your system.
   b) Discuss any ethical implications or potential misuse of such a system.
   c) Propose guidelines for responsible development and use of cognitive visual language AI.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, visual design, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words. Stay within the specified word count for each section.

For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The AI system design clearly incorporates the given cognitive principle and visual element",
            "The cognitive-visual mapping and language generation process are well-defined and logically consistent",
            "The proposal demonstrates creative problem-solving and interdisciplinary knowledge application",
            "The experimental design and potential applications show deep understanding and insightful reasoning",
            "The response includes a clear and informative ASCII art or Unicode diagram of the system architecture"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
