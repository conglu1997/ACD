class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "graph": {
                    "nodes": ["A", "B", "C", "D", "E", "F", "G"],
                    "edges": [("A", "B", 1), ("B", "C", 3), ("A", "C", 4), ("C", "D", 2), ("D", "E", 1), ("B", "E", 6), ("E", "F", 2), ("C", "F", 5), ("F", "G", 1), ("D", "G", 3)]
                },
                "start": "A",
                "end": "G"
            },
            "2": {
                "graph": {
                    "nodes": ["A", "B", "C", "D", "E", "F"],
                    "edges": [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), ("F", "A"), ("A", "C"), ("B", "D"), ("C", "E")]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "start" in t:
            return f"""Find the shortest path in the following graph from the start node to the end node.

Nodes: {t['graph']['nodes']}
Edges: {t['graph']['edges']}
Start Node: {t['start']}
End Node: {t['end']}

Submit your response as a plain text string in the format: Shortest Path: [path] with Distance: [distance]"""
        else:
            return f"""Determine if the following graph is bipartite.

Nodes: {t['graph']['nodes']}
Edges: {t['graph']['edges']}

Submit your response as a plain text string in the format: Bipartite: [Yes/No]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "start" in t:
            validation_criteria = [
                "The response should correctly identify the shortest path from the start node to the end node.",
                "The distance should be correctly calculated.",
                "The path should be presented in the correct format as specified in the instructions."]
        else:
            validation_criteria = [
                "The response should correctly determine if the graph is bipartite.",
                "The response should be presented in the correct format as specified in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
