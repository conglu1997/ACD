import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_problems = [
            {
                "problem": "Protein folding prediction",
                "constraint": "Minimize energy consumption",
                "quantum_concept": "Quantum tunneling",
                "concept_explanation": "the quantum mechanical phenomenon where a particle tunnels through a barrier that it classically could not surmount"
            },
            {
                "problem": "Gene regulatory network inference",
                "constraint": "Maximize information transfer",
                "quantum_concept": "Quantum entanglement",
                "concept_explanation": "a quantum mechanical phenomenon where the quantum states of two or more objects have to be described with reference to each other, even though the individual objects may be spatially separated"
            }
        ]
        return {
            "1": random.choice(biological_problems),
            "2": random.choice(biological_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired genetic algorithm to solve the complex biological problem of {t['problem']}, while addressing the constraint to {t['constraint']}. Your algorithm must specifically incorporate the quantum concept of {t['quantum_concept']} ({t['concept_explanation']}). Your response should include:

1. Algorithm Overview (200-250 words):
   a) Describe the key components of your quantum-inspired genetic algorithm.
   b) Explain how it incorporates principles from quantum mechanics (especially {t['quantum_concept']}), information theory, and evolutionary biology.
   c) Discuss how your algorithm addresses the given biological problem and constraint.

2. Quantum Mechanics Integration (150-200 words):
   a) Detail how {t['quantum_concept']} is used in your algorithm.
   b) Explain how this quantum concept enhances the genetic algorithm's performance or capabilities.
   c) Provide a mathematical or conceptual representation of a quantum operation in your algorithm, focusing on {t['quantum_concept']}.

3. Information Theory Application (150-200 words):
   a) Describe how information theory concepts are applied in your algorithm.
   b) Explain how these concepts contribute to solving the biological problem or addressing the constraint.
   c) Discuss any novel information-theoretic measures or techniques you've incorporated.

4. Evolutionary Process (150-200 words):
   a) Outline the evolutionary aspects of your algorithm, including selection, crossover, and mutation operators.
   b) Explain how these operators are modified or enhanced by quantum and information theory principles, particularly {t['quantum_concept']}.
   c) Describe how your algorithm maintains biological plausibility while incorporating quantum-inspired elements.

5. Performance Analysis (100-150 words):
   a) Propose a method for evaluating the performance of your algorithm compared to classical approaches.
   b) Discuss potential advantages and limitations of your quantum-inspired approach, especially related to the use of {t['quantum_concept']}.
   c) Suggest how the algorithm's performance might scale with problem complexity.

6. Interdisciplinary Implications (75-100 words):
   a) Discuss how your algorithm might contribute to advancements in quantum computing, information theory, or evolutionary biology.
   b) Propose a potential application of your algorithm outside of the original biological context.

7. Ethical Considerations (75-100 words):
   a) Identify potential ethical implications or concerns related to the development or application of your algorithm.
   b) Suggest guidelines for responsible use and development of such interdisciplinary algorithms.

Ensure your response demonstrates a deep understanding of quantum mechanics (especially {t['quantum_concept']}), information theory, and evolutionary biology. Use appropriate technical terminology and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response with clear headings for each section.

Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the biological problem of {t['problem']} and the constraint to {t['constraint']}.",
            f"The proposed algorithm must incorporate the quantum concept of {t['quantum_concept']} in a meaningful and scientifically plausible way.",
            "The algorithm must integrate principles from quantum mechanics, information theory, and evolutionary biology, demonstrating a clear understanding of each field.",
            "The submission must include all seven required elements as specified in the instructions, with each section adequately addressing its respective topics.",
            "The proposed quantum-inspired genetic algorithm must be logically coherent and demonstrate a clear understanding of how the interdisciplinary concepts work together.",
            "The response must be creative and propose novel ideas while remaining grounded in scientific principles from the relevant fields.",
            f"The explanation of how {t['quantum_concept']} enhances the algorithm must be scientifically plausible, well-reasoned, and demonstrate a deep understanding of the quantum concept.",
            "The performance analysis and ethical considerations must be thoughtful and demonstrate an understanding of the broader implications of the proposed algorithm."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
