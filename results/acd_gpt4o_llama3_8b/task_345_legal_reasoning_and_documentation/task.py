class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A client is facing charges of theft for allegedly taking merchandise from a store without paying. They claim it was an honest mistake and they intended to pay but got distracted. Generate a legal defense argument for the client, including relevant legal principles and potential defenses.",
            },
            "2": {
                "scenario": "A small business owner wants to draft a non-compete agreement for their employees to prevent them from working with competitors for a certain period after leaving the company. Generate a draft of the non-compete agreement, including key clauses and legal considerations.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario:
{t['scenario']}

Your response should include the following sections:
1. Legal Principles: Outline the relevant legal principles or laws applicable to the scenario.
2. Argument/Document: Provide the legal argument or draft the legal document as specified in the scenario.
3. Additional Considerations: Include any additional legal considerations or advice that could be relevant to the client or situation.

Ensure that your response is detailed, clear, logical, and demonstrates a thorough understanding of legal reasoning and documentation. Provide enough detail in each section to show a deep comprehension of the scenario and applicable laws. Each section should be clearly labeled and well-organized. Submit your response as a plain text string.

Example response format:

Legal Principles:
- Principle 1: Description...
- Principle 2: Description...

Argument/Document:
- Introduction:...
- Main Points:...
- Conclusion:...

Additional Considerations:
- Consideration 1:...
- Consideration 2:...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The legal principles should be accurately outlined and relevant to the scenario.",
            "The legal argument or document should be clear, logical, and well-structured.",
            "Additional considerations should be relevant and provide useful legal advice.",
            "Each section should be clearly labeled and well-organized."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
