class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'role': 'Software Developer', 'questions': ['Tell me about yourself.', 'Why do you want to work at our company?', 'Describe a challenging project you worked on and how you overcame it.']},
            '2': {'role': 'Marketing Manager', 'questions': ['What is your experience with digital marketing?', 'How do you handle tight deadlines?', 'Can you give an example of a successful campaign you led?']}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are participating in a job interview for the role of {t['role']}. Respond to the following interview questions appropriately. Ensure that your responses are coherent, relevant, and demonstrate a good understanding of the role. Highlight your relevant experience and skills specific to the role in your answers.

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}
3. {t['questions'][2]}

Submit your responses as a plain text string in the following format:

Response 1: [Your response to question 1]
Response 2: [Your response to question 2]
Response 3: [Your response to question 3]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The responses should be relevant to the job role.", "The responses should be coherent and contextually appropriate.", "The responses should demonstrate a good understanding of the role and its requirements.", "The responses should highlight relevant experience and skills specific to the role."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
