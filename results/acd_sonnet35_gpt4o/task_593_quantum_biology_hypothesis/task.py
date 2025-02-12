import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "magnetoreception in birds",
            "olfaction (sense of smell)",
            "DNA mutation repair",
            "neurotransmitter release",
            "circadian rhythm regulation",
            "protein folding"
        ]
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition",
            "quantum vibrations"
        ]
        return {
            "1": {"process": random.choice(biological_processes), "effect": random.choice(quantum_effects)},
            "2": {"process": random.choice(biological_processes), "effect": random.choice(quantum_effects)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Formulate and analyze a novel hypothesis for a quantum effect in a biological process. Specifically, explore how {t['effect']} might play a role in {t['process']}. Your response should include:

1. Hypothesis Formulation (200-250 words):
   a) Clearly state your hypothesis about how {t['effect']} could influence {t['process']}.
   b) Explain the theoretical basis for your hypothesis, drawing on current understanding of both quantum mechanics and biology.
   c) Describe the potential mechanism by which this quantum effect could operate in the biological system.

2. Theoretical Framework (250-300 words):
   a) Develop a theoretical framework that supports your hypothesis.
   b) Explain how this framework integrates principles from quantum mechanics and biology.
   c) Discuss any existing models or theories that your framework builds upon or challenges.
   d) Include at least one mathematical equation or formalism that describes a key aspect of your proposed quantum biological interaction.

3. Experimental Design (250-300 words):
   a) Propose a detailed theoretical experiment to test your hypothesis.
   b) Describe the experimental setup, including any specialized equipment or techniques required.
   c) Explain how you would measure or detect the proposed quantum effect in the biological process.
   d) Discuss potential challenges in implementing this experiment and how they might be overcome.
   e) Describe expected results that would support or refute your hypothesis.

4. Implications and Future Directions (200-250 words):
   a) Discuss the potential implications of your hypothesis if proven correct.
   b) Explain how this could impact our understanding of {t['process']} and biological systems in general.
   c) Propose two potential applications that could arise from this quantum biological effect.
   d) Suggest future research directions or extensions of your work.

5. Critical Analysis (150-200 words):
   a) Identify potential weaknesses or limitations in your hypothesis and experimental design.
   b) Discuss alternative explanations for the proposed quantum effects in {t['process']}.
   c) Explain how your hypothesis could be further refined or improved based on this critical analysis.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biological systems. Use appropriate scientific terminology and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific rigor and plausibility. Your total response should be between 1050-1300 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The hypothesis must involve {t['effect']} in {t['process']}.",
            "The response must include a clear hypothesis formulation, theoretical framework, experimental design, implications discussion, and critical analysis.",
            "The theoretical framework must include at least one mathematical equation or formalism.",
            "The experimental design must be detailed and address potential challenges.",
            "The response must demonstrate a deep understanding of both quantum mechanics and biological systems.",
            "The proposed hypothesis and experiment must be creative yet scientifically plausible.",
            "The response must be well-structured and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
