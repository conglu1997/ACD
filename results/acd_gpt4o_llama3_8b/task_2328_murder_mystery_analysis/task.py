class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "On a stormy night, five people were present in a mansion: Mr. Green, Mrs. Blue, Dr. Black, Miss Red, and the butler, James. Mr. Green was found dead in the library at midnight with a stab wound. Each person provided an alibi: Mrs. Blue was in the kitchen cooking dinner, Dr. Black was in his room reading a book, Miss Red was in the garden taking a walk, and James was cleaning the study. The mansion's security system shows that no one entered or left the mansion during the storm. Investigate the scenario and identify the culprit."
            },
            "2": {
                "scenario": "In a small village, a well-known baker, Mr. Baker, was found dead in his bakery during the early hours of the morning with signs of poisoning. Four suspects were identified: his apprentice, Tom; his rival, Ms. Sweet; his neighbor, Mr. Crust; and his wife, Mrs. Baker. Each provided an alibi: Tom claimed he was at home sleeping, Ms. Sweet was at her bakery, Mr. Crust was at the market buying ingredients, and Mrs. Baker was visiting a friend. The village is small and everyone knows each other's routines. Investigate the scenario and identify the culprit."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following murder mystery scenario and identify the culprit. Provide a detailed explanation of your reasoning, including any inconsistencies in the alibis and any logical deductions you made to reach your conclusion.\n\nScenario: {t['scenario']}\n\nSubmit your response as a plain text string with the following sections:\n\n1. Analysis: [Your detailed analysis of the scenario]\n2. Culprit: [The name of the person you believe is the culprit]\n3. Reasoning: [Your explanation for why you identified this person as the culprit]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should include separate sections for analysis, culprit identification, and reasoning.", "The analysis should be detailed and logically consistent.", "The reasoning should clearly explain why the identified person is the culprit.", "The logical flow and consistency of the reasoning should be evident."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
