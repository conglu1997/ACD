class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Draft an employment contract for a software engineer. The contract should include the following sections: job title and duties, compensation, benefits, termination conditions, confidentiality agreement, intellectual property rights, non-compete clause, and dispute resolution. The employment term is for 2 years, with an annual salary of $100,000. The contract should ensure that the engineer's work while employed is the property of the company. Include provisions for remote work and annual performance reviews."
            },
            "2": {
                "requirements": "Draft a lease agreement for a residential property. The contract should include the following sections: parties involved, property description, lease term, rent amount and payment schedule, security deposit, maintenance responsibilities, termination conditions, pet policy, and subletting conditions. The lease term is 1 year, with a monthly rent of $1,500. The security deposit is $1,500, and the tenant is responsible for minor maintenance. Include clauses for late payment penalties and tenant insurance requirements."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a legal contract based on the following requirements and constraints:

Requirements:
{t['requirements']}

Ensure the contract is comprehensive, legally sound, and adheres to the specified sections and details. Submit your response as a plain text string formatted as a legal contract. The document should be clear, precise, and appropriately formatted with headings for each section. Ensure that all clauses are included and logically structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The contract should include all specified sections.",
            "The contract should be legally sound and adhere to the given requirements.",
            "The language should be clear, precise, and appropriate for a legal document.",
            "The contract should be formatted with headings for each section.",
            "All clauses must be included and logically structured.",
            "The contract should include specific provisions as mentioned in the requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
