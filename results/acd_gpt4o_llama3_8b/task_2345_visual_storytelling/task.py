class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "images": [
                    "A boy holding a kite", 
                    "The kite stuck in a tree", 
                    "The boy climbing the tree to retrieve the kite"
                ],
                "required_elements": ["The story must include a lesson learned by the boy"]
            },
            "2": {
                "images": [
                    "A family sitting at a dinner table", 
                    "A dog begging for food", 
                    "The dog knocking over a glass of water"
                ],
                "required_elements": ["The story must include a humorous moment"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and engaging story based on the given series of image descriptions. Ensure the story logically connects the content of each image and forms a complete narrative. The story should be at least 300 words long and must incorporate all the provided image descriptions and required elements.

Image Descriptions:
{'; '.join(t['images'])}

Required Elements:
{'; '.join(t['required_elements'])}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story must be coherent and logically connect the content of each image.",
            "The story must be engaging and at least 300 words long.",
            "The story must include all the required elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
