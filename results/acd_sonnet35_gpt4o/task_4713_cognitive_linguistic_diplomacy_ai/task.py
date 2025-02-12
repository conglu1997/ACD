import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conflicts = [
            "territorial dispute in the South China Sea",
            "nuclear non-proliferation negotiations with Iran",
            "trade tensions between the United States and China",
            "border conflict between India and Pakistan",
            "peace process in the Israeli-Palestinian conflict"
        ]
        cognitive_biases = [
            "confirmation bias",
            "in-group favoritism",
            "fundamental attribution error",
            "loss aversion",
            "anchoring effect"
        ]
        linguistic_features = [
            "metaphorical framing",
            "politeness strategies",
            "hedging language",
            "presupposition",
            "deictic expressions"
        ]
        
        return {
            "1": {
                "conflict": random.choice(conflicts),
                "cognitive_bias": random.choice(cognitive_biases),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "conflict": random.choice(conflicts),
                "cognitive_bias": random.choice(cognitive_biases),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses cognitive science and linguistic principles to analyze and mediate the {t['conflict']}. Your system should specifically address the cognitive bias of {t['cognitive_bias']} (the tendency to {TaskFamily.get_bias_description(t['cognitive_bias'])}) and focus on the linguistic feature of {t['linguistic_feature']} (which involves {TaskFamily.get_linguistic_feature_description(t['linguistic_feature'])}) in diplomatic communications. Your response should include the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cognitive-linguistic diplomacy.
   b) Explain how these components interact to analyze diplomatic communications and mediate conflicts.
   c) Detail how your system incorporates cognitive science and linguistic principles.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Cognitive Bias Analysis (200-250 words):
   a) Explain how your system identifies and analyzes the specified cognitive bias in diplomatic communications.
   b) Describe strategies your AI employs to mitigate the effects of this bias.
   c) Provide an example of how your system would handle a specific instance of this bias in the given conflict.

3. Linguistic Feature Processing (200-250 words):
   a) Detail how your system analyzes and interprets the specified linguistic feature in diplomatic texts or speeches.
   b) Explain how this analysis contributes to understanding cultural nuances and intentions.
   c) Describe how your system uses this linguistic insight to improve communication between parties.

4. Conflict Mediation Approach (250-300 words):
   a) Outline your AI system's approach to mediating the specified international conflict.
   b) Explain how it integrates cognitive and linguistic analyses to propose resolution strategies.
   c) Describe a hypothetical scenario where your system successfully identifies a communication issue and suggests an intervention.
   d) Discuss how your system adapts its mediation strategies based on cultural contexts.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI in sensitive diplomatic situations.
   b) Address potential biases in your system and how you mitigate them.
   c) Propose guidelines for the responsible use of AI in international conflict resolution.

6. Evaluation and Improvement (150-200 words):
   a) Suggest methods to evaluate the effectiveness of your AI system in real-world diplomatic scenarios.
   b) Describe how you would incorporate feedback from diplomats and conflict resolution experts.
   c) Propose potential improvements or extensions to enhance your system's capabilities.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, artificial intelligence, and international relations. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining practical feasibility and ethical considerations.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words. Include a word count at the end of your response."""

    @staticmethod
    def get_bias_description(bias: str) -> str:
        descriptions = {
            "confirmation bias": "interpret information in a way that confirms preexisting beliefs",
            "in-group favoritism": "favor one's own group over others",
            "fundamental attribution error": "attribute others' behavior to their character rather than situational factors",
            "loss aversion": "prefer avoiding losses to acquiring equivalent gains",
            "anchoring effect": "rely too heavily on the first piece of information offered"
        }
        return descriptions.get(bias, "")

    @staticmethod
    def get_linguistic_feature_description(feature: str) -> str:
        descriptions = {
            "metaphorical framing": "using figurative language to shape perception of issues",
            "politeness strategies": "using language to maintain face and manage social relations",
            "hedging language": "using words or phrases to express uncertainty or lack of commitment",
            "presupposition": "implying information without directly stating it",
            "deictic expressions": "using context-dependent words like 'here' or 'now'"
        }
        return descriptions.get(feature, "")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive science, linguistics, and international relations.",
            "The AI system design is innovative and well-explained, with clear integration of cognitive bias analysis and linguistic feature processing.",
            "The proposed solution effectively addresses the given international conflict while considering cultural and linguistic nuances.",
            "The response considers ethical implications and potential biases in AI-driven conflict resolution.",
            "The submission is well-structured, within the specified word count, and uses appropriate technical terminology from all relevant fields.",
            "The proposed AI system design is practically feasible with current or near-future technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
