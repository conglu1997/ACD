import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "quantum_concept": "quantum entanglement",
                "ethical_dilemma": "privacy and free will",
                "context": "interstellar communication"
            },
            {
                "quantum_concept": "quantum superposition",
                "ethical_dilemma": "identity and consciousness",
                "context": "medical treatment"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a thought experiment that explores the ethical implications of {t['quantum_concept']} in the context of {t['context']}, focusing on the ethical dilemma of {t['ethical_dilemma']}. Your response should include:

1. Thought Experiment Design (250-300 words):
   a) Describe the setup of your thought experiment, incorporating {t['quantum_concept']} as a key element.
   b) Explain how the scenario relates to {t['context']}.
   c) Clearly state the ethical dilemma involving {t['ethical_dilemma']}.

2. Quantum Mechanics Explanation (150-200 words):
   a) Explain the relevant aspects of {t['quantum_concept']} in lay terms.
   b) Discuss how this quantum phenomenon is crucial to the ethical implications in your thought experiment.

3. Ethical Analysis (200-250 words):
   a) Analyze the ethical implications of your thought experiment.
   b) Present arguments for at least two different ethical positions.
   c) Discuss how {t['quantum_concept']} challenges traditional notions of {t['ethical_dilemma']}.

4. Philosophical and Scientific Implications (150-200 words):
   a) Explore how your thought experiment might influence our understanding of {t['ethical_dilemma']}.
   b) Discuss potential implications for scientific research or technological development.

5. Real-World Connections (100-150 words):
   a) Relate your thought experiment to current or near-future technological developments.
   b) Propose how insights from your analysis could inform policy or ethical guidelines.

Ensure your response demonstrates a deep understanding of both quantum mechanics and ethical philosophy. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and philosophical rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The thought experiment should incorporate {t['quantum_concept']} as a key element",
            f"The ethical dilemma should clearly involve {t['ethical_dilemma']}",
            f"The context of {t['context']} should be well-integrated into the scenario",
            "The response should demonstrate a deep understanding of both quantum mechanics and ethical philosophy",
            "The ethical analysis should present multiple perspectives and explore the implications thoroughly"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
