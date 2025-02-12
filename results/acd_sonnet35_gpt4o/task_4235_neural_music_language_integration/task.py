import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        linguistic_features = ['syntax', 'semantics', 'phonology', 'pragmatics']
        genres = ['pop', 'classical', 'jazz', 'hip-hop', 'folk']
        languages = ['English', 'Mandarin', 'Spanish', 'Arabic', 'Hindi']
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'musical_element': random.choice(musical_elements),
                'linguistic_feature': random.choice(linguistic_features),
                'genre': random.choice(genres),
                'language': random.choice(languages)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network model that simulates the brain's simultaneous processing of music and language, then apply it to analyze cross-modal interactions in song lyrics and melodies. Focus on the musical element of {t['musical_element']} and the linguistic feature of {t['linguistic_feature']} in the context of {t['genre']} music and {t['language']} lyrics. Your response should include the following sections:

1. Neuroscientific Framework (250-300 words):
   a) Explain the current understanding of how the brain processes music and language simultaneously.
   b) Describe the neural pathways and brain regions involved in processing {t['musical_element']} and {t['linguistic_feature']}.
   c) Discuss any known interactions or overlaps between these processes.

2. Neural Network Architecture (300-350 words):
   a) Design a neural network architecture that models the simultaneous processing of {t['musical_element']} and {t['linguistic_feature']}.
   b) Explain how your model incorporates neuroscientific principles in its design.
   c) Describe the input and output representations for both musical and linguistic information.
   d) Include a diagram or pseudocode representation of your model's key components.

3. Cross-modal Integration (200-250 words):
   a) Explain how your model integrates musical and linguistic information.
   b) Describe any novel mechanisms or algorithms used for cross-modal processing.
   c) Discuss how your model handles potential conflicts or synergies between {t['musical_element']} and {t['linguistic_feature']}.

4. Application to {t['genre']} Music and {t['language']} Lyrics (250-300 words):
   a) Apply your model to analyze a specific example of {t['genre']} music with {t['language']} lyrics.
   b) Describe how your model would process and interpret the musical and linguistic elements.
   c) Discuss any genre-specific or language-specific challenges and how your model addresses them.

5. Predictions and Hypotheses (150-200 words):
   a) Generate two testable predictions about cross-modal interactions in music and language processing based on your model.
   b) Propose an experiment to validate these predictions, including methodology and expected results.

6. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your model and potential areas for improvement.
   b) Suggest two future research directions that could extend or refine your approach.
   c) Consider potential applications of your model in cognitive science, music therapy, or language learning.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the musical element of {t['musical_element']} and the linguistic feature of {t['linguistic_feature']}.",
            f"The model effectively integrates principles from neuroscience, music theory, and computational linguistics.",
            f"The application to {t['genre']} music and {t['language']} lyrics is well-explained and plausible.",
            "The proposed neural network architecture is innovative and scientifically grounded.",
            "The response demonstrates a deep understanding of cross-modal interactions in music and language processing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
