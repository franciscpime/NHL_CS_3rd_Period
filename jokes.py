import sys
import pyjokes

LANGUAGES = ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "ru", "sv"]

def read_arg():
    
    # The default language is en
    default = "en"

    # If no extra argument is entered
    if len(sys.argv) < 2:
         return default

    # If the extra argument is in uppercase, handle as if lowercase
    arg = sys.argv[1].lower()

    # Must start with a "-"" followed by 2 letters for the language
    if not (arg.startswith("-") and len(arg) == 3):
         return default
    
    # Remove "-"
    lang = arg[1:]

    # If a non-existing language is entered
    if lang not in LANGUAGES:
         return default    
    return lang


def get_single_joke(lang):
    try:
         joke = pyjokes.get_joke(language=lang)
         return joke
    except Exception:
         return "Bad joke"


def main():
    lang = read_arg()
    joke = get_single_joke(lang)
    print(joke)


if __name__ == "__main__":
	main()
