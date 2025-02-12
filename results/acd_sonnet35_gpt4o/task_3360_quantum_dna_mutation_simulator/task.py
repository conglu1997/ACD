import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "decoherence"
        ]
        biological_processes = [
            "DNA replication",
            "transcription",
            "protein folding",
            "enzymatic catalysis"
        ]
        evolutionary_mechanisms = [
            "natural selection",
            "genetic drift",
            "gene flow",
            "mutation"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate and analyze potential quantum effects in DNA mutation and evolution. Your system should focus on the quantum principle of {t['quantum_principle']}, the biological process of {t['biological_process']}, and the evolutionary mechanism of {t['evolutionary_mechanism']}. Your response should include:

1. Quantum-Biological Interface (250-300 words):
   a) Explain how the specified quantum principle could potentially influence the given biological process.
   b) Describe the theoretical basis for quantum effects in this biological context.
   c) Discuss any existing evidence or hypotheses related to quantum effects in this area of biology.

2. Simulation System Architecture (200-250 words):
   a) Outline the key components of your quantum computing system for simulating these processes.
   b) Explain how your system models both quantum and biological aspects of the problem.
   c) Describe any novel quantum algorithms or techniques used in your simulation.

3. Evolutionary Implications (200-250 words):
   a) Analyze how the quantum effects you're simulating could impact the specified evolutionary mechanism.
   b) Propose a hypothesis about how quantum-influenced mutations might affect evolutionary processes.
   c) Discuss potential long-term consequences for species evolution if these quantum effects are significant.

4. Simulation Experiment Design (150-200 words):
   a) Propose an experiment using your system to test a specific hypothesis about quantum effects in DNA mutation or evolution.
   b) Describe the variables, methodology, and expected outcomes of your experiment.
   c) Explain how you would validate the results of your quantum simulation.

5. Challenges and Limitations (100-150 words):
   a) Identify potential challenges in simulating quantum biological processes.
   b) Discuss limitations of current quantum computing technology for this application.
   c) Propose potential solutions or future research directions to address these challenges.

6. Interdisciplinary Implications (100-150 words):
   a) Discuss how your quantum DNA mutation simulator could impact other fields of study.
   b) Propose two potential applications of your system outside of evolutionary biology.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and evolutionary theory. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['quantum_principle']} and how it could potentially influence {t['biological_process']}.",
            f"The simulation system architecture effectively integrates quantum computing concepts with biological modeling, particularly for {t['biological_process']}.",
            f"The analysis of evolutionary implications shows a deep understanding of {t['evolutionary_mechanism']} and how it might be affected by quantum-influenced mutations.",
            "The proposed experiment is well-designed and could potentially yield meaningful insights into quantum effects in DNA mutation or evolution.",
            "The response shows creativity and innovation in applying quantum principles to biological systems, while maintaining scientific plausibility.",
            "The interdisciplinary implications discussed demonstrate a nuanced understanding of the potential impact of quantum biology on other fields of study."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
