import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                "process": "DNA replication",
                "problem": "implement a sorting algorithm"
            },
            {
                "process": "protein folding",
                "problem": "solve the traveling salesman problem"
            }
        ]
        return {
            "1": random.choice(biological_processes),
            "2": random.choice(biological_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language inspired by the biological process of {t['process']}. Then, use your language to {t['problem']}. Your response should include:

1. Language Design (4-5 sentences):
   - Explain how your language mimics the biological process.
   - Describe key features and syntax of your language.
   - Explain how your language handles basic programming concepts (e.g., variables, loops, functions).

2. Code Example (10-15 lines of code):
   - Provide a sample code snippet in your language that demonstrates its key features.
   - Include comments explaining what each part of the code does.

3. Problem Solution (4-5 sentences):
   - Explain how you would use your language to {t['problem']}.
   - Describe the algorithm or approach you would use.
   - Discuss any unique advantages your language provides for solving this problem.

4. Biological Analogy (2-3 sentences):
   - Draw a parallel between your solution and the biological process that inspired your language.

5. Limitations and Potential Improvements (2-3 sentences):
   - Discuss any limitations of your language or solution.
   - Suggest potential improvements or extensions.

Ensure your response is creative, scientifically grounded, and demonstrates a clear understanding of both the biological process and the computational problem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design clearly mimics the specified biological process.",
            "The code example demonstrates key features of the language and is well-commented.",
            "The problem solution leverages unique aspects of the language design.",
            "The biological analogy is insightful and well-explained.",
            "Limitations and potential improvements are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
