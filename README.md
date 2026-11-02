# Attest-datamodel

Fælles SQLAlchemy-modeller til applikationer, der bruger attestdatabasen. Pakken
eksporterer `Base`, de mappede klasser og deres enum-typer fra
`attest_data_model`. Applikationerne bør bruge den samme gennemgåede udgivelse
og importere modellerne fra pakken i stedet for at vedligeholde lokale kopier.

## Installation

Pakken kan installeres direkte fra dette offentlige GitHub-repository uden at
udgive den til PyPI eller flytte en wheel-fil. Git skal være installeret og
tilgængeligt i `PATH`. Tilføj følgende linje til `requirements.txt` i hver
applikation, og erstat `<full-commit-sha>` med det samme testede commit i alle
applikationer:

```text
attest-data-model @ git+https://github.com/Randers-Kommune-Digitalisering/attest-data-model.git@<full-commit-sha>
```

Opret et virtuelt miljø i applikationsprojektet, og installer afhængighederne
lokalt, for eksempel i PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

I applikationens GitHub Actions-workflow kan den samme fil installeres efter
`actions/checkout` og `actions/setup-python`:

```yaml
- name: Install dependencies
	run: python -m pip install -r requirements.txt
```

Pip henter kildekoden, bygger pakken midlertidigt og installerer den sammen
med dens afhængigheder. Et offentligt repository kræver ingen deploy key.
Fastlås et commit frem for den flytbare `main`-gren, så lokale installationer
og CI bruger samme modelversion.

Applikationerne kan for eksempel bruge
`from attest_data_model import AttestationRequest, OrderStatus`. Opgrader hver
applikation med en gennemgået ændring af afhængigheden, og kør dens
integrationstests mod det aftalte databaseskema inden udrulning.

## Udgivelser og databaseændringer

Pakkens første version er `1.0.0`. Følg semantisk versionering: Hæv
hovedversionen ved inkompatible ændringer af modellen eller databasekontrakten,
underversionen ved bagudkompatible tilføjelser og rettelsesversionen ved
bagudkompatible fejlrettelser. Byg en wheel med
`python -m pip wheel . --no-deps`, og test med
`python -m unittest discover -s tests`. Et udgivelsestag kan markere det
testede commit, men det er ikke nødvendigt for installation fra Git. Flyt
aldrig et udgivelsestag. Den nuværende
`.github/workflows/publish-to-pypi.yml` udgiver automatisk tags som `v1.0.0`
til PyPI; deaktivér eller fjern workflowet, inden sådanne tags oprettes, hvis
pakken ikke skal udgives der.

Modellerne migrerer ikke databasen. Opbevar Alembic-migrationer i det projekt,
der ejer databasen, koordinér migrationer og udrulning af applikationer med
kompatible pakkeversioner, og brug ikke `Base.metadata.create_all()` som
migrationsstrategi i produktion. Skemaet indeholder personoplysninger. Vurder
risici for databeskyttelsen, begræns databaseadgang til det nødvendige, brug
krypterede forbindelser og anvend genererede data frem for produktionsdata i
tests.