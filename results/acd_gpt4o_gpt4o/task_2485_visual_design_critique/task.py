class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "design": "A simple webpage with a header, a main content section with text and an image, and a footer.",
                "criteria": [
                    "Composition: Assess the arrangement of elements on the page.",
                    "Color: Evaluate the use of color schemes and their effectiveness.",
                    "Balance: Determine whether the design feels balanced or not.",
                    "Typography: Critique the choice and use of fonts."
                ],
                "type": "critique"
            },
            "2": {
                "design": "A complex magazine cover featuring a main image, several smaller images, headlines, and subheadings.",
                "criteria": [
                    "Composition: Assess the arrangement of elements on the cover.",
                    "Color: Evaluate the use of color schemes and their effectiveness.",
                    "Balance: Determine whether the design feels balanced or not.",
                    "Typography: Critique the choice and use of fonts."
                ],
                "type": "critique"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze and critique the provided visual design based on the following criteria:\n
{', '.join(t['criteria'])}\n
Here is the description of the design:\n{t['design']}\n
Provide your critique in plain text format. Your response should address each of the criteria in detail, demonstrating an understanding of design principles. Maintain a coherent and logical structure in your critique."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The critique should address each of the provided criteria.",
            "The critique should be detailed and demonstrate an understanding of design principles.",
            "The critique should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
