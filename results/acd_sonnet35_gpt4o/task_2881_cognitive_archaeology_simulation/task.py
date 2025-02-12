import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "artifact": "Paleolithic cave paintings",
                "cognitive_process": "Symbolic thinking",
                "brain_region": "Prefrontal cortex"
            },
            {
                "artifact": "Neolithic pottery patterns",
                "cognitive_process": "Spatial reasoning",
                "brain_region": "Parietal lobe"
            },
            {
                "artifact": "Bronze Age writing systems",
                "cognitive_process": "Language processing",
                "brain_region": "Broca's and Wernicke's areas"
            },
            {
                "artifact": "Iron Age metallurgy techniques",
                "cognitive_process": "Causal reasoning",
                "brain_region": "Dorsolateral prefrontal cortex"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational simulation of ancient cognitive processes based on the archaeological artifact of {t['artifact']}, focusing on the cognitive process of {t['cognitive_process']} and its relation to the {t['brain_region']}. Your task is to create an innovative model that integrates archaeological evidence, neuroimaging data, and evolutionary psychology principles.

Provide your response in the following format:

1. Archaeological Context (150-200 words):
   Describe the chosen artifact and its historical context. Explain its significance in understanding ancient cognition.

2. Cognitive Process Analysis (200-250 words):
   a) Analyze the specific cognitive process associated with the artifact.
   b) Explain how this process might have evolved and its importance in human cognitive development.
   c) Describe how the specified brain region is involved in this cognitive process.

3. Computational Model Design (300-350 words):
   a) Propose a computational model that simulates the identified cognitive process in the context of the ancient artifact.
   b) Explain how your model incorporates neuroimaging data and evolutionary psychology principles.
   c) Describe the key components and algorithms of your model.
   d) Include a high-level pseudocode or flow diagram of your simulation.

4. Data Integration (200-250 words):
   a) Explain how archaeological data would be used to inform and validate your model.
   b) Describe how you would integrate modern neuroimaging data into your simulation of ancient cognition.
   c) Discuss any challenges in reconciling ancient evidence with modern neuroscientific understanding.

5. Simulation Outcomes and Interpretation (200-250 words):
   a) Describe the expected outcomes of your simulation.
   b) Explain how these outcomes could provide insights into ancient cognitive processes.
   c) Discuss how your simulation results could be validated or tested against archaeological evidence.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your computational model could impact the fields of archaeology, neuroscience, and evolutionary psychology.
   b) Propose a novel hypothesis about ancient cognition that could be tested using your model.

7. Ethical Considerations and Limitations (100-150 words):
   a) Identify potential ethical issues or limitations in simulating and interpreting ancient cognition.
   b) Propose guidelines for responsible use and interpretation of such simulations in archaeological and cognitive science research.

Ensure your response demonstrates a deep understanding of cognitive archaeology, neuroscience, and computational modeling. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the archaeological artifact of {t['artifact']}, the cognitive process of {t['cognitive_process']}, and its relation to the {t['brain_region']}",
            "The computational model design should be innovative, coherent, and demonstrate a clear understanding of cognitive archaeology principles",
            "The response should show interdisciplinary integration of archaeology, neuroscience, and computational modeling",
            "The simulation outcomes and interpretation should be thoughtful and well-reasoned",
            "The proposed interdisciplinary implications and novel hypothesis should be creative and relevant to the fields involved"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
