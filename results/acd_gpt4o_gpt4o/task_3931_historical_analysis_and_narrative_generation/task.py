class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"historical_event": "The signing of the Treaty of Versailles in 1919", "context": "This treaty ended World War I and imposed heavy reparations on Germany."},
            "2": {"criteria": "Generate a historical narrative set in the 18th century, focusing on the daily life of a blacksmith in a small European village. The village is known for its ironworks and has a local fair every summer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "historical_event" in t:
            instructions = f"""Your task is to analyze the following historical event:

{t['historical_event']}

{t['context']}

Provide a clear and detailed analysis of the event, explaining its causes, key participants, and consequences. Your analysis should be structured as follows:

1. Overview of the event
2. Causes leading up to the event
3. Key participants and their roles
4. Immediate and long-term consequences

Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to generate a historical narrative based on the following criteria:

{t['criteria']}

Ensure your narrative is historically accurate, engaging, and detailed. It should provide a vivid depiction of the daily life of a blacksmith in a small European village in the 18th century. Structure your narrative logically and ensure it covers:

1. Description of the setting
2. Daily activities and routines
3. Interactions with other villagers
4. Any significant events or challenges faced by the blacksmith

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "historical_event" in t:
            criteria = ["The response should provide a clear and detailed analysis of the given historical event.", "The analysis should include causes, key participants, and consequences.", "The analysis should be logically structured and coherent.", "The response should be historically accurate and relevant to the context provided."]
        else:
            criteria = ["The response should generate a historically accurate narrative that fits the provided criteria.", "The narrative should be engaging, detailed, and provide a vivid depiction of daily life.", "The narrative should be logically structured and coherent.", "The response should cover all specified points, including setting, daily activities, interactions, and significant events."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
