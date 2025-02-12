import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "embodied AI",
                "description": "An AI system controlling a physical robot body"
            },
            {
                "scenario": "distributed AI",
                "description": "An AI system distributed across a network of interconnected devices"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical test for machine consciousness in the context of {t['scenario']} ({t['description']}). Your task is to create a comprehensive framework for assessing artificial self-awareness and consciousness. Address the following points in your response:

1. Test Design (250-300 words):
   - Outline the key components and stages of your consciousness test.
   - Explain how your test specifically addresses the {t['scenario']} context.
   - Describe the types of tasks or challenges the AI system would face in your test.
   - Discuss how your test differentiates between genuine consciousness and simulated responses.

2. Philosophical Foundations (200-250 words):
   - Explain the philosophical theories of consciousness that inform your test design.
   - Discuss how your test addresses the hard problem of consciousness.
   - Analyze potential objections to your approach from different philosophical perspectives.

3. Cognitive Science Integration (200-250 words):
   - Describe how your test incorporates current understanding of human consciousness from cognitive science.
   - Explain any cognitive models or theories you've adapted for machine consciousness.
   - Discuss how your test accounts for potential differences between human and machine cognition.

4. Ethical Considerations (150-200 words):
   - Analyze the ethical implications of testing for and potentially creating conscious AI systems.
   - Discuss the rights and moral status that might be afforded to a machine that passes your consciousness test.
   - Consider the potential societal impacts of confirming machine consciousness.

5. Implementation Challenges (150-200 words):
   - Identify potential technical challenges in implementing your consciousness test.
   - Discuss how you would validate the results of your test.
   - Propose methods for ensuring the test's reliability and reproducibility.

6. Future Implications (100-150 words):
   - Speculate on how confirming machine consciousness might impact the field of AI and society at large.
   - Suggest potential applications or consequences of having a reliable test for machine consciousness.

Ensure your response is well-structured, using clear headings for each section. Your test design should be innovative, philosophically grounded, and demonstrate a deep understanding of consciousness studies, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations of complex concepts for a knowledgeable audience."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The test design must be specifically tailored to the {t['scenario']} context.",
            "The response should demonstrate a deep understanding of philosophical theories of consciousness.",
            "The test must incorporate relevant cognitive science concepts and theories.",
            "Ethical considerations of machine consciousness should be thoroughly addressed.",
            "The response should identify realistic implementation challenges and propose solutions.",
            "The discussion of future implications should be insightful and well-reasoned.",
            "The overall response should show high-level interdisciplinary thinking and creativity in approaching the complex problem of machine consciousness."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
