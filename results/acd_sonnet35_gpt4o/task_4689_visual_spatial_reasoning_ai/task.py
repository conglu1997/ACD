import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        spatial_tasks = [
            'mental rotation',
            'spatial perspective taking',
            'spatial memory',
            'spatial pattern recognition'
        ]
        environments = [
            'non-Euclidean geometry',
            'fractal landscapes',
            'tesseract (4D cube) navigation',
            'Möbius strip topology'
        ]
        cognitive_constraints = [
            'limited working memory',
            'attention bottleneck',
            'perceptual illusions',
            'cognitive load effects'
        ]
        return {
            "1": {
                "spatial_task": random.choice(spatial_tasks),
                "environment": random.choice(environments),
                "cognitive_constraint": random.choice(cognitive_constraints)
            },
            "2": {
                "spatial_task": random.choice(spatial_tasks),
                "environment": random.choice(environments),
                "cognitive_constraint": random.choice(cognitive_constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human visual-spatial reasoning and can solve complex geometric and navigational problems in abstract 3D environments. Your system should focus on the spatial task of {t['spatial_task']}, operate in an environment characterized by {t['environment']}, and account for the cognitive constraint of {t['cognitive_constraint']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for visual-spatial reasoning.
   b) Explain how your system integrates principles from cognitive science and computer vision.
   c) Detail how your system addresses the specified spatial task, environment, and cognitive constraint.
   d) Include a high-level diagram or pseudocode snippet illustrating a key component of your system.

2. Visual-Spatial Representation (250-300 words):
   a) Explain how your system represents and manipulates visual-spatial information.
   b) Describe how this representation accounts for the unique properties of the specified environment.
   c) Discuss how your system's representation compares to current theories of human visual-spatial cognition.

3. Problem-Solving Mechanism (250-300 words):
   a) Detail the algorithms or processes your system uses to solve visual-spatial problems.
   b) Explain how these mechanisms are adapted to the specified spatial task.
   c) Describe how your system handles the given cognitive constraint.

4. Learning and Adaptation (200-250 words):
   a) Explain how your system learns from experience and adapts to new visual-spatial challenges.
   b) Discuss any novel approaches to machine learning or neural network architectures used in your system.
   c) Describe how your system might develop new problem-solving strategies over time.

5. Performance Evaluation (200-250 words):
   a) Propose methods for evaluating your system's performance on visual-spatial reasoning tasks.
   b) Compare your system's expected performance to human performance on similar tasks.
   c) Discuss any potential limitations or biases in your evaluation methods.

6. Ethical Considerations and Applications (200-250 words):
   a) Discuss potential ethical issues in developing AI systems that mimic human cognitive processes.
   b) Propose guidelines for responsible development and use of visual-spatial AI systems.
   c) Suggest potential applications of your system in fields such as robotics, urban planning, or cognitive rehabilitation.

Ensure your response demonstrates a deep understanding of visual-spatial cognition, AI, and the specified concepts. Use appropriate terminology and provide clear explanations for complex ideas. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use numbered lists where appropriate. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively addresses the spatial task of {t['spatial_task']}, the environment of {t['environment']}, and the cognitive constraint of {t['cognitive_constraint']}",
            "The system architecture demonstrates a clear integration of cognitive science and computer vision principles",
            "The visual-spatial representation and problem-solving mechanisms are well-explained and tailored to the task and environment",
            "The learning and adaptation processes are clearly described and innovative",
            "The performance evaluation methods are appropriate and well-reasoned",
            "Ethical considerations and potential applications are thoughtfully addressed",
            "The response is creative, scientifically plausible, and demonstrates interdisciplinary knowledge"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
