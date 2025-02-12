import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        proteins = [
            {
                "name": "Amyloid beta",
                "relevance": "Alzheimer's disease",
                "challenge": "Multiple stable conformations"
            },
            {
                "name": "Prion protein",
                "relevance": "Neurodegenerative diseases",
                "challenge": "Misfolding and aggregation"
            }
        ]
        return {
            "1": random.choice(proteins),
            "2": random.choice(proteins)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-biological hybrid system for modeling protein folding, focusing on {t['name']} (relevant to {t['relevance']}). Your system should address the specific challenge of {t['challenge']}. Provide your response in the following format:

1. Quantum-Biological Hybrid System Design (300-350 words):
   a) Describe the key components of your hybrid system, including both quantum and classical elements.
   b) Explain how quantum principles are leveraged to model protein folding.
   c) Detail how your system integrates biological data and quantum computations.
   d) Discuss any novel features that specifically address the challenge of {t['challenge']}.
   e) Include a simple equation or mathematical representation related to your quantum-biological system.

2. Implementation for {t['name']} (250-300 words):
   a) Outline the steps to apply your system to model the folding of {t['name']}.
   b) Describe how your system accounts for the protein's specific characteristics and folding challenges.
   c) Explain how you would validate your model's predictions against experimental data.
   d) Discuss potential insights your system might provide about {t['relevance']}.

3. Quantum Advantage Analysis (200-250 words):
   a) Compare the performance of your quantum-biological hybrid system to classical protein folding simulations.
   b) Analyze the potential speedup or accuracy improvements offered by the quantum components.
   c) Discuss any limitations or challenges specific to the quantum aspects of your system.

4. Scalability and Future Prospects (200-250 words):
   a) Evaluate the scalability of your system to larger, more complex proteins.
   b) Propose potential improvements or extensions to your system for future development.
   c) Discuss how advancements in quantum hardware might impact the capabilities of your system.

5. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical considerations in using quantum-enhanced simulations for protein folding research.
   b) Discuss the possible societal impacts of more accurate protein folding predictions, especially in the context of {t['relevance']}.
   c) Propose guidelines for responsible development and use of quantum-biological hybrid systems in medical research.

Ensure your response demonstrates a deep understanding of quantum computing, molecular biology, and bioinformatics. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and considering real-world implications.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a quantum-biological hybrid system for modeling protein folding, with a focus on {t['name']}.",
            f"The system adequately addresses the specific challenge of {t['challenge']}.",
            "The quantum advantage analysis demonstrates a clear understanding of both quantum computing and protein folding simulations.",
            "The response shows interdisciplinary knowledge integration and creative problem-solving in quantum physics and molecular biology.",
            "The ethical and societal implications are thoughtfully considered and discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
