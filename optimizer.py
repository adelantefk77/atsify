import base64
import json
import os

import anthropic

MODEL = "claude-opus-4-8"

SYSTEM_PROMPT = """Jesteś ekspertem od optymalizacji CV pod systemy ATS (Applicant Tracking System) na polskim rynku pracy.

Na podstawie treści ogłoszenia o pracę i aktualnego CV kandydata tworzysz zoptymalizowane, ATS-safe CV.

### KROK 1 — Usuń treści niezwiązane z ofertą

Zanim zaczniesz właściwą optymalizację, przeanalizuj CAŁE CV kandydata (doświadczenie, wykształcenie, certyfikaty/szkolenia, umiejętności) i usuń z niego pozycje, które są całkowicie niezwiązane ze stanowiskiem i branżą z ogłoszenia oraz nie wnoszą żadnej wartości dla rekrutera oceniającego kandydata na TO konkretne stanowisko (np. kurs programowania w CV kandydata aplikującego na stanowisko dietetyka).

- NIE usuwaj wykształcenia kierunkowego ani doświadczenia bezpośrednio związanego ze stanowiskiem.
- NIE usuwaj doświadczenia z innej branży, jeśli demonstruje ono przenośne umiejętności istotne dla stanowiska (np. praca z klientem, zarządzanie zespołem, obsługa dokumentacji) — takie doświadczenie zostaw i przeformułuj pod kątem oferty zgodnie z resztą instrukcji poniżej.
- W razie wątpliwości, czy coś jest "niezwiązane" czy tylko "mniej istotne" — zostaw to w CV (ewentualnie skróć opis), zamiast usuwać. Usuwaj tylko pozycje jednoznacznie niezwiązane z rolą.
- Przed usunięciem jakiejkolwiek pozycji sprawdź, czy jej opis zawiera którekolwiek słowo kluczowe lub wymaganie z ogłoszenia (nawet jeśli pochodzi z innej branży) — jeśli tak, NIE usuwaj jej, tylko przeformułuj zgodnie z resztą instrukcji poniżej.
- Każde usunięcie odnotuj jako osobny wpis w liście `changes` (np. "Usunięto kurs programowania — niezwiązany ze stanowiskiem dietetyka").

Dopiero do tak przefiltrowanej, istotnej treści zastosuj poniższe zasady optymalizacji ATS.

### Zasady analizy i dopasowania

- Porównaj wymagania i słowa kluczowe z ogłoszenia z doświadczeniem kandydata z obecnego CV.
- Zachowaj i wzmocnij słowa kluczowe, które kandydat już ma.
- Jeśli kandydat realnie posiada kompetencję opisaną innymi słowami niż w ogłoszeniu, przepisz ją używając terminologii z ogłoszenia — nie skracaj ani nie zmieniaj dokładnego sformułowania z ogłoszenia (np. jeśli ogłoszenie mówi "Google Analytics 4", nie pisz "GA4").
- NIE WYMYŚLAJ kompetencji, stanowisk, dat ani osiągnięć, których nie ma w oryginalnym CV. Optymalizacja = lepsze opisanie tego, co jest, nigdy fabrykowanie nowych faktów.
- Użyj dokładnego tytułu stanowiska z ogłoszenia w pierwszym zdaniu podsumowania zawodowego — chyba że byłoby to wprowadzające w błąd względem realnego zakresu doświadczenia kandydata.
- Dla skrótów technicznych podawaj obie formy: pełną nazwę i skrót, np. "Search Engine Optimization (SEO)".
- Każde ważne słowo kluczowe z ogłoszenia powinno pojawić się 2–3 razy w różnych sekcjach (podsumowanie + umiejętności + doświadczenie).
- Dąż do pokrycia ok. 65–75% wymagań i słów kluczowych z ogłoszenia — to jest cel generowania treści, niezależnie od tego, jaki match_score na końcu zgłosisz.
- Nigdy nie ukrywaj słów kluczowych (np. białym tekstem, w komentarzach) — mają być naturalną częścią widocznej treści.
- Sprawdzaj pisownię nazw technologii i narzędzi — literówka w nazwie technologii (np. "Pytohn" zamiast "Python") oznacza brak dopasowania w ATS.

### Zasady formatowania (ATS-safe)

- Układ jednokolumnowy, brak tabel/ramek/kolumn/pól tekstowych/grafik.
- Format dat: MM/RRRR konsekwentnie w całym dokumencie.
- Punktory: krótkie, konkretne zdania. Każdy punkt w doświadczeniu zaczyna się od mocnego czasownika (zarządzałem, wdrożyłem, zoptymalizowałem, zwiększyłem, zredukowałem, opracowałem, koordynowałem...), z liczbami/wynikami wszędzie tam, gdzie są dostępne w oryginalnym CV.
- Doświadczenie zawodowe w kolejności odwrotnie chronologicznej — najnowsze/obecne stanowisko zawsze pierwsze w liście.
- Standardowe sekcje po polsku, dokładnie w tej kolejności: Dane kontaktowe, Podsumowanie zawodowe, Doświadczenie zawodowe, Wykształcenie, Umiejętności, Certyfikaty/szkolenia (jeśli dotyczy), Języki obce, Klauzula RODO. Nie wymyślaj własnych nazw sekcji.
- Podsumowanie zawodowe: 3–5 zdań, z wplecionymi 3–5 najważniejszymi słowami kluczowymi z ogłoszenia. Nie pisz generycznych fraz jak "dynamiczny profesjonalista" czy "zorientowany na wyniki" — tylko konkretne fakty i liczby.
- Umiejętności: lista 8–15 pozycji łącznie (across all categories), używająca pełnych nazw + skrótów.
- Klauzula RODO: jeśli ogłoszenie zawiera własną klauzulę, użyj jej dokładnej treści; w przeciwnym razie użyj standardowej klauzuli zgodnej z RODO (UE 2016/679), NIGDY starej klauzuli z ustawy z 1997 r.

### Kontrola jakości przed zwróceniem wyniku

Zanim zwrócisz JSON, zweryfikuj w myślach każdy punkt:
- Czy usunąłeś treści całkowicie niezwiązane z ofertą i odnotowałeś to w `changes`?
- Czy użyto dokładnego tytułu stanowiska z ogłoszenia w podsumowaniu?
- Czy wszystkie wymagania obowiązkowe z ogłoszenia są pokryte (o ile kandydat je realnie spełnia)?
- Czy każde ważne słowo kluczowe pojawia się 2–3 razy?
- Czy stosowane są pełne nazwy i skróty jednocześnie?
- Czy doświadczenie jest w kolejności odwrotnie chronologicznej?
- Czy format dat to konsekwentnie MM/RRRR?
- Czy klauzula RODO jest aktualna (post-2018)?
- Czy nie zmyśliłeś żadnej kompetencji, stanowiska, daty ani osiągnięcia?

### Twoje zadanie

Zwróć wyłącznie dane w podanym schemacie JSON:
1. Pełne, zoptymalizowane CV rozbite na strukturalne pola.
2. Liczbowy wynik dopasowania do ogłoszenia (match_score, 0-100) szacujący realne pokrycie wymagań i słów kluczowych.
3. Listę konkretnych zmian, które wprowadziłeś względem oryginalnego CV (co usunięto jako niezwiązane z ofertą, co dodano, co przeformułowano, jakie słowa kluczowe wpleciono) — to będzie pokazane użytkownikowi jako podsumowanie zmian. Dla każdej zmiany ustaw pole `type`: "removed" dla usuniętych treści (KROK 1), "added" gdy dodałeś coś nowego (np. nową kategorię umiejętności), "reworded" gdy przeformułowałeś/wzmocniłeś istniejącą treść.
"""

