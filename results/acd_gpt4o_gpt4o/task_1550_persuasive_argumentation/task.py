class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are running for student body president. Craft a persuasive argument to convince your peers to vote for you, focusing on your leadership qualities and vision for the school.", "sample_argument": "Voting for me as your student body president will ensure that every student's voice is heard. My leadership experience as class president for the past two years has equipped me with the skills necessary to represent you effectively. I plan to implement more extracurricular activities and ensure that the school environment is inclusive and welcoming for all."},
            "2": {"scenario": "A local community is deciding whether to build a new public park. Create a persuasive argument in favor of building the park, highlighting the benefits to the community.", "sample_argument": "Building a new public park will provide a safe and green space for families to enjoy outdoor activities. It will promote community wellness, foster social interactions, and increase property values in the area. The park will also serve as a venue for community events, bringing residents together."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        sample_argument = t["sample_argument"]
        instructions = f"""Your task involves two parts:\n\n1. Persuasive Argument Generation: Craft a persuasive argument for the following scenario:\n\nScenario: {scenario}\n\n2. Argument Critique: Critically evaluate the following argument:\n\nArgument: {sample_argument}\n\nYour persuasive argument should be compelling, well-structured, and make effective use of rhetorical strategies. Your critique should identify strengths and weaknesses in the provided argument, and suggest improvements where applicable.\n\nResponse Format:\nPersuasive Argument: <Your argument>\nArgument Critique: <Your critique>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The persuasive argument should be compelling, well-structured, and relevant to the scenario.",
            "The argument should make effective use of rhetorical strategies such as ethos, pathos, and logos.",
            "The critique should accurately identify strengths and weaknesses of the provided argument.",
            "The critique should suggest reasonable improvements where applicable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
