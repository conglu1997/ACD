import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'neurological_condition': 'anxiety disorders',
                'brain_region': 'amygdala',
                'musical_element': 'rhythm'
            },
            {
                'neurological_condition': 'depression',
                'brain_region': 'prefrontal cortex',
                'musical_element': 'harmony'
            },
            {
                'neurological_condition': 'ADHD',
                'brain_region': 'anterior cingulate cortex',
                'musical_element': 'tempo'
            },
            {
                'neurological_condition': 'chronic pain',
                'brain_region': 'insular cortex',
                'musical_element': 'timbre'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven neurofeedback system for personalized music therapy, focusing on treating {t['neurological_condition']} by targeting the {t['brain_region']} through modulation of {t['musical_element']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven neurofeedback system for music therapy.
   b) Explain how your system integrates real-time brain activity monitoring with AI-driven music generation.
   c) Detail how the system targets the {t['brain_region']} and modulates {t['musical_element']} to address {t['neurological_condition']}.
   d) Discuss any novel AI algorithms or approaches used in your system.
   e) Provide a simple diagram or pseudocode snippet (5-10 lines) illustrating a key aspect of your system design.

2. Neuroscientific Basis (250-300 words):
   a) Explain the neurological mechanisms underlying {t['neurological_condition']} and how they relate to the {t['brain_region']}.
   b) Describe how modulation of {t['musical_element']} can influence brain activity in the {t['brain_region']}.
   c) Discuss any relevant neuroscientific theories or studies that support your approach.

3. AI and Machine Learning Approach (250-300 words):
   a) Detail the machine learning algorithms used for analyzing brain activity and generating personalized music.
   b) Explain how your AI system learns and adapts to individual patient responses over time.
   c) Describe any data preprocessing or feature extraction techniques used in your system.

4. Music Theory Integration (200-250 words):
   a) Explain how your system incorporates music theory principles in generating therapeutic music.
   b) Describe how {t['musical_element']} is specifically manipulated to achieve the desired neurological effects.
   c) Discuss any challenges in balancing therapeutic efficacy with musical aesthetics.

5. Cross-Cultural Considerations (150-200 words):
   a) Discuss how your system accounts for cultural differences in music perception and emotional responses.
   b) Explain any adaptations necessary for the system to be effective across different cultural contexts.
   c) Address potential challenges in implementing your system globally.

6. Ethical Considerations and Safety Measures (200-250 words):
   a) Identify potential ethical concerns related to using AI and neurofeedback in music therapy.
   b) Propose safeguards to ensure patient safety and data privacy.
   c) Discuss how you would address issues of informed consent and potential psychological side effects.

7. Evaluation and Efficacy Assessment (200-250 words):
   a) Propose a method for evaluating the efficacy of your system in treating {t['neurological_condition']}.
   b) Describe specific outcome measures and how you would collect and analyze this data.
   c) Discuss potential limitations of your evaluation approach and how you might address them.

8. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research to advance your AI-driven neurofeedback system for music therapy.
   b) Briefly explain how these research directions could address current limitations or open up new possibilities.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music therapy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1650-2050 words. Present any diagrams or pseudocode as ASCII art or text-based representations within your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and music therapy.",
            "The system architecture is well-designed and integrates real-time brain activity monitoring with AI-driven music generation.",
            "The neuroscientific basis is well-explained and supported by relevant theories or studies.",
            "The AI and machine learning approach is detailed and appropriate for the task.",
            "Music theory principles are effectively incorporated into the system design.",
            "Cross-cultural considerations are thoughtfully addressed.",
            "Ethical considerations and safety measures are thoroughly addressed.",
            "The evaluation and efficacy assessment method is well-designed and considers potential limitations.",
            "Future research directions are relevant and well-justified.",
            "The response is innovative while maintaining scientific plausibility and ethical responsibility.",
            "The response adequately addresses all required sections with appropriate depth and clarity, adhering to the specified word counts.",
            "A simple diagram or pseudocode snippet is provided and effectively illustrates a key aspect of the system design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
