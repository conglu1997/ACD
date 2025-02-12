import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            "The invention of the printing press",
            "The discovery of penicillin",
            "The assassination of Julius Caesar",
            "The signing of the Magna Carta",
            "The fall of Constantinople"
        ]
        domains = [
            "Technology",
            "Politics",
            "Social structures",
            "Economics",
            "Culture and art"
        ]
        
        tasks = {}
        for i in range(2):
            event = random.choice(historical_events)
            domain1, domain2 = random.sample(domains, 2)
            tasks[str(i+1)] = {
                "historical_event": event,
                "primary_domain": domain1,
                "secondary_domain": domain2
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and construct a detailed counterfactual historical scenario based on preventing or significantly altering the event: {t['historical_event']}. Your task is to explore how this change would affect the course of history, focusing primarily on the domain of {t['primary_domain']}, with secondary considerations for {t['secondary_domain']}. Your response should include:

1. Event Analysis (150-200 words):
   a) Briefly describe the original historical event and its significance.
   b) Explain the specific change you're introducing to create the counterfactual scenario.
   c) Discuss the immediate consequences of this change.

2. Primary Domain Impact ({t['primary_domain']}) (250-300 words):
   a) Analyze in detail how the counterfactual scenario would affect this domain.
   b) Describe potential short-term and long-term consequences.
   c) Identify key figures or subsequent events that would be significantly altered.
   d) Explain any potential ripple effects or unexpected outcomes.

3. Secondary Domain Impact ({t['secondary_domain']}) (200-250 words):
   a) Examine how changes in the primary domain would influence this secondary domain.
   b) Describe potential interconnections and feedback loops between the two domains.
   c) Identify any surprising or counterintuitive effects in this domain.

4. Alternative Timeline (200-250 words):
   a) Construct a brief timeline of major events in your counterfactual history, focusing on the 100 years following the change.
   b) Highlight key divergences from actual history.
   c) Explain the reasoning behind each major event in your timeline.

5. Critical Analysis (150-200 words):
   a) Evaluate the plausibility of your counterfactual scenario.
   b) Discuss any potential logical inconsistencies or challenges in your analysis.
   c) Reflect on what this exercise reveals about the nature of historical causality and interconnectedness.

6. Comparative Reflection (100-150 words):
   a) Compare the world in your counterfactual scenario to actual history.
   b) Discuss whether the overall outcome is better, worse, or simply different, and why.
   c) Consider what lessons this comparison might offer for understanding current global challenges.

Ensure your response demonstrates a deep understanding of historical events, causal relationships, and the interconnectedness of different domains of human activity. Use appropriate historical terminology and provide clear explanations for your reasoning. Be creative in your counterfactual scenario while maintaining logical consistency and plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the historical event and its significance",
            "The counterfactual scenario is creative yet plausible",
            "The analysis of the primary and secondary domains is thorough and insightful",
            "The alternative timeline is logically consistent and well-reasoned",
            "The critical analysis shows awareness of the complexities and challenges in counterfactual reasoning",
            "The comparative reflection offers meaningful insights into historical processes and current issues",
            "The response is well-structured, with clear headings for each section",
            "The total word count is between 1050-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
