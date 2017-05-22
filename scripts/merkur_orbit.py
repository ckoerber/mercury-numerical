#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Darstellung des Merkurorbits mit VPython


# ----------------------------------
## Laden der Hilfsmodule
# ----------------------------------

# Da es unglaublich viel Zeit kostet ein Programm für 3-dimensionale graphische Darstellung selber 
# zu schreiben, lassen wir uns die Arbeit von "Vpython" abnehmen. Doch dazu müssen wir zunächst 
# dieses Modul bereitstellen. Das erreicht man mit Hilfe des Befehls "import" oder "from .. import".

from visual import vector, sphere, color, curve, rate, display

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

# Physikalische Größen/Einheiten
ms = 1.98892 * 1.e30 # Sonnenmassen
AE = 1.49598 * 1.e11 # Astronomische Einheit
T  = 60 * 60 * 24    # 1 Tag
dt = 1./24*6         # 8 Stunden
# Die Gravitationskonstante
G  = 6.6738 * 1.e-11 * ms / AE**3 * T**2
print "Gravitationskonstante G = {0:1.4e} AE^3 * Tage^2 /M_Sonne".format(G)
# Die Massen der Planten (in Sonnenmassen)
m_sonne  = 1.
m_merkur = 0.055
# Die Anfangspositionen der Planeten zum Zeitpunkt t = 0
r_sonne_0  = vector(0,0,0)
r_merkur_0 = vector(0,0.307,0) # Perihel
# Die Anfangsgeschwindigkeiten zum Zeitpunkt t = 0
v_m = 47.36 * 1.e3 / AE * T
v_s = - v_m * m_merkur / m_sonne # Impulserhaltung
v_sonne_0  = vector(v_s,0,0)
v_merkur_0 = vector(v_m ,0,0)
print "v_Merkur v = {0:1.4e} AE / Tage ".format(v_m)

# ----------------------------------
## (a) Berechnung des Orbits
# ----------------------------------

# Die Berechnung des Orbits läuft wie folgt ab. Man übermittelt der Funktion "merkur_zeit_schritt" 
# die aktuelle Position und Geschwindigkeit des Merkurs und der Sonne. Das Ergebnis der Rechnung 
# sollist die jeweils neuen Positionen und Geschwindigkeiten nach einem Zeitintervall "dt" sein.

def merkur_zeit_schritt(r_merkur, v_merkur, r_sonne, v_sonne):
  # <----- Ändere dies ------->
  # Berechne den Vektor der von Merkur nach Sonne zeigt
  r_ms = r_sonne - r_merkur
  # Berechne die Kräfte
  try:
    F_ms = - G * m_sonne * m_merkur / r_ms.mag()**2 * r_ms.norm()
  except TypeError:
    F_ms = - G * m_sonne * m_merkur / r_ms.mag**2 * r_ms.norm()
  F_sm = - F_ms
  # Berechne die daraus resultierenden Geschwindigkeiten
  v_sonne_neu  = v_sonne  + F_ms / m_sonne  * dt
  v_merkur_neu = v_merkur + F_sm / m_merkur * dt
  # Und letztendlich die neuen Positionen
  r_sonne_neu  = r_sonne  + v_sonne_neu  * dt
  r_merkur_neu = r_merkur + v_merkur_neu * dt

  # Übergabe der eben ermittelten Vektoren
  return r_merkur_neu, v_merkur_neu, r_sonne_neu, v_sonne_neu

# Test: Was ist das Ergebnis von?
merkur_zeit_schritt(r_merkur_0, v_merkur_0, r_sonne_0, v_sonne_0)

# Ergebnis:
# (<0.006838, 0.466915, 0.000000>,
#  <0.027353, -0.000339, 0.000000>,
#  <-0.000376, 0.000005, 0.000000>,
#  <-0.001504, 0.000019, 0.000000>)

# ----------------------------------
## (b) Zeichnung des Orbits
# ----------------------------------

def zeichne_orbit():
  # <----- Ändere dies ------->
  # "Erstelle Merkur und Sonne"
  merkur = sphere( pos=r_merkur_0, radius=0.01, color=color.red   )
  sonne  = sphere( pos=r_sonne_0 , radius=0.1, color=color.yellow)
  # Erstelle die Bahnkurve für Merkur
  merkur.bahn = curve(color=color.black)
  # Weise den Planeten ihre Anfangsgeschwindigkeiten zu
  merkur.velocity = v_merkur_0
  sonne.velocity  = v_sonne_0
  # Starte die Animation
  t = 0
  while t < 120*6:
    # Bildaktualisierungsrate
    rate(18)
    # Zeichne die Bahnkurve
    merkur.bahn.append( pos=merkur.pos )
    # Berechne die neuen Positionen
    merkur.pos, merkur.velocity, sonne.pos , sonne.velocity = merkur_zeit_schritt( 
        merkur.pos, merkur.velocity, sonne.pos , sonne.velocity
    )
    # Nicht vergessen: Ändere die Zeit.
    t += dt


# ----------------------------------
## Ausführen der Funktionen
# ----------------------------------

display(background=color.white)
zeichne_orbit()



##############################################################################
##############################################################################
##############################################################################
# Zusatzaufgaben:
# Periheldrehung mit 1/r^3 (Parameter)
# Dreikörperkräfte -> Parameter für nächsten relevanten Planeten raussuchen

