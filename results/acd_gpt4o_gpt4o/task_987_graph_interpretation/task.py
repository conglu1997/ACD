class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"graph_data": "Month: Jan, Value: 100; Month: Feb, Value: 150; Month: Mar, Value: 200; Month: Apr, Value: 250; Month: May, Value: 300; Month: Jun, Value: 350; Month: Jul, Value: 300; Month: Aug, Value: 250; Month: Sep, Value: 200; Month: Oct, Value: 150; Month: Nov, Value: 100; Month: Dec, Value: 50", "questions": ["What is the highest value represented in the graph?", "During which month did the value peak?"]},
            "2": {"graph_data": "Quarter: Q1, Value: 100; Quarter: Q2, Value: 200; Quarter: Q3, Value: 300; Quarter: Q4, Value: 400", "questions": ["Identify the trend shown in the graph.", "What can be inferred about the data in the third quarter?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the information from the provided graph data and answer the specific questions.

Graph Data: {t['graph_data']}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Instructions:
1. Analyze the graph data carefully.
2. Provide clear and concise answers to the questions based on your analysis of the graph data.
3. Ensure your answers are accurate and derived from the data presented in the graph.
4. Provide your answers in the specified format.

Your response should be in the following format:
Answer 1: [Your answer to question 1]
Answer 2: [Your answer to question 2]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answers should accurately reflect the data presented in the graph data.", "The answers should be clear and concise.", "The answers should be in the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
