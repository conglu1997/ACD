import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = ['coral reef', 'rainforest', 'desert', 'tundra', 'grassland']
        environmental_challenges = ['climate change mitigation', 'water scarcity', 'biodiversity loss', 'pollution control', 'sustainable resource management']
        ai_techniques = ['neural networks', 'evolutionary algorithms', 'swarm intelligence', 'reinforcement learning', 'fuzzy logic']
        
        tasks = [
            {
                'ecosystem': random.choice(ecosystems),
                'challenge': random.choice(environmental_challenges),
                'ai_technique': random.choice(ai_techniques)
            },
            {
                'ecosystem': random.choice(ecosystems),
                'challenge': random.choice(environmental_challenges),
                'ai_technique': random.choice(ai_techniques)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic AI system inspired by the {t['ecosystem']} ecosystem to address the environmental challenge of {t['challenge']}, utilizing {t['ai_technique']} as the primary AI technique. Your response should include the following sections:

1. Ecosystem Analysis (200-250 words):
   a) Describe key characteristics and processes of the {t['ecosystem']} ecosystem relevant to {t['challenge']}.
   b) Identify at least three specific biological mechanisms or strategies from this ecosystem that could inspire technological solutions.
   c) Explain how these mechanisms contribute to the ecosystem's resilience or efficiency.

2. Biomimetic AI System Design (300-350 words):
   a) Present your AI system's architecture, explaining how it mimics the identified biological mechanisms.
   b) Describe how you integrate {t['ai_technique']} with the biomimetic elements.
   c) Explain how your system addresses the challenge of {t['challenge']}.
   d) Include a diagram or flowchart of your system (describe it in words if you cannot provide an actual image).

3. Implementation and Scalability (200-250 words):
   a) Outline the steps required to implement your system in a real-world setting.
   b) Discuss potential challenges in scaling the solution and how they might be overcome.
   c) Propose a method to measure the effectiveness of your system in addressing {t['challenge']}.

4. Environmental Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative environmental impacts of implementing your system.
   b) Discuss any unintended consequences that might arise from widespread adoption.
   c) Compare the environmental footprint of your solution to traditional approaches to {t['challenge']}.

5. Ethical Implications (150-200 words):
   a) Identify and discuss at least two ethical concerns related to your biomimetic AI system.
   b) Propose guidelines for responsible development and use of such systems.
   c) Discuss the potential societal impacts of your technology, considering both benefits and risks.

6. Future Developments (150-200 words):
   a) Suggest two potential advancements or modifications to your system that could enhance its capabilities.
   b) Discuss how your approach could be adapted to address other environmental challenges.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of the chosen ecosystem, environmental science, artificial intelligence, and biomimicry principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and environmental responsibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['ecosystem']} ecosystem and its relevance to {t['challenge']}.",
            f"The biomimetic AI system design effectively integrates {t['ai_technique']} with biomimetic elements inspired by the {t['ecosystem']}.",
            "The proposed system addresses the specified environmental challenge in a plausible and innovative manner.",
            "The response includes a thoughtful analysis of environmental impacts, ethical implications, and future developments.",
            "The submission is well-structured, clear, and adheres to the specified word count range (1200-1500 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
