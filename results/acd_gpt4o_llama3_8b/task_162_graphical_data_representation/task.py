class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": {"Category A": 30, "Category B": 45, "Category C": 25}, "graph_type": "pie chart"},
            "2": {"graph": "<svg width='400' height='200'><rect x='50' y='50' width='40' height='100' style='fill:blue;'/><rect x='150' y='70' width='40' height='80' style='fill:red;'/><rect x='250' y='90' width='40' height='60' style='fill:green;'/></svg>", "graph_type": "bar graph"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "data" in t:
            return f"""Complete the following task based on the given data:

Data:
{t['data']}

Graph Type: {t['graph_type']}

Generate a {t['graph_type']} that accurately represents the data. Submit your graph as SVG code in a plain text string. Ensure that each category is represented by a distinct color, and that the proportions accurately reflect the data. The SVG code must include appropriate labels for each category."""
        elif "graph" in t:
            return f"""Complete the following task based on the given graph:

Graph Type: {t['graph_type']}

Graph:
{t['graph']}

Interpret the {t['graph_type']} and describe the information it conveys. Submit your interpretation as a plain text string. Your interpretation should include the values represented by each bar, the corresponding categories, and any apparent trends or insights."""
        else:
            raise ValueError("Invalid task data")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "data" in t:
            criteria = ["The SVG code should accurately represent the provided data as a pie chart.", "Each category should be represented by a distinct color.", "The proportions should accurately reflect the data.", "The SVG code must include appropriate labels for each category."]
        elif "graph" in t:
            criteria = ["The interpretation should accurately describe the information conveyed by the bar graph.", "The interpretation should include the values represented by each bar and the corresponding categories.", "The interpretation should identify any apparent trends or insights.", "The interpretation should be clear and well-structured."]
        else:
            raise ValueError("Invalid task data")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0