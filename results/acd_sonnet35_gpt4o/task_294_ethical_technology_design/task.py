import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "global_issue": "Climate Change",
                "technology_type": "Atmospheric Carbon Capture"
            },
            {
                "global_issue": "Food Insecurity",
                "technology_type": "Vertical Farming"
            },
            {
                "global_issue": "Infectious Disease Outbreaks",
                "technology_type": "AI-Powered Early Warning System"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical technology to address the global issue of {t['global_issue']} using {t['technology_type']}. Your task is to:

1. Technology Design (250-300 words):
   - Describe the core functioning of your proposed technology.
   - Explain how it addresses the given global issue.
   - Discuss the scientific or engineering principles underlying its operation.
   - Cite at least one relevant scientific principle or study to support your design.

2. Potential Negative Consequences (200-250 words):
   - Identify at least three potential negative consequences or ethical concerns arising from the widespread adoption of this technology.
   - Analyze how these consequences might impact different societal groups or stakeholders.

3. Safeguards and Mitigation Strategies (200-250 words):
   - Propose specific safeguards or regulations to mitigate each of the identified negative consequences.
   - Explain the rationale behind each safeguard and how it would be implemented.

4. Future Implications (150-200 words):
   - Discuss how this technology might evolve over the next 50 years.
   - Explore potential long-term societal changes resulting from its adoption.

Ensure your response is well-structured, using clear headings for each section. Your analysis should be creative yet grounded in scientific and ethical principles, demonstrating a deep understanding of the complex interplay between technology and society.

Your total response should be between 800-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the global issue of {t['global_issue']} using {t['technology_type']}",
            "The technology design should be innovative, scientifically grounded, and clearly explained",
            "At least one relevant scientific principle or study must be cited in the technology design section",
            "At least three potential negative consequences must be identified and analyzed",
            "Safeguards and mitigation strategies should be specific, feasible, and well-reasoned",
            "The future implications section should demonstrate foresight and consideration of long-term societal impacts",
            "The overall response should show a balance between creativity and practical, ethical considerations",
            "All four sections (Technology Design, Potential Negative Consequences, Safeguards and Mitigation Strategies, and Future Implications) must be adequately addressed",
            "The response should be between 800-1000 words in total"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
