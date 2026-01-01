from googletrans import Translator
import json
import re

def add_tamil_translated_titles(json_file):
    translator = Translator()

    # Load existing JSON
    with open(json_file, "r", encoding="utf-8") as f:
        movies = json.load(f)

    # Update each movie
    for movie in movies:
        title = movie.get("title", "").strip()

        if not title:
            movie["tamil_translated_title"] = ""
            continue

        try:
            result = translator.translate(
                re.sub(r"[^A-Za-z0-9 ]+", "", title),
                src="en",   # force English
                dest="ta"
            )
            movie["tamil_translated_title"] = result.text
        except Exception as e:
            print(f"❌ Translation failed for '{title}': {e}")
            movie["tamil_translated_title"] = title

    # Save back to the SAME file
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)

    print(f"✅ Updated and saved in same file: {json_file}")
