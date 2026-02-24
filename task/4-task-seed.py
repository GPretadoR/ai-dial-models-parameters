from task.app.main import run

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal

# With seed parameter - should give consistent results
print("\n" + "="*60)
print("Testing with seed=42 and n=5")
print("="*60)
run(
    deployment_name='gpt-4o',
    seed=42,
    n=5
)

# Without seed parameter - should give more varied results
print("\n" + "="*60)
print("Testing without seed and n=5 (more variety expected)")
print("="*60)
run(
    deployment_name='gpt-4o',
    n=5
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.
# For Anthropic and Gemini this parameter will be ignored