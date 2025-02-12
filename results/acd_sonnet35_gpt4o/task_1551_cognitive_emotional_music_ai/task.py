import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_states = ['focused attention', 'working memory', 'cognitive flexibility', 'processing speed']
        emotional_states = ['joy', 'sadness', 'anger', 'fear', 'surprise']
        musical_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        therapeutic_goals = ['stress reduction', 'mood elevation', 'cognitive enhancement', 'emotional regulation']
        
        return {
            "1": {
                "cognitive_state": random.choice(cognitive_states),
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "therapeutic_goal": random.choice(therapeutic_goals)
            },
            "2": {
                "cognitive_state": random.choice(cognitive_states),
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "therapeutic_goal": random.choice(therapeutic_goals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes music based on cognitive and emotional states, then apply it to a therapeutic scenario. Your system should focus on the cognitive state of {t['cognitive_state']}, the emotional state of {t['emotional_state']}, and primarily utilize the musical element of {t['musical_element']} to achieve the therapeutic goal of {t['therapeutic_goal']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system.
   b) Explain how it integrates cognitive and emotional state analysis with music generation and analysis.
   c) Detail the key components and their interactions.
   d) Discuss any novel elements in your design that enable cognitive-emotional music processing.

2. Cognitive-Emotional Music Mapping (200-250 words):
   a) Explain how your system maps {t['cognitive_state']} and {t['emotional_state']} to musical parameters.
   b) Describe the theoretical basis for these mappings, citing relevant research in cognitive science and music psychology.
   c) Provide a specific example of how a combination of {t['cognitive_state']} and {t['emotional_state']} would be translated into musical output, focusing on {t['musical_element']}.

3. Music Generation and Analysis Algorithms (200-250 words):
   a) Describe the AI algorithms used for music generation and analysis in your system.
   b) Explain how these algorithms incorporate cognitive and emotional state information.
   c) Discuss how your system ensures musical coherence and aesthetic quality while addressing cognitive-emotional goals.

4. Therapeutic Application (200-250 words):
   a) Describe how your system would be applied to achieve the therapeutic goal of {t['therapeutic_goal']}.
   b) Explain the process of generating and adapting music in real-time based on a patient's changing cognitive and emotional states.
   c) Discuss potential challenges in this therapeutic application and how your system addresses them.

5. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate the effectiveness of your system in achieving {t['therapeutic_goal']}.
   b) Describe the metrics you would use to assess both the musical quality and the cognitive-emotional impact.
   c) Explain how you would validate the system's ability to accurately map {t['cognitive_state']} and {t['emotional_state']} to music.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI-generated music for therapeutic purposes.
   b) Address privacy concerns related to cognitive and emotional state monitoring.
   c) Propose guidelines for responsible use of your system in clinical settings.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, emotion research, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and therapeutic plausibility.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains how {t['cognitive_state']} and {t['emotional_state']} are mapped to musical parameters, focusing on {t['musical_element']}.",
            f"The system design clearly describes how AI is used to generate and analyze music for the therapeutic goal of {t['therapeutic_goal']}.",
            "The answer demonstrates a deep understanding of music theory, cognitive science, emotion research, and artificial intelligence principles.",
            "The proposed AI system is innovative yet scientifically and therapeutically plausible.",
            "The response addresses all required sections with appropriate detail and length.",
            "The ethical implications and evaluation methodology are thoughtfully explored.",
            "A specific example of translating cognitive and emotional states into musical output is provided and clearly explained.",
            "The total response is between 1150-1450 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
