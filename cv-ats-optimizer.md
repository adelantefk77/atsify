# Skill: Optymalizator CV pod systemy ATS

## Opis

Agent AI, który na podstawie treści ogłoszenia o pracę i aktualnego CV kandydata tworzy zoptymalizowane CV zgodne z wymaganiami systemów ATS (Applicant Tracking System). Wynikiem są dwa pliki gotowe do wysłania: `.pdf` i `.docx`.

---

## Wejście

Agent otrzymuje dwa pliki:

1. **`ogloszenie.txt`** — treść ogłoszenia o pracę (skopiowana ze strony, czysty tekst)
2. **`cv_aktualne.pdf`** lub **`cv_aktualne.docx`** — aktualne CV kandydata

---

## Wyjście

Agent generuje dwa pliki:

1. **`Imie_Nazwisko_CV.pdf`** — PDF tekstowy (wyeksportowany z Worda lub Google Docs, NIE z Canvy)
2. **`Imie_Nazwisko_CV.docx`** — plik Word do dalszej edycji

---

## Instrukcje dla agenta

### KROK 1 — Analiza ogłoszenia

Przeczytaj dokładnie plik `ogloszenie.txt` i wypisz:

- **Tytuł stanowiska** — dosłowna nazwa z ogłoszenia (będzie użyta jako tytuł zawodowy w CV)
- **Wymagania obowiązkowe** — słowa kluczowe z sekcji „Wymagania" (traktuj jako priorytetowe)
- **Wymagania mile widziane** — słowa kluczowe dodatkowe
- **Obowiązki** — terminy z sekcji „Obowiązki" / „Zakres odpowiedzialności"
- **Technologie i narzędzia** — wszystkie nazwy narzędzi, systemów, języków programowania, certyfikatów
- **Klauzula RODO** — jeśli ogłoszenie zawiera własną klauzulę, zapisz jej dokładną treść

Dla każdego terminu technicznego (skrót lub pełna nazwa) zanotuj obie formy:
- `SEO` → `Search Engine Optimization (SEO)`
- `PM` → `Project Manager / Zarządzanie projektami (PM)`

### KROK 2 — Analiza aktualnego CV

Przeczytaj plik `cv_aktualne` i wypisz:

- Dane osobowe (imię, nazwisko, telefon, e-mail, miasto, LinkedIn)
- Wszystkie stanowiska z datami (MM/RRRR), nazwą firmy, miastem i opisem obowiązków
- Wykształcenie z datami i tytułami
- Istniejące umiejętności i narzędzia
- Certyfikaty i szkolenia
- Języki obce z poziomem

### KROK 3 — Dopasowanie i luki

Porównaj dane z kroków 1 i 2:

- Które słowa kluczowe z ogłoszenia **są już obecne** w CV? → zachowaj i wzmocnij
- Które słowa kluczowe z ogłoszenia **brakuje** w CV? → sprawdź, czy kandydat ma tę kompetencję opisaną inaczej; jeśli tak, przepisz używając języka z ogłoszenia
- Które wymagania obowiązkowe **kandydat realnie spełnia** (nawet jeśli nie użył tych słów)? → dodaj do CV w odpowiednich miejscach
- **Nie wymyślaj kompetencji, których kandydat nie posiada.** Optymalizacja = lepsze opisanie tego, co jest.

### KROK 4 — Budowanie zoptymalizowanego CV

Utwórz nowe CV zgodnie z poniższymi zasadami:

#### 4.1 Struktura i formatowanie (ATS-safe)

- **Układ jednokolumnowy** — żadnych tabel, ramek, kolumn, pól tekstowych
- **Czcionka**: Arial lub Calibri, 11 pkt dla tekstu, 14 pkt dla nagłówków sekcji
- **Marginesy**: 2,54 cm (standardowe) lub 1,27 cm
- **Kolor**: czarny tekst na białym tle — żadnych kolorowych nagłówków, ikon, wykresów
- **Punktory**: wyłącznie `•` lub `-` — żadnych gwiazdek, strzałek, emoji
- **Dane kontaktowe**: umieść w treści dokumentu (NIE w nagłówku/stopce Word)
- **Format dat**: MM/RRRR konsekwentnie w całym dokumencie

