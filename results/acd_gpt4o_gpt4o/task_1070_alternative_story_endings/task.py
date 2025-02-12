class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_story": "Little Red Riding Hood",
                "summary": "Little Red Riding Hood goes to visit her grandmother, but encounters a wolf who disguises himself as her grandmother and tries to eat her."
            },
            "2": {
                "original_story": "The Three Little Pigs",
                "summary": "Three little pigs build houses of straw, sticks, and bricks. A wolf blows down the first two houses but fails to blow down the brick house."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to create an alternative ending for the following classic story based on the given summary:\n\nOriginal Story: {t['original_story']}\nSummary: {t['summary']}\n\nYour alternative ending should adhere to the following guidelines:\n1. Maintain coherence with the original plot and characters.\n2. Be imaginative and provide a unique twist or change to the ending.\n3. Ensure the new ending is logical and fits within the context of the story.\n\nProvide your response in plain text format.\n\nExample Response:\nFor Little Red Riding Hood: 'Instead of being eaten by the wolf, Little Red Riding Hood realizes something is off and cleverly tricks the wolf into revealing his true identity. She then manages to escape and warn the villagers, who capture the wolf and ensure the safety of the forest.'"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new ending maintains coherence with the original plot and characters.",
            "The new ending is imaginative and provides a unique twist.",
            "The new ending is logical and fits within the context of the story."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
