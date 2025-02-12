class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"discovery": "A new element that defies the periodic table"},
            "2": {"discovery": "A method for instantaneous teleportation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a fictional scientific discovery and explain it as if it were a real article in a popular science magazine. Here is the discovery you need to write about:\n\n{t['discovery']}\n\nYour article should be engaging, informative, and written in a style that is accessible to a general audience. Ensure that your article includes the following elements:\n1. A catchy headline.\n2. An introduction that hooks the reader.\n3. A detailed explanation of the discovery, including how it was made and its potential implications.\n4. Quotes from fictional scientists or experts.\n5. A conclusion that summarizes the significance of the discovery.\n\nSubmit your article in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The article should be engaging and informative.",
            "The explanation should be detailed and scientifically plausible within the fictional context.",
            "The article should include a catchy headline, an engaging introduction, a detailed explanation, quotes from fictional experts, and a conclusion.",
            "The article should be well-structured and coherent.",
            "The writing style should be accessible to a general audience."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
