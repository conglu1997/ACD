import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        communication_aspects = [
            {
                'focus': 'Emotional States',
                'constraint': 'Temporal Dynamics'
            },
            {
                'focus': 'Abstract Concepts',
                'constraint': 'Information Density'
            },
            {
                'focus': 'Sensory Experiences',
                'constraint': 'Energy Efficiency'
            },
            {
                'focus': 'Memory Retrieval',
                'constraint': 'Signal Interference'
            },
            {
                'focus': 'Decision-Making Processes',
                'constraint': 'Cognitive Load'
            }
        ]
        
        tasks = [
            random.choice(communication_aspects),
            random.choice(communication_aspects)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network-based language for direct brain-to-brain communication, focusing on {t['focus']} and constrained by {t['constraint']}. Then, analyze its potential impact and propose experiments to test it. Your response should include:

1. Neural Language Design (300-350 words):
   a) Describe the basic structure and components of your neural network language.
   b) Explain how it encodes and transmits information related to {t['focus']}.
   c) Detail how the language addresses the constraint of {t['constraint']}.
   d) Provide an example of how a simple concept or experience would be communicated in this language.
   e) Include a simple ASCII diagram or schematic representing the structure of your neural language, using characters such as |, -, +, >, <, and ^.

2. Cognitive Mechanisms (250-300 words):
   a) Explain how your language interfaces with existing brain structures and processes.
   b) Describe any novel cognitive mechanisms that might emerge from using this language.
   c) Discuss how the language might handle complex or abstract thoughts.
   d) Address potential challenges in learning and adapting to this new form of communication.

3. Societal and Ethical Implications (200-250 words):
   a) Analyze how widespread adoption of this neural language might impact society and culture.
   b) Discuss potential benefits and risks to individual privacy and autonomy.
   c) Explore how this technology might affect social interactions and relationships.
   d) Address ethical concerns related to equity of access and potential for misuse.

4. Comparative Analysis (150-200 words):
   a) Compare your neural network language to traditional spoken and written languages.
   b) Discuss how this comparison might inform our understanding of human cognition and communication.
   c) Identify potential limitations or drawbacks of your proposed neural network language.

5. Experimental Design (250-300 words):
   Propose two experiments to test the efficacy and impact of your neural network language:
   a) Experiment 1: Design an experiment to test how well your language facilitates communication of {t['focus']}.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would validate (or invalidate) your language design.
   b) Experiment 2: Design an experiment to evaluate how your language handles the constraint of {t['constraint']}.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would demonstrate your language's effectiveness.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and cognitive science. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and cognitive science.",
            "The neural language design is creative, plausible, and well-suited for the specified focus and constraint.",
            "The cognitive mechanisms are clearly explained and consider both existing brain structures and potential novel processes.",
            "The societal and ethical implications are thoroughly analyzed, considering both benefits and risks.",
            "The comparative analysis with traditional languages is insightful and informative, including potential limitations of the proposed language.",
            "The proposed experiments are well-designed and would effectively test the language's efficacy and impact.",
            "The response uses technical terminology appropriately and provides clear explanations.",
            "The overall response is well-structured, coherent, and adheres to the specified format and word count.",
            "The ASCII diagram or schematic effectively represents the structure of the designed neural language.",
            "The response includes specific examples of how the neural language would communicate concepts related to the given focus and constraint."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