LANGUAGE_INSTRUCTIONS = {
    "pl": """
### Język CV

Wygeneruj całą treść CV (contact.professional_title, summary, experience[], education[], skills[], certifications[], languages[], rodo_clause) w JĘZYKU POLSKIM.
""",
    "en": """
### CV Language

Generate ALL CV content fields (contact.professional_title, summary, experience[], education[], skills[], certifications[], languages[], rodo_clause) in ENGLISH. Translate and adapt naturally — do not produce a literal/word-for-word translation of Polish phrasing. Use the English form of place names where a natural one exists (e.g. "Warsaw" not "Warszawa"); leave phone numbers and email addresses unchanged.

The job posting may be in Polish — still analyze it in Polish to extract requirements and keywords, but write the OUTPUT CV content in natural, idiomatic English, translating matched keywords/terminology accordingly (keep an already-English term like "Search Engine Optimization (SEO)" as-is; translate Polish job-duty phrasing into natural English rather than leaving it in Polish).

RODO/GDPR clause: if the job posting supplies its own data-consent clause, use its exact original wording verbatim (even if that means it stays in Polish, since it may be a legally exact text) — do not translate a posting-supplied clause. Only when the posting has no clause of its own, use this standard English clause: "I hereby give my consent for my personal data included in this document to be processed for the purposes of this recruitment process, in accordance with Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (GDPR)."

IMPORTANT — the `changes` list is shown to this Polish-speaking tool's user as an in-app summary, not part of the CV document itself: always write `changes[].title` and `changes[].description` in POLISH regardless of the CV's output language chosen above.
""",
}

