class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "time_period": "Upper Paleolithic",
                "artifact": "Cave paintings"
            },
            "2": {
                "time_period": "Neolithic",
                "artifact": "Early writing systems"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = """Design a novel computational model to simulate the cognitive processes of early humans during the {time_period} period, based on archaeological evidence and modern neuroscience. Then, use your model to analyze the development of symbolic thinking as evidenced by {artifact}. Your response should include:1. Cognitive Model Design (300-350 words):   a) Describe the architecture of your computational model for simulating early human cognition.   b) Explain how your model incorporates principles from modern neuroscience.   c) Detail how archaeological evidence from the {time_period} period informs your model's design.   d) Discuss any assumptions or limitations in your approach.2. Simulation of Cognitive Processes (250-300 words):   a) Explain how your model simulates key cognitive processes relevant to the development of symbolic thinking.   b) Describe how these processes might have evolved during the {time_period} period.   c) Discuss how your model accounts for environmental and social factors that may have influenced cognitive development.3. Analysis of Symbolic Thinking (250-300 words):   a) Use your model to analyze the cognitive processes involved in creating and understanding {artifact}.   b) Explain how your simulation provides insights into the development of symbolic thinking.   c) Discuss any discrepancies between your model's predictions and the archaeological evidence.4. Comparative Analysis (200-250 words):   a) Compare the cognitive processes simulated by your model to those of modern humans.   b) Identify key differences and similarities in symbolic thinking capabilities.   c) Speculate on the evolutionary pressures that may have driven these changes.5. Interdisciplinary Implications (200-250 words):   a) Discuss how your model and its results might inform or challenge current theories in archaeology and cognitive science.   b) Explain how this approach could be applied to other questions in cognitive archaeology.   c) Propose a specific research question that could be explored using your model.6. Ethical Considerations (150-200 words):   a) Discuss the ethical implications of using computational models to study ancient cognition.   b) Address potential biases in your model and how they might affect interpretations of human cognitive evolution.   c) Propose guidelines for the responsible use of such models in archaeological and cognitive research.Ensure your response demonstrates a deep understanding of cognitive science, archaeology, and neuroscience. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.Format your response with clear headings for each section. Your total response should be between 1350-1650 words.Important notes:1. A computational model in this context refers to a set of algorithms or mathematical representations that simulate cognitive processes. Your model should be able to process inputs and generate outputs that mimic aspects of early human cognition.2. While your model should be novel, it can be inspired by existing principles in cognitive science and neuroscience. The innovation lies in how you apply and combine these principles to simulate early human cognition.3. Be creative in drawing connections between different fields. Consider how insights from neuroscience can inform your interpretation of archaeological evidence, and vice versa.4. Provide specific details about your model's architecture and functioning, avoiding vague or general descriptions.5. Do not use external resources or pre-existing models. Rely on your own knowledge and creative problem-solving abilities."""
        return base_instructions.format(**t)

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, archaeology, and neuroscience.",
            "The cognitive model design is innovative, well-explained, and scientifically plausible.",
            "The simulation of cognitive processes and analysis of symbolic thinking are detailed and insightful.",
            "The comparative analysis and discussion of interdisciplinary implications show strong reasoning and creativity.",
            "The ethical considerations are thoughtful and demonstrate an understanding of the broader implications of the research.",
            "The response presents a novel computational model that creatively combines principles from different fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
