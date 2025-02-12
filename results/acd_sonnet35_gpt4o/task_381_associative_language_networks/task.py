import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time", "love", "freedom", "knowledge", "creativity",
            "justice", "nature", "technology", "identity", "change"
        ]
        return {
            "1": {"concept": random.choice(concepts)},
            "2": {"concept": random.choice(concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an Associative Language Network (ALN) for the concept of '{t['concept']}'. Your task consists of the following steps:\n\n" + \
               "1. Network Design (200-250 words):\n" + \
               "   a) Describe the structure of your ALN, including node types and connection mechanisms.\n" + \
               "   b) Explain how your network incorporates principles from neural networks and cognitive science.\n" + \
               "   c) Discuss how your ALN represents and processes the given concept in a non-linear, associative manner.\n\n" + \
               "2. Implementation (200-250 words):\n" + \
               "   a) Provide a Python-like pseudocode implementation of the core components of your ALN.\n" + \
               "   b) Include functions for node creation, association formation, and concept processing.\n" + \
               "   c) Explain how your implementation handles ambiguity and context in language processing.\n\n" + \
               "3. Example Processing (150-200 words):\n" + \
               "   a) Demonstrate how your ALN would process the sentence: 'The concept of {t['concept']} is constantly evolving.'\n" + \
               "   b) Explain the network's internal state changes and the resulting interpretation.\n\n" + \
               "4. Comparative Analysis (150-200 words):\n" + \
               "   a) Compare your ALN to traditional NLP approaches for understanding and generating language related to abstract concepts.\n" + \
               "   b) Discuss potential advantages and limitations of your approach.\n\n" + \
               "5. Cognitive Implications (150-200 words):\n" + \
               "   a) Analyze how your ALN might reflect or diverge from human cognitive processes in language understanding.\n" + \
               "   b) Discuss potential insights your model could provide for cognitive science or linguistics.\n\n" + \
               "6. Future Directions (100-150 words):\n" + \
               "   a) Propose two potential research projects or applications that could build upon your ALN.\n" + \
               "   b) Briefly describe the methodology and expected outcomes of these projects.\n\n" + \
               "Ensure your response demonstrates a deep understanding of neural networks, cognitive science, and natural language processing. " + \
               "Be creative in your design while maintaining scientific and computational plausibility. " + \
               "Your total response should be between 1000-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate word counts.",
            "The Associative Language Network design is novel, well-explained, and incorporates principles from neural networks and cognitive science.",
            "The implementation pseudocode is coherent and addresses core ALN functionalities.",
            "The example processing demonstrates a non-linear, associative approach to language understanding.",
            "The comparative analysis and cognitive implications sections show deep understanding and insightful analysis.",
            "The response demonstrates creativity, interdisciplinary knowledge, and analytical thinking throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
