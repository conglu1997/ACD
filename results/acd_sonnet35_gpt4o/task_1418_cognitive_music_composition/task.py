import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_effects = [
            'attention modulation',
            'memory enhancement',
            'emotional regulation',
            'spatial reasoning improvement'
        ]
        musical_elements = [
            'rhythm',
            'harmony',
            'timbre',
            'melody'
        ]
        
        tasks = {
            "1": {
                "cognitive_effect": random.choice(cognitive_effects),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "cognitive_effect": random.choice(cognitive_effects),
                "musical_element": random.choice(musical_elements)
            }
        }
        
        # Ensure the two tasks are different
        while tasks["1"] == tasks["2"]:
            tasks["2"] = {
                "cognitive_effect": random.choice(cognitive_effects),
                "musical_element": random.choice(musical_elements)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates music based on cognitive principles of auditory processing and musical perception, then use it to compose a piece aimed at inducing the cognitive effect of {t['cognitive_effect']}, focusing primarily on the musical element of {t['musical_element']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI music generation system.
   b) Explain how your system incorporates principles of auditory processing and musical perception.
   c) Detail how your system is designed to target specific cognitive effects through music.

2. Cognitive-Musical Analysis (200-250 words):
   a) Analyze the relationship between {t['cognitive_effect']} and musical features, particularly {t['musical_element']}.
   b) Discuss relevant research in cognitive neuroscience and music psychology that informs your approach.
   c) Explain how manipulating {t['musical_element']} could potentially induce or enhance {t['cognitive_effect']}.

3. Composition Process (250-300 words):
   a) Describe the step-by-step process your AI system would use to compose a piece targeting {t['cognitive_effect']}.
   b) Explain how your system would manipulate {t['musical_element']} to achieve the desired effect.
   c) Discuss any challenges in translating cognitive principles into musical parameters, and how your system addresses them.

4. Musical Output Description (150-200 words):
   a) Provide a detailed description of the composition your system would generate.
   b) Explain how specific features of the composition relate to {t['cognitive_effect']} and {t['musical_element']}.
   c) Discuss how the composition might be perceived by human listeners.

5. Evaluation and Ethical Considerations (150-200 words):
   a) Propose methods to evaluate the effectiveness of your AI-generated music in inducing {t['cognitive_effect']}.
   b) Discuss potential risks or ethical concerns related to using AI-generated music to influence cognition.
   c) Suggest guidelines for responsible development and use of cognitive-effect-targeted AI music.

Ensure your response demonstrates a deep understanding of cognitive neuroscience, music theory, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the relationship between {t['cognitive_effect']} and musical elements, particularly {t['musical_element']}.",
            "The AI system design is technically sound and incorporates principles from cognitive neuroscience and music psychology.",
            "The composition process and musical output description are creative, detailed, and plausibly linked to the target cognitive effect.",
            "The response shows awareness of the challenges and ethical considerations in using AI-generated music to influence cognition.",
            "The answer is well-structured, clear, and uses appropriate technical terminology from cognitive science, music theory, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
