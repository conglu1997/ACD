class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "thunderstorm",
                "scientific_details": [
                    "A thunderstorm is a storm with thunder and lightning.",
                    "It is produced by cumulonimbus clouds.",
                    "Thunderstorms can produce strong winds, heavy rain, and sometimes hail."
                ]
            },
            "2": {
                "phenomenon": "coral reef",
                "scientific_details": [
                    "A coral reef is an underwater ecosystem characterized by reef-building corals.",
                    "Reefs are formed of colonies of coral polyps held together by calcium carbonate.",
                    "They are home to a diverse array of marine life."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a description of the following natural phenomenon that is both scientifically accurate and artistically appealing. Your description should integrate the provided scientific details in a way that is evocative and engaging.

Natural Phenomenon: {t['phenomenon']}

Scientific Details:
{chr(10).join('- ' + detail for detail in t['scientific_details'])}

Your response should be a well-crafted paragraph that paints a vivid picture of the phenomenon while accurately conveying the scientific information. Submit your response as a plain text string in the following format:

Description: [Your detailed description here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should be scientifically accurate.",
            "The description should be artistically appealing and evocative.",
            "The scientific details provided should be integrated into the description.",
            "The description should paint a vivid picture of the phenomenon."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
