class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"case_facts": "John Doe is suing XYZ Corporation for breach of contract. John claims that XYZ failed to deliver the goods within the agreed timeframe, causing him significant financial loss. XYZ Corporation argues that the delay was due to unforeseen circumstances beyond their control and thus, they are not liable for the breach. Additionally, XYZ Corporation had communicated the potential for delays beforehand.",
                   "legal_principle": "In contract law, a party may be excused from performance if they can prove that the breach was due to unforeseen and unavoidable events (force majeure). However, the party must also show that they took reasonable steps to mitigate the impact of the breach."},
            "2": {"case_facts": "Jane Smith is seeking damages from ABC Company for personal injury. Jane alleges that she was injured due to a defective product manufactured by ABC. ABC Company asserts that Jane misused the product and that the injury was a result of her own negligence. Furthermore, ABC Company claims that they provided adequate warnings about the proper use of the product.",
                   "legal_principle": "Under product liability law, a manufacturer can be held liable for injuries caused by a defective product if the product was used as intended and the defect was the direct cause of the injury. The manufacturer must also ensure that adequate warnings and instructions are provided to prevent misuse."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to generate a legal argument based on the provided case facts and legal principle. Ensure that your argument is structured, coherent, and persuasive. Here are the details:\n\nCase Facts: {case_facts}\n\nLegal Principle: {legal_principle}\n\nSubmit your argument in plain text format. Your response should be structured as follows:\n\n1. Introduction\n2. Application of Legal Principle\n3. Conclusion""".format(case_facts=t['case_facts'], legal_principle=t['legal_principle'])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be structured and coherent.",
            "The argument should accurately apply the legal principle to the case facts.",
            "The argument should be persuasive and logically sound.",
            "The argument should be divided into Introduction, Application of Legal Principle, and Conclusion sections."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
