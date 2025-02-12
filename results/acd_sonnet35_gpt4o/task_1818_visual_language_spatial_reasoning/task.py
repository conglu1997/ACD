import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'concept': 'Temporal sequence',
                'problem_domain': 'Cause and effect relationships in ecosystems'
            },
            {
                'concept': 'Hierarchical structures',
                'problem_domain': 'Organizational dynamics in social networks'
            },
            {
                'concept': 'Topological transformations',
                'problem_domain': 'Protein folding in molecular biology'
            },
            {
                'concept': 'Symmetry and asymmetry',
                'problem_domain': 'Architectural design principles'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a visual language system for representing complex spatial relationships, focusing on the concept of {t['concept']}. Then, use this visual language to solve an abstract reasoning problem in the domain of {t['problem_domain']}. Your response should include the following sections:

1. Visual Language Design (250-300 words):
   a) Describe the basic elements and syntax of your visual language.
   b) Explain how your language represents the concept of {t['concept']}.
   c) Provide examples of how complex ideas within this concept can be expressed.
   d) Discuss how your visual language compares to natural languages in expressing spatial relationships.
   e) Include a brief example (2-3 sentences) of your visual language using ASCII art or Unicode characters.

2. Language Application (200-250 words):
   a) Present an abstract reasoning problem related to {t['problem_domain']}.
   b) Explain how you would represent this problem using your visual language.
   c) Provide a visual representation of the problem (use ASCII art or Unicode characters).

3. Problem-Solving Process (200-250 words):
   a) Describe step-by-step how to solve the problem using your visual language.
   b) Explain any unique advantages your visual language provides in solving this type of problem.
   c) Discuss potential challenges in using this language for problem-solving.

4. Cognitive Implications (150-200 words):
   a) Analyze how using this visual language might affect cognitive processes related to spatial reasoning.
   b) Discuss potential applications in fields such as education, cognitive therapy, or artificial intelligence.

5. AI Integration (200-250 words):
   a) Propose a method for training an AI to understand and generate expressions in your visual language.
   b) Discuss challenges in implementing this AI system and potential solutions.
   c) Explain how this AI could be evaluated for proficiency in the visual language.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical implications of widespread adoption of your visual language.
   b) Propose guidelines for responsible development and use of such a language system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and the specified problem domain. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words. Include a word count at the end of each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The visual language effectively represents the concept of {t['concept']}.",
            f"The problem and its solution in the domain of {t['problem_domain']} are clearly presented using the visual language.",
            "The response demonstrates creativity and innovation in the visual language design while maintaining logical consistency.",
            "The cognitive implications and AI integration aspects are thoughtfully considered and well-reasoned.",
            "The response shows a high level of understanding in linguistics, cognitive science, and the specified problem domain, using appropriate terminology.",
            "The visual representations (ASCII art or Unicode characters) effectively illustrate the language and problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
