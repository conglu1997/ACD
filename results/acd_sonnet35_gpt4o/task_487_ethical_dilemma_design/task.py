import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        professions = [
            "Artificial Intelligence Researcher",
            "Environmental Scientist",
            "Genetic Engineer",
            "Investigative Journalist",
            "Corporate Executive",
            "Public Health Official",
            "Space Exploration Engineer",
            "Education Technology Developer"
        ]
        ethical_principles = [
            "Autonomy",
            "Beneficence",
            "Non-maleficence",
            "Justice",
            "Privacy",
            "Transparency",
            "Sustainability",
            "Dignity"
        ]
        
        tasks = {}
        for i in range(2):
            profession = random.choice(professions)
            principle1, principle2 = random.sample(ethical_principles, 2)
            tasks[str(i+1)] = {
                "profession": profession,
                "principle1": principle1,
                "principle2": principle2
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fictional ethical dilemma for a {t['profession']} that involves a conflict between the ethical principles of {t['principle1']} and {t['principle2']}. Then, analyze the dilemma and propose potential solutions. Provide your response in the following format:

1. Dilemma Description (100-150 words):
   Present a detailed scenario that creates a genuine ethical conflict for the {t['profession']}. Ensure the dilemma clearly involves tension between {t['principle1']} and {t['principle2']}.

2. Ethical Analysis (200-250 words):
   a) Explain how the scenario creates conflict between {t['principle1']} and {t['principle2']}.
   b) Discuss the potential consequences of prioritizing one principle over the other.
   c) Analyze any relevant professional codes of ethics or legal considerations.

3. Potential Solutions (200-250 words):
   Propose two distinct approaches to resolving the dilemma:
   a) Solution 1: [Brief description]
      - Ethical justification
      - Potential positive and negative outcomes
   b) Solution 2: [Brief description]
      - Ethical justification
      - Potential positive and negative outcomes

4. Reflection (100-150 words):
   Discuss the broader implications of this dilemma for the profession and society. Consider how emerging technologies or social changes might affect similar ethical conflicts in the future.

Ensure your response demonstrates a deep understanding of the ethical principles involved, the specific challenges of the profession, and the complexity of real-world ethical decision-making. Be creative in your scenario design while maintaining plausibility and relevance to current or near-future professional contexts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed, plausible ethical dilemma specific to the given profession",
            f"The ethical analysis clearly explains the conflict between {t['principle1']} and {t['principle2']}",
            "Two distinct, well-justified solutions are proposed with thoughtful consideration of their implications",
            "The reflection demonstrates an understanding of broader societal and future implications",
            "The overall response shows creativity, critical thinking, and effective communication of complex ethical concepts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
