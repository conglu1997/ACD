class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem_statement": "Using knowledge of history and technology, propose a method for preserving ancient manuscripts that are deteriorating due to environmental factors. Describe the method and explain how it addresses both historical preservation and technological feasibility."
            },
            "2": {
                "problem_statement": "Integrate concepts from literature and psychology to design a therapeutic program that uses storytelling to help individuals cope with trauma. Describe the program and explain how it leverages literary techniques and psychological principles to achieve its goals."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to solve the following interdisciplinary problem. Use your knowledge from multiple disciplines to generate a coherent and feasible solution."
            " Ensure your response integrates relevant concepts and demonstrates a deep understanding of the involved fields. Provide your response in plain text format and make sure to address the following points:\n\n"
            "1. Identify the key disciplines involved.\n"
            "2. Propose a solution that integrates knowledge from these disciplines.\n"
            "3. Explain how your solution addresses the problem effectively.\n"
            "4. Provide examples or references to support your solution where applicable.\n"
            "5. Ensure your response is between 300 and 500 words."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should identify the key disciplines involved.",
            "The proposed solution should integrate knowledge from these disciplines effectively.",
            "The explanation should demonstrate how the solution addresses the problem.",
            "The response should provide examples or references where applicable.",
            "The response should be coherent and within the word limit."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
