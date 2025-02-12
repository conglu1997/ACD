class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"diagram_type": "flowchart", "description": "Create a flowchart representing the process of online shopping. Include the following steps: Browse Products, Add to Cart, Checkout, Payment, Order Confirmation."},
            "2": {"diagram_type": "network diagram", "description": "Create a network diagram for a small office network. Include the following components: Router, Switch, 3 Computers, Printer, Server."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        diagram_type = t["diagram_type"]
        description = t["description"]
        return f"""Generate a text description for a {diagram_type} based on the following specifications:

Description:
{description}

Your text description should include:
1. A brief overview of the diagram, explaining its purpose and scope.
2. A detailed description of each component and its connections or relationships, including any relevant attributes or properties.
3. Any additional notes or annotations that are relevant to understanding the diagram.

Submit your text description as a plain text string in the format:

Overview: [Your overview]

Component Descriptions:
1. [Component 1]: [Description]
2. [Component 2]: [Description]
...

Connections:
1. [Connection 1]: [Description]
2. [Connection 2]: [Description]
...

Additional Notes: [Any additional notes]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The text description should include a clear overview explaining the diagram's purpose and scope.",
            "All specified components should be described in detail, including their attributes or properties.",
            "The connections or relationships between components should be clearly described and logical.",
            "Any additional notes or annotations should be relevant and helpful in understanding the diagram.",
            "The overall description should be coherent, logically structured, and free from significant errors."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
