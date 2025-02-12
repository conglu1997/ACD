class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the incident commander at a wildfire emergency. The fire is spreading rapidly towards a residential area. You have limited resources and must decide how to allocate them to maximize safety and minimize damage. New information will be provided at intervals, and you must adjust your decisions accordingly.",
                "initial_info": "The fire is currently 3 miles from the nearest homes. You have 3 fire trucks, 2 water tankers, and a team of 20 firefighters. The wind is blowing towards the residential area at 10 mph.",
                "follow_up_info": "The wind speed has increased to 20 mph, and the fire is now 1.5 miles from the homes. Additional resources: 1 fire truck and 10 firefighters have arrived."
            },
            "2": {
                "scenario": "You are the emergency coordinator at a chemical spill incident. Hazardous chemicals have leaked from a tanker truck on a busy highway. You need to manage the evacuation of nearby areas, coordinate with emergency services, and contain the spill. New information will be provided at intervals, and you must adjust your decisions accordingly.",
                "initial_info": "The spill is located at the intersection of Highway 50 and Main Street. There is a residential neighborhood half a mile away and a school within a mile. You have 4 hazmat teams, 3 ambulances, and a team of 10 police officers.",
                "follow_up_info": "The wind direction has changed, pushing the chemical fumes towards the residential neighborhood. Additional resources: 2 hazmat teams and 2 ambulances have arrived."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with managing an emergency scenario. You will receive evolving information, and you must make real-time decisions based on this information. Your goal is to maximize safety and minimize damage.

Scenario: {t['scenario']}

Initial Information: {t['initial_info']}

Submit your initial plan, and be prepared to adjust it as new information is provided. Your response should include:
1. Your initial plan based on the given information.
2. Adjustments to your plan as new information is provided.

Submit your response as a plain text string in the following format:
- Initial Plan: [Your initial plan]
- Adjusted Plan: [Your adjustments based on new information]

Ensure that your responses are coherent, logical, and demonstrate an understanding of the evolving situation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The initial plan should be coherent and based on the given information.",
            "Adjustments to the plan should be logical and based on the new information provided.",
            "The response should demonstrate an understanding of the evolving situation and the need to adapt.",
            "The plan should aim to maximize safety and minimize damage.",
            "The response should be well-structured and clearly communicated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
