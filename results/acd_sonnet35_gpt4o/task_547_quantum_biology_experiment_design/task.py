import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition"
        ]
        biological_systems = [
            "photosynthesis",
            "magnetoreception in birds",
            "olfaction (sense of smell)",
            "enzyme catalysis"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_system": random.choice(biological_systems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an experiment to test the role of {t['quantum_effect']} in {t['biological_system']}. Your response should include:

1. Background (150-200 words):
   a) Briefly explain the quantum effect and its potential relevance to the biological system.
   b) Summarize current scientific understanding and any existing evidence for quantum effects in this or similar biological systems.

2. Hypothesis (50-100 words):
   Clearly state your hypothesis about how {t['quantum_effect']} might play a role in {t['biological_system']}.

3. Experimental Design (300-350 words):
   a) Describe your experimental setup, including any specialized equipment or techniques required.
   b) Explain your methodology, including control groups and variables to be measured.
   c) Discuss how your experiment specifically tests for {t['quantum_effect']} in {t['biological_system']}.
   d) Address potential challenges in isolating quantum effects from classical phenomena.

4. Data Analysis (150-200 words):
   a) Describe how you would analyze the data collected from your experiment.
   b) Explain what results would support or refute your hypothesis.
   c) Discuss any statistical methods or modeling techniques you would use.

5. Potential Implications (100-150 words):
   Discuss the broader implications of your experiment, regardless of the outcome. How might the results impact our understanding of quantum biology or biological processes in general?

6. Ethical Considerations (50-100 words):
   Address any ethical considerations related to your experimental design, particularly if it involves living organisms.

7. Future Directions (100-150 words):
   Propose two follow-up studies or experiments that could build on your results, regardless of the outcome.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biology, as well as experimental design principles. Be creative in your approach while maintaining scientific rigor and plausibility. Your total response should be between 900-1250 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['quantum_effect']} and its potential role in {t['biological_system']}.",
            "The experimental design must be scientifically sound and specifically target the quantum effect in the given biological system.",
            "The response must address the challenges of isolating quantum effects from classical phenomena in biological systems.",
            "The data analysis plan must be appropriate for the proposed experiment and hypothesis.",
            "The response must demonstrate creativity and originality in the experimental approach while maintaining scientific plausibility.",
            "The discussion of potential implications and future directions must show a broad understanding of the field of quantum biology.",
            "The response must address relevant ethical considerations.",
            "The overall response must demonstrate interdisciplinary knowledge integration and advanced scientific reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
