class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Interpret the following scientific diagram and provide a detailed explanation of the process it represents:\n\n[A simple diagram of the water cycle showing evaporation, condensation, precipitation, and collection, including labels for bodies of water, clouds, and rain]"},
            "2": {"task": "Create a scientific diagram that visually represents the following process: Photosynthesis. Ensure that your diagram includes labels for key components such as sunlight, water, carbon dioxide, oxygen, and glucose. Additionally, indicate the chloroplasts in plant cells where this process occurs."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to work with scientific concepts based on the following description. Depending on the task, you may need to either interpret a scientific diagram or create one based on a provided explanation. Here is the task:\n\n{t['task']}\n\nSubmit your solution in plain text format. Ensure your response is clear, accurate, and detailed in explaining or representing the scientific process. For Task 1, provide your response in the following format:\nExplanation: [Your detailed explanation of the diagram]\nFor Task 2, provide your response in the following format:\nDiagram Description: [Your description of the diagram and labels]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The scientific explanation must be clear and accurate.", "The diagram must be correctly labeled and represent the specified process.", "The response must adhere to standard scientific terminology and conventions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
