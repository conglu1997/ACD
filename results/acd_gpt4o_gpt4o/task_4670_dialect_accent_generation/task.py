class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a dialogue in a Southern American English dialect. The dialogue should be between two friends discussing their weekend plans."},
            "2": {"prompt": "Generate a dialogue in a British Cockney accent. The dialogue should be between a shopkeeper and a customer discussing the price of vegetables."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        instructions = f"""Your task is to generate a dialogue based on the given prompt, using the specified dialect or accent. Ensure that the dialogue is realistic and captures the unique linguistic features of the dialect or accent.

{prompt}

Provide your response in the following format:

Dialogue: [Your dialogue here]

Example for Southern American English dialect:
Friend 1: Hey y'all, what're we plannin' for the weekend?
Friend 2: I reckon we could go fishin' down by the creek.
Friend 1: Sounds good to me. I'll bring the bait, you bring the cooler.

Example for British Cockney accent:
Shopkeeper: 'Ello gov'nor, what can I do ya for?
Customer: Just need some tomahhtoes and a loaf of bread.
Shopkeeper: Righto, that'll be two quid fifty.
Customer: Cheers, mate."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be realistic and coherent.",
            "The dialogue should capture the unique linguistic features of the specified dialect or accent.",
            "The dialogue should be engaging and contextually appropriate for the given prompt."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
