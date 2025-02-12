import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "historical_invention": "The printing press",
                "future_technology": "Quantum computing",
                "historical_period": "15th century Europe"
            },
            {
                "historical_invention": "The steam engine",
                "future_technology": "Artificial intelligence",
                "historical_period": "18th century Industrial Revolution"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reimagine {t['historical_invention']} from {t['historical_period']} using the advanced future technology of {t['future_technology']}. Then, analyze its potential impact on both the original time period and our current era. Your response should include:

1. Historical Context (150-200 words):
   a) Briefly describe {t['historical_invention']} and its significance in {t['historical_period']}.
   b) Explain the key technological principles behind the original invention.

2. Futuristic Reimagining (250-300 words):
   a) Describe your reimagined version of {t['historical_invention']} incorporating {t['future_technology']}.
   b) Explain how {t['future_technology']} enhances or transforms the original invention's capabilities.
   c) Discuss any novel features or functionalities in your reimagined design.

3. Technical Feasibility (200-250 words):
   a) Analyze the technical challenges of implementing your reimagined invention in {t['historical_period']}.
   b) Discuss how these challenges might be overcome using only knowledge and resources from that era.
   c) Explain any fundamental scientific principles that would need to be discovered earlier to make your invention possible.

4. Historical Impact Analysis (200-250 words):
   a) Hypothesize how your reimagined invention might have altered the course of history if introduced in {t['historical_period']}.
   b) Discuss potential societal, economic, and technological changes that could have resulted.
   c) Analyze any ethical implications or challenges that might have arisen.

5. Modern Era Implications (200-250 words):
   a) Explain how your reimagined historical invention might be relevant or applicable in our current era.
   b) Discuss any advantages it might have over existing modern technologies.
   c) Analyze potential impacts on contemporary society, economy, and technology.

6. Reflective Analysis (150-200 words):
   a) Compare the innovation processes of the original invention and your reimagined version.
   b) Discuss what this exercise reveals about the nature of technological progress and human creativity.
   c) Reflect on the importance of historical context in shaping technological development.

Ensure your response demonstrates a deep understanding of both historical and futuristic technologies. Use appropriate terminology and provide clear explanations where necessary. Be creative in your reimagining while maintaining scientific plausibility and historical accuracy. Your total response should be between 1150-1450 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the historical invention and the future technology.",
            "The reimagined invention creatively and plausibly incorporates the future technology into the historical context.",
            "The analysis of historical impact is well-reasoned and considers multiple aspects of society.",
            "The discussion of modern implications is insightful and relevant.",
            "The reflective analysis shows critical thinking about technological progress and innovation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
