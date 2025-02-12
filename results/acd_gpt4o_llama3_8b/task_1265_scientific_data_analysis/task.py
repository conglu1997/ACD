class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": [
                {"temperature": 20, "pressure": 101.3, "volume": 1.0},
                {"temperature": 25, "pressure": 101.3, "volume": 1.2},
                {"temperature": 30, "pressure": 101.3, "volume": 1.4},
                {"temperature": 35, "pressure": 101.3, "volume": 1.6}
            ], "prompt": "Analyze the relationship between temperature and volume at constant pressure."},
            "2": {"data": [
                {"time": 0, "concentration": 100},
                {"time": 10, "concentration": 90},
                {"time": 20, "concentration": 81},
                {"time": 30, "concentration": 73},
                {"time": 40, "concentration": 66}
            ], "prompt": "Analyze the relationship between time and concentration in a first-order reaction."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "temperature" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Data:
{t["data"]}

Analyze the relationship between temperature and volume at constant pressure. Your analysis should include:
1. A description of the observed relationship.
2. A possible explanation for the observed relationship based on scientific principles.
3. Any assumptions or limitations of the data.

Ensure your analysis is coherent, well-structured, and scientifically sound. Submit your response as a plain text string in paragraph format."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Data:
{t["data"]}

Analyze the relationship between time and concentration in a first-order reaction. Your analysis should include:
1. A description of the observed relationship.
2. A possible explanation for the observed relationship based on scientific principles.
3. Any assumptions or limitations of the data.

Ensure your analysis is coherent, well-structured, and scientifically sound. Submit your response as a plain text string in paragraph format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "temperature" in t["prompt"]:
            criteria = ["The analysis should describe the relationship between temperature and volume.", "The explanation should be based on scientific principles.", "The analysis should mention any assumptions or limitations."]
        else:
            criteria = ["The analysis should describe the relationship between time and concentration.", "The explanation should be based on scientific principles.", "The analysis should mention any assumptions or limitations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
