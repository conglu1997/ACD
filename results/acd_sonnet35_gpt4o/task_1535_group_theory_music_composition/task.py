import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            {
                "element": "rhythm",
                "group_operation": "cyclic permutations"
            },
            {
                "element": "harmony",
                "group_operation": "dihedral group transformations"
            }
        ]
        return {
            "1": random.choice(musical_elements),
            "2": random.choice(musical_elements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel music composition system based on group theory principles, focusing on {t['element']} and using {t['group_operation']}. Then, use this system to create and analyze a short musical piece. Your response should include:

1. System Design (250-300 words):
   a) Explain how you will apply {t['group_operation']} to {t['element']} in your composition system.
   b) Describe the mathematical structure of your system, including the group elements and operations.
   c) Discuss how your system maintains musical coherence while adhering to group theory principles.
   d) Provide a simple example of how a basic musical idea would be transformed in your system.

2. Composition Process (200-250 words):
   a) Outline the steps you would take to compose a short piece using your system.
   b) Explain how you balance mathematical rigor with artistic expression in your composition process.
   c) Describe any constraints or guidelines you would follow to ensure the piece remains musically interesting.

3. Musical Analysis (200-250 words):
   a) Provide a brief description or notation of a short musical piece (8-16 measures) created using your system.
   b) Analyze the piece, explaining how it demonstrates the principles of your composition system.
   c) Discuss any emerging patterns or structures that result from applying group theory to music.

4. Theoretical Implications (150-200 words):
   a) Explore how your system challenges or extends traditional music theory concepts.
   b) Discuss potential applications of your system in music education or analysis.
   c) Propose an experiment to test the perceptual effects of group theory-based compositions on listeners.

5. Computational Implementation (150-200 words):
   a) Describe how you would implement your composition system as a computer program.
   b) Outline the main algorithms or data structures you would use.
   c) Discuss any challenges in translating the mathematical system into a computational model.

Ensure your response demonstrates a deep understanding of both group theory and music theory. Use appropriate terminology from mathematics and music throughout your explanation. Be creative in your approach while maintaining mathematical rigor and musical plausibility.

Format your response with clear headings for each section, and number your points where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and creative application of group theory principles to music composition.",
            "The designed system is mathematically sound and musically coherent.",
            "The composition process and musical analysis show how the system is applied in practice.",
            "The response explores theoretical implications and potential applications of the system.",
            "The computational implementation is feasible and well-explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
