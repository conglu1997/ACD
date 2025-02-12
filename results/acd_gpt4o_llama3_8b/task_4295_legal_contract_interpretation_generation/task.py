class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "contract": "This agreement is made on the 1st of January, 2023, between ABC Corp (hereinafter referred to as 'Party A') and XYZ Inc (hereinafter referred to as 'Party B'). Party A agrees to provide consulting services to Party B for a duration of 12 months, starting from the date of this agreement. The services provided will include market analysis, strategy development, and implementation support. Party B agrees to compensate Party A with a monthly retainer of $10,000, payable on the 1st of each month. Both parties agree to maintain confidentiality and not disclose any proprietary information to third parties.",
                "task": "interpret"
            },
            "2": {
                "requirements": "Generate a clause for the termination of the contract, ensuring it covers termination for cause and without cause, notice periods, any financial implications, and the process for dispute resolution.",
                "task": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'interpret':
            return f"""Complete the following task based on the given legal contract:

Contract:
{t['contract']}

Task: Interpret the contract and provide detailed explanations for the following clauses:
1. The duration and scope of the services provided by Party A.
2. The compensation terms for Party A.
3. The confidentiality agreement between the parties.

Submit your response as a plain text string in the following format:

1. Duration and Scope: [Your explanation here]
2. Compensation: [Your explanation here]
3. Confidentiality: [Your explanation here]"""
        elif t['task'] == 'generate':
            return f"""Complete the following task based on the specified requirements:

Requirements:
{t['requirements']}

Task: Generate a new clause for the termination of the contract. Ensure that the clause covers termination for cause and without cause, notice periods, any financial implications, and the process for dispute resolution.

Submit your response as a plain text string in the following format:

Termination Clause: [Your generated clause here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'interpret':
            criteria = [
                "The explanation should accurately reflect the details of the contract clauses.",
                "The explanation should be clear, precise, and cover all specified clauses."
            ]
        elif t['task'] == 'generate':
            criteria = [
                "The generated termination clause should cover termination for cause and without cause.",
                "The clause should include notice periods, any financial implications, and the process for dispute resolution.",
                "The language should be formal, clear, and legally appropriate."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
