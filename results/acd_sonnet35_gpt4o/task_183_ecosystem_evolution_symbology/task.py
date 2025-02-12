import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        planets = [
            {
                "name": "Zephyria",
                "initial_conditions": "High oxygen content, intense UV radiation, rapid day-night cycle",
                "major_events": ["Meteor impact", "Rapid temperature increase", "Evolution of flight"]
            },
            {
                "name": "Aquarius",
                "initial_conditions": "Mostly ocean, low gravity, dim red dwarf star",
                "major_events": ["Emergence of land", "Global cooling period", "Development of symbiotic relationships"]
            },
            {
                "name": "Ferrosa",
                "initial_conditions": "Iron-rich crust, strong magnetic field, thick atmosphere",
                "major_events": ["Emergence of metallovores", "Atmospheric thinning", "Development of electromagnetic sense"]
            },
            {
                "name": "Umbra",
                "initial_conditions": "Tidally locked, permanent twilight zone, extreme temperature gradients",
                "major_events": ["Massive volcanic eruption", "Evolution of heat regulation", "Emergence of bioluminescence"]
            }
        ]
        return {
            "1": random.choice(planets),
            "2": random.choice(planets)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a symbolic language to represent ecosystem evolution on the fictional planet {t['name']}, then use it to describe the planet's ecological history. Your task has four parts:

1. Symbolic Language Design (200-250 words):
   a) Create a set of symbols or glyphs that can represent various ecological concepts (e.g., species, environmental factors, evolutionary processes).
   b) Explain the meaning of at least 10 basic symbols in your system.
   c) Describe how these symbols can be combined or modified to represent more complex concepts.
   d) Explain how your system can represent changes over time or causal relationships.
   e) Justify your choice of symbols based on relevant scientific principles.

2. Initial Ecosystem Description (150-200 words):
   a) Using your symbolic language, represent the initial ecosystem of {t['name']} given these conditions: {t['initial_conditions']}
   b) Provide a brief written explanation of what your symbols represent in this initial ecosystem.

3. Ecosystem Evolution (200-250 words):
   a) Using your symbolic language, show how the ecosystem evolves through these three major events: {', '.join(t['major_events'])}
   b) For each event, provide a brief written explanation of the changes represented by your symbols.

4. Analysis of Symbolic Representation (150-200 words):
   a) Discuss the strengths and limitations of your symbolic language in representing complex ecological concepts and changes.
   b) Explain how this system might be useful for scientists studying ecosystem evolution, both on {t['name']} and potentially on Earth or other planets.
   c) Suggest one way your symbolic language could be expanded or improved for future use.

Ensure your response demonstrates a deep understanding of ecological principles, evolutionary biology, and symbolic reasoning. Be creative in your design while maintaining scientific plausibility and internal consistency.

Format for symbolic representations:
- Use ASCII characters or simple Unicode symbols for your glyphs.
- Present complex concepts as combinations of basic symbols, e.g., [A+B]C or A→B⇒C.
- Use arrows (→, ⇒, ↑, ↓) to represent changes or causal relationships.
- Enclose groupings in parentheses or brackets.

Provide your response with clear headings for each section and sub-section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and creative design for a symbolic language that can effectively represent ecological concepts and changes.",
            "The symbolic language design is justified based on relevant scientific principles.",
            "The initial ecosystem description and evolution stages are represented using the designed symbolic language and are consistent with the given conditions and events.",
            "The explanations of the symbolic representations demonstrate a strong understanding of ecological principles and evolutionary processes.",
            "The analysis of the symbolic representation shows insight into its strengths, limitations, and potential applications.",
            "The overall response displays creativity, scientific plausibility, and internal consistency in the design and application of the symbolic language.",
            "The response follows the specified format for symbolic representations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
