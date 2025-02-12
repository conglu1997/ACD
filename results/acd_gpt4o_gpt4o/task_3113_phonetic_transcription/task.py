class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sentence": "The quick brown fox jumps over the lazy dog."
            },
            "2": {
                "word": "onomatopoeia"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "sentence" in t:
            return (
                "Your task is to provide the phonetic transcription of the following sentence using the International Phonetic Alphabet (IPA): \n\n"
                "Sentence: {sentence}\n"
                "Provide your transcription in IPA format and plain text.").format(sentence=t['sentence'])
        elif "word" in t:
            return (
                "Your task is to provide the phonetic transcription of the following word using the International Phonetic Alphabet (IPA): \n\n"
                "Word: {word}\n"
                "Provide your transcription in IPA format and plain text.").format(word=t['word'])
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge

        instructions = TaskFamily.get_instructions(t)
        criteria = []

        if "sentence" in t:
            correct_transcription = "ðə kwɪk braʊn fɑks dʒʌmps ˈoʊvər ðə ˈleɪzi dɑɡ"
            criteria.append(f"The phonetic transcription should be {correct_transcription}.")
        elif "word" in t:
            correct_transcription = "ˌɒnəˌmætəˈpiə"
            criteria.append(f"The phonetic transcription should be {correct_transcription}.")

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
