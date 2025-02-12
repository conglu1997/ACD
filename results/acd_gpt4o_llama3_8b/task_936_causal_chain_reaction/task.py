class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_condition": "A cat knocks over a vase in a living room.", "actions": ["The vase falls off the table.", "The vase shatters on the floor.", "The noise wakes up the dog.", "The dog starts barking.", "The barking wakes up the baby."]},
            "2": {"initial_condition": "A tree branch breaks during a storm.", "actions": ["The branch falls on a power line.", "The power line snaps.", "The power goes out in the neighborhood.", "Traffic lights go out at an intersection.", "There is a car accident at the intersection."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Predict the outcomes of the following chain of events based on the initial condition provided:

Initial Condition: '{t["initial_condition"]}'

Actions:
1. {t["actions"][0]}
2. {t["actions"][1]}
3. {t["actions"][2]}
4. {t["actions"][3]}
5. {t["actions"][4]}

Your response should describe the logical outcomes of these actions in sequence, considering all potential consequences. Submit your prediction as a plain text string. Ensure that your response is logically coherent and realistic."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should logically follow from the initial condition and actions provided.",
            "The outcomes should be realistic and consider potential consequences of each action.",
            "The response should describe the outcomes in a coherent sequence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
