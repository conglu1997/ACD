import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "Privacy",
                "time_period": "50 years",
                "context": "Social media and digital communication"
            },
            {
                "concept": "Intelligence",
                "time_period": "100 years",
                "context": "Artificial intelligence and cognitive enhancement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and predict semantic drift in large language models for the concept of '{t['concept']}' over the next {t['time_period']} in the context of {t['context']}. Compare this drift to historical linguistic changes in human languages. Your analysis should include:

1. Current Semantics (100-150 words):
   a) Define the current meaning and connotations of '{t['concept']}' in large language models.
   b) Explain how this compares to the current understanding in human languages.

2. Predicted Semantic Drift in AI (200-250 words):
   a) Describe how you expect the meaning of '{t['concept']}' to change in large language models over the specified time period.
   b) Explain the factors that might contribute to this drift, considering technological advancements and societal changes.
   c) Provide specific examples of how the usage and connotations might evolve.

3. Comparison to Human Language Evolution (200-250 words):
   a) Analyze how the predicted AI semantic drift compares to historical changes in human languages.
   b) Discuss similarities and differences in the mechanisms of change.
   c) Provide an example of a similar semantic shift from human language history.

4. Implications for AI Development (150-200 words):
   a) Discuss the potential impact of semantic drift on AI systems' long-term reliability and consistency.
   b) Propose methods to mitigate negative effects of semantic drift in AI models.

5. Ethical Considerations (100-150 words):
   a) Explore the ethical implications of semantic drift in AI language models.
   b) Discuss potential societal impacts and propose guidelines for responsible AI development in light of semantic drift.

6. Novel Research Question (50-75 words):
   Propose a specific, testable research question that arises from your analysis of semantic drift in AI language models.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be analytical and insightful in your comparisons and predictions.

Format your response with clear headings for each section. Your total response should be between 800-1075 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately defines and compares the current semantics of '{t['concept']}' in AI models and human languages.",
            f"The analysis provides a plausible and well-reasoned prediction of semantic drift for '{t['concept']}' in AI models over the specified time period.",
            "The comparison between AI semantic drift and human language evolution is insightful and well-supported with examples.",
            "The response discusses implications for AI development and proposes relevant mitigation strategies.",
            "Ethical considerations are thoughtfully explored with proposed guidelines for responsible AI development.",
            "The proposed research question is specific, testable, and relevant to the analysis of semantic drift in AI language models.",
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
