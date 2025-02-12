import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "natural_language": "Hopi",
                "programming_paradigm": "functional programming"
            },
            "2": {
                "natural_language": "Pirahã",
                "programming_paradigm": "object-oriented programming"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the concept of linguistic relativity (Sapir-Whorf hypothesis) in the context of programming languages, focusing on the relationship between {t['natural_language']} and {t['programming_paradigm']}. Your task is to:

1. Briefly explain the concept of linguistic relativity and its potential implications for cognition (2-3 sentences).

2. Describe key linguistic features of {t['natural_language']} and how they might influence thought patterns of its speakers (3-4 sentences).

3. Explain the main principles of {t['programming_paradigm']} and how it shapes the way programmers approach problem-solving (3-4 sentences).

4. Draw parallels between the cognitive effects of {t['natural_language']} and {t['programming_paradigm']}, highlighting any similarities or differences in how they might influence thinking (4-5 sentences).

5. Based on your analysis, propose a novel programming language feature or paradigm that incorporates aspects of {t['natural_language']} to potentially enhance problem-solving capabilities. Describe its syntax and functionality (5-6 sentences).

6. Discuss potential benefits and challenges of implementing your proposed feature in real-world programming scenarios (3-4 sentences).

7. Speculate on how widespread adoption of your proposed feature might influence software development practices and potentially even broader cognitive patterns in society (3-4 sentences).

Ensure your response is well-reasoned, creative, and grounded in both linguistic and computer science principles. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response explains linguistic relativity and its implications for cognition",
            f"Key linguistic features of {t['natural_language']} are described with their potential cognitive effects",
            f"Main principles of {t['programming_paradigm']} are explained in relation to problem-solving approaches",
            f"Parallels are drawn between cognitive effects of {t['natural_language']} and {t['programming_paradigm']}",
            "A novel programming language feature is proposed, incorporating aspects of the natural language",
            "Potential benefits and challenges of implementing the proposed feature are discussed",
            "The response speculates on the broader implications of adopting the proposed feature",
            "The answer demonstrates understanding of linguistics, computer science, and cognitive science concepts",
            "The response is well-organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