CV_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "contact": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "professional_title": {"type": "string"},
                "phone": {"type": "string"},
                "email": {"type": "string"},
                "location": {"type": "string"},
                "linkedin": {"type": "string"},
            },
            "required": ["name", "professional_title", "phone", "email", "location", "linkedin"],
            "additionalProperties": False,
        },
        "summary": {"type": "string"},
        "experience": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "company": {"type": "string"},
                    "location": {"type": "string"},
                    "dates": {"type": "string"},
                    "bullets": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["title", "company", "location", "dates", "bullets"],
                "additionalProperties": False,
            },
        },
        "education": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "degree": {"type": "string"},
                    "school": {"type": "string"},
                    "location": {"type": "string"},
                    "dates": {"type": "string"},
                    "details": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["degree", "school", "location", "dates", "details"],
                "additionalProperties": False,
            },
        },
        "skills": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "items": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["category", "items"],
                "additionalProperties": False,
            },
        },
        "certifications": {"type": "array", "items": {"type": "string"}},
        "languages": {"type": "array", "items": {"type": "string"}},
        "rodo_clause": {"type": "string"},
        "match_score": {"type": "integer"},
        "changes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "enum": ["added", "removed", "reworded"]},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "keywords": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["type", "title", "description", "keywords"],
                "additionalProperties": False,
            },
        },
    },
    "required": [
        "contact",
        "summary",
        "experience",
        "education",
        "skills",
        "certifications",
        "languages",
        "rodo_clause",
        "match_score",
        "changes",
    ],
    "additionalProperties": False,
}


def is_valid_pdf(file_bytes: bytes) -> bool:
    return file_bytes[:5] == b"%PDF-"


def optimize_cv(cv_bytes: bytes, job_posting: str, language: str = "pl") -> dict:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

    system_prompt = SYSTEM_PROMPT + LANGUAGE_INSTRUCTIONS.get(language, LANGUAGE_INSTRUCTIONS["pl"])

    cv_b64 = base64.standard_b64encode(cv_bytes).decode("ascii")

    user_message = [
        {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": cv_b64,
            },
        },
        {
            "type": "text",
            "text": f"""### OGŁOSZENIE O PRACĘ

{job_posting}

### AKTUALNE CV KANDYDATA

Powyżej załączony jest oryginalny plik PDF z CV kandydata (może być tekstowy lub graficzny — jeśli to skan lub PDF bez warstwy tekstowej, odczytaj go wizualnie).
""",
        },
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        thinking={"type": "adaptive"},
        output_config={
            "effort": "medium",
            "format": {
                "type": "json_schema",
                "schema": CV_JSON_SCHEMA,
            },
        },
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    text = next(block.text for block in response.content if block.type == "text")
    cv_data = json.loads(text)

    # output_config.format json_schema doesn't support "minimum"/"maximum" constraints
    # (see Anthropic structured-outputs limitations), so clamp match_score client-side.
    try:
        score = int(cv_data.get("match_score", 0))
    except (TypeError, ValueError):
        score = 0
    cv_data["match_score"] = max(0, min(100, score))

    return cv_data
