class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Interpret the following clause from a contract and provide a summary of its implications for both parties involved. Clause: 'The Contractor shall not be liable for any indirect, incidental, or consequential damages arising out of or in connection with the performance of this Agreement.'"},
            "2": {"prompt": "Analyze the following legal statute and explain its significance in the context of employment law. Statute: 'It shall be unlawful for any employer to fail or refuse to hire or to discharge any individual, or otherwise to discriminate against any individual with respect to his compensation, terms, conditions, or privileges of employment, because of such individual's race, color, religion, sex, or national origin.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following legal text and provide a coherent legal argument or summary based on the given text. Ensure that your interpretation is clear, accurate, and based on legal principles. Incorporate relevant legal concepts and precedents where applicable:

{t['prompt']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should be clear and accurate.",
            "The interpretation should incorporate relevant legal concepts and precedents.",
            "The interpretation should provide a coherent legal argument or summary.",
            "The interpretation should be based on legal principles.",
            "The interpretation should address the implications for the parties involved (if applicable)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
