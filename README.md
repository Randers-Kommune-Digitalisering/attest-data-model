# Attest-datamodel

Fælles SQLAlchemy-modeller til applikationer, der bruger attestdatabasen. Pakken
eksporterer `Base`, de mappede klasser og deres enum-typer fra
`attest_data_model`. Applikationerne bør bruge den samme gennemgåede udgivelse
og importere modellerne fra pakken i stedet for at vedligeholde lokale kopier.

## Installation

Udgiv en uforanderlig version til organisationens private, PyPI-kompatible
pakkeregister, og fastlås derefter den præcise version i hver applikations
afhængigheder:

```text
attest-data-model==1.0.0
```

Konfigurer adgang til pakkeregisteret via driftsmiljøets godkendte løsning til
håndtering af adgangsoplysninger, ikke i dette repository. GitHub Packages er
ikke et PyPI-kompatibelt pakkeregister til Python. Hvis et privat pakkeregister
ikke er tilgængeligt, skal pakken installeres fra et bestemt Git-commit (og
have et udgivelsestag, så versionen er nem at finde):

```text
attest-data-model @ git+https://github.com/<org>/attest-data-model.git@<full-commit-sha>
```

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
`python -m unittest discover -s tests`. Opret et tag på det testede commit, og
udgiv dets build. Overskriv aldrig en udgivet version, og flyt aldrig et
udgivelsestag.

Modellerne migrerer ikke databasen. Opbevar Alembic-migrationer i det projekt,
der ejer databasen, koordinér migrationer og udrulning af applikationer med
kompatible pakkeversioner, og brug ikke `Base.metadata.create_all()` som
migrationsstrategi i produktion. Skemaet indeholder personoplysninger. Vurder
risici for databeskyttelsen, begræns databaseadgang til det nødvendige, brug
krypterede forbindelser og anvend genererede data frem for produktionsdata i
tests.