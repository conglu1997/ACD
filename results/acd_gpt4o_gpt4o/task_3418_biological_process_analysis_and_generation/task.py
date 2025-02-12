class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"process_description": "Describe the process of photosynthesis in plants."},
            "2": {"criteria": "Generate a new biological scenario involving genetic mutation in a population of bacteria and describe its potential impact."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'process_description' in t:
            return f"""Your task is to analyze the following biological process or phenomenon and provide a detailed explanation of it.

Process Description: {t['process_description']}

Ensure your explanation is accurate, detailed, and covers all key aspects of the process. Use clear and precise language appropriate for a scientific context.
"""
        else:
            return f"""Your task is to generate a new biological scenario based on the given criteria and provide a detailed description of its impact.

Criteria: {t['criteria']}

Ensure your scenario is original, scientifically plausible, and described in detail. Use clear and precise language appropriate for a scientific context.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'process_description' in t:
            criteria = ["The explanation should be accurate, detailed, and cover all key aspects of the described process."]
        else:
            criteria = ["The generated scenario should be original, scientifically plausible, and described in detail."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
