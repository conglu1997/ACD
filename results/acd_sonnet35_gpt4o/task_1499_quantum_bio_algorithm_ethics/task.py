import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        biological_problems = [
            "protein folding",
            "gene regulatory networks",
            "enzyme kinetics",
            "neural signal processing"
        ]
        ethical_considerations = [
            "data privacy",
            "equitable access to technology",
            "potential for misuse in bioweapons",
            "impact on traditional research methods"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_problem": random.choice(biological_problems),
                "ethical_consideration": random.choice(ethical_considerations)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_problem": random.choice(biological_problems),
                "ethical_consideration": random.choice(ethical_considerations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired algorithm to address the biological problem of {t['biological_problem']}, focusing on the quantum principle of {t['quantum_principle']}. Then, analyze its potential impact on scientific research and discuss the ethical implications of its use, with particular attention to {t['ethical_consideration']}. Your response should include the following sections:

1. Algorithm Design (250-300 words):
   a) Describe the key components and functioning of your quantum-inspired algorithm.
   b) Explain how it incorporates the quantum principle of {t['quantum_principle']}.
   c) Discuss how your algorithm addresses the biological problem of {t['biological_problem']}.
   d) Provide a high-level pseudocode or flow diagram of your algorithm.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your algorithm bridges quantum principles with biological processes.
   b) Discuss any novel approaches or insights gained from this quantum-biological integration.
   c) Address potential challenges in implementing your algorithm for real-world biological applications.

3. Scientific Impact Analysis (200-250 words):
   a) Analyze how your algorithm could advance research in {t['biological_problem']}.
   b) Discuss potential broader impacts on the field of biology and related disciplines.
   c) Compare the advantages of your approach to traditional methods in the field.

4. Ethical Implications (200-250 words):
   a) Examine the ethical considerations surrounding the development and use of your algorithm, focusing on {t['ethical_consideration']}.
   b) Discuss potential unintended consequences or misuse of this technology.
   c) Propose guidelines for the responsible development and application of quantum-inspired biological algorithms.

5. Future Prospects and Challenges (150-200 words):
   a) Speculate on how quantum-inspired biological algorithms might evolve in the next decade.
   b) Identify key technical or conceptual challenges that need to be overcome.
   c) Suggest two potential research directions that could significantly enhance the capabilities of your approach.

Ensure your response demonstrates a deep understanding of quantum computing principles, biological processes, and research ethics. Use appropriate terminology from quantum physics, biology, and ethics. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1000-1250 words.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-designed quantum-inspired algorithm addressing {t['biological_problem']} using the principle of {t['quantum_principle']}.",
            "The algorithm design should be innovative yet scientifically plausible.",
            "The analysis should demonstrate a deep understanding of both quantum computing and biology.",
            f"The ethical implications, particularly regarding {t['ethical_consideration']}, must be thoroughly discussed.",
            "The response must include all five required sections with appropriate content and adherence to word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
