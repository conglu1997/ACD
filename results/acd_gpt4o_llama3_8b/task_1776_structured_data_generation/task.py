class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "unstructured_text": "John went to the store and bought milk, bread, and eggs. He spent a total of $10. On his way back, he met his friend Mike who told him about a new book he was reading. They decided to meet at the park the next day to discuss it further while jogging together. Later that evening, John cooked dinner using the ingredients he bought, and the meal turned out delicious."
            },
            "2": {
                "unstructured_text": "The company announced a new product launch next month. The product, a smartwatch, will have features like heart rate monitoring, GPS, and a long battery life. It is expected to be priced at $199. The marketing team has planned a series of promotional events including online ads, social media campaigns, and a launch event at the headquarters. Additionally, there will be a special discount for the first 100 customers who pre-order the smartwatch."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following unstructured text into a structured format. You can use tables, bullet points, or any other appropriate structure to clearly present the information. Ensure that the structured data is comprehensive and easy to understand. Submit your response as a plain text string.\n\nUnstructured Text: {t['unstructured_text']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The structured data should include all relevant information from the unstructured text.",
            "The structured data should be clear and easy to understand.",
            "The structured data should be well-organized and appropriately formatted."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
