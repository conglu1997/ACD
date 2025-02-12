import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "mental_health_condition": "depression",
                "brain_region": "prefrontal cortex",
                "music_genre": "classical"
            },
            {
                "mental_health_condition": "anxiety",
                "brain_region": "amygdala",
                "music_genre": "ambient"
            },
            {
                "mental_health_condition": "PTSD",
                "brain_region": "hippocampus",
                "music_genre": "world music"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates personalized therapeutic music based on real-time brain activity analysis, and evaluate its potential impact on mental health treatment. Your system should focus on the mental health condition of {t['mental_health_condition']}, primarily involve the {t['brain_region']}, and generate music in the {t['music_genre']} genre. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neuro-adaptive music therapy.
   b) Explain how your system analyzes brain activity in real-time, focusing on the {t['brain_region']}.
   c) Detail how the AI generates personalized music based on the analyzed brain activity.
   d) Discuss how your system specifically addresses {t['mental_health_condition']} through {t['music_genre']} music.

2. Neuroscientific Basis (250-300 words):
   a) Explain the neuroscientific principles underlying your system's approach to {t['mental_health_condition']}.
   b) Discuss how activity in the {t['brain_region']} relates to {t['mental_health_condition']} and how your system targets this relationship.
   c) Describe how your system adapts to individual differences in neural patterns and responses to music.

3. AI and Music Generation (250-300 words):
   a) Describe the AI architecture used for music generation in the {t['music_genre']} genre.
   b) Explain how musical elements are selected and combined based on brain activity data.
   c) Discuss any novel algorithms or approaches necessary for real-time adaptive composition.

4. Therapeutic Process Analysis (200-250 words):
   a) Analyze how this AI system might enhance current music therapy practices for {t['mental_health_condition']}.
   b) Discuss potential benefits and challenges compared to traditional music therapy methods.
   c) Explore how the system might influence our understanding of the relationship between music and mental health.

5. Clinical Application and Evaluation (200-250 words):
   a) Propose a clinical trial design to evaluate the efficacy of your system for treating {t['mental_health_condition']}.
   b) Discuss potential outcome measures and how you would assess the system's impact.
   c) Address potential challenges in implementing this technology in clinical settings.

6. Ethical Considerations (150-200 words):
   a) Identify and discuss at least two ethical concerns raised by your neuro-adaptive music therapy system.
   b) Propose guidelines for the responsible development and use of such technology in mental health treatment.
   c) Discuss potential impacts on music therapists and the mental health care industry.

7. Future Research Directions (100-150 words):
   a) Propose two potential extensions or applications of your neuro-adaptive music therapy system.
   b) Suggest experiments that could further explore the relationship between brain activity, music, and mental health.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, music theory, and mental health treatment. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and clinical relevance.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, music theory, and mental health treatment",
            f"The system architecture effectively addresses {t['mental_health_condition']} using {t['music_genre']} music and focuses on the {t['brain_region']}",
            "The AI and music generation approach is innovative and scientifically plausible",
            "The response includes a well-designed clinical trial proposal and addresses ethical considerations",
            "The writing is clear, well-structured, and within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
