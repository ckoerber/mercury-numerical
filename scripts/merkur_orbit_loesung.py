# -*- coding: utf-8 -*-

### Darstellung des Merkurorbits mit VPython

# ----------------------------------
## Laden der Hilfsmodule
# ----------------------------------

# Da es unglaublich viel Zeit kostet ein Programm für 3-dimensionale graphische Darstellung selber
# zu schreiben, lassen wir uns die Arbeit von "Vpython" abnehmen. Doch dazu müssen wir zunächst
# dieses Modul bereitstellen. Das erreicht man mit Hilfe des Befehls "import" oder "from .. import".

from visual import *

# Schreibt man
#   "from visual import *"
# bedeutet dies: "Lade alle Funktionen von Vpython so, dass man sie direkt verwenden kann:
#   "func = function(..)".
# Würde man
#   "import visual"
# schreiben, so müsste man die Funktion wie folgt aufrufen:
#   "func = visual.function(..)".

# Eine Dokumentation von Modulen lässt sich durch den Befehl "help( modul_name )" aufrufen.
#
# Tipp: Will man eine Eingabe unterdrücken, so lässt sich dies auch mit "#" tun. Der darauf
# folgende Text wird dabei von Python überlesen.

# help(visual)

# ----------------------------------
## Aufgabe 1: Merkurorbit)
# ----------------------------------

# Funktionen werden in Python wie folgt deklariert:
# def func(x):
#     .... Rechnung und Anderes ....
# 
# Diese wollen wir nun nutzen. Um die Umlaufbahn des Merkurs darzustellen, ist es sinvoll die
# Aufgabe in zwei Abschnitte zu Teilen:
# (a) Berchnung des Orbits
# (b) Zeichnung des Orbits
# Für beide Abschnitte werden wir Funktionen nutzen.


# ----------------------------------
## Parameter
# ----------------------------------

# Für Merkur Parameter siehe http://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html
# Für Sonnen Parameter siehe http://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html

# Alle Größen sind in einem angepassten Einheitensystem gegeben:
#  - Längen in Einheiten von R0 = 1e10 m
#  - Zeiten in Einheiten von T0 = 1 d = 60*60*24 s
#  - Massen in Einheiten von M0 = m_sonne = 1.989e30 kg

# Massen von Sonne und Merkur
m_sonne = 1.
m_merkur = 1.66e-7

# Anfangsposition und -geschwindigkeit des Merkur (im Perihel)
r_merkur_0 = vector(0, 4.6, 0)  # im Perihel
v_merkur_0 = vector(0.51, 0, 0) # im Perihel
# Anfangsposition und -geschwindigkeit der Sonne (festgelegt als Koordinatenursprung)
r_sonne_0 = vector(0, 0, 0)
v_sonne_0 = - v_merkur_0 * m_merkur / m_sonne # Impulserhaltung

# Gravitationskonstante berechnet als G' * M0 * T0**2 / R0**3
# mit G' = 6.6738e11 m**3 / kg / s**2
G = 0.99

# Scharzschild parameter
rS = 3.e-7

# Dauer der Simulation in Erdentagen
T = 88
# Zeitschritt der Simulation in Erdentagen
dt = 2*v_merkur_0.mag/G/100

# ----------------------------------
## (a) Berechnung des Orbits
# ----------------------------------

# Die Berechnung des Orbits läuft wie folgt ab. Man übermittelt der Funktion "merkur_zeit_schritt"
# die aktuelle Position und Geschwindigkeit des Merkurs und der Sonne. Das Ergebnis der Rechnung
# soll die jeweils neuen Positionen und Geschwindigkeiten nach einem Zeitintervall "dt" sein.

def merkur_zeit_schritt(r_merkur, v_merkur, r_sonne, v_sonne, alpha=0):
  # Berechne den Vektor der von Merkur nach Sonne zeigt
  r_ms = r_sonne - r_merkur
  # Berechne die Kraefte
  F_ms = - G * m_sonne * m_merkur / r_ms.mag**2 * norm(r_ms)
  F_ms = F_ms - G * m_sonne * m_merkur * alpha / r_ms.mag**3 * norm(r_ms) * rS
  F_sm = - F_ms
  # Berechne die daraus resultierenden Geschwindigkeiten
  v_sonne_neu  = v_sonne  + F_ms / m_sonne  * dt
  v_merkur_neu = v_merkur + F_sm / m_merkur * dt
  # Und letztendlich die neuen Positionen
  r_sonne_neu  = r_sonne  + v_sonne_neu  * dt
  r_merkur_neu = r_merkur + v_merkur_neu * dt

  # uebergabe der eben ermittelten Vektoren
  return r_merkur_neu, v_merkur_neu, r_sonne_neu, v_sonne_neu

# Test: Was ist das Ergebnis von?
merkur_zeit_schritt(r_merkur_0, v_merkur_0, r_sonne_0, v_sonne_0)

# ----------------------------------
## (b) Zeichnung des Orbits
# ----------------------------------

def zeichne_orbit(alpha=0):
  # "Erstelle Merkur und Sonne"
  merkur = sphere( pos=r_merkur_0, radius=0.2, color=color.red   )
  sonne  = sphere( pos=r_sonne_0 , radius=0.8, color=color.yellow)
  # Erstelle die Bahnkurve fuer Merkur
  merkur.bahn = curve(color=color.white)
  # Weise den Planeten ihre Anfangsgeschwindigkeiten zu
  merkur.velocity = v_merkur_0
  sonne.velocity  = v_sonne_0
  # Starte die Animation
  t = 0
  while t < 88*6:
    # Bildaktualisierungsrate
    rate(1000)
    # Zeichne die Bahnkurve
    merkur.bahn.append( pos=merkur.pos )
    # Berechne die neuen Positionen
    merkur.pos, merkur.velocity, sonne.pos , sonne.velocity = merkur_zeit_schritt( 
        merkur.pos, merkur.velocity, sonne.pos , sonne.velocity, alpha=alpha
    )
    # Nicht vergessen: Ändere die Zeit.
    t += dt


# ----------------------------------
## Ausführen der Funktionen
# ----------------------------------

zeichne_orbit(5.e6)

