import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_issues = [
            {
                "issue": "Climate Change",
                "description": "Design a game that raises awareness and promotes action on climate change."
            },
            {
                "issue": "Income Inequality",
                "description": "Create a game that illustrates the challenges of income inequality and encourages players to think about solutions."
            },
            {
                "issue": "Mental Health Stigma",
                "description": "Develop a game that addresses mental health stigma and promotes understanding and empathy."
            },
            {
                "issue": "Racial Discrimination",
                "description": "Design a game that explores the impacts of racial discrimination and encourages players to challenge their biases."
            }
        ]
        return {str(i+1): issue for i, issue in enumerate(random.sample(social_issues, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a game that addresses the social issue of {t['issue']} through gamification. {t['description']}

Gamification in this context means applying game-design elements and game principles to non-game contexts, specifically to address and raise awareness about social issues.

Your task is to:

1. Game Concept (100-150 words):
   Provide an overview of your game, including its genre, basic mechanics, and how it relates to the social issue. Specify the target audience for your game and explain why you chose this demographic.

2. Psychological Principles (100-150 words):
   Explain how your game incorporates at least two psychological principles (e.g., cognitive dissonance, social proof, framing effect) to influence player behavior or understanding.

3. Sociological Theories (100-150 words):
   Describe how your game design reflects at least two sociological theories or concepts (e.g., social constructionism, conflict theory, symbolic interactionism) relevant to the social issue.

4. Game Mechanics (150-200 words):
   Detail the core game mechanics, including how players interact with the game and how these interactions relate to the social issue. Explain how these mechanics reinforce the psychological principles and sociological theories you've incorporated.

5. Impact Measurement (100-150 words):
   Propose a method to measure the real-world impact of your game on players' understanding of or behavior related to the social issue. Include at least one quantitative and one qualitative measure.

Ensure your game design is engaging, educational, and has the potential to create meaningful impact on the chosen social issue. Strive to balance entertainment value with educational content and social impact. Your response should demonstrate a deep understanding of game design principles, psychology, sociology, and the complexities of the social issue.

Format your response using clear headings for each section. Your total response should be between 600-800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The game concept effectively addresses the social issue of {t['issue']}",
            "The design incorporates at least two relevant psychological principles",
            "The game reflects at least two applicable sociological theories or concepts",
            "The game mechanics are well-explained and reinforce the psychological and sociological elements",
            "The proposed impact measurement includes both quantitative and qualitative measures",
            "The overall game design is creative, engaging, and balances entertainment with educational content",
            "The response specifies a target audience and justifies the choice",
            "The response demonstrates a deep understanding of game design, psychology, sociology, and the social issue",
            "The response follows the specified format and is within the 600-800 word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
