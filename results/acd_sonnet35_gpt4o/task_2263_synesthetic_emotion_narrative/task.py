import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "emotion": "nostalgia",
                "context": "revisiting childhood home",
                "sensory_focus": "smell"
            },
            {
                "emotion": "anxiety",
                "context": "public speaking",
                "sensory_focus": "touch"
            },
            {
                "emotion": "awe",
                "context": "witnessing a natural wonder",
                "sensory_focus": "sight"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a 'synesthetic narrative' that blends sensory experiences, emotions, and physiological responses for the following scenario:

Emotion: {t['emotion']}
Context: {t['context']}
Sensory Focus: {t['sensory_focus']}

Your task has four parts:

1. Synesthetic Narrative (200-250 words):
   Write a short narrative that describes the experience of the given emotion in the specified context, focusing on the indicated sensory modality. Your narrative should:
   a) Vividly describe the sensory experiences associated with the emotion.
   b) Include physiological responses that accompany the emotion.
   c) Use synesthetic metaphors that blend different sensory modalities.
   d) Maintain a coherent narrative structure while exploring the emotional-sensory experience.

2. Linguistic Analysis (150-200 words):
   Analyze the linguistic features of your narrative, including:
   a) The types of sensory words and metaphors used.
   b) How syntax and rhythm contribute to the emotional impact.
   c) Any novel linguistic constructions you created to express the synesthetic experience.

3. Cognitive-Emotional Mapping (150-200 words):
   Explain how your narrative reflects the cognitive and neurological aspects of the emotion-sensory experience:
   a) Describe the potential neural pathways involved in this synesthetic experience.
   b) Discuss how the blending of sensory modalities might reflect or influence cognitive processes.
   c) Hypothesize about the evolutionary or cultural factors that might contribute to this particular emotional-sensory association.

4. Cross-Cultural Perspective (100-150 words):
   Consider how this synesthetic emotional experience might be perceived or expressed differently in another culture of your choice:
   a) Describe potential differences in sensory associations or metaphors.
   b) Explain how cultural factors might influence the perception and expression of this emotion-sensory blend.
   c) Suggest how these cultural differences could impact communication or empathy across cultures.

Ensure your response demonstrates creativity, emotional intelligence, and a deep understanding of sensory perception, neurology, and cultural influences on emotion. Use appropriate terminology from relevant fields and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The synesthetic narrative vividly blends sensory experiences, emotions, and physiological responses",
            "The linguistic analysis demonstrates a deep understanding of language features and their emotional impact",
            "The cognitive-emotional mapping shows insight into neurological and evolutionary aspects of the experience",
            "The cross-cultural perspective thoughtfully considers how the experience might differ in another culture",
            "The overall response demonstrates creativity, emotional intelligence, and interdisciplinary knowledge application"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
