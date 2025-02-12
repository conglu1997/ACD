class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "create", "constraints": "A depends on B and C, B depends on D and E, C depends on F, D depends on G and H, E depends on I, F depends on J."},
            "2": {"task": "analyze", "graph": "A -> B, A -> C, B -> D, B -> E, C -> F, D -> G, D -> H, E -> I, F -> J"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "create":
            return f"Your task is to create a dependency graph based on the following constraints: {t['constraints']}.\n\nSubmit the graph in the format 'Node -> Dependent Node'."
        elif t["task"] == "analyze":
            return f"Your task is to analyze the following dependency graph: {t['graph']}. Identify any potential issues or bottlenecks in the graph.\n\nSubmit your analysis in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "create":
            criteria = [
                "The generated graph should correctly represent the given constraints.",
                "The format of the graph should be 'Node -> Dependent Node'."
            ]
        elif t["task"] == "analyze":
            criteria = [
                "The analysis should correctly identify any potential issues or bottlenecks in the graph.",
                "The analysis should be logical and coherent."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
