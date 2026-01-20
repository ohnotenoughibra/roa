import json

def validate_games():
    """Validate the generated games JSON file"""
    print("Validating nogi-games-library.json...")

    # Load the JSON file
    with open('/home/user/roa/nogi-games-library.json', 'r') as f:
        data = json.load(f)

    games = data['games']
    metadata = data['metadata']

    # Required fields for each game
    required_fields = ['id', 'name', 'topic', 'gameNumber', 'topPlayer',
                      'bottomPlayer', 'coaching', 'skills', 'favorite',
                      'lastUsed', 'created']

    # Valid topics
    valid_topics = [
        "Guard Passing", "Guard Retention", "Half Guard", "Top Control",
        "Mount", "Back Control", "Front Headlock", "Turtle", "Escapes",
        "Submissions", "Leg Locks", "Takedowns", "Transitions"
    ]

    errors = []
    warnings = []

    # Validate metadata
    print("\n=== Metadata Validation ===")
    print(f"Total games: {metadata['totalGames']}")
    print(f"Total topics: {metadata['totalTopics']}")
    print(f"Generated: {metadata['generated']}")

    if metadata['totalGames'] != len(games):
        errors.append(f"Metadata totalGames ({metadata['totalGames']}) doesn't match actual count ({len(games)})")
    else:
        print("✓ Game count matches metadata")

    # Validate each game
    print("\n=== Game Validation ===")
    unique_ids = set()
    topic_counts = {}

    for i, game in enumerate(games):
        # Check required fields
        for field in required_fields:
            if field not in game:
                errors.append(f"Game {i}: Missing required field '{field}'")

        # Check unique IDs
        if game['id'] in unique_ids:
            errors.append(f"Game {i}: Duplicate ID {game['id']}")
        unique_ids.add(game['id'])

        # Check valid topic
        if game['topic'] not in valid_topics:
            errors.append(f"Game {i} ({game['name']}): Invalid topic '{game['topic']}'")

        # Count topics
        topic = game['topic']
        topic_counts[topic] = topic_counts.get(topic, 0) + 1

        # Check field types
        if not isinstance(game['name'], str) or len(game['name']) == 0:
            errors.append(f"Game {i}: Invalid name")

        if not isinstance(game['topPlayer'], str) or len(game['topPlayer']) == 0:
            warnings.append(f"Game {i} ({game['name']}): topPlayer is empty or invalid")

        if not isinstance(game['bottomPlayer'], str) or len(game['bottomPlayer']) == 0:
            warnings.append(f"Game {i} ({game['name']}): bottomPlayer is empty or invalid")

        if not isinstance(game['skills'], str):
            warnings.append(f"Game {i} ({game['name']}): skills should be string")
        elif not game['skills'].startswith('#'):
            warnings.append(f"Game {i} ({game['name']}): skills should start with #")

        if not isinstance(game['favorite'], bool):
            errors.append(f"Game {i} ({game['name']}): favorite should be boolean")

        if game['lastUsed'] is not None and not isinstance(game['lastUsed'], (int, type(None))):
            errors.append(f"Game {i} ({game['name']}): lastUsed should be number or null")

    print(f"Validated {len(games)} games")
    print(f"✓ All games have unique IDs")

    # Print topic distribution
    print("\n=== Topic Distribution ===")
    for topic in valid_topics:
        count = topic_counts.get(topic, 0)
        print(f"{topic}: {count} games")

    # Check for balanced distribution
    avg_count = len(games) / len(valid_topics)
    for topic, count in topic_counts.items():
        if count < avg_count * 0.8 or count > avg_count * 1.2:
            warnings.append(f"Topic '{topic}' has unbalanced count: {count} (avg: {avg_count:.1f})")

    # Print results
    print("\n=== Validation Results ===")
    if errors:
        print(f"✗ {len(errors)} ERRORS found:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
        return False
    else:
        print("✓ No errors found!")

    if warnings:
        print(f"\n⚠ {len(warnings)} warnings:")
        for warning in warnings[:5]:  # Show first 5 warnings
            print(f"  - {warning}")
        if len(warnings) > 5:
            print(f"  ... and {len(warnings) - 5} more warnings")
    else:
        print("✓ No warnings!")

    # Generate import snippet
    print("\n=== Import Snippet for HTML ===")
    print("""
To import these games into your HTML file:

1. Copy the 'games' array from nogi-games-library.json
2. In your HTML file, replace the existing 'games = [...]' with:

   let games = [
     // paste games here
   ];

Or add this code to load from JSON:

   fetch('nogi-games-library.json')
     .then(response => response.json())
     .then(data => {
       games = data.games;
       renderGames();
     });
""")

    return True

if __name__ == "__main__":
    success = validate_games()
    exit(0 if success else 1)
