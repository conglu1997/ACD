import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                'process': 'Photosynthesis',
                'quantum_aspect': 'Quantum coherence in energy transfer'
            },
            {
                'process': 'DNA mutation and repair',
                'quantum_aspect': 'Quantum tunneling in proton transfer'
            }
        ]
        
        return {str(i+1): random.choice(biological_processes) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 45 minutes to design a novel quantum algorithm inspired by the biological process of {t['process']}, focusing on the quantum aspect of {t['quantum_aspect']}. Your response should include:

1. Biological Process Analysis (200-250 words):
   a) Explain the key features of {t['process']}, focusing on {t['quantum_aspect']}.
   b) Describe how quantum effects play a role in this biological process.

2. Quantum Algorithm Design (300-350 words):
   a) Present your quantum algorithm, detailing its structure and function.
   b) Explain how your algorithm mimics or adapts the biological process.
   c) Describe the quantum operations and gates used in your algorithm.
   d) Provide a high-level pseudocode or quantum circuit diagram for your algorithm.

3. Example Processing (150-200 words):
   a) Provide a small, specific input example for your algorithm.
   b) Walk through how your algorithm would process this input, step by step.

4. Potential Applications (200-250 words):
   a) Propose two potential applications of your quantum algorithm in different fields.
   b) Explain how these applications leverage the bio-inspired aspects of your algorithm.
   c) Discuss any advantages your algorithm might have over classical approaches.

5. Complexity Analysis (150-200 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare its efficiency to known classical algorithms for similar problems.

6. Quantum Error Correction (150-200 words):
   a) Discuss potential sources of quantum errors in your algorithm.
   b) Propose a suitable quantum error correction method for your algorithm.
   c) Explain how this error correction method would be implemented.

7. Limitations and Future Work (150-200 words):
   a) Discuss potential limitations or challenges in implementing your algorithm.
   b) Propose ideas for future research to extend or improve your algorithm.

8. Interdisciplinary Implications (150-200 words):
   a) Discuss how your bio-inspired quantum algorithm might contribute to our understanding of the original biological process.
   b) Explore potential insights this work could offer to the field of quantum biology.

Ensure your response demonstrates a deep understanding of quantum computing principles, biological processes, and algorithmic design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of {t['process']} and its quantum aspects is accurate and clear.",
            "The quantum algorithm design is novel, well-structured, and clearly inspired by the biological process.",
            "The example processing demonstrates a concrete understanding of how the algorithm works.",
            "The proposed applications are innovative and leverage the bio-inspired aspects of the algorithm.",
            "The complexity analysis demonstrates a good understanding of quantum algorithm efficiency.",
            "The quantum error correction discussion is relevant and well-reasoned.",
            "The discussion of limitations and future work shows critical thinking and insight.",
            "The interdisciplinary implications are thoughtfully explored and demonstrate a broad understanding of quantum biology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
