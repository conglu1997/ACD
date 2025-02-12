class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "Smartphone", "requirements": "The smartphone should have a foldable screen, a battery life of at least 48 hours, and a camera with at least 108 megapixels. It should also support 5G connectivity and have an eco-friendly design."},
            "2": {"product": "Electric Car", "requirements": "The electric car should have a range of at least 500 miles on a single charge, autonomous driving capabilities, and a solar panel roof for additional charging. It should also prioritize passenger safety and comfort."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a new {t['product']} based on the following requirements:

Requirements: {t['requirements']}

Ensure that your design is innovative, practical, and meets all the specified requirements. Describe the key features, functionality, and design elements of the product. Submit your design as a plain text string in the following format:

- Product Name: [Your product name]
- Key Features: [Describe the key features in detail]
- Functionality: [Explain the functionality and how it meets the requirements]
- Design Elements: [Describe the design elements and their benefits]

Example:
- Product Name: SuperPhone X
- Key Features: Foldable screen, 48-hour battery life, 108 MP camera, 5G connectivity, eco-friendly materials
- Functionality: The foldable screen allows for a larger display area without increasing the phone's size when folded, etc.
- Design Elements: The eco-friendly materials include recycled aluminum and biodegradable plastics, etc."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should meet all the specified requirements.",
            "The design should be innovative and practical.",
            "The submission should follow the provided format.",
            "The key features should be detailed and relevant.",
            "The functionality should clearly explain how it meets the requirements.",
            "The design elements should be well-described and beneficial."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
