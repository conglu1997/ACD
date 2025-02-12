import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            "protein folding",
            "gene regulatory networks",
            "neurotransmitter dynamics",
            "cellular metabolism"
        ]
        ethical_issues = [
            "genetic discrimination",
            "privacy of genetic information",
            "equitable access to personalized treatments",
            "unintended consequences of genetic modifications"
        ]
        tasks = [
            {
                "biological_system": system,
                "ethical_issue": issue
            }
            for system in biological_systems
            for issue in ethical_issues
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing simulation of {t['biological_system']} and analyze its ethical implications for personalized medicine and genetic privacy, with a particular focus on {t['ethical_issue']}. Your response should include:

1. Quantum Simulation Design (300-350 words):
   a) Describe the key components of your quantum computing simulation for {t['biological_system']}.
   b) Explain how quantum algorithms or principles are utilized in your simulation.
   c) Discuss the advantages of using quantum computing for this biological system compared to classical computing approaches.
   d) Address potential challenges in implementing this simulation and propose solutions.
   e) Provide a simple diagram or pseudocode (5-10 lines) illustrating a key aspect of your quantum simulation design.

2. Biological System Analysis (250-300 words):
   a) Explain the complexity of {t['biological_system']} and why it's a suitable candidate for quantum simulation.
   b) Describe how your simulation captures the essential features and dynamics of the biological system.
   c) Discuss potential insights or discoveries that could be gained from this quantum simulation.

3. Personalized Medicine Applications (200-250 words):
   a) Propose three potential applications of your quantum simulation in personalized medicine.
   b) Explain how these applications could improve current medical practices or patient outcomes.
   c) Discuss any limitations or potential risks associated with these applications.

4. Ethical Implications Analysis (250-300 words):
   a) Analyze the ethical implications of your quantum simulation, focusing on {t['ethical_issue']}.
   b) Discuss how the use of this technology might impact individual privacy, social equity, and healthcare policies.
   c) Propose guidelines or safeguards to address the identified ethical concerns.

5. Future Directions and Societal Impact (200-250 words):
   a) Suggest two potential advancements or extensions of your quantum bio-simulation.
   b) Discuss how these advancements might further impact society, healthcare, and individual rights.
   c) Propose a framework for ongoing ethical evaluation and regulation of quantum bio-simulations.

Ensure your response demonstrates a deep understanding of quantum computing, biology, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing practical and ethical considerations.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words. Include a word count at the end of each section and a total word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the quantum simulation of {t['biological_system']} and analyzes the ethical implications related to {t['ethical_issue']}.",
            "The quantum simulation design is innovative, scientifically plausible, and clearly explained, including a diagram or pseudocode.",
            "The response demonstrates a deep understanding of quantum computing, biology, and bioethics, using appropriate technical terminology.",
            "The personalized medicine applications are well-thought-out, relevant, and their limitations are discussed.",
            "The ethical implications analysis is thorough, considers multiple perspectives, and proposes concrete guidelines or safeguards.",
            "The response is creative while maintaining scientific accuracy and interdisciplinary coherence.",
            "All five sections are adequately addressed within the specified word count ranges.",
            "The response includes word counts for each section and a total word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
