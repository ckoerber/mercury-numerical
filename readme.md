Mercury Numerical Guidlines

Die Ordnerstruktur
- Die ".tex" Datei ist im "tex/" Ordner
- Wenn ihr ein Terminal nutzt -> "make" erstellt die tex Datei und kopiert das ".pdf" in den Root Ordner ("normal" kompilieren funktioniert natürich auch)
- In "Links.pages" gibt es ein paar Referenzen (Danke Inka)
- "papers/" beinhaltet die Beispielpaper


Daten bei "git" Uploaden
- Besucht das repository in eurem lokalen Ordner
- Holt euch die aktuelle Version: "git pull"
- Testet ob ihr im development Branch seid: "git branch" sollte ein grünes "devel" wiedergeben
- (wenn nicht tippt "git checkout devel" [Ihr solltet immer in diesem Branch arbeiten])
- Fügt Änderungen hinzu: "git add 'filename'" (das könnt ihr mehrfach wiederholen)
- Speichert Änderung in einer (lokalen) Version ab "git commit -m 'Nachricht'"
- Sendet die lokalen Änderung an 'devel' nach GitLab ('origin') "git push origin devel -u" (Sobald ihr diesen Befehl einmalig eingegeben habt, reicht auch ein einfaches "git push")
- Fertig
- Macht euch keine Sorgen darüber, dass jemand Anderes an der Datei arbeitet: Git speichert alle Änderungen getrennt ab.


Daten bei "git" Downloaden
- "git pull"

Einrichten von "git"
- Wechselt zu einem lokalen Ordner der Wahl "cd mercury"
- Kopiert dieses Repository "git clone ssh://git@gitlab.version.fz-juelich.de:10022/Mercury-Numerical/ed-paper.git"
- Wechselt zu dem Entwicklungszweig: "git checkout devl"
- Jetzt könnt ihr lokale Änderungen vornehmen und sie uploaden, wenn ihr zufrieden seid.