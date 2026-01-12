from backend.story_generator import generate_story


def main():
    print("🎬 AI Story Generator")
    print("Generate a short story for animated videos\n")

    user_input = input("Enter your story idea: ")

    print("\nGenerating story...\n")
    story = generate_story(user_input)

    print("📖 Generated Story:\n")
    print(story)


if __name__ == "__main__":
    main()
