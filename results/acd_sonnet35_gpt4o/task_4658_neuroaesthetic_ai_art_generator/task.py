import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_forms = ['visual art', 'music', 'poetry', 'dance']
        brain_regions = ['prefrontal cortex', 'insula', 'amygdala', 'hippocampus']
        aesthetic_qualities = ['beauty', 'sublimity', 'humor', 'novelty']
        
        return {
            "1": {
                "art_form": random.choice(art_forms),
                "brain_region": random.choice(brain_regions),
                "aesthetic_quality": random.choice(aesthetic_qualities)
            },
            "2": {
                "art_form": random.choice(art_forms),
                "brain_region": random.choice(brain_regions),
                "aesthetic_quality": random.choice(aesthetic_qualities)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a series of neuroscience experiments to study the neural basis of aesthetic experiences, focusing on {t['aesthetic_quality']} in {t['art_form']}, with particular attention to the role of the {t['brain_region']}. Then, propose an AI system that can generate novel {t['art_form']} based on these findings. Your response should include the following sections:

1. Experimental Design (300-350 words):
   a) Describe three experiments to investigate the neural correlates of {t['aesthetic_quality']} in {t['art_form']}, focusing on the {t['brain_region']}.
   b) Explain the methodology, including participant selection, stimuli, and data collection techniques.
   c) Discuss how you will control for confounding variables and ensure the validity of your results.
   d) Propose at least one novel neuroimaging technique or analysis method.

2. Data Analysis and Interpretation (200-250 words):
   a) Explain the data analysis techniques you will use to process the neuroimaging data.
   b) Describe how you will correlate neural activity with subjective aesthetic experiences.
   c) Discuss potential challenges in interpreting the results and how you would address them.
   d) Propose a method to quantify {t['aesthetic_quality']} based on neural activity patterns.

3. AI System Architecture (250-300 words):
   a) Propose an AI system capable of generating novel {t['art_form']} based on your experimental findings.
   b) Describe the key components and functionalities of your AI system.
   c) Explain how the system incorporates the neural correlates of {t['aesthetic_quality']} in its generative process.
   d) Discuss how the AI would simulate or interface with activity in the {t['brain_region']}.
   e) Provide a specific example of how your AI system would generate a piece of {t['art_form']}.

4. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to studying and artificially replicating aesthetic experiences.
   b) Address concerns about the impact of AI-generated art on human creativity and the art world.
   c) Propose guidelines for responsible development and use of neuroaesthetic AI systems.
   d) Discuss potential dual-use concerns and mitigation strategies.

5. Interdisciplinary Implications (200-250 words):
   a) Explain how your research and AI system could contribute to our understanding of human cognition and creativity.
   b) Discuss potential applications in fields such as art therapy, education, or human-computer interaction.
   c) Propose a related research direction that combines insights from your system with another scientific or artistic discipline.
   d) Speculate on how this technology might evolve in the next 20 years.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your experimental approach and AI system.
   b) Suggest two specific improvements or extensions to your research.
   c) Propose a follow-up study that could further explore the relationship between neural activity and aesthetic experience in {t['art_form']}.
   d) Discuss potential societal impacts of widespread adoption of neuroaesthetic AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, psychology, art theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of neuroaesthetics and its application to {t['art_form']}.",
            f"The experimental design should be well-thought-out, innovative, and focused on {t['aesthetic_quality']} and the {t['brain_region']}.",
            "The AI system proposal should be innovative, capable of generating novel art, and grounded in the experimental findings.",
            "The response should show a deep understanding of the interdisciplinary nature of neuroaesthetics and propose creative applications.",
            "Ethical considerations should be thoughtfully addressed, including dual-use concerns.",
            "The proposed future directions should be logical, build on the presented research, and consider long-term societal impacts.",
            "The response should adhere to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
