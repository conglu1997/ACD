class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "identify",
                "text": "As the thunder roared and the lightning flashed, she clutched the old photograph, tears streaming down her face. Memories of happier times flooded her mind, mixing with the dread of the present storm."
            },
            "2": {
                "task_type": "generate",
                "emotion": "anticipation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'identify':
            return f"""Identify the primary emotion conveyed in the following text and explain your reasoning:

Text: {t['text']}

Submit your response as a plain text string in the following format:

Emotion: [Your identified emotion]
Reasoning: [Your explanation for why this is the primary emotion conveyed]

Ensure your reasoning clearly connects the text to the identified emotion."""
        else:
            return f"""Generate a sentence that evokes the following emotion and explain your reasoning:

Emotion: {t['emotion']}

Submit your response as a plain text string in the following format:

Sentence: [Your generated sentence]
Reasoning: [Your explanation for why this sentence evokes the specified emotion]

Ensure your generated sentence is coherent and effectively evokes the specified emotion."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'identify':
            validation_criteria = ["The identified emotion should be relevant to the text.", "The reasoning should clearly explain why the identified emotion is the primary one conveyed.", "The explanation should logically connect the emotion to the text."]
        else:
            validation_criteria = ["The generated sentence should effectively evoke the specified emotion.", "The reasoning should clearly explain why the sentence evokes the emotion.", "The sentence should be coherent and target the specified emotion."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
