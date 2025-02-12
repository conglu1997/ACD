class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "You are a detective trying to solve a case. You have the following clues: 1) A witness saw a red car leaving the scene. 2) There were footprints of size 10 shoes. 3) A wallet with an ID of a known criminal was found nearby. Based on these clues, infer the most likely scenario and describe how you would proceed with the investigation."},
            "2": {"problem": "You are a scientist trying to identify the cause of a mysterious illness in a small town. You have the following data: 1) Symptoms include fever, fatigue, and rash. 2) The illness appeared suddenly and affected people of all ages. 3) A recent report mentioned a possible contamination in the local water supply. Based on this information, infer the most likely cause of the illness and propose a plan to address it."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following problem based on the incomplete information provided. Carefully consider the clues and make logical inferences to form a coherent solution. Ensure that your response is well-reasoned, detailed, and addresses all aspects of the problem. Here is the problem: {t['problem']} Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should logically infer the most likely scenario based on the given clues.", "The response should provide a detailed and coherent plan or solution.", "The response should address all aspects of the problem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
