import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "cognitive_process": "decision-making",
                "emotional_state": "anxiety",
                "musical_style": "classical"
            },
            {
                "cognitive_process": "memory consolidation",
                "emotional_state": "nostalgia",
                "musical_style": "jazz"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on cognitive processes and emotional states, then analyze its output for a given scenario. Your task involves the following steps:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for cognitive music composition.
   b) Explain how it integrates cognitive science principles, emotional modeling, and music theory.
   c) Detail how the system addresses the challenge of translating cognitive processes and emotions into musical elements.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Cognitive-Emotional Mapping (200-250 words):
   a) Explain how your system models the cognitive process of {t['cognitive_process']}.
   b) Describe how it represents and processes the emotional state of {t['emotional_state']}.
   c) Discuss how these cognitive and emotional models are translated into musical parameters (e.g., rhythm, harmony, melody).

3. Musical Composition Process (200-250 words):
   a) Describe the step-by-step process your AI system would use to compose a piece in the {t['musical_style']} style.
   b) Explain how the cognitive process and emotional state influence each step of the composition.
   c) Discuss any novel techniques or algorithms used in your composition process.

4. Output Analysis (250-300 words):
   a) Provide a detailed description of the expected musical output for the given scenario.
   b) Analyze how the composed piece reflects the cognitive process of {t['cognitive_process']} and the emotional state of {t['emotional_state']}.
   c) Explain how the {t['musical_style']} style is maintained while expressing the cognitive-emotional state.
   d) Discuss any challenges or limitations your system might face in this scenario.

5. Evaluation and Implications (200-250 words):
   a) Propose a method to evaluate the effectiveness of your AI system in translating cognitive-emotional states into music.
   b) Discuss the potential implications of your system for our understanding of music cognition and emotional expression.
   c) Explore how this AI system might be used in fields such as music therapy, cognitive science research, or AI-assisted creativity.
   d) Suggest two directions for future research or improvements to your system.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and AI architectures. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, music theory, and AI architectures.",
            "The proposed AI system integrates cognitive processes, emotional modeling, and music composition in a novel and plausible way.",
            "The analysis of the system's output for the given scenario is detailed and coherent.",
            "The response shows creativity and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
