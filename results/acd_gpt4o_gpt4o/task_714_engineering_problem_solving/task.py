class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design a bridge to span a river 100 meters wide. The bridge must support a load of 1000 kg at any point. Describe the type of bridge you would design, the materials you would use, and the reasoning behind your choices.",
                "title": "Bridge Design"
            },
            "2": {
                "problem": "Design a simple irrigation system for a small farm of 1 hectare that maximizes water efficiency. Describe the components of the system, the materials you would use, and the reasoning behind your choices.",
                "title": "Irrigation System Design"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        title = t["title"]
        instructions = f"""Your task is to solve the following engineering problem by applying relevant scientific principles.

Title: {title}
Problem: {problem}

Your response should include:
1. A detailed description of your proposed solution.
2. An explanation of the scientific principles that underpin your design.
3. Justification for your choice of materials and components.
4. Any calculations or assumptions you have made.

Provide your response in plain text format, ensuring that it is comprehensive and technically sound.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a coherent and technically sound solution to the problem.",
            "The response should explain the scientific principles behind the proposed design.",
            "The response should justify the choice of materials and components.",
            "The response should include any necessary calculations or assumptions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
