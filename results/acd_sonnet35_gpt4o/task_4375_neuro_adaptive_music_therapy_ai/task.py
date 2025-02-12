import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "condition": "Post-traumatic stress disorder (PTSD)",
                "brain_region": "Amygdala",
                "therapeutic_goal": "Reduce anxiety and hyperarousal"
            },
            {
                "condition": "Major depressive disorder",
                "brain_region": "Prefrontal cortex",
                "therapeutic_goal": "Improve mood and cognitive function"
            },
            {
                "condition": "Attention deficit hyperactivity disorder (ADHD)",
                "brain_region": "Dorsolateral prefrontal cortex",
                "therapeutic_goal": "Enhance attention and executive function"
            },
            {
                "condition": "Chronic pain",
                "brain_region": "Anterior cingulate cortex",
                "therapeutic_goal": "Reduce pain perception and improve pain management"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates personalized music therapy sessions based on real-time brain activity, focusing on patients with {t['condition']}. Your system should specifically target activity in the {t['brain_region']} and aim to {t['therapeutic_goal']}. Your response should include the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for neuro-adaptive music therapy.
   b) Explain how these components interact to process brain activity data and generate music.
   c) Detail how your system adapts to real-time changes in neural activity.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Neural Data Processing (200-250 words):
   a) Explain how your system processes and interprets brain activity data from the {t['brain_region']}.
   b) Describe the specific neural markers or patterns your system looks for.
   c) Discuss how your system handles noise and variability in neural signals.
   d) Explain how you ensure the privacy and security of patients' brain data.

3. Music Generation Algorithm (250-300 words):
   a) Describe the AI algorithm used for generating therapeutic music.
   b) Explain how your algorithm incorporates principles of music therapy.
   c) Detail how the generated music adapts to changes in brain activity.
   d) Provide an example of how your system would alter the music in response to a specific change in neural activity.

4. Therapeutic Application (200-250 words):
   a) Explain how your system addresses the specific therapeutic goal to {t['therapeutic_goal']}.
   b) Describe how you measure the effectiveness of the generated music therapy.
   c) Discuss potential risks or contraindications of your approach.
   d) Propose a method for integrating your AI system with traditional music therapy practices.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI-generated music for therapy.
   b) Address potential concerns about AI interpreting and influencing brain activity.
   c) Propose guidelines for the responsible development and use of neuro-adaptive AI music therapy.

6. Future Developments (150-200 words):
   a) Suggest potential improvements or extensions to your system.
   b) Discuss how your system could be adapted for other neurological or psychiatric conditions.
   c) Propose a novel research direction that could emerge from your work on neuro-adaptive music therapy AI.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music therapy. Be creative in your approach while maintaining scientific and medical plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and music therapy principles.",
            "The AI system design is innovative, plausible, and well-explained, with a clear architecture and example of how it adapts to neural activity.",
            "The neural data processing component is scientifically grounded and addresses practical considerations like noise handling and data privacy.",
            "The music generation algorithm effectively incorporates music therapy principles and adapts to brain activity in a meaningful way.",
            "The therapeutic application is well-reasoned, addresses the specific condition and goal, and considers integration with traditional practices.",
            "The response specifically addresses the given condition ({t['condition']}) and brain region ({t['brain_region']}) in a meaningful way.",
            "Ethical implications are thoroughly analyzed, and responsible development guidelines are proposed.",
            "Future developments and research directions are innovative and relevant.",
            "The response is well-structured, using appropriate terminology and clear explanations for complex concepts.",
            "The total response falls within the 1200-1500 word range, with each section adhering to the specified word count."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
