import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "physics",
            "biology",
            "computer science",
            "economics",
            "psychology",
            "music",
            "architecture",
            "culinary arts"
        ]
        return {
            "1": {"domain1": random.choice(domains), "domain2": random.choice(domains)},
            "2": {"domain1": random.choice(domains), "domain2": random.choice(domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create, analyze, and extend a conceptual blend between {t['domain1']} and {t['domain2']}. Follow these steps:

1. Conceptual Blend Creation (150-200 words):
   Create a novel conceptual blend that combines key elements from both {t['domain1']} and {t['domain2']}. Describe the resulting blended concept in detail, explaining how it incorporates aspects of both source domains.

2. Cognitive Analysis (200-250 words):
   Analyze the cognitive processes involved in creating your conceptual blend. Include:
   a) The specific elements selected from each domain and why.
   b) The emergent structure that arises in the blended space.
   c) How this blend challenges or extends our understanding of either or both domains.

3. Practical Application (150-200 words):
   Propose a practical application or innovation based on your conceptual blend. Explain how this application could potentially impact either or both of the source domains or a different field entirely.

4. Blend Extension (100-150 words):
   Extend your original blend by incorporating an element from a third domain of your choice. Briefly describe how this addition alters or enhances the blended concept.

5. Meta-cognitive Reflection (100-150 words):
   Reflect on the challenges you faced in creating and analyzing this conceptual blend. Discuss any insights you gained about your own cognitive processes and creative thinking strategies.

Ensure your response demonstrates a deep understanding of conceptual blending theory, the chosen domains, and cognitive linguistics. Be as creative and innovative as possible while maintaining scientific and logical coherence. Your conceptual blends should be novel and insightful, but also plausible within the framework of the source domains.

Format your response as follows:

Conceptual Blend Creation:
[Your content here]

Cognitive Analysis:
[Your content here]

Practical Application:
[Your content here]

Blend Extension:
[Your content here]

Meta-cognitive Reflection:
[Your content here]

Adhere to the specified word counts for each section and ensure your overall response is well-structured and coherent."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and application of conceptual blending theory.",
            "The conceptual blend created is novel, coherent, and effectively combines elements from both specified domains.",
            "The cognitive analysis is insightful and accurately describes the blending process.",
            "The practical application proposed is innovative and logically derived from the conceptual blend.",
            "The blend extension creatively incorporates a third domain and enhances the original concept.",
            "The meta-cognitive reflection shows depth of thought and self-awareness in the creative process.",
            "The overall response is well-structured, coherent, and adheres to the specified word counts and format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
