import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "protein folding",
            "gene expression regulation",
            "neurotransmitter signaling",
            "cellular metabolism"
        ]
        quantum_properties = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        return {
            "1": {
                "process": random.choice(biological_processes),
                "quantum_property": random.choice(quantum_properties)
            },
            "2": {
                "process": random.choice(biological_processes),
                "quantum_property": random.choice(quantum_properties)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing system for simulating {t['process']}, focusing on the quantum property of {t['quantum_property']}. Then, analyze its potential applications in medicine and the ethical implications of its use. Your response should include:\n\n" \
               f"1. Quantum Biosimulation System Design (250-300 words):\n" \
               f"   a) Describe the architecture of your quantum computing system for simulating {t['process']}.\n" \
               f"   b) Explain how your system utilizes {t['quantum_property']} to enhance the simulation.\n" \
               f"   c) Discuss any novel approaches or algorithms in your design.\n\n" \
               f"2. Biological Process Modeling (200-250 words):\n" \
               f"   a) Explain how your system models {t['process']} at the quantum level.\n" \
               f"   b) Describe the advantages of your quantum approach over classical simulation methods.\n" \
               f"   c) Identify potential challenges in accurately simulating this biological process.\n\n" \
               f"3. Medical Applications (200-250 words):\n" \
               f"   a) Propose two potential applications of your quantum biosimulation system in medicine or drug discovery.\n" \
               f"   b) Explain how these applications could advance current medical research or treatment methods.\n" \
               f"   c) Discuss any limitations or challenges in translating simulation results to real-world medical applications.\n\n" \
               f"4. Ethical Implications (200-250 words):\n" \
               f"   a) Analyze the ethical considerations of using quantum computing for biological simulations.\n" \
               f"   b) Discuss potential misuse or unintended consequences of this technology.\n" \
               f"   c) Propose guidelines for the responsible development and use of quantum biosimulation systems.\n\n" \
               f"5. Future Prospects (150-200 words):\n" \
               f"   a) Speculate on how quantum biosimulation might evolve in the next decade.\n" \
               f"   b) Suggest two areas of research that could significantly enhance the capabilities of your system.\n" \
               f"   c) Discuss how advancements in this field might impact society and scientific research.\n\n" \
               f"Ensure your response demonstrates a deep understanding of quantum computing, biological processes, and ethical reasoning. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from quantum physics, biology, and ethics."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear description of a quantum computing system for simulating {t['process']}, utilizing {t['quantum_property']}.",
            "The biological process modeling section demonstrates a deep understanding of both quantum mechanics and the specified biological process.",
            "The proposed medical applications are innovative and well-reasoned.",
            "The ethical implications are thoroughly analyzed, considering multiple perspectives.",
            "The response demonstrates interdisciplinary knowledge integration across quantum computing, biology, and ethics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
