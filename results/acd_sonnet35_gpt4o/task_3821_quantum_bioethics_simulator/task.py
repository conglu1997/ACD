import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        bioethical_dilemmas = [
            "genetic enhancement of human embryos",
            "creation of human-animal chimeras for organ transplantation",
            "use of brain-computer interfaces for cognitive enhancement",
            "development of autonomous AI for medical decision-making",
            "creation of artificial wombs for human gestation"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "decoherence",
            "quantum annealing"
        ]
        return {
            "1": {
                "bioethical_dilemma": random.choice(bioethical_dilemmas),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "bioethical_dilemma": random.choice(bioethical_dilemmas),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing simulation system to model complex bioethical scenarios and their potential outcomes across multiple universes, then use it to analyze the bioethical dilemma of {t['bioethical_dilemma']}. Your system should specifically incorporate the quantum principle of {t['quantum_principle']}. Provide your response in the following format:

1. Quantum Bioethics Simulator Design (300-350 words):
   a) Describe the overall architecture of your quantum computing simulation system.
   b) Explain how it models bioethical scenarios across multiple universes.
   c) Detail how you've incorporated the specified quantum principle into your system.
   d) Discuss how your system integrates biological processes and ethical frameworks.

2. Simulation Process (250-300 words):
   a) Outline the steps your system takes to simulate a bioethical scenario.
   b) Explain how it generates and evaluates multiple potential outcomes.
   c) Describe how the system handles ethical variables and decision points.
   d) Discuss how quantum effects influence the simulation results.

3. Analysis of the Given Bioethical Dilemma (300-350 words):
   a) Apply your quantum bioethics simulator to the specified dilemma.
   b) Present and interpret the results of your simulation.
   c) Discuss how the quantum principle affects the ethical landscape of this scenario.
   d) Compare the outcomes across different simulated universes.

4. Ethical Implications (200-250 words):
   a) Analyze the ethical implications revealed by your simulation.
   b) Discuss how quantum effects might influence our understanding of bioethics.
   c) Consider potential biases or limitations in your simulation approach.

5. Potential Applications and Future Developments (200-250 words):
   a) Propose two potential applications of your quantum bioethics simulator.
   b) Suggest how this technology could impact policy-making and medical research.
   c) Discuss potential future enhancements to your system.

6. Challenges and Limitations (150-200 words):
   a) Identify key technological and philosophical challenges in implementing your system.
   b) Discuss any ethical concerns about using quantum simulations for bioethical decision-making.
   c) Propose potential solutions or areas for further research.

Ensure your response demonstrates a deep understanding of quantum mechanics, bioethics, and computational modeling. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a quantum computing simulation system that incorporates the quantum principle of {t['quantum_principle']} and analyzes the bioethical dilemma of {t['bioethical_dilemma']}.",
            "The system design must demonstrate a clear integration of quantum mechanics, bioethics, and computational modeling.",
            "The simulation process must be clearly explained, including how it generates and evaluates multiple outcomes across different universes.",
            "The analysis of the given bioethical dilemma must be thorough and demonstrate how quantum effects influence the ethical landscape.",
            "The response must discuss ethical implications, potential applications, and challenges of the proposed system.",
            "The response must be creative and speculative while maintaining scientific plausibility.",
            "Appropriate terminology from quantum mechanics, bioethics, and computational modeling must be used throughout the response.",
            "The response must be well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
