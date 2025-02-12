import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        writing_systems = [
            "Cuneiform",
            "Egyptian Hieroglyphs",
            "Oracle Bone Script",
            "Linear B"
        ]
        problems = [
            "Sort a list of integers",
            "Find the prime factors of a number"
        ]
        tasks = {
            str(i+1): {
                "writing_system": random.choice(writing_systems),
                "problem": random.choice(problems)
            } for i in range(2)
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical ancient programming language based on the {t['writing_system']} writing system, then use it to solve the following computational problem: {t['problem']}. Your response should include:

1. Language Design (250-300 words):
   a) Describe the key features of your ancient programming language, including its syntax and basic operations.
   b) Explain how these features are inspired by or derived from the {t['writing_system']} writing system.
   c) Provide at least 3 example 'code snippets' in your language, with explanations of their functions.
   d) Discuss any unique characteristics or limitations of your language compared to modern programming languages.

2. Historical Context (150-200 words):
   a) Briefly describe the historical and cultural context of the {t['writing_system']} writing system.
   b) Explain how your programming language design reflects the technological and mathematical knowledge of the civilization that used this writing system.
   c) Discuss any anachronisms in your language design and justify their inclusion.

3. Problem Solution (200-250 words):
   a) Present a solution to the given problem ({t['problem']}) using your ancient programming language.
   b) Provide a step-by-step explanation of how your code works.
   c) Discuss any challenges you encountered in implementing this solution with your language, and how you addressed them.

4. Comparative Analysis (150-200 words):
   a) Compare your ancient programming language to a modern programming language of your choice.
   b) Discuss the strengths and weaknesses of your language for solving computational problems.
   c) Explain how features of your language might have influenced the development of programming if it had actually existed.

5. Implications and Speculations (150-200 words):
   a) Discuss how the existence of such a programming language might have altered the course of technological history.
   b) Speculate on potential applications or consequences of your language in its historical context.
   c) Propose an interesting research question that this hypothetical language raises about the nature of computation or the development of writing systems.

Ensure your response demonstrates a deep understanding of both the historical writing system and modern programming concepts. Be creative in your language design while maintaining historical plausibility and computational functionality. Use appropriate terminology from both linguistics and computer science.

Format your response with clear headings for each section. Your total response should be between 900-1150 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The ancient programming language should be clearly based on the {t['writing_system']} writing system.",
            "The language design should be creative, coherent, and well-explained.",
            f"A valid solution to the problem '{t['problem']}' should be provided using the designed language.",
            "The response should demonstrate a deep understanding of both historical writing systems and programming concepts.",
            "The analysis and speculations should be insightful and thought-provoking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
