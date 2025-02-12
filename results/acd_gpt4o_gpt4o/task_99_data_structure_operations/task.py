class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"tree": "A(B(D)(E))(C(F)(G))", "operation": "inorder_traversal", "expected_result": "D B E A F C G"},
            "2": {"graph": {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": [], "E": [], "F": [], "G": []}, "operation": "find_path", "start": "A", "end": "E", "expected_result": "A -> B -> E"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "tree" in t:
            return f"""Perform the following operation on the given tree:

Tree (nested representation): {t["tree"]}
Operation: {t["operation"]}

Provide the result of the operation in plain text format."""
        else:
            return f"""Perform the following operation on the given graph:

Graph (adjacency list): {t["graph"]}
Operation: {t["operation"]}
Start Node: {t["start"]}
End Node: {t["end"]}

Provide the result of the operation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should match the expected result: {t['expected_result']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
