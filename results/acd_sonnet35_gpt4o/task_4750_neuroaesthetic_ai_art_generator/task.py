import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_styles = ['abstract expressionism', 'surrealism', 'minimalism', 'pop art', 'digital art']
        brain_regions = ['visual cortex', 'amygdala', 'prefrontal cortex', 'hippocampus', 'insula']
        cognitive_processes = ['attention', 'emotion', 'memory', 'decision-making', 'creativity']
        
        return {
            "1": {
                "art_style": random.choice(art_styles),
                "brain_region": random.choice(brain_regions),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "art_style": random.choice(art_styles),
                "brain_region": random.choice(brain_regions),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates art based on principles of neuroaesthetics and cognitive neuroscience, focusing on the art style of {t['art_style']}, the brain region {t['brain_region']}, and the cognitive process of {t['cognitive_process']}. Then, analyze its outputs and ethical implications. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI art generation system.
   b) Explain how it incorporates principles of neuroaesthetics and cognitive neuroscience.
   c) Detail how your system models the specified brain region and cognitive process.
   d) Discuss how these neural models influence the generation of {t['art_style']} art.

2. Artistic Process Simulation (200-250 words):
   a) Explain how your AI system simulates the artistic process.
   b) Describe how it generates {t['art_style']} art based on the activity of the {t['brain_region']}.
   c) Discuss how the system incorporates the cognitive process of {t['cognitive_process']} into its art generation.
   d) Provide a step-by-step example of how your system would create a specific artwork.

3. Neuroaesthetic Analysis (200-250 words):
   a) Analyze the generated art from a neuroaesthetic perspective.
   b) Explain how the artwork might engage the viewer's {t['brain_region']} and {t['cognitive_process']}.
   c) Discuss potential emotional and cognitive responses to the generated art.
   d) Compare your AI's output to human-created {t['art_style']} art in terms of neuroaesthetic principles.

4. Ethical Implications (200-250 words):
   a) Discuss ethical considerations of using AI to generate art based on neuroscientific principles.
   b) Analyze potential impacts on human artists and the art world.
   c) Consider implications for our understanding of creativity and consciousness.
   d) Propose guidelines for the responsible development and use of neuroaesthetic AI art systems.

5. Future Applications and Research (150-200 words):
   a) Suggest potential applications of your system in fields such as therapy, education, or entertainment.
   b) Propose two novel research questions that arise from your neuroaesthetic AI art system.
   c) Discuss how this technology might evolve in the next decade and its potential societal impacts.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and art theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and art theory.",
            f"The system architecture effectively incorporates principles of neuroaesthetics and cognitive neuroscience, with a focus on {t['brain_region']} and {t['cognitive_process']}.",
            f"The artistic process simulation convincingly explains how {t['art_style']} art is generated based on neural models.",
            "The neuroaesthetic analysis provides insightful connections between the generated art and human cognitive responses.",
            "Ethical implications are thoroughly considered, with thoughtful guidelines proposed.",
            "Future applications and research directions are innovative and well-reasoned.",
            "The response is well-structured, clear, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
