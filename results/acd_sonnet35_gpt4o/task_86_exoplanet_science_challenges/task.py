import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        planet_properties = [
            {
                "name": "Zephyria",
                "unique_property": "Atmosphere composed primarily of helium, with trace amounts of exotic particles",
                "challenge": "Propose a method for humans to communicate long-distance on this planet, given that sound waves behave differently in a helium-rich atmosphere."
            },
            {
                "name": "Chronos",
                "unique_property": "Extreme time dilation effects due to proximity to a massive black hole",
                "challenge": "Design a sustainable food production system for a colony on this planet, considering the time dilation effects on plant growth and human metabolism."
            },
            {
                "name": "Magnetar",
                "unique_property": "Incredibly strong and constantly shifting magnetic fields",
                "challenge": "Develop a transportation system for the planet's inhabitants that can function reliably despite the intense and unpredictable magnetic fields."
            }
        ]
        return {str(i+1): planet for i, planet in enumerate(random.sample(planet_properties, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a scientist tasked with solving challenges on the fictional exoplanet {t['name']}. This planet has the following unique property: {t['unique_property']}.

Your challenge is to: {t['challenge']}

Provide a detailed response that includes:

1. A brief explanation of the scientific principles relevant to the planet's unique property and the challenge (2-3 sentences).

2. Your proposed solution to the challenge, including any necessary technologies or adaptations (4-5 sentences).

3. An analysis of potential obstacles or limitations to your solution and how they might be overcome (2-3 sentences).

4. A discussion of how your solution might impact the planet's ecosystem or the lives of its inhabitants (2-3 sentences).

5. One potential area of scientific research or technological development that could be advanced by studying or implementing your solution (2-3 sentences).

Ensure your response is grounded in real scientific principles while demonstrating creativity in applying these principles to the unique conditions of the exoplanet. Your total response should not exceed 400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific challenge related to {t['name']} and its unique property",
            "The solution should be grounded in real scientific principles and demonstrate understanding of relevant physics, biology, or other scientific fields",
            "The proposed solution should be creative and tailored to the unique conditions of the exoplanet",
            "The response should include a thoughtful analysis of potential obstacles and their solutions",
            "The discussion of ecosystem or inhabitant impact should be logical and consider multiple factors",
            "The suggested area of scientific research or technological development should be relevant and potentially impactful",
            "The response should be well-organized and clearly communicate complex scientific ideas",
            "The total response should not exceed 400 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
