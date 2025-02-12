class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idioms": ["break the ice", "spill the beans"]},
            "2": {"idioms": ["kick the bucket", "hit the nail on the head"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        idioms = ', '.join(t["idioms"])
        return f"""Generate contextually appropriate sentences using the following idiomatic expressions: {idioms}. For each idiom, provide:
1. A brief explanation of its meaning.
2. A contextually appropriate sentence that uses the idiom correctly.

Submit your response as a plain text string in the following format:

Idiom: [Idiom]
Meaning: [Brief explanation of the idiom's meaning]
Sentence: [Contextually appropriate sentence using the idiom]

Example:
Idiom: break the ice
Meaning: To initiate conversation in a social setting.
Sentence: At the party, Sarah told a funny joke to break the ice and get everyone talking.

Idiom: spill the beans
Meaning: To reveal a secret.
Sentence: John couldn't keep it to himself any longer and finally spilled the beans about the surprise party.

Idiom: kick the bucket
Meaning: To die.
Sentence: The old man kicked the bucket after a long illness.

Idiom: hit the nail on the head
Meaning: To describe exactly what is causing a situation or problem.
Sentence: When Jane said that Tom was irresponsible, she really hit the nail on the head.

Make sure that your explanations are clear and your sentences illustrate the idioms in a natural and contextually appropriate way."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Each idiom should be correctly explained.",
            "Each sentence should use the idiom in a contextually appropriate manner.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
