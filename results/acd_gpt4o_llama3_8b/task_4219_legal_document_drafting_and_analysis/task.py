class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document": "This Agreement is made as of [Date], by and between [Party A], having its principal place of business at [Address] (hereinafter referred to as 'Party A') and [Party B], having its principal place of business at [Address] (hereinafter referred to as 'Party B').\n\nParty A and Party B agree as follows:\n\n1. Term. The term of this Agreement shall commence on the date hereof and shall continue until terminated by either party.\n\n2. Confidentiality. Each party agrees to hold in confidence all information disclosed by the other party.\n\n3. Governing Law. This Agreement shall be governed by and construed in accordance with the laws of [State].", "task_type": "analysis"},
            "2": {"criteria": "Draft an employment contract including the following elements: 1. Parties Involved, 2. Employment Term, 3. Duties and Responsibilities, 4. Compensation, 5. Termination Clause, 6. Confidentiality Clause, 7. Governing Law.", "task_type": "drafting"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "analysis":
            return f"""Complete the following task based on the given legal document:\n\nDocument:\n{t['document']}\n\nTask: Identify and list the key elements of the document, such as involved parties, terms, and specific clauses. Submit your analysis as a plain text string in the following format:\n\nKey Elements:\n1. Parties Involved: [Your response here]\n2. Term: [Your response here]\n3. Confidentiality Clause: [Your response here]\n4. Governing Law: [Your response here]"""
        elif t["task_type"] == "drafting":
            return f"""Complete the following task based on the given criteria:\n\nCriteria:\n{t['criteria']}\n\nTask: Draft a comprehensive employment contract that includes all specified elements. Ensure that the contract is structured logically and adheres to formal legal language and formatting. Submit your drafted contract as a plain text string in the following format:\n\nDrafted Contract:\n[Your drafted contract here]"""
        else:
            raise ValueError("Invalid task type")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "analysis":
            criteria = ["The analysis should correctly identify the key elements of the legal document.", "The response should be well-structured and formatted correctly."]
        elif t["task_type"] == "drafting":
            criteria = ["The drafted contract should include all specified elements.", "The contract should follow formal legal language and structure.", "The contract should be logically structured and free of ambiguities."]
        else:
            raise ValueError("Invalid task type")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0