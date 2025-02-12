import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_concepts = [
            "Linear time",
            "Cyclical time",
            "Branching time",
            "Eternal present",
            "Time dilation",
            "Temporal recursion"
        ]
        
        linguistic_features = [
            "Tense systems",
            "Aspect markers",
            "Temporal adverbs",
            "Time-based metaphors",
            "Temporal connectives",
            "Evidentiality markers"
        ]
        
        cognitive_effects = [
            "Memory formation",
            "Decision making",
            "Future planning",
            "Emotional processing",
            "Attention allocation",
            "Causal reasoning"
        ]
        
        tasks = {}
        for i in range(2):
            selected_concept = random.choice(time_concepts)
            selected_feature = random.choice(linguistic_features)
            selected_effect = random.choice(cognitive_effects)
            
            tasks[str(i+1)] = {
                "time_concept": selected_concept,
                "linguistic_feature": selected_feature,
                "cognitive_effect": selected_effect
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and manipulates the perception of time through language, focusing on the time concept of {t['time_concept']}, the linguistic feature of {t['linguistic_feature']}, and its effect on {t['cognitive_effect']}. Your response should include the following sections:

1. Theoretical Foundation (200-250 words):
   a) Explain the chosen time concept and its relevance to human cognition.
   b) Describe how the selected linguistic feature relates to the expression of time.
   c) Discuss current theories on how time perception affects the specified cognitive process.

2. AI System Architecture (250-300 words):
   a) Design a novel AI architecture that models temporal perception based on the given time concept.
   b) Explain how your system incorporates the specified linguistic feature in its language processing.
   c) Describe how the AI manipulates time perception to influence the chosen cognitive effect.
   d) Include a high-level diagram or pseudocode representing your system's key components and their interactions.

3. Temporal-Linguistic Modeling (200-250 words):
   a) Explain how your AI system represents and processes temporal information.
   b) Describe the mechanisms used to manipulate time perception through language.
   c) Provide examples of how your system might alter temporal expressions to achieve specific cognitive effects.

4. Cognitive Impact Analysis (200-250 words):
   a) Analyze how your system's manipulation of time perception could influence the specified cognitive process.
   b) Discuss potential benefits and risks of altering time perception through language.
   c) Propose experiments to measure the cognitive effects of your system's temporal-linguistic manipulations.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss ethical considerations related to manipulating time perception through AI and language.
   b) Explore philosophical questions raised by the ability to alter subjective experiences of time.
   c) Consider potential societal impacts of widespread use of temporal-linguistic AI systems.

6. Future Research Directions (150-200 words):
   a) Propose three specific areas for further research to advance your temporal-linguistic AI system.
   b) Discuss potential applications of your system in fields such as psychology, education, or therapy.
   c) Speculate on how this technology might evolve and impact our understanding of time, language, and cognition.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified time concept, linguistic feature, and cognitive effect",
            "The AI system design is innovative and plausibly integrates temporal perception, language processing, and cognitive manipulation",
            "The analysis of cognitive impacts and ethical implications is thorough and thought-provoking",
            "The response is well-structured, clear, and adheres to the specified format and word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
