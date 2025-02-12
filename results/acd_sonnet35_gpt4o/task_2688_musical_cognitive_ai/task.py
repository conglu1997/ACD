import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre']
        cognitive_processes = ['memory', 'attention', 'emotion', 'decision-making']
        application_domains = ['data analysis', 'pattern recognition', 'natural language processing', 'creative problem-solving']
        
        tasks = [
            {
                'musical_element': random.choice(musical_elements),
                'cognitive_process': random.choice(cognitive_processes),
                'application_domain': random.choice(application_domains),
                'example_data': 'C4-E4-G4-C5 chord progression'
            },
            {
                'musical_element': random.choice(musical_elements),
                'cognitive_process': random.choice(cognitive_processes),
                'application_domain': random.choice(application_domains),
                'example_data': '4/4 time signature with syncopated rhythm'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses {t['musical_element']} as a fundamental structure for information encoding and processing, based on cognitive neuroscience theories of how the brain processes music in relation to {t['cognitive_process']}. Then, apply your system to a problem in the domain of {t['application_domain']}. Use the following example data as a starting point for your design: {t['example_data']}.

Your response should include:

1. Theoretical Framework (200-250 words):
   a) Explain how {t['musical_element']} is processed in the human brain.
   b) Describe how this relates to the cognitive process of {t['cognitive_process']}.
   c) Propose a model for how {t['musical_element']} could be used to encode and process information in an AI system.

2. System Architecture (250-300 words):
   a) Outline the key components of your AI system.
   b) Explain how your system encodes information using {t['musical_element']}.
   c) Describe how your system processes this information to perform tasks.
   d) Discuss any novel algorithms or techniques your system employs.

3. Application to {t['application_domain']} (250-300 words):
   a) Describe a specific problem in {t['application_domain']} that your system could address.
   b) Explain how your musical cognitive AI system would approach this problem.
   c) Compare your approach to traditional methods in this domain.
   d) Provide a concrete example of how your system would process the given example data ({t['example_data']}) in this application.

4. Implementation Details (200-250 words):
   a) Provide a high-level pseudocode or flowchart of a key algorithm in your system.
   b) Explain how this algorithm incorporates both musical and cognitive elements.
   c) Describe how the algorithm would process the example data ({t['example_data']}).

5. Evaluation and Testing (150-200 words):
   a) Propose methods to evaluate the performance of your system.
   b) Describe an experiment to test the effectiveness of your musical cognitive AI approach.
   c) Discuss potential challenges in evaluating such a novel system.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical concerns related to using music-inspired AI systems.
   b) Explore broader implications for our understanding of cognition and AI.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how your approach could be applied to other domains or cognitive processes.

Ensure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and AI technologies. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Theoretical Framework:') followed by your response for that section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive neuroscience, and AI technologies.",
            f"The theoretical framework effectively explains how {t['musical_element']} is processed in the brain and relates to {t['cognitive_process']}.",
            "The system architecture is innovative and clearly explains how musical elements are used for information encoding and processing.",
            f"The application to {t['application_domain']} is well-explained and demonstrates the potential advantages of the musical cognitive AI approach.",
            f"The response includes a concrete example of how the system would process the given example data ({t['example_data']}) in the application domain.",
            "The implementation details include a clear algorithm or flowchart that incorporates both musical and cognitive elements and explains how it would process the example data.",
            "The evaluation and testing section proposes valid methods and experiments to assess the system's performance.",
            "Ethical and societal implications are thoughtfully considered.",
            "Future directions are insightful and demonstrate the potential for further development.",
            "The response is creative and innovative while maintaining scientific and technological plausibility.",
            "All sections are adequately addressed within the specified word count ranges and formatted correctly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
