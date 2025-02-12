import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Optimize traffic flow in a smart city",
            "Predict and mitigate the effects of climate change on biodiversity"
        ]
        return {
            str(i+1): {
                'problem': problem,
                'synesthesia_type': random.choice(['color-grapheme', 'sound-color', 'taste-shape'])
            } for i, problem in enumerate(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on synesthesia principles and apply it to solve a complex problem. Your task has the following parts:

1. Synesthetic Programming Language Design (250-300 words):
   a) Explain how you will incorporate the synesthesia type '{t['synesthesia_type']}' into your programming language.
   b) Describe the basic syntax and structure of your language, providing at least 3 concrete examples of code snippets.
   c) Discuss how your language's synesthetic basis affects its expressive capabilities and potential applications.

2. Core Concepts and Features (150-200 words):
   a) Define at least 5 core concepts or features of your synesthetic programming language.
   b) Explain how these concepts/features reflect the synesthetic properties of your language.
   c) Provide a short code snippet demonstrating each concept/feature, ensuring each example is distinct and illustrative.

3. Problem-Solving Application (200-250 words):
   Apply your synesthetic programming language to address the following problem:
   "{t['problem']}"
   a) Outline a high-level algorithm or approach to solve the problem using your language.
   b) Provide a sample of pseudocode in your synesthetic language for a key part of the solution, at least 10-15 lines long.
   c) Explain how the synesthetic properties of your language contribute to solving this problem.

4. Cognitive and Computational Analysis (200-250 words):
   a) Analyze the potential cognitive benefits and challenges of using your synesthetic programming language.
   b) Discuss any unique computational properties that emerge from your language design.
   c) Compare the efficiency and expressiveness of your language to traditional programming paradigms for the given problem, using specific examples.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how your synesthetic programming language might influence or change approaches to problem-solving in computer science.
   b) Explore potential applications of your language in fields outside of computer science (e.g., art, education, cognitive therapy).
   c) Propose an experiment to test the cognitive effects of using your synesthetic programming language, including a hypothesis and basic methodology.

Ensure your response demonstrates a deep understanding of synesthesia, programming language design, and the problem domain. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining logical consistency and computational feasibility. Include concrete examples and code snippets throughout your response to illustrate your ideas.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of synesthesia and its application to programming language design",
            "The synesthetic programming language is well-defined with clear syntax and structure, illustrated by concrete code examples",
            "The language is creatively and logically applied to the given problem, with a detailed pseudocode sample",
            "The analysis of cognitive and computational aspects is insightful and well-reasoned, with specific examples",
            "The interdisciplinary implications are thoughtfully explored, including a well-formulated experiment proposal"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
