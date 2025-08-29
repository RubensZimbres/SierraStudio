# Task for Sierra Studio

## Assumptions:
 - the code is supposed to identify emails that are spam
 - the code has missing parts, and probably wrong code

## Approach
- hands-on approach: I fixed the code, made it work, then enhance it with classes, inheritance, unit tests, extreme examples
- ideas were appearing while I improved the code (practical approach)

## Trade-offs:
- Using 4o-mini, that is not the most powerful model, but it is cost efficient for large volume and outputs a valid JSON. We could use 4o, that offers better quality, but it is more expensive.

## Unit tests, edge cases
- For the sake of simplicity and speed, I created only two unit tests, to check for:
- **Valid JSON**
- **Test the detection**

## What I would improve:
- Besides the code provided and suggestions, I would implement:
- **async** for production level code
- **comprehensive unit tests** including prompt injection
- **Python --args** to run customized script via CLI
- **mypy, pytest, ruff** to check for code quality
- **LLM hyperparameters** to improve accuracy of spam detection
- **LLM evaluation**

## Errors I found in the provided script
- Line 0: Missing imports: openai, json
- Line 1: | None - I understand that we don't want None on the output
- Line 2: unnecessary \ backslash
- Line 7 to 10: Instructions and output type inside json payload, what is wrong: think step by step and bool/str
- Line 7 to 10: examples should have explicit True/False in the JSON payload, bool only in the in the instructions, outside JSON
- Line 7 to 10: invalid JSON format in the example: missing comma in structure + prompt instructions inside JSON format
- Line 7 to 10: should be valid JSON as example:
{
"is_spam": True,
"reason": "because offers a deal"
}
- Line 14: OpenAI client not defined
- Line 16: system message not defined
- Line 14: No OpenAI API Key
- Line 14: No explicit definition that we want the output as a JSON, and not text (response_format variable added)
- Line 14: I would add async according to my previous experience at Zendata, for production-level code
- Line 23: 'res' is not a proper name for a variable, as it does not have any meaning
- Line 24: 'if' is useless, also because else is not being used
- Line 25: json loads would be enough, to load a valid JSON

## How to run the code

- Run the check_spam function:
```python
python3 solution.py
```

- Run the unit tests:
```python
python3 unit_tests.py
```

**No AI Companions, code completion or Generative AI tools were used in this analysis**
