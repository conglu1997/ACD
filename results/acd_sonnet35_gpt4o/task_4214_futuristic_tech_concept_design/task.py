import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_principles = [
            "quantum entanglement",
            "dark energy manipulation",
            "zero-point energy harvesting",
            "gravity wave modulation"
        ]
        technological_domains = [
            "transportation",
            "energy production",
            "information processing",
            "environmental manipulation"
        ]
        timeframes = [
            "near future (50 years)",
            "distant future (500 years)"
        ]
        return {
            "1": {
                "principle": random.choice(scientific_principles),
                "domain": random.choice(technological_domains),
                "timeframe": random.choice(timeframes)
            },
            "2": {
                "principle": random.choice(scientific_principles),
                "domain": random.choice(technological_domains),
                "timeframe": random.choice(timeframes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a conceptual advanced technology based on the speculative scientific principle of {t['principle']}, applied to the domain of {t['domain']}. Then, analyze its potential applications and societal impacts in the {t['timeframe']}. Your response should include:\n\n" \
               f"1. Technology Concept (250-300 words):\n" \
               f"   a) Describe your proposed technology, explaining how it utilizes {t['principle']}.\n" \
               f"   b) Explain the core mechanisms or processes involved in your technology.\n" \
               f"   c) Discuss any theoretical or engineering challenges in realizing this technology.\n\n" \
               f"2. Scientific Foundation (200-250 words):\n" \
               f"   a) Elaborate on the current understanding of {t['principle']} and how your technology extends it.\n" \
               f"   b) Propose any new scientific theories or principles necessary for your technology to function.\n" \
               f"   c) Describe how your technology integrates knowledge from multiple scientific disciplines.\n\n" \
               f"3. Applications in {t['domain']} (200-250 words):\n" \
               f"   a) Propose three potential applications of your technology in the specified domain.\n" \
               f"   b) Explain how these applications could transform current approaches or solve existing problems.\n" \
               f"   c) Discuss any limitations or potential negative consequences of these applications.\n\n" \
               f"4. Societal Impact Analysis (200-250 words):\n" \
               f"   a) Analyze the potential societal impacts of your technology in the {t['timeframe']}.\n" \
               f"   b) Consider effects on economy, environment, social structures, and human behavior.\n" \
               f"   c) Discuss any ethical considerations or potential misuses of the technology.\n\n" \
               f"5. Development Roadmap (150-200 words):\n" \
               f"   a) Propose a high-level roadmap for developing your technology, considering the given timeframe.\n" \
               f"   b) Identify key milestones and potential obstacles in the development process.\n" \
               f"   c) Suggest areas of research or technological advancements necessary to realize your concept.\n\n" \
               f"Ensure your response demonstrates a deep understanding of advanced scientific concepts, engineering principles, and futuristic thinking. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from relevant fields and provide clear explanations for complex ideas."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear description of an advanced technology based on {t['principle']} applied to {t['domain']}.",
            "The scientific foundation section demonstrates a deep understanding of the specified principle and proposes plausible extensions or new theories.",
            "The proposed applications are innovative and well-reasoned, with consideration of potential limitations.",
            f"The societal impact analysis thoroughly considers the implications of the technology in the {t['timeframe']}.",
            "The development roadmap is logical and addresses key challenges in realizing the proposed technology.",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
