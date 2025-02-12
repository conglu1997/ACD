class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_scenario": "You are the captain of a spaceship on a mission to explore a distant planet. Suddenly, you receive a distress signal from a nearby asteroid field. The signal indicates that a civilian ship is in distress and needs immediate help. What do you do?",
                "followups": {
                    "rescue": "As you approach the asteroid field, you detect hostile alien ships surrounding the civilian ship. Do you engage them in combat or attempt to negotiate for the release of the civilian ship?",
                    "ignore": "You continue your mission towards the distant planet, but your ship's systems start malfunctioning, causing a loss of power in critical areas. Do you investigate the cause of the malfunctions or maintain your course towards the planet, hoping the issues will resolve?"
                }
            },
            "2": {
                "initial_scenario": "You are the mayor of a small town facing a severe drought. A proposal comes in to build a dam upstream to secure the water supply, but it will displace a nearby village of about 500 people. The dam is projected to solve the town's water issues for the next decade. What do you do?",
                "followups": {
                    "build": "The dam construction begins, but the displaced villagers' protests are intensifying, and media coverage is turning negative. Do you offer substantial compensation packages to the villagers or enforce the construction using legal and police measures?",
                    "reject": "The drought worsens, and water shortages become critical, leading to rationing and public unrest. Do you introduce strict water rationing measures and seek external aid from neighboring regions or launch a campaign to promote water conservation and look for alternative water sources?"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Navigate through the following evolving scenario by making decisions at each step. Your decisions should reflect careful consideration of the situation and its potential consequences. Here is the initial scenario:

{t['initial_scenario']}

Respond with your decision in the following format:
Decision: [Your choice]

You will receive a follow-up scenario based on your choice that you must also address."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The decision should logically follow from the scenario.",
            "The decision should demonstrate situational awareness and adaptability.",
            "The response should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
