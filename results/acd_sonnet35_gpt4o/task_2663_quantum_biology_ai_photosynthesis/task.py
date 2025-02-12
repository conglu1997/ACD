import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling"
        ]
        applications = [
            "solar energy harvesting",
            "artificial photosynthesis",
            "quantum computing"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_effect": random.choice(quantum_effects),
                "application": random.choice(applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by {t['quantum_effect']} in photosynthesis to optimize energy transfer in {t['application']}. Quantum coherence refers to the phenomenon where particles maintain a well-defined phase relationship over an extended period, allowing for efficient energy transfer.

Your response should include the following sections:

1. Quantum Biology Analysis (200-250 words):
   a) Explain the role of {t['quantum_effect']} in natural photosynthesis.
   b) Describe how this quantum effect contributes to the efficiency of energy transfer in plants.
   c) Discuss current scientific understanding and any controversies surrounding this quantum effect in biological systems.

2. AI System Architecture (250-300 words):
   a) Propose a novel AI architecture that mimics or draws inspiration from {t['quantum_effect']} in photosynthesis.
   b) Explain how your AI system incorporates quantum principles to optimize energy transfer.
   c) Describe the key components of your AI system and their interactions.
   d) Include a high-level diagram or pseudocode representing your architecture.

3. Application to {t['application']} (200-250 words):
   a) Explain how your quantum-inspired AI system could be applied to {t['application']}.
   b) Discuss the potential advantages of your approach over classical methods.
   c) Identify any challenges in implementing your system and propose solutions.

4. Quantum-Classical Interface (150-200 words):
   a) Describe how your AI system bridges the gap between quantum effects and classical computation.
   b) Explain any novel algorithms or data structures used to represent quantum information in a classical system.

5. Performance Analysis (200-250 words):
   a) Propose methods to evaluate the performance of your quantum-inspired AI system.
   b) Compare the theoretical efficiency of your system to both natural photosynthesis and current artificial systems.
   c) Discuss any potential limitations or trade-offs in your approach.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of implementing your quantum-inspired AI system in {t['application']}.
   b) Propose two potential research directions to further develop or expand upon your architecture.
   c) Speculate on how advancements in this field might impact society and scientific understanding.

Ensure your response demonstrates a deep understanding of quantum biology, artificial intelligence, and the specific application area. Be creative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Cite relevant scientific literature to support your claims and proposals throughout your response.

Format your response with clear headings for each section, including the word count for each section in parentheses at the end. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts",
            f"The AI system design clearly incorporates principles of {t['quantum_effect']} and addresses {t['application']}",
            "The response includes a high-level diagram or pseudocode for the AI architecture",
            "The response demonstrates a deep understanding of quantum biology, AI, and the specific application area",
            "The response is creative, scientifically plausible, and well-explained",
            "The response addresses ethical implications and future research directions",
            "The response cites relevant scientific literature to support claims and proposals"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
