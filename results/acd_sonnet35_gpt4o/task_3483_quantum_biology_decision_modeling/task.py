import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition",
            "zero-point energy fluctuations",
            "quantum zeno effect"
        ]
        biological_processes = [
            "photosynthesis",
            "magnetoreception in birds",
            "olfaction (sense of smell)",
            "enzyme catalysis",
            "DNA mutation repair",
            "ion channel gating"
        ]
        decision_contexts = [
            "foraging behavior",
            "mate selection",
            "predator avoidance",
            "migration patterns",
            "circadian rhythm regulation",
            "immune system response"
        ]
        
        tasks = {}
        for i in range(1, 3):
            quantum_effect = random.choice(quantum_effects)
            biological_process = random.choice(biological_processes)
            decision_context = random.choice(decision_contexts)
            tasks[str(i)] = {
                "quantum_effect": quantum_effect,
                "biological_process": biological_process,
                "decision_context": decision_context
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Quantum biology is an emerging field that explores how quantum mechanical phenomena might play a role in biological processes. Your task is to model and analyze how the quantum effect of {t['quantum_effect']} might influence the biological process of {t['biological_process']} in the context of {t['decision_context']}. Your response should include:

1. Quantum-Biological Interface (250-350 words):
   a) Explain the basic principles of {t['quantum_effect']} and how it might manifest in biological systems.
   b) Describe the key features of {t['biological_process']} and how it relates to {t['decision_context']}.
   c) Propose a mechanism by which {t['quantum_effect']} could influence {t['biological_process']}.

2. Mathematical Model (250-350 words):
   a) Develop a mathematical model that incorporates both quantum and classical elements to describe the influence of {t['quantum_effect']} on {t['biological_process']}.
   b) Explain the key variables, parameters, and equations in your model.
   c) Discuss any assumptions or simplifications made in your model.

3. Predictions and Implications (200-300 words):
   a) Use your model to make specific predictions about how {t['quantum_effect']} might affect {t['decision_context']}.
   b) Discuss the potential evolutionary advantages or disadvantages of quantum-influenced decision-making in this context.
   c) Propose an experiment that could test your model's predictions.

4. Comparative Analysis (200-300 words):
   a) Compare your quantum-influenced model with a classical model of the same biological process.
   b) Discuss the key differences in predictions or explanatory power between the two models.
   c) Analyze the conditions under which quantum effects would be most relevant or negligible.

5. Challenges and Future Directions (150-250 words):
   a) Identify the main challenges in experimentally verifying quantum effects in {t['biological_process']}.
   b) Suggest two potential technological applications inspired by your model.
   c) Propose a related research question in quantum biology that could be explored using a similar approach.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biological systems. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and its potential role in biological systems.",
            f"The mathematical model effectively incorporates both quantum and classical elements to describe {t['biological_process']}.",
            f"The predictions and implications for {t['decision_context']} are logically derived from the model and biologically plausible.",
            "The comparative analysis between quantum-influenced and classical models is insightful and well-reasoned.",
            "The response identifies relevant challenges and proposes innovative future directions for research in quantum biology.",
            "The overall response demonstrates creativity, interdisciplinary knowledge integration, and speculative scientific reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
