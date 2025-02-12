class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Analyze the given food web and predict the impact of removing a top predator from the ecosystem. Provide a detailed explanation of your reasoning, including the potential cascading effects on other species and the overall ecosystem stability.",
                "food_web": {
                    "predator": "Shark",
                    "prey": ["Tuna", "Seal"],
                    "interactions": {
                        "Shark": ["Tuna", "Seal"],
                        "Tuna": ["Small Fish"],
                        "Seal": ["Small Fish", "Crustaceans"],
                        "Small Fish": ["Plankton"],
                        "Crustaceans": ["Plankton"]
                    }
                }
            },
            "2": {
                "description": "Propose a solution to mitigate the impact of an invasive species introduced into the given ecosystem. Provide a detailed explanation of your proposed measures, the rationale behind them, and how they will help restore balance to the ecosystem.",
                "invasive_species": "Lionfish",
                "ecosystem": {
                    "native_species": ["Parrotfish", "Grouper", "Coral"],
                    "interactions": {
                        "Lionfish": ["Parrotfish", "Grouper"],
                        "Parrotfish": ["Algae"],
                        "Grouper": ["Small Fish"],
                        "Coral": ["Algae"],
                        "Algae": []
                    }
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'food_web' in t:
            return f"""Your task is to analyze the given food web and predict the impact of removing a top predator from the ecosystem.

Description: {t['description']}

Food Web:
Top Predator: {t['food_web']['predator']}
Prey: {', '.join(t['food_web']['prey'])}
Interactions: {t['food_web']['interactions']}

Provide a detailed explanation of your reasoning, including the potential cascading effects on other species and the overall ecosystem stability. Structure your response as follows:

1. Impact on direct prey: [Your explanation]
2. Cascading effects: [Your explanation]
3. Overall ecosystem stability: [Your explanation]"""
        elif 'invasive_species' in t:
            return f"""Your task is to propose a solution to mitigate the impact of an invasive species introduced into the given ecosystem.

Description: {t['description']}

Invasive Species: {t['invasive_species']}
Ecosystem:
Native Species: {', '.join(t['ecosystem']['native_species'])}
Interactions: {t['ecosystem']['interactions']}

Provide a detailed explanation of your proposed measures, the rationale behind them, and how they will help restore balance to the ecosystem. Structure your response as follows:

1. Proposed measures: [Your explanation]
2. Rationale: [Your explanation]
3. Restoration of balance: [Your explanation]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
