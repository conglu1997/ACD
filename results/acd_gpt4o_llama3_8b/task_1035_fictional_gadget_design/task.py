class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"function": "time travel", "context": "a wristwatch for a secret agent"},
            "2": {"function": "instant translation", "context": "a pair of glasses for a diplomat"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        function = t['function']
        context = t['context']
        return f"""Design a fictional gadget based on the following function and context:

Function: {function}
Context: {context}

Ensure that your design includes a detailed description of the gadget's appearance, how it works, and how it fits into the specified context. The description should be between 100 to 200 words. Submit your design as a plain text string.

Example Function: invisibility
Example Context: a cloak for a spy
Example Description: Imagine a cloak that appears as a sleek, black garment made of a lightweight, shimmering fabric. When activated by a hidden button on the collar, the cloak bends light around the wearer, rendering them invisible to the naked eye. This technology is perfect for spies needing to perform covert operations without being detected. The cloak also has embedded sensors that alert the wearer to nearby movement, ensuring they remain hidden from potential threats."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The design should include details about the gadget's appearance.", "The design should explain how the gadget works.", "The design should fit the specified context.", "The design should be coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
