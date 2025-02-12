import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "confirmation bias",
            "anchoring bias",
            "availability heuristic",
            "dunning-kruger effect",
            "bandwagon effect"
        ]
        social_scenarios = [
            "political decision-making",
            "economic resource allocation",
            "educational system design",
            "environmental policy development",
            "healthcare prioritization"
        ]
        tasks = [
            {
                'cognitive_bias': random.choice(cognitive_biases),
                'social_scenario': random.choice(social_scenarios)
            },
            {
                'cognitive_bias': random.choice(cognitive_biases),
                'social_scenario': random.choice(social_scenarios)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) that incorporates the cognitive bias of {t['cognitive_bias']}, then use it to analyze social dynamics in a hypothetical society focusing on {t['social_scenario']}. Your response should include:

1. Conlang Design (250-300 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how the language's structure and vocabulary reflect and reinforce the given cognitive bias.
   c) Provide three example sentences in your conlang with translations and explanations of how they embody the cognitive bias.

2. Cognitive Bias Analysis (200-250 words):
   a) Explain the chosen cognitive bias and its effects on human thinking and behavior.
   b) Discuss how your conlang's features might influence or exacerbate this bias in its speakers.
   c) Analyze potential benefits and drawbacks of a language that reinforces this particular cognitive bias.

3. Hypothetical Society Description (200-250 words):
   a) Describe a hypothetical society that uses your conlang as its primary language.
   b) Explain how the cognitive bias embedded in the language might shape this society's culture, values, and institutions.
   c) Discuss any unique social structures or practices that might emerge as a result of this biased language.

4. Social Scenario Analysis (250-300 words):
   a) Apply your conlang and its embedded cognitive bias to the given social scenario.
   b) Provide a detailed analysis of how the language might influence decision-making and social dynamics in this context.
   c) Describe potential positive and negative outcomes of approaching this scenario through the lens of your biased language.
   d) Suggest how awareness of the language's bias might affect the scenario's outcome.

5. Comparative Linguistic Analysis (150-200 words):
   a) Compare your conlang to natural languages, highlighting similarities and differences in how they handle the given cognitive bias.
   b) Discuss how your conlang might interact with or influence speakers of other languages.
   c) Analyze the potential for your conlang to be adopted as an auxiliary language and its implications.

6. Ethical Implications and Future Research (150-200 words):
   a) Discuss the ethical considerations of designing and using a language that intentionally incorporates cognitive biases.
   b) Propose guidelines for responsible use of such a language in research or social engineering.
   c) Suggest two potential experiments or studies to further explore the effects of your biased conlang on cognition and social behavior.

Ensure your response demonstrates a deep understanding of linguistics, cognitive psychology, and social dynamics. Be creative in your language design while maintaining internal consistency and plausibility. Use appropriate terminology from relevant fields and provide clear explanations for your choices.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive biases, and social dynamics.",
            "The conlang design is creative, internally consistent, and effectively incorporates the specified cognitive bias.",
            "The analysis of the social scenario is thorough and plausibly connects the conlang's influence to social outcomes.",
            "The ethical implications are thoughtfully considered, and proposed guidelines and future research are relevant and insightful.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
