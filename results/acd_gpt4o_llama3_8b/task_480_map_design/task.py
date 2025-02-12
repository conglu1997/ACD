class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "map_type": "fantasy world",
                "requirements": "Design a map of a fantasy world that includes at least three cities, two rivers, and one mountain range. The cities should be connected by roads, and the rivers should flow from the mountains to the sea. Include forests or deserts to add detail. Provide a brief description of each city, explaining its unique characteristics and role in the world."
            },
            "2": {
                "map_type": "theme park",
                "requirements": "Design a map of a theme park that includes at least five attractions, three food stalls, and two rest areas. The attractions should be labeled, and there should be pathways connecting all locations. Include thematic zones to add detail. Provide a brief description of each attraction, explaining its unique features and appeal."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a map based on the following requirements:

Map Type: {t['map_type']}
Requirements: {t['requirements']}

Ensure that your map is creative, adheres to the specified criteria, and includes all required elements. Provide labels for important locations and a brief description where requested. Submit your map as a plain text string in the following format:

For a fantasy world:
[Map Description]
City 1: [Description]
City 2: [Description]
City 3: [Description]

For a theme park:
[Map Description]
Attraction 1: [Description]
Attraction 2: [Description]
Attraction 3: [Description]
Attraction 4: [Description]
Attraction 5: [Description]

Make sure to follow the specified format exactly and provide a creative and coherent map."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The map should adhere to the specified criteria.",
            "The map should include all required elements.",
            "The map should be creative and coherent.",
            "The response should follow the specified format precisely.",
            "The descriptions should be relevant and accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
