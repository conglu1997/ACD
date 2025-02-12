class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "case_description": "A homeowner finds that a tree from their neighbor's property has fallen onto their house during a storm. The homeowner wants to know if they can hold their neighbor liable for the damages.",
                "jurisdiction": "Common Law"
            },
            "2": {
                "case_description": "An employee was fired after posting critical comments about their company on social media. The employee claims that their freedom of speech has been violated and seeks legal advice.",
                "jurisdiction": "United States"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following legal scenario and provide a reasoned judgment or advice based on the relevant laws in the specified jurisdiction. Ensure that your response is coherent, logically sound, and grounded in legal principles.

Case Description:
{t['case_description']}

Jurisdiction:
{t['jurisdiction']}

Submit your response as a plain text string in the following format:

Judgment/Advice: [Your reasoned judgment or advice]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['jurisdiction'] == 'Common Law':
            criteria = [
                "The response should mention the concept of 'duty of care'.",
                "The response should discuss 'negligence' and 'reasonable foreseeability'.",
                "The response should be logically coherent and grounded in legal principles."
            ]
        else: # United States jurisdiction
            criteria = [
                "The response should reference the First Amendment and freedom of speech rights.",
                "The response should consider the limits of these rights in the context of employment.",
                "The response should be logically coherent and grounded in legal principles."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0