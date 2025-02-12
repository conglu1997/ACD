import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_enhancements = [
            "memory augmentation",
            "accelerated learning",
            "enhanced pattern recognition",
            "expanded sensory perception"
        ]
        societal_domains = [
            "education",
            "workforce",
            "healthcare",
            "social interactions"
        ]
        return {
            "1": {
                "cognitive_enhancement": random.choice(cognitive_enhancements),
                "societal_domain": random.choice(societal_domains)
            },
            "2": {
                "cognitive_enhancement": random.choice(cognitive_enhancements),
                "societal_domain": random.choice(societal_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You have 40 minutes to complete this task. Design a hypothetical neurotechnology system that enhances human cognitive abilities through {t['cognitive_enhancement']}, then analyze its potential impacts on {t['societal_domain']} and propose ethical guidelines for its development and use. Your response should include:\n\n1. Neurotechnology System Design (300-350 words):\n   a) Describe the key components and mechanisms of your neurotechnology system.\n   b) Explain how it interfaces with the human brain to achieve {t['cognitive_enhancement']}.\n   c) Discuss any novel technologies or techniques required for your system.\n   d) Address potential safety concerns and how they are mitigated in your design.\n\n2. Cognitive Enhancement Mechanism (250-300 words):\n   a) Explain the neuroscientific principles behind your chosen cognitive enhancement.\n   b) Describe how your system modifies or augments neural processes to achieve the desired enhancement.\n   c) Discuss potential limitations or side effects of the enhancement.\n\n3. Societal Impact Analysis (250-300 words):\n   a) Analyze how your neurotechnology system could impact the domain of {t['societal_domain']}.\n   b) Discuss both potential benefits and risks to society.\n   c) Consider short-term and long-term consequences of widespread adoption.\n   d) Address issues of access, inequality, and social dynamics.\n\n4. Ethical Considerations (200-250 words):\n   a) Identify key ethical issues raised by your neurotechnology system.\n   b) Discuss implications for personal identity, free will, and human dignity.\n   c) Consider potential misuse or unintended consequences of the technology.\n\n5. Novel Ethical Framework (200-250 words):\n   a) Propose a new ethical framework specifically tailored to neurotechnology.\n   b) Your framework should introduce at least one new ethical principle not commonly found in traditional bioethics or tech ethics.\n   c) Explain how this framework addresses the unique challenges posed by cognitive enhancement technologies.\n   d) Discuss how your framework balances individual rights, societal benefits, and potential risks.\n\n6. Ethical Guidelines and Governance (200-250 words):\n   a) Based on your novel ethical framework, propose a set of ethical guidelines for the development and use of your neurotechnology system.\n   b) Suggest governance structures or regulatory frameworks to ensure responsible use.\n   c) Discuss how to balance innovation with safety and ethical concerns.\n\n7. Future Scenarios (150-200 words):\n   a) Describe a best-case scenario for the integration of your neurotechnology into society.\n   b) Describe a worst-case scenario and how it might be prevented.\n   c) Speculate on how this technology might evolve in the next 50 years.\n\nEnsure your response demonstrates a deep understanding of neuroscience, technology, ethics, and societal dynamics. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1550-1900 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['cognitive_enhancement']} and its potential impact on {t['societal_domain']}.",
            "The neurotechnology system design is innovative yet scientifically plausible.",
            "The societal impact analysis is comprehensive, balanced, and considers both short-term and long-term consequences.",
            "The ethical considerations thoroughly explore implications for personal identity, free will, and human dignity.",
            "The proposed novel ethical framework introduces at least one new ethical principle specific to neurotechnology.",
            "The ethical guidelines and governance structures are practical, aligned with the proposed ethical framework, and balance innovation with safety concerns.",
            "The future scenarios are creative, thought-provoking, and consider both positive and negative outcomes.",
            "The response shows interdisciplinary knowledge integration across neuroscience, technology, ethics, and social sciences.",
            "All sections of the response are complete and adhere to the word count guidelines.",
            "The response is well-structured with clear headings and subheadings as specified in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
