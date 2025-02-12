import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Aztec",
                "time_period": "Pre-Columbian era",
                "key_practice": "Human sacrifice"
            },
            {
                "name": "Victorian England",
                "time_period": "19th century",
                "key_practice": "Strict social etiquette"
            },
            {
                "name": "Digital Nomads",
                "time_period": "21st century",
                "key_practice": "Location-independent work"
            },
            {
                "name": "Ancient Sparta",
                "time_period": "Ancient Greece",
                "key_practice": "Military-focused education"
            },
            {
                "name": "Cyberpunk society",
                "time_period": "Near future",
                "key_practice": "Biohacking"
            }
        ]
        return {
            "1": random.choice(cultures),
            "2": random.choice(cultures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to simulate the evolution of cultural practices and beliefs for the {t['name']} culture, focusing on the key practice of {t['key_practice']} during the {t['time_period']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system for simulating cultural evolution.
   b) Explain how your system models cultural practices, beliefs, and their interactions.
   c) Detail how environmental factors, technological advancements, and inter-cultural interactions are incorporated into the simulation.

2. Cultural Analysis (200-250 words):
   a) Analyze the significance of {t['key_practice']} in {t['name']} culture during the {t['time_period']}.
   b) Identify key factors that might influence the evolution of this practice over time.
   c) Discuss potential trajectories for how this practice might evolve in different scenarios.

3. Simulation Process (200-250 words):
   a) Describe how your AI system would simulate the evolution of {t['key_practice']} over several generations.
   b) Explain how your system handles the interplay between individual beliefs and collective cultural norms.
   c) Discuss how your simulation accounts for historical events or technological advancements relevant to the {t['time_period']}.

4. Data and Machine Learning Approach (150-200 words):
   a) Specify the types of data your system would use to model {t['name']} culture and {t['key_practice']}.
   b) Describe the machine learning techniques your system would employ to predict cultural evolution.
   c) Explain how your system would validate its predictions against historical data, if available.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of simulating cultural evolution, particularly for {t['name']} culture.
   b) Address concerns about cultural sensitivity and the risk of oversimplification in your model.
   c) Propose guidelines for the responsible development and use of cultural evolution AI systems.

Ensure your response demonstrates a deep understanding of cultural anthropology, artificial intelligence, and complex systems modeling. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cultural evolution and AI systems.",
            "The proposed system architecture is well-designed and incorporates relevant factors for cultural simulation.",
            "The cultural analysis shows depth of understanding and consideration of multiple influencing factors.",
            "The simulation process is clearly explained and accounts for complex interactions between cultural elements.",
            "The data and machine learning approach is appropriate and well-justified.",
            "Ethical considerations are thoroughly addressed with thoughtful guidelines proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
