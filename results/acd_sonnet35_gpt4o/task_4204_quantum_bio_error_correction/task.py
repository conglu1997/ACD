import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "DNA replication",
            "protein folding",
            "cellular respiration",
            "photosynthesis",
            "signal transduction"
        ]
        quantum_error_correction_methods = [
            "surface code",
            "color code",
            "stabilizer code",
            "topological code",
            "bosonic code"
        ]
        molecular_biology_problems = [
            "predicting protein structures",
            "designing targeted drug delivery systems",
            "optimizing CRISPR-Cas9 gene editing",
            "modeling complex cellular networks",
            "enhancing biofuel production efficiency"
        ]
        
        return {
            "1": {
                "biological_process": random.choice(biological_processes),
                "quantum_method": random.choice(quantum_error_correction_methods),
                "problem": random.choice(molecular_biology_problems)
            },
            "2": {
                "biological_process": random.choice(biological_processes),
                "quantum_method": random.choice(quantum_error_correction_methods),
                "problem": random.choice(molecular_biology_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum error correction system inspired by the biological process of {t['biological_process']}, utilizing principles from the {t['quantum_method']} quantum error correction method. Then, apply your system to address the molecular biology problem of {t['problem']}. Your response should include the following sections:

1. Quantum-Biological Interface (300-350 words):
   a) Describe the key features of {t['biological_process']} that inspire your quantum error correction system.
   b) Explain how you incorporate principles from the {t['quantum_method']} into your bio-inspired design.
   c) Discuss the theoretical basis for applying quantum error correction to biological processes.

2. System Architecture (250-300 words):
   a) Provide a high-level overview of your quantum bio-error correction system's architecture.
   b) Explain how classical and quantum components interact in your design.
   c) Describe any novel algorithms or approaches used in your system.
   d) Include a simplified diagram or pseudocode snippet illustrating a key part of your system.

3. Application to Molecular Biology (250-300 words):
   a) Detail how your quantum bio-error correction system addresses the problem of {t['problem']}.
   b) Explain the theoretical advantages of your approach compared to classical methods.
   c) Discuss potential limitations or challenges in applying your system to this problem.

4. Simulation and Validation (200-250 words):
   a) Propose a method to simulate and test your quantum bio-error correction system.
   b) Describe how you would validate its effectiveness in addressing the given problem.
   c) Discuss potential challenges in translating simulated results to real-world biological systems.

5. Implications and Future Directions (200-250 words):
   a) Analyze the broader implications of your system for the fields of quantum computing and molecular biology.
   b) Suggest three potential avenues for further research based on your approach.
   c) Discuss how your system might contribute to our understanding of quantum effects in biological systems.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to the development and application of your system.
   b) Propose guidelines for responsible research and use of quantum-biological technologies.
   c) Discuss potential societal impacts of advancements in this field.

Ensure your response demonstrates a deep understanding of quantum computing, molecular biology, and error correction principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            "The proposed quantum bio-error correction system demonstrates a clear and plausible connection between the specified biological process and quantum error correction method.",
            "The application to the given molecular biology problem is well-explained and theoretically sound.",
            "The response shows a deep understanding of quantum computing, molecular biology, and error correction principles.",
            "The proposed simulation, validation methods, and future research directions are logical and scientifically plausible.",
            "The ethical considerations and guidelines for responsible research are thoughtful and comprehensive.",
            "The overall response is creative, innovative, and maintains scientific plausibility throughout."
        ]
        result = eval_with_llm_judge(instructions, submission, criteria)
        return float(result) if result is not None else None
