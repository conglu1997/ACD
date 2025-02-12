import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        cognitive_models = ['Appraisal Theory', 'Circumplex Model', 'Basic Emotion Theory', 'Constructionist Theory']
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre', 'dynamics']
        cultural_contexts = ['Western', 'East Asian', 'Middle Eastern', 'African', 'Latin American']
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'emotion': random.choice(emotions),
                'cognitive_model': random.choice(cognitive_models),
                'musical_element': random.choice(musical_elements),
                'cultural_context': random.choice(cultural_contexts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        cognitive_model_context = {
            'Appraisal Theory': 'which suggests emotions arise from our evaluations of events',
            'Circumplex Model': 'which arranges emotions in a circular space of arousal and valence',
            'Basic Emotion Theory': 'which proposes a set of discrete, universal emotions',
            'Constructionist Theory': 'which views emotions as constructed from more basic psychological ingredients'
        }
        
        return f"""Design an AI system that composes music to evoke the emotion of {t['emotion']} based on the {t['cognitive_model']} of emotion ({cognitive_model_context[t['cognitive_model']]}), with a focus on the musical element of {t['musical_element']}, while considering the {t['cultural_context']} cultural context. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI music composition system.
   b) Explain how it incorporates the specified cognitive model of emotion.
   c) Detail how the system will generate and manipulate the given musical element.
   d) Discuss how the system will evaluate the emotional impact of its compositions.
   e) Explain how the system accounts for the specified cultural context.
   Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Emotion-Music Mapping (250-300 words):
   a) Explain how your system translates the cognitive model's understanding of {t['emotion']} into musical parameters.
   b) Describe specific musical features or patterns your system would use to evoke {t['emotion']}.
   c) Discuss how these features align with psychological research on music and emotion.
   d) Address how the {t['cultural_context']} context influences this mapping.

3. Composition Process (250-300 words):
   a) Provide a step-by-step explanation of how your system would compose a piece of music to evoke {t['emotion']}.
   b) Explain how the system would manipulate {t['musical_element']} to achieve the desired emotional effect.
   c) Describe how the system would ensure musical coherence and aesthetic quality.
   d) Discuss how the composition process incorporates {t['cultural_context']} musical traditions.

4. Evaluation Mechanism (200-250 words):
   a) Propose a method for your system to evaluate the emotional impact of its compositions.
   b) Explain how this evaluation aligns with the {t['cognitive_model']}.
   c) Discuss potential challenges in accurately assessing emotional responses to music across different cultural backgrounds.
   d) Suggest how to validate the system's effectiveness in evoking emotions in the {t['cultural_context']} context.

5. Ethical Considerations (200-250 words):
   a) Discuss potential ethical implications of using AI to manipulate emotions through music.
   b) Consider possible misuses of this technology and propose safeguards.
   c) Explore the broader societal impact of emotionally intelligent music AI.
   d) Address ethical concerns related to cultural appropriation or misrepresentation in AI-generated music.

6. Future Developments (150-200 words):
   a) Suggest potential enhancements or applications of your system.
   b) Discuss how this technology might influence the fields of music therapy, AI creativity, or emotional intelligence in AI.
   c) Propose ways to expand the system's cultural versatility and sensitivity.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, artificial intelligence, and cultural diversity in music. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address all 6 sections outlined in the instructions",
            f"The system design should incorporate the {t['cognitive_model']} of emotion",
            f"The composition process should explain how {t['musical_element']} is manipulated to evoke {t['emotion']}",
            f"The response should demonstrate consideration of the {t['cultural_context']} cultural context",
            "The response should show understanding of cognitive science, music theory, AI, and cultural diversity in music",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The ethical considerations should be thoughtfully explored, including cultural sensitivity",
            "The response should use appropriate technical terminology and provide clear explanations"
        ]
        score = eval_with_llm_judge(instructions, submission, criteria)
        return score  # This now returns the raw score from the LLM judge, allowing for partial credit
