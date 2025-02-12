class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "script": "Linear B",
                "message": "𐀀𐀁𐀂𐀃𐀄 𐀅𐀆𐀇𐀈𐀉 𐀊𐀋𐀍𐀎𐀏",
                "evolution_period": "500 years"
            },
            "2": {
                "script": "Cuneiform",
                "message": "𒀀𒀁𒀂𒀃𒀄 𒀅𒀆𒀇𒀈𒀉 𒀊𒀋𒀍𒀎𒀏",
                "evolution_period": "1000 years"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a linguist specializing in ancient writing systems. Your task has three parts:

1. Analyze the given {t['script']} script. Describe its key characteristics, historical context, and any unique features (3-4 sentences).

2. The following message in {t['script']} has been discovered: '{t['message']}'. Provide a plausible decoding or interpretation of this message, explaining your reasoning (2-3 sentences).

3. Imagine how this script might have evolved over {t['evolution_period']}. Describe the potential changes in its structure, usage, or appearance, and create a sample of how a similar message might look in this evolved script (4-5 sentences).

Format your response as follows:

Analysis:
[Your analysis of the script]

Decoding:
[Your interpretation of the message]

Evolution:
[Your description of the script's evolution]

Evolved Message:
[Your sample of the evolved script]

Ensure your response is grounded in linguistic and historical principles while demonstrating creativity in the evolution scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed analysis of the given script, including its characteristics and historical context.",
            "The decoding of the message is plausible and the reasoning is explained.",
            "The evolution scenario is creative yet grounded in linguistic principles.",
            "An example of the evolved script is provided and is consistent with the described evolution."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
