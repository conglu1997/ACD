class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'scenario': 'Describe the step-by-step process for assembling a flat-pack bookshelf. Ensure your description covers all necessary tools, safety precautions, and the order of assembly steps.'
            },
            '2': {
                'scenario': 'Outline the detailed procedure for baking a three-layer chocolate cake from scratch. Your description should include ingredients, tools, preparation steps, baking instructions, and any tips for ensuring the cake turns out well.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the given scenario, generate a detailed step-by-step procedure:

Scenario: {t['scenario']}

Submit your response as a plain text string, ensuring that each step is clear, logically ordered, and detailed. Number each step for clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The response should correctly follow the given scenario.',
            'Each step should be clear, logically ordered, and detailed.',
            'The procedure should cover all necessary tools, materials, and precautions as applicable.',
            'The response should be formatted with each step numbered for clarity.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
