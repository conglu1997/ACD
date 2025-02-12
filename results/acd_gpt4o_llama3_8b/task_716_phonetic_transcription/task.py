class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "text_to_ipa", "text": "The quick brown fox jumps over the lazy dog.", "constraints": "Provide the IPA transcription of the given text. Ensure that the transcription accurately represents standard American English pronunciation."},
            "2": {"task_type": "ipa_to_text", "ipa": "ðə kwɪk braʊn fɑks dʒʌmps oʊvər ðə leɪzi dɔg.", "constraints": "Convert the given IPA transcription back to the original text. Ensure that the text accurately reflects the original sentence based on the IPA transcription."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "text_to_ipa":
            examples = 'Examples:\n1. Text: "Hello" -> IPA: "həˈloʊ"\n2. Text: "World" -> IPA: "wɜrld"\n3. Text: "Good morning" -> IPA: "ɡʊd ˈmɔrnɪŋ"'
            return f"Convert the following text to its phonetic transcription using the International Phonetic Alphabet (IPA): {t['text']}. {t['constraints']}\n{examples}"
        elif t["task_type"] == "ipa_to_text":
            examples = 'Examples:\n1. IPA: "həˈloʊ" -> Text: "Hello"\n2. IPA: "wɜrld" -> Text: "World"\n3. IPA: "ɡʊd ˈmɔrnɪŋ" -> Text: "Good morning"'
            return f"Convert the following IPA transcription back to the original text: {t['ipa']}. {t['constraints']}\n{examples}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "text_to_ipa":
            criteria = ["The transcription should accurately represent the pronunciation of the text using IPA symbols.", "The transcription should reflect standard American English pronunciation."]
        elif t["task_type"] == "ipa_to_text":
            criteria = ["The text should accurately reflect the original sentence based on the IPA transcription."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
