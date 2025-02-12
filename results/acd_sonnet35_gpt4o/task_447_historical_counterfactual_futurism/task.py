import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            {
                'event': 'Industrial Revolution',
                'year': 1760,
                'location': 'England',
                'key_aspect': 'Mechanization of manufacturing'
            },
            {
                'event': 'World War II',
                'year': 1939,
                'location': 'Global',
                'key_aspect': 'Development of nuclear weapons'
            },
            {
                'event': 'Moon Landing',
                'year': 1969,
                'location': 'United States',
                'key_aspect': 'First human on the moon'
            },
            {
                'event': 'Fall of the Berlin Wall',
                'year': 1989,
                'location': 'Germany',
                'key_aspect': 'End of Cold War symbolism'
            },
            {
                'event': 'Invention of the World Wide Web',
                'year': 1989,
                'location': 'Switzerland (CERN)',
                'key_aspect': 'Global information sharing'
            }
        ]
        
        tasks = [
            random.choice(historical_events),
            random.choice(historical_events)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the historical event '{t['event']}' ({t['year']}, {t['location']}) and create a counterfactual scenario based on a significant change to its key aspect: {t['key_aspect']}. Then, project how this change might have impacted technological and societal developments up to the year 2050. Your response should include:

1. Historical Context (100-150 words):
   Briefly describe the actual historical event, its causes, and its immediate consequences. Cite at least one relevant historical source.

2. Counterfactual Scenario (150-200 words):
   Present a plausible alternative scenario where the key aspect of the event is significantly altered. Your scenario should specify:
   a) The exact nature of the change
   b) The immediate effects of this change
   c) The reasoning behind your proposed alternate history

3. Technological Impact (200-250 words):
   Project how your counterfactual scenario might have affected technological developments up to 2050. Discuss at least two major technological areas that would be impacted. Use historical trends and scientific principles to support your projections.

4. Societal Changes (200-250 words):
   Analyze the potential societal changes resulting from your counterfactual scenario up to 2050. Consider aspects such as social structures, economic systems, or geopolitical dynamics. Use sociological theories or historical patterns to support your analysis.

5. Ethical Implications (150-200 words):
   Discuss the ethical implications of the alternative historical trajectory you've outlined. Consider both positive and negative consequences, and reference relevant ethical frameworks or philosophies.

6. Unintended Consequences (100-150 words):
   Propose one major unintended consequence of your counterfactual scenario that might emerge by 2050, explaining its potential impact. Justify your prediction using causal reasoning.

Ensure your response demonstrates a deep understanding of historical causality, technological trends, and societal dynamics. Be creative in your counterfactual scenario and future projections while maintaining plausibility based on historical and scientific knowledge. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 900-1200 words. Cite at least one relevant historical or scientific source in each section to support your analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the historical event and its significance, citing relevant sources.",
            "The counterfactual scenario is creative yet plausible, with well-reasoned immediate effects and clear specification of the proposed change.",
            "The technological impact analysis is insightful, considers multiple areas of development, and is supported by historical trends and scientific principles.",
            "The societal changes projected are comprehensive, logically follow from the counterfactual scenario, and are supported by sociological theories or historical patterns.",
            "The ethical implications are thoughtfully considered, addressing both positive and negative aspects, and referencing relevant ethical frameworks.",
            "The unintended consequence proposed is creative, its potential impact is well-explained, and the prediction is justified using causal reasoning.",
            "The overall response shows a high level of historical knowledge, causal reasoning, and creative forecasting, with appropriate citations throughout.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
