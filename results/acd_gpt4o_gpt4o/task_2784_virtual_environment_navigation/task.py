class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are in a dense forest with limited visibility. You have a map, a compass, and a flashlight. You must find your way out safely. Describe your actions step by step, considering potential obstacles like wild animals, rugged terrain, and the need for food and water."},
            "2": {"scenario": "You are in a futuristic city with advanced technology. Your goal is to retrieve an important artifact from a secure facility. Describe your actions step by step to achieve your goal without getting caught. Consider potential challenges like security systems, guards, and the need to blend in with the environment."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to navigate the following virtual environment scenario and make decisions to achieve the given goal:

{t["scenario"]}

Describe your actions step by step, considering potential obstacles and challenges you might face. Your response should be logical, creative, and adaptable to the situation. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The actions described should be logical and feasible within the given scenario.",
            "The response should consider potential obstacles and challenges.",
            "The actions should lead towards achieving the given goal.",
            "The response should demonstrate creativity and adaptability."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
