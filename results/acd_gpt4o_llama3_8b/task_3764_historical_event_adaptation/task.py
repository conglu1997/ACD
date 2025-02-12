class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776, where representatives from the Thirteen Colonies gathered to declare their independence from British rule. The event was marked by the signing of a formal document, the Declaration of Independence, which outlined the colonies' grievances and articulated their right to self-governance.", "new_context": "a futuristic space colony"},
            "2": {"event": "The fall of the Berlin Wall in 1989, symbolizing the end of the Cold War and the reunification of East and West Germany. The Wall, which had divided Berlin for 28 years, was dismantled by jubilant crowds, leading to the collapse of communist regimes in Eastern Europe.", "new_context": "a medieval kingdom"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Adapt the following historical event to a different cultural or technological context. Maintain the core elements of the event, but make it plausible in the new setting. Ensure that the adapted narrative is coherent, culturally appropriate, and creatively integrates the specified context.

Historical Event: {t['event']}
New Context: {t['new_context']}

Submit your adapted narrative as a plain text string.

Example:
Original Event: The signing of the Declaration of Independence in 1776, where representatives from the Thirteen Colonies gathered to declare their independence from British rule. The event was marked by the signing of a formal document, the Declaration of Independence, which outlined the colonies' grievances and articulated their right to self-governance.
New Context: a futuristic space colony
Adapted Narrative: In the year 2176, on the space colony of New Earth, the leaders of the colony gathered to sign the Declaration of Autonomy, declaring their independence from Earth's central government. The holographic document, projected in the main hall of the Colony Administration Building, was signed by representatives from various colony sectors, marking the beginning of a new era of self-governance and freedom."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The adapted narrative should maintain the core elements of the original historical event.",
            "The narrative should be coherent and culturally appropriate for the new context.",
            "The adaptation should creatively integrate the new cultural or technological context.",
            "The narrative should be plausible within the specified new setting.",
            "The adaptation should maintain historical accuracy in terms of the core elements of the event."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
