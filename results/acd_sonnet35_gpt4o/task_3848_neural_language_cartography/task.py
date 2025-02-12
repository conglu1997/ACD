import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_processes = ['phonological processing', 'syntactic parsing', 'semantic integration', 'pragmatic interpretation']
        brain_regions = ['Broca\'s area', 'Wernicke\'s area', 'angular gyrus', 'superior temporal gyrus']
        applications = ['neurolinguistic research', 'language disorder diagnosis', 'brain-computer interfaces', 'AI language model development']
        
        tasks = {
            "1": {
                "process": random.choice(language_processes),
                "region": random.choice(brain_regions),
                "application": random.choice(applications)
            },
            "2": {
                "process": random.choice(language_processes),
                "region": random.choice(brain_regions),
                "application": random.choice(applications)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical neural interface system that can map and visualize language processing in the brain in real-time, focusing on {t['process']} in the {t['region']}. Then, analyze its potential application in {t['application']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your neural interface system.
   b) Explain how your system detects and interprets neural signals related to {t['process']}.
   c) Detail the methods used to visualize language processing in real-time.
   d) Discuss any novel technologies or techniques used in your design.

2. Language Processing Visualization (200-250 words):
   a) Explain how your system specifically maps and visualizes {t['process']} in the {t['region']}.
   b) Describe the type of data or patterns your system would capture.
   c) Propose a method for distinguishing language-related neural activity from other cognitive processes.

3. Application Analysis (200-250 words):
   a) Analyze how your system could be applied to {t['application']}.
   b) Discuss the potential benefits and challenges of using this technology in this specific application.
   c) Propose a concrete example of how the system would be used in this context.

4. Integration with AI Language Models (150-200 words):
   a) Explain how the data from your neural interface system could be used to improve AI language models.
   b) Discuss potential challenges in translating neural language processing data to AI algorithms.
   c) Propose a novel approach to bridging human and artificial language processing.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to mapping and visualizing language processing in the brain.
   b) Discuss privacy concerns and propose safeguards for protecting individuals' cognitive data.
   c) Analyze potential societal implications of this technology, both positive and negative.

6. Future Developments (150-200 words):
   a) Propose potential future enhancements or expansions of your system.
   b) Discuss how this technology might evolve over the next decade.
   c) Speculate on how widespread adoption of this technology could impact society and human communication.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['process']} and its relation to the {t['region']}.",
            f"The proposed system architecture is innovative and scientifically plausible for mapping and visualizing language processing.",
            f"The analysis of the system's application in {t['application']} is thorough and insightful.",
            "The integration with AI language models is well-explained and demonstrates understanding of both neuroscience and AI.",
            "Ethical considerations are thoughtfully addressed, including privacy concerns and potential societal impacts.",
            "The response is creative, well-structured, and adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
