class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "document": "This agreement is made between ABC Corporation and XYZ Limited. ABC agrees to provide XYZ with 500 units of product A per month at a price of $10 per unit. The agreement is valid for one year, starting from January 1, 2023. Either party may terminate the agreement with a 30-day notice.",
                "criteria": "Summarize the agreement and extract the main terms including parties involved, product and quantity, price, duration, and termination clause."
            },
            "2": {
                "document": "The tenant agrees to rent the apartment located at 123 Main Street for a period of 12 months, starting from March 1, 2023. The monthly rent is $1,200, payable on the first day of each month. The tenant must maintain the property in good condition and is responsible for all utilities. The landlord may enter the premises with 24-hour notice for inspections or repairs.",
                "criteria": "Summarize the rental agreement and extract the main terms including parties involved, property address, rental period, monthly rent, tenant responsibilities, and landlord's right of entry."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"Your task is to interpret and summarize the following legal document. Extract the main terms based on the given criteria.\n\nDocument: {t['document']}\n\nCriteria: {t['criteria']}\n\nProvide your summary and extracted terms in the following format:\nSummary: [Your summary]\nExtracted Terms: [List the extracted terms based on the criteria]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should be clear and concise.",
            "The extracted terms should correctly reflect the main terms of the document.",
            "The response should be formatted correctly as per the instructions.",
            "The extracted terms should be listed according to the criteria provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
