class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe a surreal painting of a cityscape where the buildings are made of clouds and the streets are rivers flowing with stars.",
                "interpretation": "Interpret the following description of a piece of art and explain its possible meaning, themes, and emotions:\n\nDescription: A vast desert under a blood-red sky, with a single tree bearing golden leaves. Shadows of unseen creatures flicker across the sand, and in the distance, a mountain range rises like jagged teeth."
            },
            "2": {
                "prompt": "Describe a futuristic city at night where the skyscrapers are bioluminescent plants and the vehicles are flying jellyfish.",
                "interpretation": "Interpret the following description of a piece of art and explain its possible meaning, themes, and emotions:\n\nDescription: A tranquil forest with trees made of glass. The sunlight refracts through the branches, casting a kaleidoscope of colors on the forest floor. In the center, a crystal-clear pond reflects the vibrant hues, creating a surreal, dreamlike atmosphere."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given prompt and interpretation instructions:

Prompt:
{t['prompt']}

Your task is to:
1. Generate a detailed description of a piece of visual art based on the given prompt. Ensure that your description is vivid, imaginative, and captures the essence of the prompt. The description should be at least 100 words long.
2. Interpret the provided description of a piece of art and explain its possible meaning, themes, and emotions. Provide a thoughtful and insightful interpretation that demonstrates a deep understanding of the description. The interpretation should be at least 100 words long and avoid vague or superficial interpretations.

Submit your response as a plain text string in the following format:
- Description: [Your art description here]
- Interpretation: [Your interpretation here]

Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of visual art and the provided prompts.

Example Response Format:
- Description: A cityscape where buildings made of clouds float above streets flowing with stars. The atmosphere is surreal, with a dreamlike quality. The buildings are ethereal and ever-changing, while the starry rivers create a sense of wonder and mystery. The sky is an endless twilight, casting a soft glow over the scene.
- Interpretation: The description of the desert under a blood-red sky evokes a sense of desolation and foreboding. The golden leaves on the tree may symbolize hope or resilience, while the flickering shadows suggest hidden dangers or unseen forces. The jagged mountain range in the distance adds to the ominous and otherworldly atmosphere, creating a stark contrast between the beauty of the tree and the harshness of the environment. This contrast may represent the coexistence of beauty and danger in the world."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The art description should be vivid, imaginative, and at least 100 words long.",
            "The interpretation should be thoughtful, insightful, at least 100 words long, and avoid vague or superficial interpretations.",
            "The response should be well-structured and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
