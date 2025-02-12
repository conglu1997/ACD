class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document": "This Agreement is made between the Company and the Employee. The Employee agrees to maintain confidentiality of all proprietary information. The Employee shall not engage in any business that competes with the Company during the term of employment and for a period of one year thereafter. Any breach of this Agreement will result in immediate termination and possible legal action.", "questions": ["What are the confidentiality obligations of the Employee?", "Can the Employee work for a competitor after leaving the Company? If so, when?"]},
            "2": {"document": "The Tenant agrees to pay the monthly rent of $1200 on the first day of each month. The Landlord may increase the rent with a 60-day written notice. The Tenant shall not sublease the property without prior written consent from the Landlord. Any damage to the property caused by the Tenant will be the Tenant's responsibility to repair at their own cost.", "questions": ["When is the Tenant required to pay rent?", "What must the Tenant do before subleasing the property?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        document = t["document"]
        questions = "\n".join(t["questions"])
        return f"""Analyze the following legal document and answer the specified questions based on its clauses.\nDocument:\n{document}\nQuestions:\n{questions}\nEnsure your answers are accurate and directly address the questions based on the content of the document. Submit your answers as a plain text string with each answer on a new line, labeled with the respective question number."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
