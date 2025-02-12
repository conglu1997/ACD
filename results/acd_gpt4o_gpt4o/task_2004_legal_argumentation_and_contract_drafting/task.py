class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"case": "A person slipped and fell in a grocery store, sustaining injuries. They are suing the store for negligence. Draft a legal argument in support of the plaintiff's claim."},
            "2": {"contract_spec": "Draft a simple employment contract for a software developer position. Include sections for job responsibilities, salary, benefits, confidentiality, termination, intellectual property rights, and dispute resolution."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "case" in t:
            case = t["case"]
            instructions = f"""Your task is to generate a legal argument based on the following case:

Case: {case}

Your argument should include:
1. A clear statement of the legal issue.
2. Relevant legal principles and precedents.
3. Logical reasoning supporting the plaintiff's claim.
4. A conclusion summarizing the argument.

Ensure your argument is coherent, well-structured, and uses precise legal language. Provide your argument in plain text format."""
        else:
            contract_spec = t["contract_spec"]
            instructions = f"""Your task is to draft a simple employment contract based on the following specifications:

Specifications: {contract_spec}

Your contract should include the following sections:
1. Job Responsibilities
2. Salary
3. Benefits
4. Confidentiality
5. Termination
6. Intellectual Property Rights
7. Dispute Resolution

Ensure your contract is clear, detailed, and uses precise legal language. Provide your contract in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "case" in t:
            criteria = [
                "The argument should clearly state the legal issue.",
                "The argument should include relevant legal principles and precedents.",
                "The argument should use logical reasoning to support the plaintiff's claim.",
                "The argument should be coherent and well-structured.",
                "The argument should use precise legal language."]
        else:
            criteria = [
                "The contract should include sections for job responsibilities, salary, benefits, confidentiality, termination, intellectual property rights, and dispute resolution.",
                "The contract should be clear and detailed.",
                "The contract should use precise legal language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
