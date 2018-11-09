language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False

make gettext
sphinx-intl update -p _build/locale fr
