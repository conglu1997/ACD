class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game": "Chess", "scenario": "You are playing as White. The current position has your pieces as follows: King on e1, Queen on d1, Rooks on a1 and h1, Bishops on c1 and f1, Knights on b1 and g1, and pawns on a2, b2, c2, d2, e2, f2, g2, h2. Your opponent has the same setup for Black. Develop a strategy for the opening phase."},
            "2": {"game": "StarCraft II", "scenario": "You are playing as Terran against Protoss. The map is Lost Temple. Develop a strategy for the early game to secure your base and prepare for an attack."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a strategic game plan based on the following scenario:

Game: {t["game"]}
Scenario: {t["scenario"]}

The strategy should be detailed, coherent, and logically structured. It should provide clear steps to achieve the goals stated in the scenario. Ensure that the strategy takes into account the game's mechanics and possible actions of the opponent. Provide your strategy in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The strategy should be detailed.", "The strategy should be coherent.", "The strategy should be logically structured.", "The strategy should provide clear steps to achieve the goals.", "The strategy should consider the game's mechanics and possible actions of the opponent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
