import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            'Dual Process Theory',
            'Prospect Theory',
            'Bounded Rationality',
            'Cognitive Load Theory'
        ]
        problem_domains = [
            'Climate Change Mitigation',
            'Global Health Crisis Management',
            'Sustainable Urban Planning',
            'Ethical AI Governance'
        ]
        tasks = [
            {'principle': random.choice(cognitive_principles),
             'domain': random.choice(problem_domains)}
            for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized language for decision-making based on the cognitive science principle of {t['principle']}, then apply it to solve a complex problem in the domain of {t['domain']}. Your response should include:

1. Language Design (300-350 words):
   a) Describe the key features of your decision-making language, including its vocabulary, syntax, and semantics.
   b) Explain how your language incorporates the specified cognitive principle.
   c) Provide at least 3 example sentences or expressions in your language with translations and explanations.
   d) Discuss how your language differs from natural languages and how it specifically enhances decision-making processes.

2. Cognitive Foundations (200-250 words):
   a) Explain the cognitive science principles underlying your language design.
   b) Discuss how your language might influence or change thought processes related to decision-making.
   c) Address potential cognitive benefits and challenges of using your language for complex problem-solving.

3. Problem Analysis (250-300 words):
   a) Briefly describe a specific, complex problem within the given domain.
   b) Analyze this problem using your decision-making language.
   c) Explain how the cognitive principle-based features of your language contribute to a clearer understanding of the problem.

4. Solution Development (250-300 words):
   a) Use your decision-making language to develop a comprehensive solution to the problem.
   b) Provide a step-by-step explanation of your solution, highlighting how your language facilitates each stage of the decision-making process.
   c) Discuss any novel insights or approaches that emerged from using your specialized language.

5. Implementation and Evaluation (200-250 words):
   a) Propose a method for teaching and implementing your decision-making language in real-world scenarios.
   b) Suggest metrics or criteria for evaluating the effectiveness of your language in improving decision-making outcomes.
   c) Discuss potential challenges in adopting your language and how they might be overcome.

6. Ethical Considerations (150-200 words):
   a) Analyze potential ethical implications of using a specialized decision-making language.
   b) Discuss how your language might impact fairness, transparency, and accountability in decision-making processes.
   c) Propose guidelines for the responsible use of your language in high-stakes decision-making scenarios.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and the specified problem domain. Be creative in your approach while maintaining scientific and practical plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Begin each section on a new line. Your total response should be between 1350-1650 words.

Example: For a language based on 'Prospect Theory' applied to 'Climate Change Mitigation', you might design a language that emphasizes framing of outcomes and risk perception. For instance, a sentence in your language might be 'GainFrame[Renewable Energy Investment] > LossFrame[Fossil Fuel Dependency]', which translates to 'The potential gains from investing in renewable energy outweigh the perceived losses from reducing fossil fuel dependency.'

Note: This example is provided for illustrative purposes only. Your language design should be original and tailored to the specific cognitive principle and problem domain assigned to you."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['principle']} and its application to language design for decision-making.",
            "The decision-making language is well-designed, with clear explanations of its features and at least 3 example sentences or expressions.",
            f"The problem analysis and solution development effectively utilize the specialized language to address a complex issue in {t['domain']}.",
            "The response shows creativity and innovation while maintaining scientific and practical plausibility.",
            "The implementation, evaluation, and ethical considerations are thoughtfully addressed with specific examples and guidelines.",
            "The response adheres to the specified word count (1350-1650 words) and section structure, with clear headings for each numbered section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
