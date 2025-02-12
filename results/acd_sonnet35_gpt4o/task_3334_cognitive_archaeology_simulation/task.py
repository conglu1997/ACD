import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ancient_society": "Neolithic farmers of Çatalhöyük",
                "time_period": "7100-5700 BCE",
                "archaeological_mystery": "Purpose and meaning of elaborate wall paintings and sculptures",
                "cognitive_focus": "Symbolic thinking and artistic expression"
            },
            {
                "ancient_society": "Mayan civilization of Copán",
                "time_period": "5th-9th century CE",
                "archaeological_mystery": "Development and use of complex writing system",
                "cognitive_focus": "Language processing and symbolic representation"
            },
            {
                "ancient_society": "Upper Paleolithic humans in Europe",
                "time_period": "40,000-10,000 BCE",
                "archaeological_mystery": "Creation and purpose of cave paintings",
                "cognitive_focus": "Visual processing and symbolic communication"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered simulation system to model and analyze the cognitive processes of {t['ancient_society']} ({t['time_period']}), then use it to investigate the archaeological mystery of {t['archaeological_mystery']}. Your simulation should focus on {t['cognitive_focus']}. Your response should include the following sections:

1. Simulation System Architecture (300-350 words):
   a) Describe the key components of your AI-powered cognitive simulation system.
   b) Explain how your system models ancient cognitive processes, particularly {t['cognitive_focus']}.
   c) Detail how your system integrates archaeological data, cognitive science theories, and AI techniques.
   d) Provide a diagram or schematic representation of your system (describe it in words).

2. Cognitive Modeling Approach (250-300 words):
   a) Explain your approach to modeling the cognitive processes of {t['ancient_society']}.
   b) Describe how you account for cultural and environmental factors in your cognitive model.
   c) Discuss any assumptions or limitations in modeling ancient cognition.

3. Data Integration and Analysis (200-250 words):
   a) Describe the types of archaeological and anthropological data your system uses.
   b) Explain how your system processes and integrates this data into the cognitive simulation.
   c) Discuss any novel data analysis techniques you've incorporated.

4. Investigation of Archaeological Mystery (250-300 words):
   a) Describe how you use your simulation system to investigate {t['archaeological_mystery']}.
   b) Present a hypothesis about the mystery based on your simulation results.
   c) Explain how your cognitive model provides new insights into this archaeological question.

5. Validation and Verification (200-250 words):
   a) Propose methods to validate your simulation results against known archaeological evidence.
   b) Discuss potential challenges in verifying cognitive models of ancient societies.
   c) Suggest ways to improve the accuracy and reliability of your simulation system.

6. Ethical Considerations and Implications (200-250 words):
   a) Discuss ethical considerations in using AI to model ancient cognition and interpret cultural artifacts.
   b) Address potential biases in your approach and how to mitigate them.
   c) Explore the broader implications of your work for understanding human cognitive evolution.

Ensure your response demonstrates a deep understanding of cognitive science, archaeology, anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section, numbered as above (1-6). Use subheadings (a, b, c) within each section to address specific points. Begin each section on a new line. Your total response should be between 1400-1700 words, adhering to the word limits specified for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive science, archaeology, anthropology, and artificial intelligence",
            f"The simulation system effectively models ancient cognitive processes, particularly {t['cognitive_focus']}",
            f"The approach to investigating {t['archaeological_mystery']} is creative and scientifically plausible",
            "The response addresses ethical considerations and potential biases in modeling ancient cognition",
            "The proposed validation and verification methods are appropriate and well-reasoned",
            "The response is well-structured, clear, and within the specified word limit",
            "The response includes all required sections and subsections",
            "The diagram or schematic representation of the system is clearly described",
            "The hypothesis presented is logical and supported by the simulation results",
            "The response demonstrates cultural sensitivity and awareness of the limitations in interpreting ancient societies"
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
