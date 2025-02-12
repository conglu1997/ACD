class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "observations": [
                    "A group of plants exposed to a specific type of music seem to grow faster than those that are not.",
                    "The music played has a rhythmic pattern with a frequency of 440 Hz.",
                    "Plants exposed to other types of music do not show the same growth rate.",
                    "The experiment was conducted in a controlled environment with equal water, light, and soil conditions."
                ],
                "background": "Music has been known to affect plant growth, but the mechanisms are not well understood. Some studies suggest that sound waves can stimulate plant cells in various ways."
            },
            "2": {
                "observations": [
                    "A new species of bacteria was found thriving in a highly acidic environment in a remote cave.",
                    "The bacteria exhibit unique metabolic processes that are not observed in other known species.",
                    "The cave environment is rich in sulfur compounds.",
                    "The bacteria seem to convert sulfur compounds into energy."
                ],
                "background": "Extreme environments often harbor unique life forms with specialized adaptations. Sulfur-metabolizing bacteria are known in volcanic vents, but this specific metabolic pathway is novel." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        observations = "\n".join(f"- {observation}" for observation in t["observations"])
        background = t["background"]
        return f"""Based on the given observations and background information, generate a plausible scientific hypothesis. Your hypothesis should explain the underlying mechanisms or relationships between the observations. Ensure that your hypothesis is scientifically grounded and creative. Here are the observations:\n{observations}\n\nBackground Information:\n{background}\n\nSubmit your hypothesis as a plain text string in the following format: 'Hypothesis: [Your hypothesis]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The hypothesis should be scientifically plausible.", "The hypothesis should creatively explain the observations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
