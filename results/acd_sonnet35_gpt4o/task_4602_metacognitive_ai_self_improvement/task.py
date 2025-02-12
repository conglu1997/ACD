import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "Natural Language Processing",
                "specific_task": "Sentiment Analysis",
                "performance_metric": "F1 Score"
            },
            {
                "domain": "Computer Vision",
                "specific_task": "Object Detection",
                "performance_metric": "Mean Average Precision (mAP)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing its own decision-making processes, identifying areas for improvement, and implementing self-modification strategies to enhance its performance in {t['domain']}, specifically for the task of {t['specific_task']}. Your system should aim to improve its {t['performance_metric']} through self-analysis and modification. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your metacognitive AI system.
   b) Explain how your system integrates self-analysis capabilities with its primary task functionality.
   c) Detail the mechanisms for self-modification and performance monitoring.
   d) Include a high-level diagram or pseudocode illustrating the system's architecture.

2. Self-Analysis Process (250-300 words):
   a) Explain how your AI system analyzes its own decision-making processes for {t['specific_task']}.
   b) Describe the metrics and criteria used for self-evaluation.
   c) Detail how the system identifies areas for improvement in its performance.

3. Improvement Strategies (250-300 words):
   a) Outline the types of self-modification strategies your system can implement.
   b) Explain how these strategies are generated and evaluated.
   c) Describe the process of implementing and testing improvements.
   d) Provide an example of a specific improvement your system might make for {t['specific_task']}.

4. Learning and Adaptation (200-250 words):
   a) Explain how your system learns from its self-improvement attempts.
   b) Describe how it adapts its strategies over time based on their effectiveness.
   c) Discuss how the system balances exploration of new strategies with exploitation of known effective methods.

5. Safety and Ethical Considerations (200-250 words):
   a) Discuss potential risks associated with a self-modifying AI system.
   b) Explain the safeguards implemented to prevent unintended or harmful modifications.
   c) Address ethical implications of an AI system capable of self-improvement.

6. Performance Evaluation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system's self-improvement capabilities.
   b) Describe how you would measure improvements in {t['performance_metric']} over time.
   c) Suggest ways to compare your self-improving system against traditional, static AI models.

7. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your approach to metacognitive AI.
   b) Identify potential challenges in implementing this system for {t['specific_task']}.
   c) Propose future research directions to enhance the system's self-improvement capabilities.

Ensure your response demonstrates a deep understanding of AI architectures, decision theory, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately covers all seven required sections for the {t['domain']} domain and {t['specific_task']} task.",
            "The proposed system demonstrates a plausible approach to metacognitive AI with self-improvement capabilities.",
            f"The response includes specific details on how the system would improve its {t['performance_metric']} through self-analysis and modification.",
            "The submission shows creativity and innovation while maintaining scientific plausibility.",
            "The response demonstrates a deep understanding of AI architectures, decision theory, and cognitive science.",
            "Ethical considerations and safety measures are thoroughly addressed.",
            "The limitations and future directions discussed are relevant and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
