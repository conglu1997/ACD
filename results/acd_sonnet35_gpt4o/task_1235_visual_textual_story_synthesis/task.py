import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        image_sets = [
            [
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg"
            ],
            [
                "https://example.com/image4.jpg",
                "https://example.com/image5.jpg",
                "https://example.com/image6.jpg"
            ]
        ]
        text_prompts = [
            ["A mysterious object", "An unexpected encounter", "A surprising revelation"],
            ["A hidden talent", "A difficult decision", "An unlikely friendship"]
        ]
        return {
            "1": {"images": image_sets[0], "prompts": text_prompts[0]},
            "2": {"images": image_sets[1], "prompts": text_prompts[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a coherent and engaging story that integrates the following series of images with the given textual prompts. Your story should demonstrate cross-modal reasoning by seamlessly connecting the visual elements with the narrative elements.

Images:
{', '.join(t['images'])}

Textual prompts to incorporate:
{', '.join(t['prompts'])}

Your story should:
1. Incorporate all three images in the order they are presented.
2. Include all three textual prompts in your narrative.
3. Be between 300-400 words in length.
4. Maintain a coherent plot and consistent tone throughout.
5. Demonstrate creative interpretation of both visual and textual elements.

Begin your story with 'Once upon a time' and end it with 'The end.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story incorporates all three images in the correct order",
            "All three textual prompts are included in the narrative",
            "The story is between 300-400 words in length",
            "The plot is coherent and the tone is consistent throughout",
            "The story demonstrates creative interpretation of both visual and textual elements",
            "The story begins with 'Once upon a time' and ends with 'The end.'"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
