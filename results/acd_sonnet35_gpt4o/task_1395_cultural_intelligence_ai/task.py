import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_contexts = [
            {
                "culture": "Japanese",
                "key_values": ["harmony", "respect for hierarchy", "indirect communication"],
                "scenario": "business negotiation"
            },
            {
                "culture": "Brazilian",
                "key_values": ["personal relationships", "flexibility", "expressiveness"],
                "scenario": "social gathering"
            }
        ]
        return {
            "1": random.choice(cultural_contexts),
            "2": random.choice(cultural_contexts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can demonstrate cultural intelligence in a {t['culture']} cultural context, specifically for a {t['scenario']} scenario. Your system should be able to adapt its behavior based on the key cultural values of {', '.join(t['key_values'])}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the overall structure of your culturally intelligent AI system.
   b) Explain how cultural knowledge is represented and processed in your system.
   c) Detail how the system adapts its behavior based on cultural context.
   d) Discuss any novel components or mechanisms specific to cultural intelligence.

2. Cultural Knowledge Integration (200-250 words):
   a) Explain how your system incorporates and utilizes the key cultural values provided.
   b) Describe the process of cultural learning and knowledge updating in your AI.
   c) Discuss how your system handles cultural nuances and ambiguities.

3. Scenario Application (200-250 words):
   a) Provide a specific example of how your AI would behave in the given scenario.
   b) Explain how this behavior demonstrates cultural intelligence.
   c) Compare this behavior to how the AI might act in a different cultural context.

4. Evaluation Metrics (150-200 words):
   a) Propose metrics to assess the cultural intelligence of your AI system.
   b) Describe how you would test the system's performance across different cultures.
   c) Discuss the challenges in evaluating cultural intelligence in AI systems.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues in developing culturally intelligent AI.
   b) Discuss the implications of AI systems adapting to different cultural norms.
   c) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of both AI systems and cultural anthropology. Be creative in your approach while maintaining scientific and ethical plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cultural intelligence and AI systems.",
            "The proposed AI architecture is innovative and well-explained.",
            "The system effectively integrates and utilizes the provided cultural values.",
            "The scenario application clearly demonstrates cultural adaptation.",
            "Ethical considerations are thoroughly explored and addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
