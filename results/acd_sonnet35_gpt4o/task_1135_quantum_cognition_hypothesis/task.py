import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "Decision Making",
            "Memory Formation",
            "Consciousness",
            "Attention",
            "Language Processing"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Tunneling",
            "Coherence",
            "Wave Function Collapse"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "cognitive_process": random.choice(cognitive_processes),
                "quantum_concept": random.choice(quantum_concepts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop and analyze a hypothesis for quantum effects in human cognition, focusing on the cognitive process of {t['cognitive_process']} and incorporating the quantum concept of {t['quantum_concept']}. Your response should include:

1. Hypothesis Formulation (200-250 words):
   a) State your hypothesis clearly and concisely.
   b) Explain how the specified quantum concept might influence or manifest in the given cognitive process.
   c) Describe the potential mechanisms or structures in the brain that could support quantum effects.

2. Theoretical Basis (200-250 words):
   a) Discuss relevant theories or models from cognitive science that support your hypothesis.
   b) Explain how quantum mechanics principles could be applied to these cognitive theories.
   c) Address any apparent conflicts between classical neuroscience and your quantum cognition hypothesis.

3. Proposed Experimental Design (200-250 words):
   a) Outline an experiment that could test your hypothesis.
   b) Describe the methodology, including controls and variables.
   c) Explain how you would measure or detect the proposed quantum effects in cognition.

4. Potential Implications (150-200 words):
   a) Discuss the implications of your hypothesis for our understanding of human cognition.
   b) Explore potential applications in fields such as AI, neuroscience, or psychology.
   c) Address any philosophical or ethical considerations raised by your hypothesis.

5. Critical Analysis (150-200 words):
   a) Identify potential weaknesses or limitations in your hypothesis.
   b) Discuss alternative explanations for the phenomena you're addressing.
   c) Suggest future research directions to further explore or refine your hypothesis.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate scientific terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing potential criticisms.

Format your response with clear headings for each section. Your total response should be between 900-1150 words.

Provide your response in a structured format with clear section headings and subheadings as outlined above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science",
            "The hypothesis is clearly stated and logically connects the specified quantum concept to the given cognitive process",
            "The proposed experimental design is well-thought-out and feasible",
            "The response critically analyzes the hypothesis, addressing potential weaknesses and alternative explanations",
            "The writing is clear, well-structured, and uses appropriate scientific terminology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
