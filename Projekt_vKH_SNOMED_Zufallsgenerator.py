###############################################################################
# Projekt "virtuelles Krankenhaus"
#
# Programmtyp: Zufallsgenerator für Patienten (auf Basis von JSON Dokumenten)
# Patienten haben Alter, Geschecht, Krankheit (nur AIDS) und Symptome
#
# Versionsnummer: V2.0
#
# Autoren: Studenten der THB
###############################################################################



###############################################################################
 # Teilaufgabe 1: Zugriff auf unsere JSON Dokumente, damit von dort die Daten verwendet werden können.
###############################################################################



 # Import der Bibliotheken
import json
import os
from random import randint
import random



 # Pfad der JSON Dateien (Krankheiten und Patient)
CWD = os.getcwd()
AIDS_FILE_PATH = '%s/%s' % (CWD, 'Snomed_JSON_AIDS_V1_2020-12-15.json')
PATIENT_FILE_PATH =  '%s/%s' % (CWD, 'Snomed_JSON_Patient_V1_2020-12-15.json')

 # Dictionary aus den JSON Dateien erstellen
AIDS_PROPERTIES = {}
PATIENT_PROPERTIES = {}

 # Versuche: Oeffnen der JSON Dateien, Parsing (wie Casting in Java) in einen String und Speichern in Dictionary
 # Falls nicht: IOError
try:
   with open(AIDS_FILE_PATH) as data_file:
      AIDS_PROPERTIES = json.load(data_file)
except IOError as e:
   print(e)
   print('IOError: Unable to open Snomed_JSON_AIDS_V1_2020-12-15.json. Terminating execution.')
   exit(1)

try:
   with open(PATIENT_FILE_PATH) as data_file:
      PATIENT_PROPERTIES = json.load(data_file)
except IOError as e:
   print(e)
   print('IOError: Unable to open Snomed_JSON_Patient_V1_2020-12-15.json. Terminating execution.')
   exit(1)



###############################################################################
 # Teilaufgabe 2: Zufallsgenerator für das Alter (von ... bis ...) bauen.
###############################################################################



 # Auslesen des Erkrankungsalters
alterAids_pre = PATIENT_PROPERTIES['Patientendaten'][0]['Alter'] #20

 # Parsing aus String in Integer Datentyp
alterAids = int(alterAids_pre)

 #Zufaelliges Alter zwischen Risikoalter bis maximale Lebenserwartung eines Menschen (120)
zufallsAlterAids = randint(alterAids, 120)
print('Das Patient*in-Alter betraegt:')
print(zufallsAlterAids)
print()



###############################################################################
 # Teilaufgabe 3: Zufallsgenerator für das Geschlecht (m/ w/ d) bauen.
###############################################################################



 # Auslesen der Erkrankungsrate
percentMaleAids_pre = PATIENT_PROPERTIES['Patientendaten'][0]['MGeschlecht'] #77.8
percentFemaleAids_pre = PATIENT_PROPERTIES['Patientendaten'][0]['WGeschlecht'] #21.9
percentDiverseAids_pre = PATIENT_PROPERTIES['Patientendaten'][0]['DGeschlecht'] #0.3

 # Parsing aus String in Float Datentyp
percentMaleAids = float(percentMaleAids_pre) #77.8
percentFemaleAids = float(percentFemaleAids_pre) #21.9
percentDiverseAids = float(percentDiverseAids_pre) #0.3

 # von Prozent zu 0. Zahlen
decimalMaleAids = percentMaleAids / 100 #0.778
decimalFemaleAids = percentFemaleAids / 100 #0.219
decimalDiverseAids = percentDiverseAids / 100 #0.003

 # Auswahl Geschlecht m || w || d
zufallsGeschlecht = random.uniform(0,1)
if zufallsGeschlecht <= decimalMaleAids:
   print('Patient*in ist m')
elif (zufallsGeschlecht > decimalMaleAids) and (zufallsGeschlecht <= (decimalMaleAids + decimalFemaleAids)):
   print('Patient*in ist f')
elif zufallsGeschlecht >= (decimalMaleAids + decimalFemaleAids):
   print('Patient*in ist d')
else:
   print('An Error occured in elif zufallsGeschlecht, line 106.')

print()



###############################################################################
 # Teilaufgabe 4: Zufallsgenerator für die Krankheit (passend zu Alter und Geschlecht) bauen.
###############################################################################



  #####################################################
  # !!! ACHTUNG: hier sollte eine Auswahl hin, sodass zwischen allen 8 Krankheiten gewählt werden kann !!!
  ######################################################
 # Anzahl der Krankheiten aktuell 8
zufallsKrankheit = randint(1,8)



###############################################################################
 # Teilaufgabe 5: Zufallsgenerator für  Symptome (drei zufällige, passend zur Krankheit) bauen.
###############################################################################



 # Array fuer Symptome von Aids
pfadSymptomeAids = AIDS_PROPERTIES['disease']['symptom']

 # Speichern der Symptom-Namen in einem Array
namenSymptomeAids = []

for index in pfadSymptomeAids:
   namenSymptomeAids.append(index['name'])

i = 0
randomNames = []

 # 3 Zufaellige Symptomnamen wählen. Falls Duplikate drin sind, ersetzen
print('3 zufaellige Symptome:')
while i < 3:
  randomSymptomAids = random.choice(list(namenSymptomeAids))
  if randomSymptomAids in randomNames:
      print('duplicate')
  else:
      randomNames.append(randomSymptomAids)
      i = i + 1
  print(randomSymptomAids)

print()

 # Ausgabe der Symptomliste
print('3 zufaellige Symptome als Array:')
randomNames = list(set(randomNames))
print(randomNames)
