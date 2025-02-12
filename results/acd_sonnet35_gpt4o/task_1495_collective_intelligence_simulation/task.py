import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            ("environmental policy", "Developing a carbon pricing strategy"),
            ("public health crisis", "Responding to a novel infectious disease outbreak"),
            ("technological innovation", "Regulating artificial intelligence development"),
            ("economic reform", "Implementing a universal basic income system"),
            ("educational system overhaul", "Redesigning curriculum for the digital age")
        ]
        group_sizes = [10, 50, 100, 500, 1000]
        decision_methods = [
            "consensus",
            "majority vote",
            "weighted expertise",
            "hierarchical",
            "decentralized"
        ]
        return {
            "1": {
                "scenario": random.choice(scenarios),
                "group_size": random.choice(group_sizes),
                "decision_method": random.choice(decision_methods)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "group_size": random.choice(group_sizes),
                "decision_method": random.choice(decision_methods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an AI system capable of simulating collective intelligence and group decision-making processes for the following scenario:

Scenario: {t['scenario'][0]} - {t['scenario'][1]}
Group Size: {t['group_size']}
Decision Method: {t['decision_method']}

Collective intelligence refers to the enhanced capacity for problem-solving and decision-making that emerges when groups of individuals work together, often producing outcomes superior to those of any single member of the group.

Your response should include the following sections:

1. AI System Design (250-300 words):
   a) Describe the key components of your AI system for simulating collective intelligence.
   b) Explain how your system models individual agents and their interactions.
   c) Detail how your system incorporates the specified decision method.
   d) Discuss any novel AI techniques or algorithms used in your simulation.
   e) Explain how your system specifically addresses the unique aspects of the given scenario.
   f) Provide a simple diagram or flowchart illustrating the key components and processes of your AI system.

2. Collective Intelligence Model (200-250 words):
   a) Explain how your system models the emergence of collective intelligence.
   b) Describe how individual knowledge and biases are aggregated in your model.
   c) Discuss how your system handles information flow and influence between agents.
   d) Explain how your model accounts for cognitive diversity and its impact on decision-making.

3. Simulation Process (200-250 words):
   a) Provide a step-by-step description of how your AI system would run a simulation for the given scenario.
   b) Explain how your system would handle the specified group size and decision method.
   c) Describe how your simulation accounts for factors such as time pressure, information asymmetry, and external influences.
   d) Discuss how your system would evaluate the quality of the collective decision.

4. Analysis and Insights (200-250 words):
   a) Describe the expected outcomes of your simulation for the given scenario.
   b) Analyze how the group size and decision method might affect the results.
   c) Discuss any emergent behaviors or unexpected outcomes your system might reveal.
   d) Compare your AI-simulated results to what we know about human group decision-making in similar contexts.

5. Applications and Implications (150-200 words):
   a) Propose two potential real-world applications of your collective intelligence simulation system.
   b) Discuss how this technology could be used to enhance human decision-making processes.
   c) Analyze potential risks or negative consequences of relying on AI-simulated collective intelligence.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to simulate and potentially influence human collective decision-making.
   b) Address concerns about privacy, manipulation, and the potential for misuse of this technology.
   c) Propose guidelines for the responsible development and use of collective intelligence simulation systems.

Ensure your response demonstrates a deep understanding of social psychology, decision theory, and AI capabilities. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words.

You have 45 minutes to complete this task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of collective intelligence and group decision-making processes, specifically addressing the given scenario.",
            "The AI system design is innovative, coherent, and adequately incorporates the specified group size and decision method.",
            "The collective intelligence model effectively explains the emergence of group intelligence and accounts for individual differences.",
            "The simulation process is clearly described and accounts for relevant factors in group decision-making, including time pressure and information asymmetry.",
            "The analysis provides insightful predictions and meaningful comparisons to human decision-making processes in the given context.",
            "The proposed applications are practical, well-reasoned, and relevant to the simulated scenario.",
            "Ethical considerations are thoroughly addressed, with thoughtful and specific guidelines proposed for the given context.",
            "The response is well-structured, coherent, and adheres to the specified word limits and time constraint.",
            "A clear, informative, and relevant diagram or flowchart of the AI system is provided, enhancing the explanation of the system design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