#### 4.2 Standardowe sekcje (w tej kolejności)

```
1. DANE KONTAKTOWE
2. PODSUMOWANIE ZAWODOWE
3. DOŚWIADCZENIE ZAWODOWE
4. WYKSZTAŁCENIE
5. UMIEJĘTNOŚCI
6. CERTYFIKATY / SZKOLENIA  (jeśli dotyczy)
7. JĘZYKI OBCE
8. Klauzula RODO
```

**Używaj dokładnie tych nazw sekcji** — ATS rozpoznaje standardowe nagłówki. Nie używaj: „Moje kompetencje", „Toolkit", „Moja droga", „Co potrafię".

#### 4.3 Sekcja: Dane kontaktowe

```
Jan Kowalski
+48 XXX XXX XXX | jan.kowalski@email.com | Warszawa
linkedin.com/in/jankowalski
```

#### 4.4 Sekcja: Podsumowanie zawodowe

- 3–5 zdań
- Użyj **dokładnego tytułu stanowiska z ogłoszenia** w pierwszym zdaniu
- Wplecione 3–5 najważniejszych słów kluczowych z ogłoszenia
- Konkretne liczby i osiągnięcia tam, gdzie to możliwe
- **Nie pisz** generycznych fraz jak „dynamiczny profesjonalista" czy „zorientowany na wyniki"

Przykład:
> Doświadczony **Specjalista ds. Marketingu Cyfrowego** z 6-letnim stażem w zarządzaniu kampaniami performance i strategią SEO. Zwiększyłem ruch organiczny o 60% i przychody online o 1,2 mln PLN rocznie. Specjalizuję się w Google Analytics 4, Meta Ads i automatyzacji marketingu (Marketing Automation).

#### 4.5 Sekcja: Doświadczenie zawodowe

Format każdego stanowiska:

```
TYTUŁ STANOWISKA
Nazwa Firmy | Miasto | MM/RRRR – MM/RRRR (lub „obecnie")

• [Czasownik akcji] + [zadanie/zakres odpowiedzialności] + [mierzalny wynik] + [słowa kluczowe]
• [Czasownik akcji] + [zadanie] + [wynik liczbowy]
• [Czasownik akcji] + [narzędzie/technologia] + [efekt]
```

**Zasady:**
- Każdy punkt zaczyna się od mocnego czasownika: *zarządzałem, wdrożyłem, zoptymalizowałem, zwiększyłem, zredukowałem, opracowałem, koordynowałem, zaprojektowałem, negocjowałem, zautomatyzowałem*
- Dodaj liczby wszędzie tam, gdzie to możliwe (%, PLN, liczba osób, czas)
- Wplecione słowa kluczowe z ogłoszenia w naturalnym kontekście
- Kolejność odwrotnie chronologiczna (najnowsze stanowisko na górze)

#### 4.6 Sekcja: Umiejętności

Podziel na kategorie, np.:

```
Techniczne: Python, SQL, Google Analytics 4, Power BI
Narzędzia: Jira, Confluence, Salesforce, HubSpot
Języki obce: angielski (C1), niemiecki (B2)
Inne: Zarządzanie projektami (PM), Scrum, Agile
```

- Lista 8–15 pozycji
- Używaj **pełnych nazw i skrótów**: `Search Engine Optimization (SEO)`, nie samo `SEO`
- Dopasuj terminologię do słownika z ogłoszenia
- Sprawdź pisownię nazw technologii (literówka = brak dopasowania w ATS)

#### 4.7 Optymalizacja słów kluczowych — zasady końcowe

- Każde ważne słowo kluczowe powinno pojawić się **2–3 razy** w różnych sekcjach (podsumowanie + umiejętności + doświadczenie)
- Celuj w **65–75% dopasowania** słów kluczowych do ogłoszenia
- Użyj **dokładnych sformułowań z ogłoszenia** — jeśli ogłoszenie mówi „Google Analytics 4", nie pisz „GA4"
- Nie ukrywaj słów kluczowych białym tekstem ani w komentarzach — ATS to wykrywa i może odrzucić aplikację

#### 4.8 Klauzula RODO

Umieść na samym dole, czcionką 8–9 pkt:

