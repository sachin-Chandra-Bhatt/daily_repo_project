# stylish  bio generator

import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion: ").strip()
emoji = input("Enter your favorite emoji: ").strip()
website = input("Enter your website URL: ").strip()

print("\n choose a style for your bio:\n")
print("1. simple \n 2. vertical flair \n 3. emoji sandwich \n ")

style_choice = input("Enter the number of your chosen style (1, 2, or 3): ").strip()

def generate_bio(style):
    if style == "1":
        # Simple style
        bio = f"{emoji} | {name} \n {profession} | {passion} \n {website} ✌ "
    elif style == "2":
        # Vertical flair style
        bio = f"❤👌{emoji}\n {name}\n{profession}\n{passion}\n{website} ✌"
    elif style == "3":
        # Emoji sandwich style
        bio = f"{emoji} {name} {emoji}\n{profession} | {passion}\n{website} \n {emoji * 5} ✌"
    else:
        return "Invalid style choice. Please choose 1, 2, or 3."
    
    return bio

# Generate the bio based on the chosen style
bio = generate_bio(style_choice)
# Format the bio to fit within 80 characters
formatted_bio = textwrap.dedent(bio)
# Print the formatted bio
print("\nYour Stylish Bio:\n")
print(formatted_bio)