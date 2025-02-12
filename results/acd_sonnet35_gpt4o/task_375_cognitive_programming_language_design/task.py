import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "working memory capacity",
            "attention switching",
            "chunking",
            "cognitive load theory",
            "dual coding theory"
        ]
        algorithmic_problems = [
            "fibonacci sequence",
            "binary search",
            "bubble sort",
            "depth-first search",
            "breadth-first search"
        ]
        programming_paradigms = [
            "object-oriented programming",
            "functional programming",
            "procedural programming",
            "logic programming",
            "event-driven programming"
        ]
        tasks = {}
        for i in range(1, 3):
            principle = random.choice(cognitive_principles)
            problem = random.choice(algorithmic_problems)
            paradigm = random.choice(programming_paradigms)
            tasks[str(i)] = {"principle": principle, "problem": problem, "paradigm": paradigm}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a programming language based on the cognitive principle of {t['principle']}, then use it to implement the {t['problem']} algorithm and compare it with the {t['paradigm']} paradigm. Your response should include:\n\n1. Explanation of the cognitive principle (2-3 sentences)\n2. Description of your programming language (200-250 words):\n   a) Key features and syntax\n   b) How it incorporates the cognitive principle\n   c) Potential advantages over traditional programming languages\n3. Implementation of the {t['problem']} algorithm in your language (100-150 words of code or pseudocode)\n4. Brief explanation of how your language's features are utilized in the implementation (100-150 words)\n5. Analysis of how your language might affect programmer productivity and code comprehension (100-150 words)\n6. Comparison of your language with the {t['paradigm']} paradigm (100-150 words):\n   a) Similarities and differences\n   b) Potential advantages and disadvantages of your language compared to this paradigm\n\nEnsure your response is creative yet grounded in both cognitive science and programming language design principles."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the chosen cognitive principle and its application to programming language design",
            "The proposed programming language is innovative and logically incorporates the cognitive principle",
            "The implementation of the algorithm is correct and effectively uses the language's features",
            "The analysis of programmer productivity and code comprehension is insightful and well-reasoned",
            "The comparison with the given programming paradigm is thorough and demonstrates a good understanding of both the designed language and the existing paradigm"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0