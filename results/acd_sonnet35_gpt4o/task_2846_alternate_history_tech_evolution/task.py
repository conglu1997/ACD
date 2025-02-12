import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "civilization": "Ancient Egypt",
                "tech_discovery": "Electricity",
                "historical_period": "Old Kingdom"
            },
            {
                "civilization": "Roman Empire",
                "tech_discovery": "Steam Engine",
                "historical_period": "Pax Romana"
            },
            {
                "civilization": "Aztec Empire",
                "tech_discovery": "Gunpowder",
                "historical_period": "Pre-Columbian era"
            },
            {
                "civilization": "Song Dynasty China",
                "tech_discovery": "Artificial Intelligence",
                "historical_period": "Northern Song period"
            },
            {
                "civilization": "Inca Empire",
                "tech_discovery": "Telecommunications",
                "historical_period": "Imperial phase"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an alternate technological evolution path for {t['civilization']} based on the early discovery of {t['tech_discovery']} during the {t['historical_period']}. Then, extrapolate its potential impact on modern society. Your response should include:

1. Historical Context (150-200 words):
   a) Briefly describe the technological and cultural state of {t['civilization']} during the {t['historical_period']}.
   b) Explain the historical significance of {t['tech_discovery']} and its actual timeline of discovery.

2. Alternate Discovery Scenario (200-250 words):
   a) Propose a plausible scenario for the early discovery of {t['tech_discovery']} in {t['civilization']}.
   b) Describe the initial reactions and applications of this technology within the civilization.
   c) Discuss any immediate challenges or advantages this discovery might present.

3. Technological Evolution Path (250-300 words):
   a) Outline a possible path of technological evolution stemming from this early discovery.
   b) Describe key innovations or adaptations that might arise as a result.
   c) Explain how this new technology might interact with or influence other aspects of the civilization's development.

4. Cultural and Societal Impact (200-250 words):
   a) Analyze how the early adoption of {t['tech_discovery']} might alter the civilization's social structures, economy, or political systems.
   b) Discuss potential changes in warfare, trade, or international relations.
   c) Describe how this might affect the civilization's historical trajectory and interactions with other cultures.

5. Modern World Extrapolation (250-300 words):
   a) Imagine how this alternate historical path might have shaped the modern world.
   b) Describe key differences in technology, society, or geopolitics compared to our actual timeline.
   c) Propose at least one major global challenge or opportunity that might exist in this alternate present.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical implications of this alternate historical path.
   b) Analyze how this scenario might challenge or support various philosophical views on technological progress and historical determinism.

Ensure your response demonstrates a deep understanding of historical contexts, technological development processes, and societal dynamics. Use appropriate terminology from relevant fields and provide clear explanations for your speculative scenarios. Be creative in your approach while maintaining historical and scientific plausibility. Your response should go beyond simply restating historical facts and engage in thoughtful, creative speculation about alternate historical trajectories.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c) where applicable. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should accurately describe the historical context of {t['civilization']} during the {t['historical_period']}",
            f"The alternate discovery scenario for {t['tech_discovery']} should be plausible and well-reasoned",
            "The technological evolution path should be logically consistent and creative",
            "The cultural and societal impact analysis should be comprehensive and insightful",
            "The modern world extrapolation should be imaginative yet grounded in historical and technological principles",
            "The ethical and philosophical implications should be thoughtfully considered",
            "The response should demonstrate interdisciplinary knowledge integration and counterfactual reasoning",
            "The response should go beyond historical facts and engage in creative, plausible speculation",
            "The response should be properly formatted with clear headings and subheadings as specified"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
