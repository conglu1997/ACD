import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_mappings = [
            {
                "input": "sound",
                "output": "color",
                "example": "A high-pitched violin note"
            },
            {
                "input": "texture",
                "output": "taste",
                "example": "The feel of sandpaper"
            },
            {
                "input": "shape",
                "output": "smell",
                "example": "A perfect sphere"
            },
            {
                "input": "color",
                "output": "sound",
                "example": "Deep crimson red"
            },
            {
                "input": "taste",
                "output": "shape",
                "example": "The taste of lemon"
            },
            {
                "input": "smell",
                "output": "texture",
                "example": "The scent of fresh-cut grass"
            }
        ]
        return {str(i+1): random.choice(sensory_mappings) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate artificial synesthetic experiences by translating {t['input']} inputs into {t['output']} outputs. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for artificial synesthesia generation.
   b) Explain how your system processes {t['input']} inputs and generates corresponding {t['output']} outputs.
   c) Detail any novel techniques or algorithms used in your model.
   d) Include a brief description of a diagram or flowchart representing your system architecture.

2. Sensory Mapping Mechanism (200-250 words):
   a) Explain the specific mechanism used to map {t['input']} features to {t['output']} characteristics.
   b) Discuss how your system ensures consistency and coherence in the generated synesthetic experiences.
   c) Address any challenges in creating meaningful cross-modal associations.

3. Training and Data Requirements (150-200 words):
   a) Describe the type of data needed to train your artificial synesthesia system.
   b) Propose methods for collecting or generating this training data.
   c) Discuss any potential biases in the data and how to mitigate them.

4. Evaluation and Validation (200-250 words):
   a) Propose metrics for evaluating the quality and coherence of the generated synesthetic experiences.
   b) Describe an experiment to validate your system's ability to create meaningful cross-modal associations.
   c) Discuss how you would compare your system's output to the experiences of natural synesthetes.

5. Applications and Implications (150-200 words):
   a) Explore potential applications of your artificial synesthesia system in fields such as art, accessibility, or human-computer interaction.
   b) Discuss the ethical implications of creating artificial sensory experiences.
   c) Consider potential benefits and risks of widespread use of such technology.

6. Future Directions (100-150 words):
   a) Propose two potential extensions or improvements to your artificial synesthesia system.
   b) Discuss how this technology might evolve over the next decade and its potential impact on society.

7. Creative Challenge (100-150 words):
   Using your proposed system, describe the artificial synesthetic experience that would be generated for the following input: {t['example']}. Be specific and creative in your description of the {t['output']} output.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and sensory perception. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1150-1500 words.

Your response will be evaluated based on the following criteria:
1. Comprehensiveness and accuracy of the system design
2. Innovation and plausibility of the proposed mechanisms
3. Thoughtfulness in addressing challenges and limitations
4. Quality of the evaluation and validation methods
5. Insightfulness of the applications and ethical considerations
6. Creativity and coherence of the artificial synesthetic experience description
7. Adherence to the specified format and word count guidelines"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of artificial synesthesia and related cognitive science concepts",
            "The proposed AI system architecture is innovative, coherent, and scientifically plausible",
            f"The sensory mapping mechanism effectively translates {t['input']} inputs to {t['output']} outputs",
            "The training and data requirements are well-thought-out and address potential challenges",
            "The evaluation and validation methods are appropriate and well-designed",
            "The discussion of applications and implications is insightful and considers both benefits and risks",
            "The future directions proposed are innovative and relevant",
            f"The creative challenge response for the input '{t['example']}' is imaginative and consistent with the proposed system",
            "The response adheres to the specified word counts and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
