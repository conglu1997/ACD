import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "phishing attacks",
            "password management",
            "social engineering",
            "data privacy",
            "insider threats"
        ]
        psychological_principles = [
            ("operant conditioning", "Learning through consequences of behavior"),
            ("social proof", "Influence of others' actions on individual behavior"),
            ("loss aversion", "Tendency to prefer avoiding losses over acquiring gains"),
            ("gamification", "Application of game-design elements in non-game contexts"),
            ("spaced repetition", "Learning technique that involves increasing intervals between reviews")
        ]
        
        tasks = {
            "1": {
                "scenario": random.choice(scenarios),
                "principle": random.choice(psychological_principles)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "principle": random.choice(psychological_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a gamified cybersecurity training system that addresses {t['scenario']} using the psychological principle of {t['principle'][0]} ({t['principle'][1]}). Your response should include:

1. Threat Analysis (200-250 words):
   a) Analyze the chosen cybersecurity threat and its impact on organizations.
   b) Discuss common vulnerabilities and attack vectors related to this threat.
   c) Explain why traditional training methods may be ineffective for this scenario.

2. Psychological Principle Application (250-300 words):
   a) Explain the chosen psychological principle and its relevance to learning and behavior change.
   b) Describe how you will incorporate this principle into your training system.
   c) Discuss potential challenges and benefits of using this approach in cybersecurity training.

3. Game Design (300-350 words):
   a) Outline the core gameplay mechanics and how they relate to the cybersecurity scenario.
   b) Describe the game's narrative or context that will engage participants.
   c) Explain the progression system and how it reinforces learning objectives.
   d) Detail how the game provides feedback and measures participant performance.
   e) Discuss how the game adapts to different skill levels and learning styles.

4. Technical Implementation (200-250 words):
   a) Propose a technical architecture for your gamified training system.
   b) Explain how you would ensure the security of the system itself.
   c) Discuss any integration challenges with existing organizational systems.

5. Effectiveness Evaluation (150-200 words):
   a) Propose methods to measure the effectiveness of your training system.
   b) Discuss how you would collect and analyze data on participant behavior change.
   c) Suggest ways to continuously improve the system based on feedback and results.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns related to your gamified training approach.
   b) Propose guidelines to ensure responsible use of behavioral psychology in cybersecurity training.
   c) Discuss how to balance engagement with the seriousness of cybersecurity threats.

Ensure your response demonstrates a deep understanding of cybersecurity, game design principles, and behavioral psychology. Be creative in your approach while maintaining practical applicability. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cybersecurity threat and psychological principle.",
            "The game design is creative, engaging, and effectively addresses the cybersecurity scenario.",
            "The technical implementation and evaluation methods are well-thought-out and feasible.",
            "Ethical considerations are thoroughly addressed and guidelines for responsible use are provided.",
            "The overall response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
