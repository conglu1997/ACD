import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        temporal_perspectives = [
            {
                "perspective": "Future-oriented nostalgia",
                "description": "A longing for a future that may never come to pass"
            },
            {
                "perspective": "Recursive past",
                "description": "Remembering the act of remembering a past event"
            }
        ]
        
        tasks = {}
        for i in range(2):
            perspective = random.choice(temporal_perspectives)
            tasks[str(i+1)] = {
                "temporal_perspective": perspective["perspective"],
                "description": perspective["description"]
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model that incorporates principles of mental time travel and temporal cognition, then use it to generate and analyze text with complex temporal perspectives. Focus on the temporal perspective: {t['temporal_perspective']} ({t['description']}). Your response should include:

1. Temporal Cognition Framework (200-250 words):
   a) Explain the key principles of mental time travel and temporal cognition that inform your model.
   b) Describe how your model represents and processes different temporal perspectives.
   c) Discuss how your framework integrates linguistic features with cognitive processes related to time perception.

2. Language Model Architecture (250-300 words):
   a) Outline the main components of your language model and how they interact.
   b) Explain how your model incorporates the temporal cognition framework.
   c) Describe any novel mechanisms or features that allow your model to handle complex temporal perspectives.
   d) Discuss how your model might differ from traditional language models in processing temporal information.

3. Text Generation (150-200 words):
   a) Use your model to generate a short text (50-75 words) that exemplifies the given temporal perspective: {t['temporal_perspective']}.
   b) Explain how your model produced this text, highlighting the specific temporal features it incorporates.

4. Linguistic Analysis (200-250 words):
   a) Analyze the linguistic properties of your generated text, focusing on how it conveys the complex temporal perspective.
   b) Discuss any emergent linguistic patterns or structures that arise from your model's temporal processing.
   c) Compare the temporal features in your generated text to those typically found in human-generated language.

5. Cognitive Implications (150-200 words):
   a) Discuss how your model's approach to temporal cognition might inform or challenge current theories of human time perception and mental time travel.
   b) Explore potential applications of your model in studying or simulating human cognitive processes related to temporal reasoning.

6. AI and Future Directions (150-200 words):
   a) Explain how your model could enhance AI's capacity for temporal reasoning and understanding.
   b) Propose two potential research directions or experiments that could further explore the intersection of temporal cognition, linguistics, and AI based on your model.

Ensure your response demonstrates a deep understanding of temporal cognition, linguistics, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a well-designed temporal cognition framework and language model architecture",
            "The generated text should clearly demonstrate the specified temporal perspective",
            "The linguistic analysis should provide insights into how the model conveys complex temporal information",
            "The response should explore cognitive implications and potential AI applications of the model",
            "The overall response should show a deep understanding of temporal cognition, linguistics, and AI principles"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
