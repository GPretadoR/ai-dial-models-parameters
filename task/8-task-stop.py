from task.app.main import run

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

# Try with stop="\n\n" (stop at double newline)
print("\n" + "="*60)
print("Testing with stop='\\n\\n' (stops at double newline)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    stop="\n\n"
)

# Try with stop list (stop at specific phrases)
print("\n" + "="*60)
print("Testing with stop list (stops at specific headers)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)

# Optional: See full JSON with finish_reason
print("\n" + "="*60)
print("Testing with full JSON output (see finish_reason)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=False,
    stop="\n\n"
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.