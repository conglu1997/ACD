class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "documents": [
                    "Document 1: Artificial Intelligence (AI) is a broad field of computer science focused on creating systems capable of performing tasks that require human intelligence. These tasks include language understanding, problem-solving, and learning from experience.",
                    "Document 2: Machine Learning (ML) is a subset of AI that involves the use of algorithms and statistical models to enable computers to perform tasks without explicit instructions. ML systems learn from and make predictions based on data.",
                    "Document 3: Deep Learning is a subset of machine learning that uses neural networks with many layers (hence 'deep') to analyze various types of data. It has been particularly successful in areas such as image and speech recognition."
                ]
            },
            "2": {
                "documents": [
                    "Document 1: Climate change refers to long-term changes in temperature, precipitation, wind patterns, and other aspects of the Earth's climate. It is primarily driven by human activities such as burning fossil fuels, deforestation, and industrial processes.",
                    "Document 2: The greenhouse effect is a natural process that warms the Earth's surface. When the Sun's energy reaches the Earth, some of it is reflected back to space and the rest is absorbed and re-radiated by greenhouse gases. Increasing levels of greenhouse gases due to human activities enhance this effect, leading to global warming.",
                    "Document 3: Renewable energy sources, such as solar, wind, and hydroelectric power, offer alternatives to fossil fuels. They produce little to no greenhouse gases and are crucial in the fight against climate change."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and informative summary based on the following documents:

{chr(10).join(t['documents'])}

Your summary should capture the key points from each document and present them in a logical, unified manner. Ensure that the summary is concise and does not exceed 150 words. Submit your summary as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The summary should capture key points from each document.", "The summary should be coherent and logically structured.", "The summary should be concise and not exceed 150 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
