import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synaesthesia_types = [
            {
                "type": "Grapheme-color synaesthesia",
                "description": "Association of letters or numbers with specific colors",
                "application": "Cryptography"
            },
            {
                "type": "Chromesthesia",
                "description": "Association of sounds with colors",
                "application": "Music composition"
            },
            {
                "type": "Lexical-gustatory synaesthesia",
                "description": "Association of words or phonemes with tastes",
                "application": "Culinary innovation"
            },
            {
                "type": "Spatial-sequence synaesthesia",
                "description": "Perception of numerical sequences as points in space",
                "application": "Data visualization"
            }
        ]
        return {str(i+1): synesthesia for i, synesthesia in enumerate(random.sample(synaesthesia_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of simulating {t['type']} and apply it to solve a problem or generate a creative output in the domain of {t['application']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for simulating {t['type']}.
   b) Explain how your system models the relationship between the different sensory or cognitive modalities involved.
   c) Discuss any novel approaches or algorithms used in your design.

2. Training and Data (150-200 words):
   a) Describe the type of data your system would need to learn {t['type']}.
   b) Explain your approach to collecting or generating this data.
   c) Discuss any ethical considerations in data collection or system training.

3. Synaesthetic Simulation (200-250 words):
   a) Provide a detailed example of how your system would simulate a specific {t['type']} experience.
   b) Explain how this simulation captures the key features of human synaesthetic experiences.
   c) Discuss any limitations or challenges in accurately simulating {t['type']}.

4. Application to {t['application']} (250-300 words):
   a) Describe a specific problem or creative task in {t['application']} that your system will address.
   b) Explain step-by-step how your synaesthetic AI system would approach this task.
   c) Discuss how the synaesthetic capability provides unique advantages or insights for this application.
   d) Provide a concrete example of the system's output or solution.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your synaesthetic AI system.
   b) Describe how you would validate the system's outputs in the context of {t['application']}.
   c) Discuss any potential biases or limitations in your evaluation approach.

6. Implications and Future Directions (100-150 words):
   a) Discuss the potential implications of your system for our understanding of human cognition and perception.
   b) Propose two potential future applications or extensions of your synaesthetic AI system.

Ensure your response demonstrates a deep understanding of synaesthesia, artificial intelligence, and the specific application domain. Be creative in your approach while maintaining scientific and technological plausibility. Use clear headings for each section in your response.

Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified type of synaesthesia and its potential applications",
            "The AI system design is innovative, coherent, and technologically plausible",
            "The application to the specified domain is well-reasoned and showcases the unique advantages of the synaesthetic approach",
            "The response effectively addresses all required sections with appropriate detail and word count",
            "The proposed evaluation methods and future directions show critical thinking and insight"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
