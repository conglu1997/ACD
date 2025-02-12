class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "The festival is set in a coastal village, celebrates the harvest season, and includes traditional music, dance, and food."
            },
            "2": {
                "criteria": "The festival is set in a mountainous region, celebrates the lunar new year, and includes lanterns, fireworks, and traditional games."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        criteria = t['criteria']
        return f"""Create a detailed description of a fictional cultural festival based on the following criteria:

Criteria: {criteria}

Your description should include:
1. The name of the festival.
2. A brief history of its origin.
3. Key activities and events that take place during the festival.
4. Descriptions of traditional music, dance, and food (or other specified elements).
5. The overall atmosphere and significance of the festival to the local community.

Ensure your description is creative, culturally plausible, and vividly detailed. Submit your description as a plain text string in the following format:

Festival Name: [Your Festival Name]
History: [Brief History]
Key Activities: [List of Activities]
Descriptions: [Music, Dance, Food, etc.]
Atmosphere and Significance: [Overall Atmosphere and Community Significance]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the name of the festival.",
            "The response should include a brief history of the festival.",
            "The response should describe key activities and events.",
            "The response should include descriptions of music, dance, and food (or other specified elements).",
            "The response should describe the overall atmosphere and significance to the community."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
