class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"traits": ["narcissistic", "charismatic"]},
            "2": {"traits": ["introverted", "meticulous"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        traits = ', '.join(t["traits"])
        return f"""Create a fictional character with the following psychological traits: {traits}. Describe a scenario that showcases these traits in action. The description should include:
1. A brief background of the character.
2. A detailed description of the character's personality and behavior.
3. A scenario that highlights how these traits manifest in the character's actions and decisions.
4. The impact of the character's traits on the scenario's outcome.

Ensure that the character is well-developed, the scenario is engaging, and the traits are clearly illustrated. Submit your response as a plain text string in the following format:

Character Background: [Your character's background]
Personality and Behavior: [Detailed description of personality and behavior]
Scenario: [Description of the scenario]
Impact: [Impact of the traits on the scenario's outcome]

Example:
Character Background: John Doe grew up in a small town, always seeking attention and admiration from those around him. His charm and good looks quickly made him popular among his peers.
Personality and Behavior: John is narcissistic and charismatic. He often manipulates situations to be the center of attention and uses his charm to influence others.
Scenario: At a high school reunion, John makes a grand entrance, capturing everyone's attention. He starts telling exaggerated stories of his success, ensuring he remains in the spotlight.
Impact: John's narcissism leads him to dominate conversations, making others feel overshadowed. His charisma, however, keeps people engaged despite his self-centered behavior."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The character should have a well-developed background.",
            "The character's personality and behavior should be described in detail.",
            "The scenario should clearly showcase the specified traits.",
            "The impact of the traits on the scenario's outcome should be explained.",
            "The narrative should be coherent and engaging.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
