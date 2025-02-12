import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        societal_issues = [
            "climate change mitigation",
            "global food distribution",
            "urban traffic optimization",
            "pandemic response planning",
            "renewable energy integration",
            "education resource allocation",
            "healthcare accessibility"
        ]
        quantum_techniques = [
            "quantum annealing",
            "quantum approximate optimization algorithm (QAOA)",
            "variational quantum eigensolver (VQE)",
            "quantum machine learning",
            "quantum Fourier transform",
            "quantum walk algorithms",
            "quantum error correction"
        ]
        return {
            "1": {
                "societal_issue": random.choice(societal_issues),
                "quantum_technique": random.choice(quantum_techniques)
            },
            "2": {
                "societal_issue": random.choice(societal_issues),
                "quantum_technique": random.choice(quantum_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to optimize solutions for {t['societal_issue']} using {t['quantum_technique']}, then analyze its potential impact and ethical implications. Your response should include:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum computing system.
   b) Explain how your system implements {t['quantum_technique']} to address {t['societal_issue']}.
   c) Detail any novel quantum algorithms or techniques your system employs.
   d) Include a high-level diagram of your system architecture (describe it in words).

2. Problem Formulation (250-300 words):
   a) Analyze the complexities of {t['societal_issue']} and why it's suitable for quantum optimization.
   b) Explain how you would model this problem in a way that leverages quantum advantages.
   c) Discuss any simplifications or assumptions made in your problem formulation.

3. Quantum-Classical Hybrid Approach (200-250 words):
   a) Describe how your system integrates classical and quantum computing elements.
   b) Explain the role of classical preprocessing and post-processing in your solution.
   c) Discuss strategies for mitigating the limitations of current quantum hardware.

4. Performance Analysis (250-300 words):
   a) Propose metrics to evaluate your system's performance in addressing {t['societal_issue']}.
   b) Compare the expected performance of your quantum system to classical alternatives.
   c) Discuss the scalability of your approach as quantum hardware improves.

5. Societal Impact (200-250 words):
   a) Analyze the potential positive and negative consequences of implementing your system.
   b) Discuss how your solution might affect different stakeholders in society.
   c) Consider any potential unintended consequences of your approach.

6. Ethical Implications (200-250 words):
   a) Identify ethical challenges arising from using quantum computing to address societal issues.
   b) Discuss concerns related to data privacy, algorithmic bias, and decision-making transparency.
   c) Propose guidelines for the responsible development and deployment of your system.

7. Future Developments (150-200 words):
   a) Suggest potential advancements or extensions of your system in the next decade.
   b) Discuss how progress in quantum computing might further impact solutions to societal problems.
   c) Propose a research agenda to address current limitations in applying quantum computing to {t['societal_issue']}.

Ensure your response demonstrates a deep understanding of quantum computing principles, the complexities of the chosen societal issue, and the ethical considerations of applying advanced technology to social problems. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_technique']} and its application to {t['societal_issue']}.",
            "The quantum system architecture is well-designed and clearly explained.",
            "The problem formulation effectively leverages quantum advantages.",
            "The performance analysis includes meaningful comparisons to classical alternatives.",
            "The societal impact and ethical implications are thoroughly considered.",
            "The response shows innovative thinking while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
