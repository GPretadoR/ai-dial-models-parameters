from task.app.main import run

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?

# Try with presence_penalty=-2.0 (focuses on same topics)
print("\n" + "="*60)
print("Testing with presence_penalty=-2.0 (focused on same topics)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    presence_penalty=-2.0
)

# Try with presence_penalty=0.0 (neutral/default)
print("\n" + "="*60)
print("Testing with presence_penalty=0.0 (neutral)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    presence_penalty=0.0
)

# Try with presence_penalty=2.0 (explores more topics)
print("\n" + "="*60)
print("Testing with presence_penalty=2.0 (diverse topics)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    presence_penalty=2.0
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored