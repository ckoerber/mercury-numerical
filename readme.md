Mercury Numerical Guidlines

Die Ordnerstruktur
- Die ".tex" Datei ist im "tex/" Ordner
- Wenn ihr ein Terminal nutzt -> "make" erstellt die tex Datei und kopiert das ".pdf" in den Root Ordner ("normal" kompilieren funktioniert natürich auch)
- In "Links.pages" gibt es ein paar Referenzen (Danke Inka)
- "papers/" beinhaltet die Beispielpaper


Daten bei "git" Uploaden
- Besucht das repository in eurem lokalen Ordner
- Wählt den development Branch aus: "git checkout devel" (Ihr solltet immer in diesem Branch arbeiten)
- Fügt Änderungen hinzu: "git add 'filename'" (können Mehrere sein)
- Speichert Änderung in einer (lokalen) Version ab "git commit -m 'Nachricht'"
- Sendet die lokalen Änderung an 'devel' nach GitLab ('origin') "git push origin devel
- Fertig
- Macht euch keine Sorgen darüber, dass jemand Anderes an der Datei arbeitet: Git speichert alle Änderungen getrennt ab.


Daten bei "git" Downloaden
- Siehe: "https://gitlab.version.fz-juelich.de/Mercury-Numerical/ed-paper" und folgt dem Unterpunkt "clone repository"