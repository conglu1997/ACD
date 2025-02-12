import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        oscillation_types = ['delta', 'theta', 'alpha', 'beta', 'gamma']
        music_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        cognitive_functions = ['attention', 'memory', 'emotion', 'creativity']
        
        return {
            "1": {
                "oscillation": random.choice(oscillation_types),
                "music_element": random.choice(music_elements),
                "cognitive_function": random.choice(cognitive_functions)
            },
            "2": {
                "oscillation": random.choice(oscillation_types),
                "music_element": random.choice(music_elements),
                "cognitive_function": random.choice(cognitive_functions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) that translates {t['oscillation']} neural oscillations into musical {t['music_element']}, with a focus on the cognitive function of {t['cognitive_function']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your BCI system.
   b) Explain how it captures and processes {t['oscillation']} oscillations.
   c) Detail the algorithm for translating neural signals into {t['music_element']}.
   d) Discuss how the system incorporates the cognitive function of {t['cognitive_function']}.

2. Neuroscientific Basis (200-250 words):
   a) Explain the significance of {t['oscillation']} oscillations in brain function.
   b) Describe how these oscillations relate to {t['cognitive_function']}.
   c) Discuss potential challenges in accurately interpreting these neural signals.

3. Music Theory Application (200-250 words):
   a) Explain how your system applies music theory principles to generate {t['music_element']}.
   b) Provide a specific example of how a 10-second pattern of {t['oscillation']} oscillations would be translated into a musical output. Describe the neural pattern and the resulting musical element in detail.
   c) Discuss how this approach might influence or challenge traditional music composition methods.

4. Cognitive and Creative Implications (150-200 words):
   a) Analyze how this BCI might affect the user's {t['cognitive_function']}.
   b) Discuss the potential for this technology to enhance or alter the creative process in music composition.
   c) Explore any ethical considerations related to modifying cognitive functions through this BCI.

5. Future Research and Applications (150-200 words):
   a) Propose two potential applications of your BCI system outside of music composition.
   b) Suggest areas for future research to improve or expand the capabilities of your system.
   c) Discuss how this technology might contribute to our understanding of the relationship between brain function and music.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the role of {t['oscillation']} oscillations and their relation to {t['cognitive_function']}.",
            f"The system design clearly describes how {t['oscillation']} oscillations are translated into musical {t['music_element']}.",
            "The answer demonstrates a deep understanding of neuroscience, music theory, and AI principles.",
            "The proposed BCI system is innovative yet scientifically plausible.",
            "The response addresses all required sections with appropriate detail and length.",
            "The implications and future applications of the technology are thoughtfully explored.",
            "A specific example of translating a 10-second neural pattern into a musical output is provided and clearly explained.",
            "The total response is between 950-1200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
