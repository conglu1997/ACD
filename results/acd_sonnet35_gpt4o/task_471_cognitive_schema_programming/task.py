import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'domain': 'social interaction',
                'problem': 'design a conflict resolution system'
            },
            {
                'domain': 'spatial navigation',
                'problem': 'create an adaptive pathfinding algorithm'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on cognitive schemas and mental models, then use it to {t['problem']} in the domain of {t['domain']}. Your task has the following components:

1. Language Design (300-350 words):
   a) Define the basic elements and syntax of your cognitive schema-based programming language.
   b) Explain how your language incorporates principles from cognitive science and mental models.
   c) Describe at least three unique features of your language that distinguish it from traditional programming languages.
   d) Provide a simple example of how basic operations or concepts would be expressed in your language.

2. Problem Solution (250-300 words):
   a) Use your cognitive schema-based language to design a solution for the given problem: {t['problem']} in the domain of {t['domain']}.
   b) Provide a high-level overview of your solution, explaining how it leverages the unique features of your language.
   c) Include a code snippet (at least 10 lines) in your language that demonstrates a key part of your solution.

3. Cognitive Analysis (200-250 words):
   a) Analyze how your language and solution align with known cognitive processes or mental models.
   b) Discuss potential cognitive benefits or challenges of using your language compared to traditional programming approaches.
   c) Explain how your language might influence problem-solving strategies or thought processes.

4. Implementation Considerations (150-200 words):
   a) Describe how your cognitive schema-based language could be implemented or compiled.
   b) Discuss potential challenges in creating development tools (e.g., IDEs, debuggers) for your language.
   c) Propose a strategy for teaching programmers to think and code in your new paradigm.

5. Interdisciplinary Implications (150-200 words):
   a) Explore how your language and approach might impact or be applied in at least two other fields (e.g., education, artificial intelligence, human-computer interaction).
   b) Discuss potential research questions that arise from your language design.

6. Limitations and Future Directions (100-150 words):
   a) Identify at least two limitations of your cognitive schema-based language or its application to the given problem.
   b) Propose ideas for future development or expansion of your language concept.

Ensure your response demonstrates a deep understanding of cognitive science, programming language theory, and the problem domain. Be creative in your language design while maintaining logical consistency and feasibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design incorporates clear elements from cognitive science and mental models.",
            "The solution to the given problem leverages unique features of the cognitive schema-based language.",
            "The cognitive analysis demonstrates a deep understanding of cognitive processes and their relation to the language design.",
            "The response shows creativity and innovation while maintaining logical consistency and feasibility.",
            "The interdisciplinary implications and future directions are thoughtfully considered and well-reasoned.",
            "The response demonstrates a high level of integration between cognitive science, programming language theory, and the problem domain."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
