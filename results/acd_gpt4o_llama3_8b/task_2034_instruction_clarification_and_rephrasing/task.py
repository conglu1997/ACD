class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "clarify", "instructions": "To perform a factory reset on the device, first disconnect all peripheral devices. Then, press and hold the power button for 10 seconds. Upon release, immediately press the reset button located on the bottom panel. Wait for the indicator light to flash three times, signaling that the reset process has begun."},
            "2": {"task": "rephrase", "instructions": "The procedure for calibrating the machine involves several steps. Begin by ensuring the machine is powered off. Next, access the control panel and navigate to the settings menu. Select the 'Calibration' option, and follow the on-screen prompts. Once calibration is complete, verify the settings by running a test operation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "clarify":
            return f"Clarify the following instructions to make them understandable to someone who is not familiar with technical jargon. Submit your response as a plain text string.\n\nInstructions: {t['instructions']}"
        elif t["task"] == "rephrase":
            return f"Rephrase the following instructions to make them clearer and easier to follow. Submit your response as a plain text string.\n\nInstructions: {t['instructions']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
