class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "examples": [
                    {"source": "Zino kavon", "target": "I am happy"},
                    {"source": "Zen kavon", "target": "You are happy"},
                    {"source": "Zino baron", "target": "I am sad"},
                    {"source": "Zen baron", "target": "You are sad"},
                    {"source": "Zino faron", "target": "I am excited"},
                    {"source": "Zen faron", "target": "You are excited"},
                    {"source": "Zino maron", "target": "I am tired"},
                    {"source": "Zen maron", "target": "You are tired"},
                    {"source": "Zino daron", "target": "I am surprised"},
                    {"source": "Zen daron", "target": "You are surprised"}
                ],
                "sentence": "Zino naron"
            },
            "2": {
                "examples": [
                    {"source": "Kavon zen", "target": "Happy you"},
                    {"source": "Baron zen", "target": "Sad you"},
                    {"source": "Kavon zino", "target": "Happy I"},
                    {"source": "Baron zino", "target": "Sad I"},
                    {"source": "Faron zen", "target": "Excited you"},
                    {"source": "Faron zino", "target": "Excited I"},
                    {"source": "Maron zen", "target": "Tired you"},
                    {"source": "Maron zino", "target": "Tired I"},
                    {"source": "Daron zen", "target": "Surprised you"},
                    {"source": "Daron zino", "target": "Surprised I"}
                ],
                "sentence": "Naron zen"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join([f'"{ex["source"]}" -> "{ex["target"]}"' for ex in t["examples"]])
        return f"""Translate the following sentence from the invented language to English based on the provided examples and translation rules. Here are the examples:\n\n{examples}\n\nSentence to translate:\n\n{t["sentence"]}\n\nYour response should be a plain text string containing the translated sentence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate and follow the patterns established in the examples.",
            "The translated sentence should be grammatically correct in English.",
            "The meaning should be consistent with the provided examples." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
