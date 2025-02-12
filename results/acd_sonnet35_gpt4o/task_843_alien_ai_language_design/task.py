import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_structures = [
            "Hive mind with distributed processing",
            "Quantum-based cognition with probabilistic thinking",
            "Time-dilated perception spanning millennia",
            "Multidimensional spatial reasoning",
            "Emotion-centric logic system"
        ]
        communication_constraints = [
            "Can only transmit in discrete energy pulses",
            "Must communicate through manipulation of gravitational fields",
            "Uses rapid changes in color and pattern for expression",
            "Communicates by altering the quantum states of particles",
            "Exchanges information through complex chemical compounds"
        ]
        tasks = {
            "1": {
                "cognitive_structure": random.choice(cognitive_structures),
                "communication_constraint": random.choice(communication_constraints)
            },
            "2": {
                "cognitive_structure": random.choice(cognitive_structures),
                "communication_constraint": random.choice(communication_constraints)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system for artificial intelligences or hypothetical alien entities with the following characteristics:

Cognitive Structure: {t['cognitive_structure']}
Communication Constraint: {t['communication_constraint']}

Your task is to create a detailed proposal for this communication system. Include the following sections in your response:

1. Foundational Principles (200-250 words):
   a) Explain how the given cognitive structure influences the design of your communication system.
   b) Describe how you will address the communication constraint in your design.
   c) Outline the core principles that form the basis of your communication system.

2. Language Structure (250-300 words):
   a) Describe the basic units or elements of your communication system (analogous to phonemes, morphemes, or words in human languages).
   b) Explain the rules or patterns for combining these elements (similar to syntax in human languages).
   c) Discuss how complex ideas or concepts can be expressed using your system.
   d) Provide an example of how a simple message would be constructed and transmitted using your system.

3. Cognitive Integration (200-250 words):
   a) Explain how your communication system integrates with the given cognitive structure.
   b) Describe any unique features of your system that specifically cater to this type of cognition.
   c) Discuss potential cognitive advantages or limitations that might arise from using this system.

4. Comparative Analysis (150-200 words):
   a) Compare your communication system to human language, highlighting key similarities and differences.
   b) Discuss how your system might handle concepts that are challenging to express in human languages.

5. Potential Applications (150-200 words):
   a) Propose two potential applications or scenarios where your communication system could be particularly useful or effective.
   b) Explain how these applications leverage the unique features of your system.

Ensure your response demonstrates a deep understanding of linguistic principles, cognitive science, and creative problem-solving. Use clear headings for each section and be as specific and detailed as possible in your explanations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The communication system design clearly incorporates the given cognitive structure and communication constraint",
            "The language structure is well-defined and logically consistent",
            "The proposal demonstrates creative problem-solving and interdisciplinary knowledge application",
            "The comparative analysis and potential applications show deep understanding and insightful reasoning"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
