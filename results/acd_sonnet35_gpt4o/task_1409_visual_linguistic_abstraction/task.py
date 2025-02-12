import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_structure": "Nested relative clauses",
                "visual_abstraction_type": "Fractal geometry",
                "computational_problem": "Improving parsing efficiency for complex sentences",
                "example_sentence": "The cat that the dog that the man walked chased ran away."
            },
            {
                "linguistic_structure": "Polysynthetic morphology",
                "visual_abstraction_type": "Modular origami",
                "computational_problem": "Developing a more compact representation for morphologically rich languages",
                "example_word": "Tuntussuqatarniksaitengqiggtuq (Yup'ik: He had not yet said again that he was going to hunt reindeer)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret abstract visual representations of complex linguistic structures, then use it to solve a problem in computational linguistics. Focus on the linguistic structure of {t['linguistic_structure']}, using {t['visual_abstraction_type']} as the basis for your visual abstraction. Then, apply your system to the computational problem of {t['computational_problem']}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, including its main components and their interactions.
   b) Explain how your system processes linguistic input and generates visual abstractions.
   c) Detail how the system interprets and reasons about these visual abstractions.
   d) Include a diagram or detailed description of your system's architecture.

2. Visual Abstraction Mechanism (200-250 words):
   a) Explain how your system translates {t['linguistic_structure']} into {t['visual_abstraction_type']}.
   b) Describe the key features of your visual representation and how they correspond to linguistic elements.
   c) Discuss any novel algorithms or techniques used in this translation process.
   d) Provide a specific example of how your system would visually represent this linguistic input: {t['example_sentence'] if 'example_sentence' in t else t['example_word']}

3. Linguistic-Visual Reasoning (200-250 words):
   a) Explain how your system performs reasoning tasks using the visual abstractions.
   b) Provide an example of how a specific linguistic structure would be visually represented and reasoned about.
   c) Discuss how this approach might offer insights into human cognitive processes.

4. Application to Computational Problem (250-300 words):
   a) Describe how you would apply your system to {t['computational_problem']}.
   b) Explain the potential advantages of your visual abstraction approach for this problem.
   c) Discuss any challenges or limitations you anticipate and how you might address them.
   d) Provide a concrete example of how your system would process a specific input and generate a solution.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system's visual abstractions.
   b) Describe how you would validate the system's performance on the computational problem.
   c) Suggest experiments to compare your approach with traditional methods.

6. Ethical Considerations and Future Work (150-200 words):
   a) Discuss potential ethical implications or concerns related to your system.
   b) Propose guidelines for responsible development and use of such visual-linguistic AI systems.
   c) Suggest two directions for future research that could extend or improve your system.

Ensure your response demonstrates a deep understanding of linguistics, visual-spatial reasoning, and computational linguistics. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['linguistic_structure']} and provides a detailed explanation of how it can be represented using {t['visual_abstraction_type']}.",
            f"The proposed system architecture is well-designed and clearly explained, showing how it can generate and interpret visual abstractions of linguistic structures.",
            f"The application to the computational problem of {t['computational_problem']} is innovative, well-reasoned, and includes a concrete example of how the system would process a specific input.",
            "The response shows creativity and interdisciplinary thinking in combining linguistics, visual abstraction, and computational problem-solving.",
            "The response includes a specific visual representation example for the given linguistic input.",
            "The ethical considerations and future work suggestions are thoughtful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
