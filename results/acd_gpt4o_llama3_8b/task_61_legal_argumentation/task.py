class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A person is accused of stealing a valuable painting from an art gallery. The painting was last seen at the gallery at 10 PM, and the accused was seen leaving the gallery at 10:15 PM with a large bag. Security footage shows the accused near the painting at 9:50 PM. No other individuals were seen near the painting between 10 PM and 10:15 PM. The accused claims that they were simply carrying their own belongings in the bag and had no intention of stealing the painting.",
                "instructions": "Based on the above scenario, generate legal arguments for both the prosecution and the defense. Ensure that your arguments are well-reasoned, logically structured, and use appropriate legal terminology. Submit your response as a plain text string with clearly labeled sections for Prosecution Argument and Defense Argument."
            },
            "2": {
                "scenario": "A person is accused of causing a car accident by running a red light. The accident occurred at an intersection with multiple witnesses. One witness claims to have seen the accused's car enter the intersection after the light turned red. Another witness claims that the accused's car was already in the intersection when the light turned red. The accused claims that they entered the intersection while the light was still yellow.",
                "instructions": "Based on the above scenario, generate legal arguments for both the prosecution and the defense. Ensure that your arguments are well-reasoned, logically structured, and use appropriate legal terminology. Submit your response as a plain text string with clearly labeled sections for Prosecution Argument and Defense Argument."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following legal scenario, generate legal arguments for both the prosecution and the defense. Ensure that your arguments are well-reasoned, logically structured, and use appropriate legal terminology. Submit your response as a plain text string with clearly labeled sections for Prosecution Argument and Defense Argument. Here is the scenario:

{t["scenario"]}

"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a well-reasoned argument for the prosecution.",
            "The response should include a well-reasoned argument for the defense.",
            "The arguments should be logically structured and use appropriate legal terminology."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
