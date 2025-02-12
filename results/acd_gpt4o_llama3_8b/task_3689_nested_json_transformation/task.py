class TaskFamily:
    import json

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "input_json": {
                    "name": "John Doe",
                    "address": {
                        "street": "123 Main St",
                        "city": "Anytown",
                        "state": "CA"
                    },
                    "phones": [
                        {"type": "home", "number": "123-456-7890"},
                        {"type": "work", "number": "987-654-3210"}
                    ]
                },
                "transformation_rules": [
                    {"operation": "rename_key", "path": "address.city", "new_key": "town"},
                    {"operation": "add_key", "path": "address", "new_key": "zipcode", "value": "90210"},
                    {"operation": "remove_key", "path": "phones[1].type"}
                ]
            },
            "2": {
                "input_json": {
                    "product": "Widget",
                    "details": {
                        "manufacturer": "Widgets Inc.",
                        "model": "X1000",
                        "specs": {
                            "weight": "1kg",
                            "dimensions": {
                                "length": "10cm",
                                "width": "5cm",
                                "height": "3cm"
                            }
                        }
                    },
                    "price": 19.99
                },
                "transformation_rules": [
                    {"operation": "rename_key", "path": "details.specs.dimensions", "new_key": "size"},
                    {"operation": "add_key", "path": "details", "new_key": "warranty", "value": "2 years"},
                    {"operation": "remove_key", "path": "price"}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        import json
        input_json = json.dumps(t["input_json"], indent=4)
        transformation_rules = "\n".join([f"- {rule}" for rule in t["transformation_rules"]])
        return f"""Transform the given nested JSON structure according to the specified rules:\n\nInput JSON:\n{input_json}\n\nTransformation Rules:\n{transformation_rules}\n\nSubmit your transformed JSON as a plain text string in the following format:\n\nTransformed JSON: [Your transformed JSON here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # No additional criteria needed as the instructions are self-sufficient.
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
