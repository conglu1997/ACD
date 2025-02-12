class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "In July 1969, a significant event took place involving a spacecraft named Apollo 11. The event was widely covered by media and marked a major milestone in space exploration. However, details about the specific achievements, key figures involved, and the broader impact of the event are missing. Reconstruct the historical event, including the main achievements, key individuals, and its significance in the context of space exploration.",
                "solution": "The event is the Apollo 11 Moon landing. On July 20, 1969, Apollo 11 successfully landed the first humans on the Moon. Astronauts Neil Armstrong and Buzz Aldrin walked on the lunar surface, while Michael Collins orbited above in the command module. This event marked a significant achievement in space exploration, demonstrating the capabilities of human space travel and fulfilling President Kennedy's goal of landing a man on the Moon by the end of the 1960s." 
            },
            "2": {
                "data": "In November 1989, a major geopolitical event occurred in Europe, involving the tearing down of a structure that had divided a city for decades. The event symbolized the end of a significant political era and led to the reunification of a country. However, details about the structure, the city, and the broader political implications are missing. Reconstruct the historical event, including the key details about the structure, the city, and its political significance.",
                "solution": "The event is the fall of the Berlin Wall. In November 1989, the Berlin Wall, which had divided East and West Berlin since 1961, was torn down. This event symbolized the end of the Cold War and led to the reunification of Germany. The fall of the Berlin Wall marked the collapse of communist regimes in Eastern Europe and the eventual dissolution of the Soviet Union." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reconstruct the historical event from the given fragmented or partially provided information. Ensure that your reconstruction includes the main achievements, key individuals involved, and the broader significance of the event in its historical context. Here is the information:

{t["data"]}

Submit your response as a plain text string in the following format:

Event: [Your reconstructed event]
Details: [Details of the achievements, key figures, and significance]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The event reconstruction should include the main achievements.",
            "The event reconstruction should mention key individuals involved.",
            "The event reconstruction should highlight the broader significance of the event in its historical context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
