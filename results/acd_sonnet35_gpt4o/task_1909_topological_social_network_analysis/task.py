import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_structures = [
            "political polarization",
            "online communities",
            "corporate hierarchies",
            "academic collaboration networks"
        ]
        topological_concepts = [
            "homology groups",
            "persistent homology",
            "simplicial complexes",
            "Morse theory"
        ]
        societal_problems = [
            "misinformation spread",
            "social inequality",
            "organizational inefficiency",
            "echo chambers in social media"
        ]
        
        tasks = [
            {
                "social_structure": random.choice(social_structures),
                "topological_concept": random.choice(topological_concepts),
                "societal_problem": random.choice(societal_problems)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Topology is a branch of mathematics that studies the properties of geometric objects that remain unchanged under continuous deformations. In the context of social network analysis, topological approaches can reveal underlying structures and patterns that might not be apparent through traditional network analysis methods.

Design and analyze a topological model of {t['social_structure']}, incorporating the mathematical concept of {t['topological_concept']}, then apply it to address the societal problem of {t['societal_problem']}. Your response should include:

1. Topological Model Design (300-350 words):
   a) Describe the key components and structure of your topological model for {t['social_structure']}.
   b) Explain how you incorporate {t['topological_concept']} into your model.
   c) Discuss how your model captures the essential features and dynamics of {t['social_structure']}.
   d) Provide at least one mathematical formula or diagram illustrating a key aspect of your model.

2. Social Network Analysis (250-300 words):
   a) Explain how your model can be used to analyze {t['social_structure']}.
   b) Describe specific insights or patterns that can be uncovered using your topological approach.
   c) Compare your topological approach to traditional network analysis methods, highlighting its advantages.

3. Application to Societal Problem (250-300 words):
   a) Apply your topological model to address the problem of {t['societal_problem']}.
   b) Describe at least two novel insights or potential solutions that emerge from this application.
   c) Explain how these insights differ from traditional approaches to the problem.

4. Implementation and Data Requirements (200-250 words):
   a) Discuss the types of data needed to implement your model in real-world scenarios.
   b) Describe potential challenges in data collection or processing and how you would address them.
   c) Propose a method for validating your model using empirical data.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications or misuses of your topological social network model.
   b) Analyze limitations of your approach and suggest areas for future research and improvement.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your topological approach to social network analysis might influence other fields of study.
   b) Propose two potential research directions that combine your approach with other scientific or technological domains.

Ensure your response demonstrates a deep understanding of both topology and social network analysis. Be creative in your approach while maintaining mathematical rigor and sociological relevance. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must incorporate {t['topological_concept']} in modeling {t['social_structure']}",
            f"The application to {t['societal_problem']} must be thoroughly addressed",
            "The topological model should be mathematically sound and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration",
            "Ethical implications must be thoughtfully considered",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1300-1600 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
