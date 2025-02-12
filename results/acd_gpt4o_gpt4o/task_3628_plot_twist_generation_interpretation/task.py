class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_narrative": "Once upon a time in a small village, there lived a young girl named Lily. Lily loved exploring the forest near her home. One day, she found a mysterious old box hidden beneath a fallen tree. Inside the box, she discovered a map leading to a hidden treasure.", "twist_instructions": "Add a plot twist to the narrative that introduces a surprising element but maintains coherence with the initial setup."},
            "2": {"initial_narrative": "In the bustling city of Metropolis, detective John was known for his impeccable record in solving the most challenging cases. One rainy night, he received an anonymous tip about a planned heist at the city museum. John immediately set out to investigate, unaware of the danger that awaited him.", "twist_instructions": "Add a plot twist to the narrative that introduces an unexpected turn of events but keeps the storyline coherent."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_narrative = t["initial_narrative"]
        twist_instructions = t["twist_instructions"]
        instructions = f"""Your task involves two parts:\n\n1. Plot Twist Generation: Read the initial narrative provided below and then generate a plot twist that introduces a surprising element while maintaining narrative coherence.\n\nInitial Narrative: {initial_narrative}\n\n{twist_instructions}\n\n2. Plot Twist Interpretation: Explain how your plot twist fits into the story and enhances the narrative.\n\nResponse Format:\nGenerated Plot Twist: <Your plot twist>\nExplanation: <Your explanation>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plot twist should be surprising and unexpected.",
            "The plot twist should maintain coherence with the initial narrative.",
            "The explanation should clearly justify how the plot twist fits into the story and enhances the narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
