class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"specifications": "Design a simple mechanical system that uses gears and levers to lift a small weight. The system should include at least 3 gears and 2 levers."},
            "2": {"specifications": "Design a simple mechanical system that converts rotational motion into linear motion using a crank and a piston. The system should include a crank, a connecting rod, and a piston."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        specifications = t["specifications"]
        instructions = f"""Your task is to design a simple mechanical system based on the following specifications:

{specifications}

Provide a detailed description of the system, including:
1. The components of the system.
2. How the components are connected and interact with each other.
3. How the system operates to achieve the desired function.

Ensure that your description is clear, detailed, and logically sound. Provide your description in plain text format, using complete sentences and paragraphs."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should clearly identify all required components.",
            "The description should explain how the components are connected and interact.",
            "The description should logically explain how the system operates to achieve the specified function."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
