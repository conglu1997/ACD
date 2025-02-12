import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "aquatic",
                "communication_constraint": "limited visibility",
                "cognitive_focus": "spatial reasoning",
                "additional_factor": "pressure sensitivity"
            },
            {
                "environment": "arboreal",
                "communication_constraint": "need for long-distance signaling",
                "cognitive_focus": "categorical perception",
                "additional_factor": "balance adaptation"
            },
            {
                "environment": "subterranean",
                "communication_constraint": "limited auditory range",
                "cognitive_focus": "tactile information processing",
                "additional_factor": "echolocation"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the co-evolution of language and biological organisms in an {t['environment']} environment, with a focus on {t['cognitive_focus']} and the constraint of {t['communication_constraint']}. Additionally, consider the role of {t['additional_factor']} in this co-evolution process. Then, analyze its implications for understanding the relationship between communication, cognition, and biological adaptation. Your response should include the following sections:

1. Simulation Model Design (300-350 words):
   a) Describe the key components of your AI simulation model.
   b) Explain how your model integrates linguistic, biological, and cognitive elements.
   c) Detail how the model accounts for the given environment, communication constraint, cognitive focus, and additional factor.
   d) Include a brief diagram or flowchart description of your simulation model.

2. Language-Biology Co-evolution Mechanisms (250-300 words):
   a) Explain the mechanisms by which language and biological traits co-evolve in your model.
   b) Discuss how the {t['environment']} environment influences this co-evolution.
   c) Describe how the model handles the {t['communication_constraint']} constraint.
   d) Explain how {t['cognitive_focus']} and {t['additional_factor']} are incorporated into the evolutionary process.

3. Simulation Scenario (200-250 words):
   a) Provide a specific example scenario of how your system would simulate language-biology co-evolution.
   b) Describe the initial conditions, key evolutionary stages, and potential outcomes.
   c) Explain how the scenario demonstrates the interplay between communication, cognition, and biological adaptation.

4. Analysis of Emergent Properties (250-300 words):
   a) Analyze the emergent linguistic and biological properties from your simulation.
   b) Discuss how these properties relate to real-world observations in linguistics and biology.
   c) Explain any surprising or counterintuitive results from your model.

5. Implications for Understanding Cognition and Communication (200-250 words):
   a) Discuss the implications of your model for theories of language evolution and cognitive development.
   b) Explain how the simulation results might inform our understanding of the relationship between language, thought, and biological adaptation.
   c) Propose how insights from your model could be applied to other fields (e.g., AI development, linguistics, cognitive science).

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to model language and biological co-evolution.
   b) Address any limitations or potential biases in your simulation model.
   c) Propose guidelines for the responsible development and use of such AI systems in scientific research.

7. Future Directions (100-150 words):
   a) Suggest potential expansions or modifications to your model for future research.
   b) Propose a novel research question that could be explored using your simulation approach.

Ensure your response demonstrates a deep understanding of linguistics, evolutionary biology, cognitive science, and AI systems. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive simulation model design that integrates linguistic, biological, and cognitive elements in an {t['environment']} environment, considering {t['additional_factor']}.",
            f"The language-biology co-evolution mechanisms are well-explained, addressing the {t['communication_constraint']} constraint, {t['cognitive_focus']}, and the role of {t['additional_factor']}.",
            "The simulation scenario provided is specific, detailed, and demonstrates the interplay between communication, cognition, and biological adaptation.",
            "The analysis of emergent properties is thorough and relates to real-world observations in linguistics and biology.",
            "The implications for understanding cognition and communication are well-discussed and insightful.",
            "Ethical considerations and limitations of the model are addressed comprehensively.",
            "Future directions for research are proposed creatively and relevantly.",
            "The overall response demonstrates interdisciplinary knowledge synthesis, complex systems modeling, and analytical reasoning about the interplay between language, biology, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