- **Jeśli ogłoszenie zawiera własną klauzulę** → użyj jej dokładnego brzmienia
- **Jeśli brak klauzuli w ogłoszeniu** → użyj standardowej:

> *„Wyrażam zgodę na przetwarzanie moich danych osobowych dla potrzeb niezbędnych do realizacji procesu rekrutacji zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (RODO)."*

**Ważne:** Stara klauzula odwołująca się do ustawy z 1997 r. jest nieważna — nie używaj jej.

### KROK 5 — Generowanie plików wyjściowych

1. Wygeneruj dokument w formacie **DOCX** (Word-compatible XML) z zastosowanym formatowaniem
2. Wyeksportuj PDF jako **PDF tekstowy** (nie graficzny) — tekst musi być selektowalny
3. Sprawdź: zaznacz cały tekst PDF (Ctrl+A), skopiuj do notatnika — jeśli tekst jest czytelny i w poprawnej kolejności, parsowanie ATS będzie działać
4. Nazwa pliku: `Imie_Nazwisko_CV.pdf` i `Imie_Nazwisko_CV.docx`

---

## Czego NIE robić (błędy krytyczne)

| Błąd | Dlaczego | Co zrobić zamiast |
|---|---|---|
| Układ dwukolumnowy | ATS miesza kolumny, tworząc nonsens | Układ jednokolumnowy |
| Tabele i ramki | Parser gubi kolejność tekstu | Czysty tekst z punktorami |
| Grafiki, ikony, paski % | Całkowicie niewidoczne dla ATS | Tekst: „angielski C1" zamiast 4/5 gwiazdek |
| Dane kontaktowe w nagłówku Word | 25% systemów ATS nie czyta nagłówków | Dane w treści dokumentu |
| Canva, Figma, InDesign | Tekst jako warstwy graficzne = pusta strona dla ATS | Word lub Google Docs → PDF |
| Niestandardowe sekcje | ATS nie rozpozna „Moje supermoce" | Standardowe: „Umiejętności" |
| Tylko skrót lub tylko pełna nazwa | „SEO" ≠ „Search Engine Optimization" | Zawsze oba: „SEO (Search Engine Optimization)" |
| Literówki w technologiach | „Pytohn" ≠ „Python" | Sprawdź każdą nazwę techniczną |
| Brak klauzuli RODO | Pracodawca nie może legalnie przetworzyć CV | Dodaj klauzulę RODO |
| Format funkcjonalny (skill-based) | Dezorientuje algorytmy ATS | Format odwrotnie chronologiczny |

---

## Kontrola jakości przed zapisaniem pliku

Przed wygenerowaniem pliku wyjściowego odpowiedz na każde pytanie:

- [ ] Czy użyto dokładnego tytułu stanowiska z ogłoszenia w podsumowaniu?
- [ ] Czy wszystkie wymagania obowiązkowe z ogłoszenia są pokryte w CV?
- [ ] Czy każde ważne słowo kluczowe pojawia się 2–3 razy?
- [ ] Czy stosowane są pełne nazwy i skróty jednocześnie?
- [ ] Czy układ jest jednokolumnowy, bez tabel i grafik?
- [ ] Czy dane kontaktowe są w treści dokumentu (nie w nagłówku)?
- [ ] Czy nazwy sekcji są standardowe po polsku?
- [ ] Czy format dat to MM/RRRR?
- [ ] Czy klauzula RODO jest aktualna (post-2018)?
- [ ] Czy tekst PDF jest selektowalny (nie graficzny)?

---

## Kontekst: dlaczego te zasady są ważne

- **62%** polskich pracodawców używa systemów ATS (2025)
- **43%** niepowodzeń w ATS wynika z brakujących słów kluczowych
- **28%** z problemów formatowania
- CV z **dokładnym tytułem stanowiska** z ogłoszenia mają **10,6x większą szansę** na zaproszenie na rozmowę
- ATS **nie odrzuca** CV automatycznie — **rankinguje** je. Pozycja 45 z 250 to funkcjonalnie to samo co brak aplikacji
- Lider polskiego rynku ATS: **eRecruiter** (31% rekruterów); dominuje też **Traffit**, **Workday**, **SAP SuccessFactors**
