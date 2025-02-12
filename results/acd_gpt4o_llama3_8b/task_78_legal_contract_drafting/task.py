class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Draft an employment contract for a software developer. The contract should include the following sections: Job Title, Job Responsibilities, Salary, Benefits, Termination Clause, Confidentiality Agreement, Intellectual Property Agreement, Non-compete Clause, and Governing Law. Ensure the language is formal and legally binding."
            },
            "2": {
                "requirements": "Draft a lease agreement for a residential property. The contract should include the following sections: Parties Involved, Property Description, Lease Term, Rent, Security Deposit, Maintenance and Repairs, Termination Clause, Pet Policy, Subletting Clause, and Governing Law. Ensure the language is formal and legally binding."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Draft a legal contract based on the specified requirements: 

Requirements:
{t['requirements']}

Ensure the contract includes all specified sections, uses formal and legally binding language, and adheres to standard legal contract structures. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The contract should include all specified sections.", "The language should be formal and legally binding.", "The contract should adhere to standard legal contract structures."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
