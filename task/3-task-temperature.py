from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

# Try with temperature=0.0 (most deterministic)
print("\n" + "="*60)
print("Testing with temperature=0.0 (deterministic)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.0
)

# Try with temperature=0.5 (balanced)
print("\n" + "="*60)
print("Testing with temperature=0.5 (balanced)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=0.5
)

# Try with temperature=1.0 (more creative)
print("\n" + "="*60)
print("Testing with temperature=1.0 (creative)")
print("="*60)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    temperature=1.0
)

# Optional: Try with temperature=2.1 (beyond recommended range)
print("\n" + "="*60)
print("Testing with temperature=2.1 (beyond range - may error)")
print("="*60)
try:
    run(
        deployment_name='gpt-4o',
        print_only_content=True,
        temperature=2.1
    )
except Exception as e:
    print(f"Error occurred: {e}")