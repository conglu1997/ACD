class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"document": "The party of the first part (hereinafter referred to as 'Lessor') agrees to lease the premises to the party of the second part (hereinafter referred to as 'Lessee') for a term of one year commencing on the first day of January, 2023. The Lessee agrees to pay a monthly rent of $1,000 payable in advance on the first day of each month. In the event of failure to pay the rent within five days of the due date, a late fee of $50 will be applied.", "questions": ["Who is the Lessor?", "What is the term of the lease?"]},
            "2": {"document": "This agreement, entered into on the fifteenth day of March, 2023, by and between John Doe (hereinafter referred to as 'Seller') and Jane Smith (hereinafter referred to as 'Buyer'), stipulates that the Seller agrees to sell and the Buyer agrees to purchase the property located at 123 Main Street for the total sum of $250,000. The Buyer agrees to pay a deposit of $25,000 upon signing this agreement, with the balance of $225,000 to be paid at closing on or before the thirtieth day of April, 2023.", "questions": ["Who is the Buyer?", "What is the total purchase price?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        document = t["document"]
        questions = t["questions"]
        instructions = f"""Your task is to analyze the following legal document and answer the specific questions provided:

Document:
{document}

Questions:
1. {questions[0]}
2. {questions[1]}

Provide your answers in the following format:
Answer 1: [Your answer to question 1]
Answer 2: [Your answer to question 2]

Ensure that your answers are accurate and derived from the content of the document."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
