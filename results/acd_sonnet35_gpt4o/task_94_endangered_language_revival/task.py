import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            {
                "name": "Ayapaneco",
                "location": "Mexico",
                "speakers": "2",
                "unique_feature": "Complex tonal system with four distinct tones"
            },
            {
                "name": "Njerep",
                "location": "Cameroon",
                "speakers": "4",
                "unique_feature": "Extensive use of ideophones (words that evoke sensory experiences)"
            },
            {
                "name": "Koro",
                "location": "India",
                "speakers": "800",
                "unique_feature": "Unique counting system based on body parts"
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(endangered_languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the endangered language {t['name']} from {t['location']} and propose innovative methods for its preservation and revival. The language has approximately {t['speakers']} speakers and features {t['unique_feature']}.

Your task is to:

1. Analyze the significance of the language's unique feature (2-3 sentences).
2. Propose three innovative methods for preserving and reviving the language, considering modern technology and cultural contexts (2-3 sentences each).
3. Describe a potential challenge in implementing one of your methods and suggest a solution (2-3 sentences).
4. Explain how preserving this language could contribute to linguistic diversity and cultural heritage (2-3 sentences).
5. Suggest an interdisciplinary research project that could arise from studying this language (2-3 sentences).

Provide your response in the following format:

Unique Feature Analysis:
[Your analysis here]

Preservation Methods:
1. [First method]
2. [Second method]
3. [Third method]

Implementation Challenge and Solution:
[Your description here]

Contribution to Linguistic Diversity:
[Your explanation here]

Interdisciplinary Research Project:
[Your suggestion here]

Ensure your response is creative, culturally sensitive, and grounded in linguistic and anthropological principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the unique feature of {t['unique_feature']} for the {t['name']} language",
            "The preservation methods should be innovative and consider modern technology",
            "The response should demonstrate cultural sensitivity and understanding of linguistic principles",
            "The interdisciplinary research project should be relevant and creative",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
