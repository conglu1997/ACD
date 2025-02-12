import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "superposition",
                "biological_structure": "DNA",
                "information_theory_concept": "error correction"
            },
            "2": {
                "quantum_principle": "entanglement",
                "biological_structure": "neural networks",
                "information_theory_concept": "compression"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological computing system that leverages principles from quantum mechanics, molecular biology, and information theory to process and store information at the cellular level. Your system should incorporate the following elements:

1. Quantum Principle: {t['quantum_principle']}
2. Biological Structure: {t['biological_structure']}
3. Information Theory Concept: {t['information_theory_concept']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-biological computing system.
   b) Explain how these components interact to process and store information.
   c) Detail how your system incorporates the specified quantum principle, biological structure, and information theory concept.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture (describe it textually).

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your system bridges the gap between quantum phenomena and biological processes.
   b) Discuss any novel mechanisms or structures you've designed to facilitate this interface.
   c) Address potential challenges in maintaining quantum coherence in a biological environment.

3. Information Processing and Storage (250-300 words):
   a) Describe how information is encoded, processed, and stored in your system.
   b) Explain how your system leverages the specified information theory concept to enhance its capabilities.
   c) Compare the theoretical performance of your system to classical and quantum computers.

4. Potential Applications (200-250 words):
   a) Propose three potential applications of your quantum-biological computing system.
   b) Explain how each application leverages the unique features of your system.
   c) Discuss any ethical considerations or potential societal impacts of these applications.

5. Experimental Validation (150-200 words):
   a) Propose an experiment to test a key feature or prediction of your quantum-biological computing system.
   b) Describe the methodology, including necessary equipment and measurable outcomes.
   c) Discuss potential challenges in implementing this experiment and how they might be overcome.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory.",
            "The proposed system successfully integrates the specified quantum principle, biological structure, and information theory concept.",
            "The quantum-biological interface is clearly explained and addresses potential challenges.",
            "The information processing and storage mechanisms are well-described and leverage the specified information theory concept.",
            "The proposed applications are innovative and clearly leverage the unique features of the system.",
            "The experimental validation proposal is well-designed and addresses potential challenges.",
            "The response is creative while maintaining scientific plausibility.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
