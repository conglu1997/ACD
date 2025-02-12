import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        memory_processes = [
            "Encoding",
            "Consolidation",
            "Retrieval",
            "Reconsolidation"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "memory_process": random.choice(memory_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "memory_process": random.choice(memory_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based neural memory encoding system that leverages the quantum principle of {t['quantum_principle']} to enhance the human memory process of {t['memory_process']}. Your response should include the following sections:

1. System Overview (200-250 words):
   a) Describe the key components of your quantum neural memory system.
   b) Explain how it incorporates the principle of {t['quantum_principle']}.
   c) Discuss how the system interacts with the brain's natural {t['memory_process']} process.

2. Quantum-Neural Interface (200-250 words):
   a) Detail how your system interfaces with neurons at a quantum level.
   b) Explain how quantum effects are maintained in the warm, wet environment of the brain.
   c) Describe any novel materials or technologies required for this interface.

3. Information Processing (150-200 words):
   a) Explain how information is encoded, stored, or retrieved using your quantum system.
   b) Compare the efficiency and capacity of your system to traditional biological memory.
   c) Discuss any unique computational properties that arise from this quantum-neural approach.

4. Potential Applications (150-200 words):
   a) Propose at least two novel applications for your quantum neural memory system.
   b) Explain how these applications leverage the unique features of your system.
   c) Discuss the potential impact of these applications on individuals and society.

5. Challenges and Ethical Considerations (150-200 words):
   a) Identify at least two major challenges in realizing this quantum neural memory system.
   b) Discuss potential ethical implications of enhancing human memory through quantum technology.
   c) Propose guidelines or safeguards to address these ethical concerns.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and information theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible description of a quantum neural memory system incorporating {t['quantum_principle']}.",
            f"The system's interaction with the brain's {t['memory_process']} process is clearly explained.",
            "The quantum-neural interface is described in detail, addressing the challenges of maintaining quantum effects in the brain.",
            "The information processing section clearly explains how the system enhances memory capabilities beyond traditional biological limits.",
            "At least two novel and impactful applications of the system are proposed and explained.",
            "Major challenges and ethical considerations are thoughtfully discussed, with proposed guidelines or safeguards.",
            "The overall response demonstrates a strong grasp of quantum mechanics, neuroscience, and information theory principles, creatively applied to a speculative technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
