class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Explain how the greenhouse effect works and its impact on global climate change.",
                "constraints": ["Use analogies from everyday life to make the explanation understandable to a non-expert audience.", "Include at least one reference to a historical scientific figure or discovery related to the topic."]
            },
            "2": {
                "phenomenon": "Describe the process of photosynthesis and its importance to ecosystems.",
                "constraints": ["Incorporate a fictional story about a plant to illustrate the process.", "Mention at least one modern scientific application or technology that utilizes knowledge of photosynthesis."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following scientific phenomenon in a creative and interdisciplinary manner:

Phenomenon: {t['phenomenon']}
Constraints:
{chr(10).join('- ' + constraint for constraint in t['constraints'])}

Your explanation should be creative, informative, and accessible to a non-expert audience. Use analogies, stories, and references to historical or modern scientific knowledge as required. Ensure your explanation is engaging and maintains the reader's interest. Submit your response as a plain text string in the following format:

Explanation: [Your creative explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be creative and accessible to a non-expert audience.",
            "The explanation should meet the specified phenomenon and constraints.",
            "The explanation should be informative and accurate.",
            "The explanation should incorporate interdisciplinary knowledge.",
            "The explanation should be engaging and maintain the reader's interest."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
