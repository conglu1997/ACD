class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "She sells sea shells by the sea shore.",
                "mode": "to_phonetic"
            },
            "2": {
                "text": "/ʃi sɛlz si ʃɛlz baɪ ðə si ʃɔr/",
                "mode": "to_text"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['mode'] == 'to_phonetic':
            return f"Your task is to convert the following written text into its phonetic transcription using the International Phonetic Alphabet (IPA):\n\n{t['text']}\n\nProvide the phonetic transcription in plain text format. Example: 'hello' -> /həˈloʊ/"
        else:
            return f"Your task is to convert the following phonetic transcription into written text. The transcription uses the International Phonetic Alphabet (IPA):\n\n{t['text']}\n\nProvide the written text in plain text format. Example: /həˈloʊ/ -> 'hello'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The phonetic transcription must accurately represent the given text using IPA.",
            "The written text must accurately convert the given IPA transcription.",
            "The format must match the provided examples.",
            "The response must be free of any additional characters or symbols not present in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
