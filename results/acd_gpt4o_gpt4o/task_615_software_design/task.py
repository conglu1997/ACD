class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "A web-based e-commerce application allowing users to browse products, add items to a shopping cart, and checkout using a payment gateway. The system should support user authentication and inventory management."
            },
            "2": {
                "requirements": "A mobile app for a health tracking system that records user activity, sleep patterns, and dietary intake. The app should provide data visualization, goal setting, and integration with wearable devices."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        requirements = t["requirements"]
        instructions = f"""Your task is to design a software system based on the following requirements:

Requirements: {requirements}

Provide a detailed design of the system, including:

1. High-level architecture: A description of the main components and their interactions.
2. Data flow: How data moves through the system.
3. Technologies: The technologies and tools you would use to implement the system.
4. Justification: Why you chose this particular design and technologies.

Ensure that your response is comprehensive, well-structured, and demonstrates an understanding of software design principles. Provide your response in plain text format, with each section clearly labeled."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The high-level architecture should include the main components and their interactions.",
            "The data flow should be clearly described and logical.",
            "The technologies and tools chosen should be appropriate for the requirements.",
            "The justification should be clear and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
