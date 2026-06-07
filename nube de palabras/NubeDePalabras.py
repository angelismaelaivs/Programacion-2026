from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pypdf import PdfReader

# Extraer texto del PDF
reader = PdfReader('Nube\Siddhartha.pdf')
texto = ""
for page in reader.pages:
    texto += page.extract_text()

# Vamos a omitir algunas palabras
palabrasOmitir = {"yo", "tú", "él", "ella", "nosotros", "ellos", "ellas",
    "me", "te", "se", "le", "lo", "la", "les", "nos",
    "mi", "tu", "su", "mis", "tus", "sus", "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "al", "a", "en", "con", "por", "para",
    "sin", "sobre", "entre", "hasta", "desde", "ante","y", "e", "o", "u", "que", 'y'
    }

# Generar nube de palabras
nube = WordCloud(width=800, height=400, background_color='black', stopwords= palabrasOmitir).generate(texto)
plt.figure(figsize=(10, 5))
plt.imshow(nube, interpolation='bilinear')
plt.axis("off")
plt.show()