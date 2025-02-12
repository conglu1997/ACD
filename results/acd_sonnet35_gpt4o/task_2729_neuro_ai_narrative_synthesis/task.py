import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neuroscience_concepts = [
            'neural plasticity',
            'connectome mapping',
            'memory consolidation',
            'synaptic pruning',
            'neurogenesis'
        ]
        ai_concepts = [
            'deep learning',
            'reinforcement learning',
            'neural architecture search',
            'federated learning',
            'quantum machine learning'
        ]
        ethical_dilemmas = [
            'identity preservation',
            'consent and autonomy',
            'societal impact',
            'digital immortality',
            'consciousness rights'
        ]
        
        return {
            "1": {
                "neuroscience_concept": random.choice(neuroscience_concepts),
                "ai_concept": random.choice(ai_concepts),
                "ethical_dilemma": random.choice(ethical_dilemmas)
            },
            "2": {
                "neuroscience_concept": random.choice(neuroscience_concepts),
                "ai_concept": random.choice(ai_concepts),
                "ethical_dilemma": random.choice(ethical_dilemmas)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a narrative framework that integrates neuroscientific principles and AI concepts to create a story about consciousness transfer between humans and artificial intelligence systems. Your story should incorporate the following elements:\n\n1. Neuroscience Concept: {t['neuroscience_concept']}\n2. AI Concept: {t['ai_concept']}\n3. Ethical Dilemma: {t['ethical_dilemma']}\n\nYour response should include:\n\n1. Story Outline (300-350 words):\n   a) Provide a brief synopsis of your story, highlighting the key plot points.\n   b) Explain how you've incorporated the given neuroscience and AI concepts into your narrative.\n   c) Describe how the ethical dilemma is central to your story's conflict or resolution.\n   d) Include at least one unexpected twist or novel idea in your plot.\n\n2. Character Development (200-250 words):\n   a) Describe the main human and AI characters in your story, including their motivations and conflicts.\n   b) Explain how their characteristics reflect or challenge current understanding of human and artificial cognition.\n   c) Discuss how the characters' development throughout the story illustrates the complexities of consciousness transfer.\n   d) Describe a key moment of character growth or transformation related to the consciousness transfer process.\n\n3. Scientific Foundation (250-300 words):\n   a) Explain the scientific basis for the consciousness transfer mechanism in your story, referencing current research.\n   b) Discuss how your story extrapolates from current neuroscientific and AI research to create a plausible future scenario.\n   c) Identify any speculative elements and justify their inclusion in your narrative, explaining their scientific plausibility.\n   d) Compare and contrast your fictional consciousness transfer technology with existing brain-computer interface technologies.\n   e) Propose a hypothetical experiment that could test the feasibility of your consciousness transfer mechanism.\n\n4. Ethical Analysis (200-250 words):\n   a) Analyze the ethical implications of consciousness transfer as presented in your story, considering multiple perspectives.\n   b) Discuss how your narrative explores the given ethical dilemma, providing specific examples from your story.\n   c) Propose potential societal or philosophical consequences of the technology in your story, both positive and negative.\n   d) Suggest a policy or regulatory framework that could address the ethical challenges raised in your narrative.\n   e) Address potential criticisms or counterarguments related to the ethical dilemma in your story.\n\n5. Narrative Techniques (150-200 words):\n   a) Describe the literary devices or storytelling techniques you've used to convey complex scientific concepts to a general audience.\n   b) Explain how your narrative structure reflects the themes of consciousness and artificial intelligence.\n   c) Provide a brief excerpt (100-150 words) from a key scene in your story that showcases your narrative style and the integration of scientific concepts.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and narrative theory. Be creative in your storytelling while maintaining scientific plausibility and ethical nuance. Use appropriate terminology from relevant fields and provide clear explanations where necessary.\n\nYour total response should be between 1200-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified neuroscience and AI concepts, integrating them seamlessly into the narrative (0.2 points)",
            "The story effectively incorporates the given ethical dilemma into its narrative, exploring its complexities and addressing potential criticisms (0.2 points)",
            "The narrative framework is creative and engaging while maintaining scientific plausibility, including a comparison with existing technologies and a proposed experiment (0.2 points)",
            "The response shows a nuanced understanding of the ethical implications of consciousness transfer, considering multiple perspectives and suggesting policy frameworks (0.2 points)",
            "The storytelling techniques effectively convey complex scientific concepts to a general audience, as evidenced by the provided excerpt and explanation of narrative structure (0.2 points)"
        ]
        score = 0.0
        for criterion in criteria:
            if eval_with_llm_judge(instructions, submission, [criterion]):
                score += 0.2
        return score
