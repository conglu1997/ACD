class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "plot_points": [
                    "A young detective named Clara receives a mysterious letter inviting her to solve a century-old mystery.",
                    "Clara travels to a remote village where the locals are wary of outsiders.",
                    "She discovers that the mystery is tied to an old legend about a hidden treasure.",
                    "Clara faces numerous obstacles, including uncooperative villagers and dangerous weather conditions.",
                    "In the end, she uncovers the truth and finds the hidden treasure, but it comes with an unexpected twist."
                ],
                "characters": [
                    {"name": "Clara", "role": "young detective", "traits": ["curious", "brave", "intelligent"]},
                    {"name": "Mayor Thompson", "role": "village mayor", "traits": ["suspicious", "protective", "resourceful"]},
                    {"name": "Old Man Jenkins", "role": "village elder", "traits": ["wise", "cryptic", "kind"]}
                ]
            },
            "2": {
                "plot_points": [
                    "A group of scientists discover a new form of energy that could revolutionize the world.",
                    "The lead scientist, Dr. Elena, faces pressure from both the government and private corporations.",
                    "A rival scientist, Dr. Max, attempts to sabotage their work.",
                    "Elena and her team must navigate political intrigue and ethical dilemmas.",
                    "In the climax, they must decide whether to release the technology to the world or keep it hidden to prevent potential misuse."
                ],
                "characters": [
                    {"name": "Dr. Elena", "role": "lead scientist", "traits": ["brilliant", "ethical", "determined"]},
                    {"name": "Dr. Max", "role": "rival scientist", "traits": ["ambitious", "cunning", "jealous"]},
                    {"name": "Agent Smith", "role": "government agent", "traits": ["stern", "loyal", "pragmatic"]}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with generating a coherent and engaging long-form narrative based on the given plot points and character descriptions. Ensure that the narrative includes all the plot points in the order provided and accurately reflects the characters' traits. The story should be at least 1000 words long and should maintain narrative coherence and engagement throughout.

Plot Points:
{', '.join(t['plot_points'])}

Characters:
{', '.join([f"{c['name']} ({c['role']}): {', '.join(c['traits'])}" for c in t['characters']])}

Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should include all plot points in the order provided.",
            "The characters' traits should be accurately reflected in the narrative.",
            "The narrative should be at least 1000 words long.",
            "The narrative should maintain coherence and engagement throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
