import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artifacts = [
            "Paleolithic stone tools",
            "Neolithic pottery",
            "Bronze Age weaponry",
            "Iron Age jewelry"
        ]
        cognitive_processes = [
            "Spatial reasoning",
            "Symbolic thinking",
            "Social cognition",
            "Technological innovation"
        ]
        time_periods = [
            "100,000 BCE",
            "10,000 BCE",
            "3,000 BCE",
            "500 BCE"
        ]
        
        tasks = {}
        for i in range(2):
            artifact = random.choice(artifacts)
            process = random.choice(cognitive_processes)
            period = random.choice(time_periods)
            
            tasks[str(i+1)] = {
                "artifact": artifact,
                "cognitive_process": process,
                "time_period": period
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze archaeological artifacts and reconstruct ancient cognitive processes, then use it to simulate the evolution of human problem-solving capabilities. Your system should focus on {t['artifact']} from around {t['time_period']}, with a particular emphasis on reconstructing the cognitive process of {t['cognitive_process']}.

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for analyzing artifacts and reconstructing cognitive processes.
   b) Explain how your system integrates knowledge from archaeology, cognitive science, and evolutionary psychology.
   c) Detail any novel algorithms or techniques used in your system.
   d) Discuss how your system handles uncertainty and incomplete data in archaeological contexts.

2. Artifact Analysis (250-300 words):
   a) Explain how your AI system would analyze {t['artifact']} from {t['time_period']}.
   b) Describe the features or characteristics your system would focus on.
   c) Discuss how your system would infer cognitive processes from physical artifacts.
   d) Explain how your analysis accounts for the historical and cultural context of the artifacts.

3. Cognitive Process Reconstruction (250-300 words):
   a) Detail how your system reconstructs the cognitive process of {t['cognitive_process']} based on the artifact analysis.
   b) Explain the theoretical framework your system uses to model ancient cognition.
   c) Describe how your system accounts for the evolution of cognitive processes over time.
   d) Discuss any assumptions or limitations in reconstructing ancient thought processes.

4. Evolutionary Simulation (250-300 words):
   a) Explain how your system simulates the evolution of problem-solving capabilities from {t['time_period']} to the present.
   b) Describe the parameters and variables used in your evolutionary model.
   c) Discuss how your simulation accounts for environmental and cultural factors in cognitive evolution.
   d) Provide an example of a specific problem-solving capability and how it might have evolved according to your model.

5. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your system for our understanding of human cognitive evolution.
   b) Explain how your system could be applied to other areas of archaeological or cognitive research.
   c) Describe how insights from your system might inform modern cognitive science or AI development.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in using AI to reconstruct and simulate ancient cognition.
   b) Discuss the implications of using such systems to make inferences about past cultures and societies.
   c) Propose guidelines for the responsible development and use of cognitive archaeological AI systems.

Ensure your response demonstrates a deep understanding of archaeology, cognitive science, and AI technologies. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['artifact']}, the time period around {t['time_period']}, and the cognitive process of {t['cognitive_process']}.",
            "The AI system architecture integrates knowledge from archaeology, cognitive science, and evolutionary psychology in a novel and plausible manner.",
            "The artifact analysis and cognitive process reconstruction methods are well-explained and scientifically grounded.",
            "The evolutionary simulation of problem-solving capabilities is creative and considers relevant factors.",
            "The implications, applications, and ethical considerations are thoroughly addressed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The writing is clear, well-organized, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
