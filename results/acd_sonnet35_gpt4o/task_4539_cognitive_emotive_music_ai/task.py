import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_state": "flow state",
                "emotional_state": "contentment",
                "musical_style": "ambient"
            },
            {
                "cognitive_state": "divided attention",
                "emotional_state": "anxiety",
                "musical_style": "jazz"
            },
            {
                "cognitive_state": "metacognition",
                "emotional_state": "curiosity",
                "musical_style": "classical"
            },
            {
                "cognitive_state": "working memory overload",
                "emotional_state": "frustration",
                "musical_style": "electronic"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Design an AI system that can generate and analyze music based on cognitive and emotional states, integrating theories from cognitive science, neuroscience, and musicology. Your system should focus on the cognitive state of {t['cognitive_state']}, the emotional state of {t['emotional_state']}, and the musical style of {t['musical_style']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the cognitive and emotional theories your system will use to model {t['cognitive_state']} and {t['emotional_state']}.
   b) Describe how these states are typically reflected in human behavior and physiology.
   c) Discuss the key characteristics of {t['musical_style']} and how they might relate to the given cognitive and emotional states.

2. AI System Architecture (300-350 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system processes cognitive and emotional inputs to generate musical output.
   c) Describe any novel algorithms or techniques your system uses for music generation and analysis.
   d) Discuss how your system ensures coherence and emotional relevance in the generated music.

3. Music Generation Process (200-250 words):
   a) Provide a step-by-step explanation of how your AI would generate a piece of {t['musical_style']} music reflecting {t['cognitive_state']} and {t['emotional_state']}.
   b) Explain how specific musical elements (e.g., rhythm, harmony, melody) would be manipulated to convey the given states.
   c) Discuss any challenges in translating cognitive and emotional states into musical parameters.

4. Music Analysis Capabilities (200-250 words):
   a) Describe how your AI system would analyze an existing piece of music to infer the cognitive and emotional states it might induce.
   b) Explain the features or patterns your system would look for in the music.
   c) Discuss how your system would handle ambiguity or cultural differences in musical interpretation.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your AI system in generating emotionally and cognitively relevant music.
   b) Describe how you would validate the system's music analysis capabilities.
   c) Discuss the challenges in evaluating such a system and how you'd address them.

6. Potential Applications and Ethical Considerations (150-200 words):
   a) Suggest two potential applications of your cognitive-emotive music AI system.
   b) Discuss any ethical implications or potential misuses of this technology.
   c) Propose guidelines for responsible development and use of AI systems that manipulate emotions through music.

Ensure your response demonstrates a deep understanding of cognitive science, musicology, and AI technologies. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide explanations where necessary. Your total response should be between 1250-1550 words.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, musicology, and AI technologies",
            "The AI system design is creative, innovative, and scientifically plausible",
            "The response addresses all required sections comprehensively",
            "The explanation of how cognitive and emotional states are translated into musical elements is clear and well-reasoned",
            "The proposed evaluation methods and ethical considerations are thoughtful and relevant"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
