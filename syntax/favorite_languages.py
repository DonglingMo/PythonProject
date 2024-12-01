favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

languages = favorite_languages['sarah'].title()
print(languages)

language_value = favorite_languages.get('tom', 'No point value available')
print(language_value)