import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'math_concept': 'Functors',
                'application_field': 'Supply Chain Optimization',
                'example_problem': 'Optimizing multi-stage production and distribution networks',
                'sample_data': 'Production rates at 3 factories, shipping times between 5 distribution centers, and demand at 10 retail locations'
            },
            {
                'math_concept': 'Natural Transformations',
                'application_field': 'Financial Risk Management',
                'example_problem': 'Modeling and predicting market volatility across different asset classes',
                'sample_data': 'Daily returns of 50 stocks, 10 commodities, and 5 cryptocurrencies over the past 2 years'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that applies the abstract mathematical concept of {t['math_concept']} from category theory to solve real-world optimization problems in {t['application_field']}, then analyze its potential impact. 

Background: Category theory is a branch of mathematics that deals with abstract structures and relationships between these structures. It provides a unified language to describe many different mathematical structures and their transformations. Key concepts include categories, objects, morphisms, functors, and natural transformations.

Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Define and explain the key principles of {t['math_concept']} in category theory.
   b) Define at least three other related terms from category theory relevant to {t['math_concept']}.
   c) Discuss how these principles could be relevant to {t['application_field']}.
   d) Propose a novel way to represent problems in {t['application_field']} using {t['math_concept']}.

2. AI System Architecture (300-350 words):
   a) Design an AI system that leverages {t['math_concept']} for optimization in {t['application_field']}.
   b) Explain how your system translates between abstract mathematical structures and real-world data.
   c) Describe the key components and algorithms of your AI system.
   d) Discuss how your system handles uncertainty and adapts to changing conditions.

3. Problem-Solving Mechanism (300-350 words):
   a) Provide a specific example of how your AI system would approach the problem of {t['example_problem']}.
   b) Explain step-by-step how {t['math_concept']} are applied in the problem-solving process.
   c) Include a detailed mathematical formulation (with equations and definitions) that demonstrates the use of {t['math_concept']} in solving the problem.
   d) Describe how your system would process the following sample data: {t['sample_data']}.
   e) Compare your approach to traditional methods in {t['application_field']}.
   f) Discuss potential limitations or challenges in applying category theory to this problem.

4. Performance Analysis (200-250 words):
   a) Propose specific metrics to evaluate the performance of your AI system.
   b) Discuss potential advantages and limitations of your approach.
   c) Compare your category theory-based approach with at least one other mathematical approach (e.g., linear programming, dynamic programming) for solving problems in {t['application_field']}.
   d) Suggest how the system could be improved or extended.

5. Broader Impact (200-250 words):
   a) Analyze how your AI system could transform practices in {t['application_field']}.
   b) Discuss potential ethical implications or risks associated with your system.
   c) Propose two novel applications of your approach in fields other than {t['application_field']}.

6. Future Research Directions (150-200 words):
   a) Suggest areas for further research in applying category theory to AI.
   b) Discuss how your approach might influence the development of more abstract mathematical AI systems.
   c) Propose an experiment to test the limits of your system's capabilities.

Ensure your response demonstrates a deep understanding of both category theory and {t['application_field']}. Use appropriate mathematical and domain-specific terminology, providing clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d, e, f as appropriate. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately defines and explains {t['math_concept']} and at least three other related terms from category theory.",
            f"The AI system design effectively applies {t['math_concept']} to problems in {t['application_field']}, specifically addressing {t['example_problem']}.",
            "The solution includes a detailed mathematical formulation with equations and definitions, demonstrating the use of the specified mathematical concept.",
            f"The response describes how the AI system would process the given sample data: {t['sample_data']}.",
            "The solution shows creativity in connecting abstract mathematics with practical applications.",
            "The response includes a comparison with at least one other mathematical approach for solving problems in the given application field.",
            "The analysis of broader impact and future research directions is insightful and well-reasoned.",
            "The response discusses potential limitations or challenges in applying category theory to the given problem.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
