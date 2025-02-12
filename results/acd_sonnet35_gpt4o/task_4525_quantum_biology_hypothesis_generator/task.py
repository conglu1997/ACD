import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "photosynthesis",
            "magnetoreception in birds",
            "olfaction (smell)",
            "enzyme catalysis"
        ]
        quantum_phenomena = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "zero-point energy"
        ]
        return {
            "1": {"bio_process": random.choice(biological_processes), "quantum_phenomenon": random.choice(quantum_phenomena)},
            "2": {"bio_process": random.choice(biological_processes), "quantum_phenomenon": random.choice(quantum_phenomena)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and evaluates hypotheses in quantum biology, focusing on the potential role of {t['quantum_phenomenon']} in {t['bio_process']}. Your response should include:

1. Background (200-250 words):
   a) Briefly explain the chosen biological process and quantum phenomenon.
   b) Discuss current scientific understanding of their potential interaction.
   c) Highlight any existing hypotheses or research in this area.

2. AI System Design (250-300 words):
   a) Outline the key components of your AI system for hypothesis generation and evaluation.
   b) Explain how your system integrates knowledge from quantum physics and biology.
   c) Describe the data sources and types of data your system would use.
   d) Discuss any novel AI techniques or approaches used in your system.

3. Hypothesis Generation (200-250 words):
   a) Explain how your AI system generates hypotheses about quantum effects in the given biological process.
   b) Provide an example of a hypothesis your system might generate.
   c) Discuss how your system ensures the scientific plausibility of generated hypotheses.

4. Hypothesis Evaluation (200-250 words):
   a) Describe the criteria your system uses to evaluate generated hypotheses.
   b) Explain how your system assesses the potential impact and testability of hypotheses.
   c) Discuss how your system handles the speculative nature of some quantum biology concepts.

5. Experimental Design (150-200 words):
   a) Propose an experiment that could test the example hypothesis from section 3.
   b) Explain how your AI system could assist in designing and optimizing this experiment.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss potential ethical considerations in using AI for hypothesis generation in quantum biology.
   b) Explore philosophical implications of quantum effects in biological systems.
   c) Address how your system balances scientific rigor with openness to novel ideas.

Ensure your response demonstrates a deep understanding of both quantum physics and biology, as well as AI capabilities in scientific research. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific biological process ({t['bio_process']}) and quantum phenomenon ({t['quantum_phenomenon']}) given in the task.",
            "The AI system design must be logically consistent and demonstrate understanding of both quantum physics and biology.",
            "The generated hypothesis and proposed experiment must be scientifically plausible and relevant to the given biological process and quantum phenomenon.",
            "The response must include all six required sections: Background, AI System Design, Hypothesis Generation, Hypothesis Evaluation, Experimental Design, and Ethical and Philosophical Implications.",
            "The response should demonstrate creativity and interdisciplinary thinking while maintaining scientific rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
