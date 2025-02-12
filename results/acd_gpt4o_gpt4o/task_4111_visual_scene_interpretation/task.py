class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scene_description": "A park with children playing, people walking dogs, and a fountain in the center. There are trees around and some benches where people are sitting."},
            "2": {"scene_description": "A busy street market with vendors selling fruits and vegetables, people browsing the stalls, and a musician playing a guitar. There are colorful umbrellas over the stalls and a street food cart nearby."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scene_description = t["scene_description"]
        instructions = f"""Your task is to interpret the following detailed description of a visual scene and generate a narrative or explanation based on it:

{scene_description}

Provide your response in the following format:

Narrative: [Your narrative or explanation]

Example:
Scene Description: A beach with people sunbathing, children building sandcastles, and seagulls flying overhead. There are beach umbrellas and a lifeguard tower in the background.
Narrative: The beach was bustling with activity. Families gathered near the shore, with children eagerly building sandcastles while their parents relaxed under colorful umbrellas. Seagulls soared above, occasionally landing to inspect the sandy terrain. In the distance, the lifeguard tower stood as a reminder of safety and vigilance."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be coherent and logically follow the scene description.",
            "The narrative should capture the key elements described in the scene.",
            "The narrative should be vivid and engaging, providing a clear mental image of the scene."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
