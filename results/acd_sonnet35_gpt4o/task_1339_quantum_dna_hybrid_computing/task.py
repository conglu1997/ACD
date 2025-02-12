import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "dna_mechanism": "base pairing",
                "computational_problem": "protein folding prediction"
            },
            {
                "quantum_principle": "entanglement",
                "dna_mechanism": "strand displacement",
                "computational_problem": "cryptography"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-DNA computing system that leverages both quantum principles and DNA-based information processing to solve complex computational problems. Your system should incorporate the quantum principle of {t['quantum_principle']} and the DNA mechanism of {t['dna_mechanism']} to address the computational problem of {t['computational_problem']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your hybrid quantum-DNA computing system.
   b) Explain how it incorporates both quantum and DNA-based components.
   c) Detail how the system integrates {t['quantum_principle']} and {t['dna_mechanism']}.
   d) Discuss any novel interfaces or mechanisms required for quantum-DNA interaction.

2. Quantum-DNA Information Processing (250-300 words):
   a) Explain how information is encoded, processed, and read out in your hybrid system.
   b) Describe how {t['quantum_principle']} is utilized in the computation process.
   c) Detail how {t['dna_mechanism']} contributes to information processing.
   d) Discuss any synergies or unique computational properties arising from this hybrid approach.

3. Application to {t['computational_problem']} (200-250 words):
   a) Explain how your hybrid system addresses the problem of {t['computational_problem']}.
   b) Compare the potential efficiency and capabilities of your system to current approaches.
   c) Discuss any limitations or challenges specific to this application.

4. Theoretical Analysis (200-250 words):
   a) Provide a theoretical framework for the computational power of your hybrid system.
   b) Discuss how it relates to complexity classes in traditional, quantum, and DNA computing.
   c) Analyze potential speedups or unique capabilities compared to non-hybrid systems.

5. Implementation Challenges (150-200 words):
   a) Identify major technical challenges in realizing this hybrid quantum-DNA system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any required advancements in quantum technology or DNA manipulation techniques.

6. Ethical Implications and Future Prospects (150-200 words):
   a) Discuss ethical considerations of developing such powerful computational systems.
   b) Explore potential long-term impacts on scientific research and society.
   c) Propose guidelines for responsible development and use of hybrid quantum-DNA computing.

7. Summary and Conclusion (100-150 words):
   Provide a brief summary of your hybrid quantum-DNA computing system, highlighting its key features, potential impact, and the most significant challenges to be addressed.

Ensure your response demonstrates a deep understanding of quantum physics, molecular biology, and computer science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section.

Your entire response should be between 1300-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, molecular biology, and computer science.",
            "The proposed hybrid quantum-DNA computing system is novel, well-explained, and scientifically plausible.",
            "The system effectively integrates the specified quantum principle and DNA mechanism.",
            "The application to the given computational problem is clearly explained and shows potential for meaningful improvement over current approaches.",
            "The theoretical analysis is sound and insightful.",
            "Implementation challenges and ethical implications are appropriately addressed.",
            "The response is creative while maintaining scientific rigor.",
            "A concise summary is provided, highlighting key features and challenges of the proposed system.",
            "The response adheres to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
