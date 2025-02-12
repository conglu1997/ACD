class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artwork": "A surreal landscape with melting clocks, a distorted horizon, an orange sky, and a large twisted tree."},
            "2": {"artwork": "A portrait of a woman in a flowing red dress, standing in a field of sunflowers under a clear blue sky, with mountains in the background and a small cottage in the distance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Describe the following artwork in detail:\n{t['artwork']}\n\n"
            "Your description should include details about the composition, color palette, forms, and subject matter. Use descriptive and evocative language to convey the essence of the artwork. Ensure your description is coherent, vivid, and captures the visual and emotional impact of the piece. Provide your response in plain text format."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be coherent and well-structured.",
            "The description should include details about composition, color palette, forms, and subject matter.",
            "The language should be descriptive and evocative.",
            "The description should convey the visual and emotional impact of the artwork.",
            "The response should be in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0