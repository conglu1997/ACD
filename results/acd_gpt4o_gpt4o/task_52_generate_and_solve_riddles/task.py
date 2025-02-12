class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Generate a riddle about time.", "requirements": "The riddle should be original, clever, coherent, grammatically correct, and solvable."},
            "2": {"task": "Solve the following riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'", "requirements": "Provide a clear and concise answer to the riddle."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task = t["task"]
        requirements = t["requirements"]
        instructions = f"""Your task is to complete the following riddle-related task:

{task}

Ensure that your response meets the following requirements:
{requirements}

Provide your response in plain text format.

Example for Task 1: If the task was 'Generate a riddle about a tree', a good riddle could be 'I have leaves but I'm not a book, I provide shade but I'm not a hat. What am I?'

Example for Task 2: If the riddle was 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?', a correct answer would be 'An echo'."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "Generate a riddle about time.":
            criteria = [
                "The riddle should be original.",
                "The riddle should be clever.",
                "The riddle should be coherent.",
                "The riddle should be grammatically correct.",
                "The riddle should be solvable with a clear answer."]
        else:
            criteria = [
                "The answer should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
