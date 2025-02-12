import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Sanskrit', 'Arabic', 'Mandarin Chinese', 'Swahili']
        problems = [
            'Calculate the Fibonacci sequence',
            'Implement a basic sorting algorithm',
            'Create a simple text-based game',
            'Develop a basic natural language processing function'
        ]
        return {
            "1": {
                "language": random.choice(languages),
                "problem": random.choice(problems)
            },
            "2": {
                "language": random.choice(languages),
                "problem": random.choice(problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on the grammar of {t['language']}, then use it to solve the following problem: {t['problem']}. Your response should include:

1. Language Design (300-350 words):
   a) Describe the key features of your programming language.
   b) Explain how it incorporates grammatical structures from {t['language']}.
   c) Provide examples of basic syntax for variables, functions, and control structures.
   d) Discuss how your language handles unique aspects of {t['language']} (e.g., tonal systems, case structures, word order).

2. Linguistic Analysis (200-250 words):
   a) Analyze how your programming language relates to the natural language structures of {t['language']}.
   b) Discuss any challenges you encountered in adapting {t['language']} grammar to a programming context.
   c) Explain how your language might influence the thought processes of programmers using it.

3. Problem Solution (250-300 words):
   a) Present a solution to the problem "{t['problem']}" using your designed language.
   b) Provide a step-by-step explanation of how your code works.
   c) Discuss any unique features of your language that made solving this problem easier or more challenging.

4. Comparative Analysis (150-200 words):
   a) Compare your language to existing programming languages.
   b) Discuss potential advantages and disadvantages of your language.
   c) Explain how your language might be particularly suited for certain types of problems or domains.

5. Future Developments (100-150 words):
   a) Suggest two potential extensions or modifications to your language.
   b) Discuss how your language design process could be applied to other natural languages.
   c) Propose a research question that arises from your language design.

Ensure your response demonstrates a deep understanding of both linguistics and programming concepts. Be creative in your language design while maintaining practical usability. Use appropriate terminology from both fields and provide clear explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a programming language based on the grammar of {t['language']}.",
            "The language design incorporates key grammatical features of the natural language and provides clear examples of syntax.",
            f"The solution to the problem '{t['problem']}' is presented using the designed language and explained clearly.",
            "The response includes a thorough linguistic analysis and comparative analysis with existing programming languages.",
            "The response demonstrates creativity, technical accuracy, and a deep understanding of both linguistics and programming concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
