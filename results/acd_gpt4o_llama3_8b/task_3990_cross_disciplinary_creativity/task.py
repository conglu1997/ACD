class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a story that seamlessly integrates the concept of quantum mechanics with elements of surrealist art. The story should be around 500 words and should creatively combine scientific accuracy with artistic expression."
            },
            "2": {
                "prompt": "Write a poem that blends the theme of genetic engineering with the stylistic elements of impressionist painting. The poem should be around 150 words and should creatively merge scientific concepts with artistic techniques."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an integrative piece based on the following prompt. Your response should creatively blend concepts from science and art, demonstrating both scientific accuracy and artistic expression.

Prompt:
{t['prompt']}

Ensure that your piece is coherent, engaging, and accurately represents both the scientific and artistic elements. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should accurately integrate scientific concepts.",
            "The response should creatively incorporate artistic elements.",
            "The piece should be coherent and engaging.",
            "The piece should demonstrate a seamless blend of science and art."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
