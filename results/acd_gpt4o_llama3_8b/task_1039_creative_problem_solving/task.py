class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are stranded on a deserted island with only a magnifying glass, a rope, and a mirror. Devise a plan to signal for help and increase your chances of being rescued.",
                "solution": "The magnifying glass can be used to start a fire, which can create a smoke signal visible from afar. The mirror can be used to reflect sunlight and create a visual signal for passing planes or ships. The rope can be used to build a more stable structure for the fire or to create a makeshift flagpole for the mirror to catch sunlight more effectively." 
            },
            "2": {
                "scenario": "You have been tasked with designing a new type of playground equipment that encourages teamwork and creativity among children. Describe your invention and explain how it meets these goals.",
                "solution": "The invention is a giant interactive puzzle that can only be solved when multiple children work together. The puzzle pieces are large, colorful, and have different textures. Each piece requires a different type of interaction, such as pulling, rotating, or connecting with other pieces. The puzzle can have multiple levels of difficulty, encouraging creativity and problem-solving as children figure out how to assemble the pieces in different ways." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are presented with an unconventional scenario. Your task is to generate an innovative and practical solution that demonstrates creative and lateral thinking. Here is the scenario:

{t["scenario"]}

Your response should be detailed, clearly explaining your solution and the reasoning behind it. Submit your solution as a plain text string in the following format:

Solution: <your detailed solution>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should be innovative and practical.",
            "The solution should clearly explain the reasoning behind it.",
            "The solution should address all aspects of the scenario effectively."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
