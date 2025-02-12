class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "image_description": "A serene beach scene with clear blue waters, a few scattered clouds in the sky, seagulls flying overhead, and a person reading a book under a beach umbrella.",
                "task_type": "generate_audio"
            },
            "2": {
                "audio_description": "The sound of a bustling city street: honking cars, people chatting, street musicians playing, and the distant sound of a train passing by.",
                "task_type": "generate_visual"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate_audio':
            return f"""Based on the following visual description, generate an auditory description that captures the essence of the scene. Use sensory language to vividly convey the sounds that would be present in the scene. Your description should be between 100 to 150 words.

Visual Description:
{t['image_description']}

Submit your auditory description as a plain text string in the following format:

Auditory Description:
[Your auditory description here]"""
        elif t['task_type'] == 'generate_visual':
            return f"""Based on the following auditory description, generate a visual description that captures the essence of the scene. Use sensory language to vividly convey the visual elements that would be present in the scene. Your description should be between 100 to 150 words.

Auditory Description:
{t['audio_description']}

Submit your visual description as a plain text string in the following format:

Visual Description:
[Your visual description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should accurately reflect the given description.",
            "The response should use sensory language to vividly convey the scene.",
            "The response should be between 100 to 150 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
