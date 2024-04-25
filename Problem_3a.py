def read_feedback(filename):
    try:
        with open(filename, 'r') as file:
            feedback = []
            for line in file:
                feedback.append(line)
            return feedback #outside of for loop so it goes through the whole loop
    except FileNotFoundError:
        []

def categorized_comments(feedback):
    positive_keywords = ['good', 'excellent', 'happy', 'satisfied', 'amazing', 'fantastic']
    negative_keywords = ['bad', 'poor', 'unhappy', 'disappointed']
    categorized = {'positive': [], 'negative': [], 'neutral': []}

    for review in feedback:
        comment = review.lower()  #this is a string so keys don't work here
        if any(word in comment for word in positive_keywords):
            categorized['positive'].append(review)
        elif any(word in comment for word in negative_keywords):
            categorized['negative'].append(review)
        else:
            categorized['neutral'].append(review)
    return categorized

def display_categorized_feedback(categorized):
    for category, comments in categorized.items():
        print(f"\n{category.capitalize()} Feedback:")
        for review in comments:
            print(f"- {review}")

def display_summary(categorized):
    print("\nFeedback Summary:")
    for category, comments in categorized.items():
        print(f"{category.capitalize()}: {len(comments)} comments")



def main():
    feedback = read_feedback('travel_blogs.txt')
    if not feedback:
        print("No feedback available.")
        return
    
    categorized = categorized_comments(feedback)

    while True:
        print("\n1. Display Categorized Feedback\n2. Display Summary\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_categorized_feedback(categorized)
        elif choice == '2':
            display_summary(categorized)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()