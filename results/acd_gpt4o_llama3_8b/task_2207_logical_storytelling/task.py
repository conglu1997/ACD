class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "A young scientist discovers a portal to another dimension in their basement. Describe the scientist's journey and the challenges they face in the other dimension.",
                "requirements": "The narrative should include the discovery of the portal, the scientist's initial exploration, at least three challenges they face, and a logical resolution."
            },
            "2": {
                "prompt": "A detective is on the trail of a notorious thief who has been stealing valuable artifacts from museums. Describe how the detective uncovers clues, solves puzzles, and ultimately catches the thief.",
                "requirements": "The narrative should include the initial crime scene, the detective's investigation process, at least three significant clues or puzzles, and a logical conclusion where the thief is caught."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        requirements = t["requirements"]
        return f"""Create a coherent and logical narrative based on the following prompt:\n\nPrompt: {prompt}\n\nRequirements: {requirements}\n\nEnsure that your story is engaging, logically consistent, and follows the given requirements. Submit your narrative as a plain text string in the following format: 'Story: [Your story]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be engaging and logically consistent.", "The narrative should follow the given requirements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
