class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "premises": ["If it rains, the ground will be wet.", "If the ground is wet, the flowers will grow.", "It is raining."],
                "conclusion": "The flowers will grow."
            },
            "2": {
                "premises": ["All humans are mortal.", "Socrates is a human."],
                "conclusion": "Socrates is mortal."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a formal logic proof based on the given premises and conclusion. Use standard logical notation (e.g., natural deduction) and ensure the proof is logically valid. Present the proof step-by-step, clearly showing each inference. Here is an example format:

Premises:
1. If it rains, the ground will be wet.
2. It is raining.

Conclusion:
The ground is wet.

Proof:
1. If it rains, the ground will be wet. (Premise)
2. It is raining. (Premise)
3. Therefore, the ground is wet. (Modus Ponens from 1, 2)

Apply similar steps to generate the proof for the given premises and conclusion.

Premises:
{'; '.join(t['premises'])}

Conclusion:
{t['conclusion']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The logic proof should be logically valid.", "The proof should correctly derive the conclusion from the premises.", "The proof should use standard logical notation and be presented step-by-step."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
