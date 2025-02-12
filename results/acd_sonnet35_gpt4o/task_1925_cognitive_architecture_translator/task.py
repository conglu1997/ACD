import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            "symbolic reasoning",
            "connectionist networks",
            "bayesian inference",
            "embodied cognition",
            "predictive processing"
        ]
        problem_domains = [
            "spatial navigation",
            "language understanding",
            "decision making",
            "pattern recognition",
            "social interaction"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "source_architecture": random.choice(cognitive_architectures),
                "target_architecture": random.choice(cognitive_architectures),
                "problem_domain": random.choice(problem_domains)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of translating concepts and problem-solving approaches from {t['source_architecture']} to {t['target_architecture']} in the domain of {t['problem_domain']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cognitive architecture translation.
   b) Explain how your system represents and manipulates concepts from different cognitive architectures.
   c) Discuss how your system ensures fidelity in translation while accounting for fundamental differences between architectures.

2. Translation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system translates a concept or problem-solving approach from {t['source_architecture']} to {t['target_architecture']}.
   b) Describe any intermediate representations or processes used in the translation.
   c) Explain how your system handles concepts that may not have direct equivalents in the target architecture.

3. Domain-Specific Considerations (200-250 words):
   a) Discuss how your system adapts its translation process to the specific domain of {t['problem_domain']}.
   b) Provide an example of a concept or approach in this domain that might be particularly challenging to translate between the given architectures.
   c) Explain how your system would handle this challenging case.

4. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the accuracy and effectiveness of your cognitive architecture translations.
   b) Describe potential metrics or benchmarks for assessing translation quality.
   c) Discuss how you would validate that the translated concepts maintain their original meaning and utility.

5. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for advancing our understanding of cognition and AI.
   b) Propose two novel applications of cognitive architecture translation in fields such as education, AI research, or cognitive science.
   c) Speculate on how this technology might influence the development of future AI systems.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns or risks associated with cognitive architecture translation.
   b) Propose guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific cognitive architectures and problem domain involved. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['source_architecture']} and {t['target_architecture']} cognitive architectures",
            f"The proposed AI system presents a plausible and creative approach to translating between cognitive architectures in the domain of {t['problem_domain']}",
            "The translation process is well-explained and accounts for fundamental differences between architectures",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving",
            "Ethical considerations and potential applications are thoughtfully discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
