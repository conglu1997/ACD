import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        physical_constants = [
            {
                "constant": "speed of light",
                "symbol": "c",
                "value": "299,792,458 m/s"
            },
            {
                "constant": "Planck's constant",
                "symbol": "h",
                "value": "6.62607015 × 10^-34 J⋅s"
            }
        ]
        physical_phenomena = [
            "black hole event horizon",
            "quantum entanglement"
        ]
        return {
            "1": {"constant": random.choice(physical_constants), "phenomenon": random.choice(physical_phenomena)},
            "2": {"constant": random.choice(physical_constants), "phenomenon": random.choice(physical_phenomena)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language system based on the fundamental physical constant of {t['constant']['constant']} ({t['constant']['symbol']} = {t['constant']['value']}), then use it to describe the complex physical phenomenon of {t['phenomenon']}. Your task has the following parts:

1. Language Design (250-300 words):
   a) Explain how you will incorporate the given physical constant into the basic structure of your language.
   b) Describe the phonology (or alternative communication method) of your language, relating it to the constant.
   c) Outline the grammatical rules of your language, demonstrating how they reflect properties of the constant.
   d) Provide at least 5 example words or phrases in your language, with their meanings and explanations of how they relate to the constant.

2. Vocabulary Generation (150-200 words):
   a) Create a list of 10 key terms related to the given physical phenomenon.
   b) Translate these terms into your designed language.
   c) Explain how each translation reflects aspects of both the term's meaning and the physical constant.

3. Phenomenon Description (200-250 words):
   a) Write a short paragraph (5-7 sentences) describing the given physical phenomenon using your designed language.
   b) Provide an English translation of your description.
   c) Explain how your language's unique features enhance the description of the phenomenon.

4. Language Analysis (200-250 words):
   a) Discuss how your language's structure might influence or change the understanding of the physical phenomenon.
   b) Analyze the strengths and limitations of your language in describing complex physical concepts.
   c) Propose how your language might be used to generate new insights or hypotheses about the physical world.

5. Interdisciplinary Implications (150-200 words):
   a) Explore how your language might be applied in fields outside of physics (e.g., philosophy, art, education).
   b) Discuss the potential cognitive effects of using a physics-based language for general communication.
   c) Propose an experiment to test the impact of your language on scientific reasoning or problem-solving.

Ensure your response demonstrates a deep understanding of both linguistics and physics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and linguistic coherence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design incorporates the given physical constant in its basic structure, phonology, and grammatical rules",
            "At least 5 example words or phrases are provided with clear explanations of their relation to the constant",
            "A list of 10 key terms related to the given physical phenomenon is translated into the designed language with explanations",
            "A short paragraph describing the physical phenomenon is written in the designed language and translated to English",
            "The language analysis discusses how the language structure might influence understanding of the physical phenomenon",
            "Interdisciplinary implications of the language are explored, including potential applications and cognitive effects",
            "The response demonstrates a deep understanding of both linguistics and physics",
            "The language design is creative while maintaining scientific plausibility and linguistic coherence"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
