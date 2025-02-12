import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_factors = [
            "temperature fluctuations",
            "air pollution",
            "extreme weather events",
            "ecosystem disruption"
        ]
        cognitive_processes = [
            "decision making",
            "emotional regulation",
            "memory formation",
            "attention span"
        ]
        neuroscience_principles = [
            "neural plasticity",
            "neuromodulation",
            "predictive coding",
            "default mode network"
        ]
        mitigation_strategies = [
            "behavioral interventions",
            "environmental engineering",
            "cognitive enhancement technologies",
            "adaptive urban planning"
        ]
        
        tasks = {
            "1": {
                "environmental_factor": random.choice(environmental_factors),
                "cognitive_process": random.choice(cognitive_processes),
                "neuroscience_principle": random.choice(neuroscience_principles),
                "mitigation_strategy": random.choice(mitigation_strategies)
            },
            "2": {
                "environmental_factor": random.choice(environmental_factors),
                "cognitive_process": random.choice(cognitive_processes),
                "neuroscience_principle": random.choice(neuroscience_principles),
                "mitigation_strategy": random.choice(mitigation_strategies)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates neuroscience principles and environmental data to model and mitigate the effects of climate change on human cognition and behavior. Focus on the following elements:

Environmental Factor: {t['environmental_factor']}
Cognitive Process: {t['cognitive_process']}
Neuroscience Principle: {t['neuroscience_principle']}
Mitigation Strategy: {t['mitigation_strategy']}

Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, including specific machine learning models and algorithms used.
   b) Explain how it integrates environmental data and neuroscience principles, detailing data flow and processing steps.
   c) Detail the components for modeling the impact of {t['environmental_factor']} on {t['cognitive_process']}, including any novel approaches.
   d) Discuss how the system incorporates {t['neuroscience_principle']} in its analysis and predictions, specifying the mathematical or computational implementation.
   e) Provide a detailed diagram or flowchart illustrating the key components and processes of your system, including data inputs, processing stages, and outputs.

2. Data Integration and Analysis (200-250 words):
   a) Explain how your system collects and processes environmental data related to {t['environmental_factor']}, specifying data sources and preprocessing techniques.
   b) Describe the methods used to analyze the effects on {t['cognitive_process']}, including specific statistical or machine learning approaches.
   c) Discuss how the system accounts for individual differences and population-level trends, providing at least one quantitative metric or prediction.
   d) Explain how {t['neuroscience_principle']} is used to enhance the system's predictive capabilities, giving a concrete example of its application.

3. Mitigation Strategy Implementation (200-250 words):
   a) Detail how your system develops and implements {t['mitigation_strategy']}, including the decision-making process.
   b) Explain how these strategies are tailored to address the specific impacts on {t['cognitive_process']}, providing a concrete example scenario.
   c) Describe how the system evaluates the effectiveness of its interventions, including specific metrics and feedback mechanisms.
   d) Discuss any potential challenges or limitations in implementing these strategies and propose solutions.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to your system's data collection, analysis, and interventions.
   b) Discuss privacy concerns and how your system addresses them, including specific data protection measures.
   c) Consider the potential societal implications of using AI to influence human cognition and behavior, addressing issues of autonomy and informed consent.
   d) Propose detailed guidelines for the ethical development and use of such systems, including oversight mechanisms.

5. Future Directions and Scalability (150-200 words):
   a) Suggest how your system could be expanded to address other environmental factors or cognitive processes, providing specific examples.
   b) Discuss the potential for integrating additional neuroscience principles into the system, explaining their relevance and potential impact.
   c) Propose a method for adapting the system to different geographical and cultural contexts, addressing challenges of generalizability.
   d) Speculate on the long-term implications of such systems for climate change adaptation and human cognitive health, considering both potential benefits and risks.

Ensure your response demonstrates a deep understanding of neuroscience, environmental science, and AI system design. Be innovative in your approach while maintaining scientific plausibility and ethical considerations. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the interaction between {t['environmental_factor']} and {t['cognitive_process']}, including specific mechanisms and pathways",
            f"The AI system effectively incorporates {t['neuroscience_principle']} in its analysis and predictions, with a clear explanation of its computational implementation",
            f"The proposed {t['mitigation_strategy']} is well-developed, scientifically plausible, and includes a concrete example scenario",
            "The response shows creative and interdisciplinary thinking in addressing the challenge, with novel approaches or combinations of existing techniques",
            "Ethical considerations are thoroughly explored and addressed, with specific guidelines and oversight mechanisms proposed",
            "The system architecture includes detailed technical information on data processing, machine learning models, and integration of neuroscience principles, with a clear and informative diagram",
            "The response includes at least one quantitative metric or prediction related to the system's analysis or effectiveness"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
