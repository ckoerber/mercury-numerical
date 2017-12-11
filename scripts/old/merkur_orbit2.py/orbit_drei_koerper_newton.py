# -*- coding: utf-8 -*-

### Darstellung des Merkurorbits mit VPython

# ----------------------------------
## Laden der Hilfsmodule
# ----------------------------------

# Da es unglaublich viel Zeit kostet ein Programm für 3-dimensionale graphische Darstellung selber 
# zu schreiben, lassen wir uns die Arbeit von "Vpython" abnehmen. Doch dazu müssen wir zunÃ¤chst 
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
# Für Venus Parameter siehe  http://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
# Für Sonnen Parameter siehe http://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html

# Physikalische Größen/Einheiten
ms = 1.9885 * 1.e30 # Sonnenmassen
AE = 1.49598 * 1.e11 # Astronomische Einheit
T  = 60 * 60 * 24    # 1 Tag
dt = 1./24*6         # 6 Stunden
# Die Gravitationskonstante
G  = 6.6738 * 1.e-11 * ms / AE**3 * T**2
print "Gravitationskonstante G = {0:1.4e} AE^3 * Tage^2 /M_Sonne".format(G)
# Die Massen der Planten (in Sonnenmassen)
m_sonne  = 1.
m_merkur = 1.66e-7
m_venus  = 2.448e-6
# Die Anfangspositionen der Planeten zum Zeitpunkt t = 0
r_sonne_0  = vector(0,0,0)
r_merkur_0 = vector(0,0.307,0) # Perihel
r_venus_0  = vector(0,0.719,0) # Perihel (Aphel: -0.728
# Die Anfangsgeschwindigkeiten zum Zeitpunkt t = 0
v_m = 58.98 * 1.e3 / AE * T
v_v = 35.26 * 1.e3 / AE * T # Perihel (Aphel: -34.79)
v_merkur_0 = vector(v_m,0,0)
v_venus_0  = vector(v_v,0,0)
v_sonne_0  = -v_merkur_0*m_merkur/m_sonne - v_venus_0*m_venus/m_sonne
print "v_Merkur v = {0:1.4e} AE / Tage ".format(v_m)
print "v_Venus v = {0:1.4e} AE / Tage ".format(v_v)

# ----------------------------------
## (a) Berechnung des Orbits
# ----------------------------------

# Die Berechnung des Orbits läuft wie folgt ab. Man übermittelt der Funktion "merkur_zeit_schritt" 
# die aktuelle Position und Geschwindigkeit des Merkurs und der Sonne. Das Ergebnis der Rechnung 
# soll die jeweils neuen Positionen und Geschwindigkeiten nach einem Zeitintervall "dt" sein.

def zeit_schritt(r_merkur, v_merkur, r_venus, v_venus, r_sonne, v_sonne):
  # Berechen die Abstandsvektoren
  r_ms = r_sonne - r_merkur
  r_vs = r_sonne - r_venus
  r_mv = r_venus - r_merkur
  # Berechne die Kräfte
  # Beachte: ein \ heißt, dass der Ausdruck in der nächsten Zeile weiter geht.
  F_m = G * m_sonne  * m_merkur / r_ms.mag**2 * norm(r_ms)\
        + G * m_venus  * m_merkur / r_mv.mag**2 * norm(r_mv)
  F_v = G * m_sonne  * m_venus  / r_vs.mag**2 * norm(r_vs)\
        + G * m_merkur * m_venus  / r_mv.mag**2 * (-1 * norm(r_mv))
  F_s = G * m_merkur * m_sonne  / r_ms.mag**2 * (-1 * norm(r_ms))\
        + G * m_venus  * m_sonne  / r_vs.mag**2 * (-1 * norm(r_vs))

  # Berechne die daraus resultierenden Geschwindigkeiten
  v_sonne_neu  = v_sonne  + F_s / m_sonne  * dt
  v_venus_neu  = v_venus  + F_v / m_venus * dt
  v_merkur_neu = v_merkur + F_m / m_merkur * dt
  # Und letztendlich die neuen Positionen
  r_sonne_neu  = r_sonne  + v_sonne_neu  * dt
  r_venus_neu  = r_venus  + v_venus_neu  * dt
  r_merkur_neu = r_merkur + v_merkur_neu * dt

  # übergabe der eben ermittelten Vektoren
  return r_merkur_neu, v_merkur_neu, r_venus_neu, v_venus_neu, r_sonne_neu, v_sonne_neu


# ----------------------------------
## (b) Zeichnung des Orbits
# ----------------------------------

def zeichne_orbit():
  # "Erstelle Merkur und Sonne"
  merkur = sphere(pos=r_merkur_0, radius=0.01, color=color.red)
  venus  = sphere(pos=r_venus_0,  radius=0.02, color=color.orange)
  sonne  = sphere(pos=r_sonne_0,  radius=0.1,  color=color.yellow)
  # Erstelle die Bahnkurve für Merkur
  merkur.bahn = curve(color=color.white)
  venus.bahn = curve(color=color.blue)
  # Weise den Planeten ihre Anfangsgeschwindigkeiten zu
  merkur.velocity = v_merkur_0
  venus.velocity  = v_venus_0
  sonne.velocity  = v_sonne_0
  # Starte die Animation
  t = 0
  while t < 1000000:
    # Bildaktualisierungsrate
    rate(60)
    # Zeichne die Bahnkurve
    merkur.bahn.append(pos=merkur.pos)
    venus.bahn.append(pos=venus.pos)
    # Berechne die neuen Positionen
    merkur.pos, merkur.velocity, venus.pos, venus.velocity, sonne.pos , sonne.velocity = zeit_schritt( 
      merkur.pos, merkur.velocity, venus.pos, venus.velocity, sonne.pos , sonne.velocity
    )
    # Nicht vergessen: Ändere die Zeit.
    t += dt

zeichne_orbit()
