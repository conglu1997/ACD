import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing",
            "quantum walks"
        ]
        creative_challenges = [
            "designing a sustainable city on Mars",
            "creating a universal language for interspecies communication",
            "developing a non-invasive brain-computer interface",
            "inventing a new form of renewable energy",
            "solving the global food security crisis"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "creative_challenge": random.choice(creative_challenges)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "creative_challenge": random.choice(creative_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired artificial general intelligence (AGI) system capable of solving complex, open-ended problems, focusing on the quantum principle of {t['quantum_principle']}. Then, apply your system to the creative challenge of {t['creative_challenge']}. Your response should include the following sections:

1. Quantum-Inspired AGI Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AGI system.
   b) Explain how your system incorporates the quantum principle of {t['quantum_principle']}.
   c) Discuss how your system achieves general intelligence capabilities.
   d) Provide a high-level diagram or pseudocode illustrating your system's architecture.

2. Quantum-Classical Integration (250-300 words):
   a) Explain how your system integrates quantum and classical computing elements.
   b) Describe any novel quantum algorithms or approaches used in your AGI system.
   c) Discuss potential advantages of your quantum-inspired approach over classical AGI systems.

3. Creative Problem-Solving Approach (300-350 words):
   a) Outline how your AGI system approaches the challenge of {t['creative_challenge']}.
   b) Provide a step-by-step explanation of your system's problem-solving process.
   c) Describe at least two innovative solutions your system might generate.
   d) Explain how the quantum principle of {t['quantum_principle']} contributes to the creative process.

4. Ethical and Societal Implications (200-250 words):
   a) Discuss potential ethical concerns related to your quantum-inspired AGI system.
   b) Analyze possible societal impacts of applying your system to real-world problems.
   c) Propose guidelines for responsible development and use of quantum-inspired AGI.

5. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your quantum-inspired AGI approach.
   b) Suggest areas for future research and development in quantum AGI systems.
   c) Propose an experiment to validate the effectiveness of your system.

Ensure your response demonstrates a deep understanding of quantum computing principles, AGI theory, and creative problem-solving techniques. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum principle and how it can be applied to AGI systems.",
            "The proposed AGI architecture is well-designed and coherently integrates quantum and classical elements.",
            "The creative problem-solving approach is logical, innovative, and clearly leverages the quantum-inspired AGI system.",
            "The response addresses ethical and societal implications thoughtfully and proposes reasonable guidelines.",
            "Limitations and future directions are identified and discussed realistically.",
            "The overall response is well-structured, coherent, and demonstrates interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
