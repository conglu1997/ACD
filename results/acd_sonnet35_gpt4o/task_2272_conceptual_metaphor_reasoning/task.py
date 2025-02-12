import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_domain": "Journey",
                "target_domain": "Life",
                "problem_domain": "Career Development"
            },
            {
                "source_domain": "War",
                "target_domain": "Argument",
                "problem_domain": "Conflict Resolution"
            },
            {
                "source_domain": "Building",
                "target_domain": "Theory",
                "problem_domain": "Scientific Research"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze, create, and apply conceptual metaphors to explore abstract concepts and solve problems across different domains. Your task involves working with the conceptual metaphor '{t['target_domain']} IS A {t['source_domain']}' and applying it to the problem domain of {t['problem_domain']}. Provide your response in the following format:

1. Metaphor Analysis (200-250 words):
   a) Explain the key components of the given conceptual metaphor.
   b) Discuss how this metaphor shapes our understanding of the target domain.
   c) Provide three specific mappings between elements of the source and target domains.

2. Novel Metaphor Creation (200-250 words):
   a) Create a new conceptual metaphor related to the given problem domain.
   b) Explain the rationale behind your choice of source and target domains.
   c) Describe at least three mappings between elements of your new metaphor.
   d) Discuss potential insights or perspectives gained from this new metaphor.

3. Problem-Solving Application (250-300 words):
   a) Identify a specific problem or challenge within the given problem domain.
   b) Apply both the given metaphor and your novel metaphor to analyze this problem.
   c) Propose a solution or approach to the problem inspired by these metaphors.
   d) Explain how the metaphorical reasoning led to your proposed solution.

4. Metaphor Limitations and Ethical Considerations (150-200 words):
   a) Discuss potential limitations or drawbacks of using these metaphors in the problem domain.
   b) Address any ethical considerations that arise from applying these metaphors.
   c) Suggest how to mitigate these limitations or ethical concerns.

5. Cross-Domain Application (200-250 words):
   a) Propose an application of your novel metaphor to a completely different domain.
   b) Explain how this cross-domain application might lead to new insights or innovations.
   c) Discuss any challenges that might arise in this cross-domain application.

Ensure your response demonstrates a deep understanding of conceptual metaphors, their role in cognition, and their potential applications in problem-solving and innovation. Be creative in your approach while maintaining logical consistency and addressing real-world challenges."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual metaphors and their cognitive implications",
            "The novel metaphor created is original, well-explained, and relevant to the problem domain",
            "The application of metaphors to problem-solving is logical, creative, and insightful",
            "The analysis of metaphor limitations and ethical considerations is thorough and thoughtful",
            "The cross-domain application of the novel metaphor is innovative and well-reasoned",
            "The overall response shows strong interdisciplinary thinking and creative problem-solving skills"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0