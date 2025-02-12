class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "The chart below shows the sales performance of three products: Product A, Product B, and Product C over the last four quarters. Product A has shown a steady increase in sales, Product B's sales have fluctuated, and Product C has seen a decline.",
                "image_url": "https://example.com/sales_chart.png",
                "question": "What insights can you derive from the sales performance chart?"
            },
            "2": {
                "text": "The image below depicts various weather patterns observed over the past month, including rainfall, temperature variations, and wind speeds. The region has experienced unseasonably high rainfall and lower-than-average temperatures.",
                "image_url": "https://example.com/weather_patterns.png",
                "question": "How would you describe the weather trends and their potential impact on local agriculture?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        image_url = t["image_url"]
        question = t["question"]
        instructions = f"""Your task is to interpret and analyze the information provided in both the text and the linked image. Here is the text: '{text}'.

Refer to the image at the following URL: {image_url}

Question: {question}

Provide a coherent and comprehensive response that integrates insights from both the text and the image. Your response should be in plain text format and should clearly address the question posed."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should integrate information from both the text and the image.",
            "The response should be coherent and comprehensive.",
            "The insights provided should be accurate and relevant to the question."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
