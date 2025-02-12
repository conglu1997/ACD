class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create an interactive story where the reader is a detective solving a mystery. The story should have at least 3 decision points, each with 2 choices, leading to different outcomes.",
                "requirements": "Ensure the story is engaging, logically consistent, and each choice leads to a unique but coherent narrative path."
            },
            "2": {
                "prompt": "Create an interactive story where the reader is an explorer discovering a hidden treasure. The story should have at least 3 decision points, each with 2 choices, leading to different outcomes.",
                "requirements": "Ensure the story is engaging, logically consistent, and each choice leads to a unique but coherent narrative path."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an interactive story based on the following prompt:\n\n{t['prompt']}\n\n{t['requirements']}\n\nSubmit your interactive story as a plain text string, clearly marking the decision points and the choices available at each point. Ensure that the narrative is engaging, logically consistent, and each choice leads to a unique but coherent narrative path.\n\nFormat:\nDecision Point 1:\nChoice A: [Text for choice A]\nChoice B: [Text for choice B]\n\nDecision Point 2 (if Choice A was selected):\nChoice A: [Text for choice AA]\nChoice B: [Text for choice AB]\n\nDecision Point 2 (if Choice B was selected):\nChoice A: [Text for choice BA]\nChoice B: [Text for choice BB]\n\n...\n\nExample:\nDecision Point 1:\nChoice A: The detective decides to question the butler.\nChoice B: The detective decides to search the library.\n\nDecision Point 2 (if Choice A was selected):\nChoice A: The butler reveals a crucial clue.\nChoice B: The butler is evasive and unhelpful.\n\nDecision Point 2 (if Choice B was selected):\nChoice A: The detective finds a hidden diary in the library.\nChoice B: The detective finds nothing of interest in the library.\n\n..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interactive story should have at least 3 decision points, each with 2 choices.",
            "The narrative should be engaging and logically consistent.",
            "Each choice should lead to a unique but coherent narrative path.",
            "The format should match the specified structure.",
            "The story should contain no logical inconsistencies or plot holes."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
