class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Three friends, Alice, Bob, and Charlie, went on a trip together. They each chose a different mode of transportation: car, bike, and train. They also visited different places: a museum, a park, and a beach. Lastly, they each bought a different souvenir: a postcard, a keychain, and a magnet. Based on the following clues, determine who chose which mode of transportation, visited which place, and bought which souvenir:\n\n1. Alice did not go by bike and did not visit the beach.\n2. The person who went by car visited the park.\n3. Bob bought the keychain and did not visit the museum.\n4. The person who visited the beach bought the magnet.\n5. Charlie went by train.\n\nSubmit your solution in the following format:\n\n- Alice: [transportation, place, souvenir]\n- Bob: [transportation, place, souvenir]\n- Charlie: [transportation, place, souvenir]"
            },
            "2": {
                "puzzle": "Four students, Daniel, Emily, Fiona, and George, participated in a science fair. Each of them presented a project on a different subject: physics, chemistry, biology, and astronomy. They also each won a different prize: first, second, third, and fourth place. Based on the following clues, determine who presented which subject and won which prize:\n\n1. Daniel did not present the physics project and did not win first place.\n2. The student who presented the chemistry project won second place.\n3. Emily presented the biology project.\n4. The student who won first place did not present the astronomy project.\n5. Fiona won third place.\n\nSubmit your solution in the following format:\n\n- Daniel: [subject, prize]\n- Emily: [subject, prize]\n- Fiona: [subject, prize]\n- George: [subject, prize]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logic puzzle:\n\n{t['puzzle']}\n\nSubmit your solution in the specified format as plain text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
