import pandas as pd

raw_data = """
J.SINNER
Jannik Sinner
ITA Italy
Ranking 1

23 y/o | Right handed
C.ALCARAZ
Carlos Alcaraz
ESP Spain
Ranking 2

22 y/o | Right handed
A.ZVEREV
Alexander Zverev
GER Germany
Ranking 3

28 y/o | Right handed
T.FRITZ
Taylor Fritz
USA United States
Ranking 4

27 y/o | Right handed
J.DRAPER
Jack Draper
GBR Great Britain
Ranking 5

23 y/o | Left handed
N.DJOKOVIC
Novak Djokovic
SRB Serbia
Ranking 6

37 y/o | Right handed
C.RUUD
Casper Ruud
NOR Norway
Ranking 7

26 y/o | Right handed
L.MUSETTI
Lorenzo Musetti
ITA Italy
Ranking 8

23 y/o | Right handed

A.DE MINAUR
Alex De Minaur
AUS Australia
Ranking 9

26 y/o | Right handed
H.RUNE
Holger Rune
DEN Denmark
Ranking 10

22 y/o | Right handed
D.MEDVEDEV
Daniil Medvedev
---
Ranking 11

29 y/o | Right handed
T.PAUL
Tommy Paul
USA United States
Ranking 12

28 y/o | Right handed
B.SHELTON
Ben Shelton
USA United States
Ranking 13

22 y/o | Left handed
A.FILS
Arthur Fils
FRA France
Ranking 14

20 y/o | Right handed
F.TIAFOE
Frances Tiafoe
USA United States
Ranking 15

27 y/o | Right handed
G.DIMITROV
Grigor Dimitrov
BUL Bulgaria
Ranking 16

34 y/o | Right handed
A.RUBLEV
Andrey Rublev
---
Ranking 17

27 y/o | Right handed
F.CERUNDOLO
Francisco Cerundolo
ARG Argentina
Ranking 18

26 y/o | Right handed
J.MENSIK
Jakub Mensik
CZE Czech Republic
Ranking 19

19 y/o | Right handed
S.TSITSIPAS
Stefanos Tsitsipas
GRE Greece
Ranking 20

26 y/o | Right handed
T.MACHAC
Tomas Machac
CZE Czech Republic
Ranking 21

24 y/o | Right handed
U.HUMBERT
Ugo Humbert
FRA France
Ranking 22

26 y/o | Left handed
S.KORDA
Sebastian Korda
USA United States
Ranking 23

24 y/o | Right handed
K.KHACHANOV
Karen Khachanov
---
Ranking 24

28 y/o | Right handed
A.POPYRIN
Alexei Popyrin
AUS Australia
Ranking 25

25 y/o | Right handed
A.DAVIDOVICH FOKINA
Alejandro Davidovich Fokina
ESP Spain
Ranking 26

25 y/o | Right handed
D.SHAPOVALOV
Denis Shapovalov
CAN Canada
Ranking 27

26 y/o | Left handed
M.BERRETTINI
Matteo Berrettini
ITA Italy
Ranking 28

29 y/o | Right handed
B.NAKASHIMA
Brandon Nakashima
USA United States
Ranking 29

23 y/o | Right handed
F.AUGER-ALIASSIME
Felix Auger-Aliassime
CAN Canada
Ranking 30

24 y/o | Right handed
H.HURKACZ
Hubert Hurkacz
POL Poland
Ranking 31

28 y/o | Right handed
G.MPETSHI PERRICARD
Giovanni Mpetshi Perricard
FRA France
Ranking 32

21 y/o | Right handed
A.MICHELSEN
Alex Michelsen
USA United States
Ranking 33

20 y/o | Right handed
T.GRIEKSPOOR
Tallon Griekspoor
NED Netherlands
Ranking 34

28 y/o | Right handed
F.COBOLLI
Flavio Cobolli
ITA Italy
Ranking 35

23 y/o | Right handed
S.BAEZ
Sebastian Baez
ARG Argentina
Ranking 36

24 y/o | Right handed
J.LEHECKA
Jiri Lehecka
CZE Czech Republic
Ranking 37

23 y/o | Right handed
J.THOMPSON
Jordan Thompson
AUS Australia
Ranking 38

31 y/o | Right handed
M.ARNALDI
Matteo Arnaldi
ITA Italy
Ranking 39

24 y/o | Right handed
A.MULLER
Alexandre Muller
FRA France
Ranking 40

28 y/o | Right handed
N.BORGES
Nuno Borges
POR Portugal
Ranking 41

28 y/o | Right handed
G.MONFILS
Gael Monfils
FRA France
Ranking 42

38 y/o | Right handed
M.GIRON
Marcos Giron
USA United States
Ranking 43

31 y/o | Right handed
L.SONEGO
Lorenzo Sonego
ITA Italy
Ranking 44

30 y/o | Right handed
L.DARDERI
Luciano Darderi
ITA Italy
Ranking 45

23 y/o | Right handed
M.KECMANOVIC
Miomir Kecmanovic
SRB Serbia
Ranking 46

25 y/o | Right handed
D.GOFFIN
David Goffin
BEL Belgium
Ranking 47

34 y/o | Right handed
P.MARTINEZ
Pedro Martinez
ESP Spain
Ranking 48

28 y/o | Right handed
Z.BERGS
Zizou Bergs
BEL Belgium
Ranking 49

25 y/o | Right handed
Q.HALYS
Quentin Halys
FRA France
Ranking 50

28 y/o | Right handed
A.BUBLIK
Alexander Bublik
KAZ Kazakhstan
Ranking 51

27 y/o | Right handed
C.UGO CARABELLI
Camilo Ugo Carabelli
ARG Argentina
Ranking 52

25 y/o | Right handed
G.DIALLO
Gabriel Diallo
CAN Canada
Ranking 53

23 y/o | Right handed
J.FEARNLEY
Jacob Fearnley
GBR Great Britain
Ranking 54

23 y/o | Right handed
TM.ETCHEVERRY
Tomas Martin Etcheverry
ARG Argentina
Ranking 55

25 y/o | Right handed
F.MAROZSAN
Fabian Marozsan
HUN Hungary
Ranking 56

25 y/o | Right handed
R.BAUTISTA AGUT
Roberto Bautista Agut
ESP Spain
Ranking 57

37 y/o | Right handed
J.MUNAR
Jaume Munar
ESP Spain
Ranking 58

28 y/o | Right handed
L.DJERE
Laslo Djere
SRB Serbia
Ranking 59

29 y/o | Right handed
B.BONZI
Benjamin Bonzi
FRA France
Ranking 60

28 y/o | Right handed
A.TABILO
Alejandro Tabilo
CHI Chile
Ranking 61

27 y/o | Left handed
K.NISHIKORI
Kei Nishikori
JPN Japan
Ranking 62

35 y/o | Right handed
R.CARBALLES BAENA
Roberto Carballes Baena
ESP Spain
Ranking 63

32 y/o | Right handed
F.COMESANA
Francisco Comesana
ARG Argentina
Ranking 64

24 y/o | Right handed
J.FONSECA
Joao Fonseca
BRA Brazil
Ranking 65

18 y/o | Right handed
D.ALTMAIER
Daniel Altmaier
GER Germany
Ranking 66

26 y/o | Right handed
L.TIEN
Learner Tien
USA United States
Ranking 67

19 y/o | Left handed
M.BELLUCCI
Mattia Bellucci
ITA Italy
Ranking 68

23 y/o | Left handed
D.DZUMHUR
Damir Dzumhur
BIH Bosnia and Herzegovina
Ranking 69

32 y/o | Right handed
Y.BU
Yunchaokete Bu
CHN China
Ranking 70

23 y/o | Right handed
A.RINDERKNECH
Arthur Rinderknech
FRA France
Ranking 72

29 y/o | Right handed
R.SAFIULLIN
Roman Safiullin
---
Ranking 73

27 y/o | Right handed
H.GASTON
Hugo Gaston
FRA France
Ranking 74

24 y/o | Left handed
Y.NISHIOKA
Yoshihito Nishioka
JPN Japan
Ranking 75

29 y/o | Left handed
C.MOUTET
Corentin Moutet
FRA France
Ranking 76

26 y/o | Left handed
H.MEDJEDOVIC
Hamad Medjedovic
SRB Serbia
Ranking 77

21 y/o | Right handed
A.VUKIC
Aleksandar Vukic
AUS Australia
Ranking 78

29 y/o | Right handed
R.HIJIKATA
Rinky Hijikata
AUS Australia
Ranking 79

24 y/o | Right handed
A.KOVACEVIC
Aleksandar Kovacevic
USA United States
Ranking 80

26 y/o | Right handed
C.O'CONNELL
Christopher O'Connell
AUS Australia
Ranking 82

30 y/o | Right handed
R.COLLIGNON
Raphael Collignon
BEL Belgium
Ranking 84

23 y/o | Right handed
V.KOPRIVA
Vit Kopriva
CZE Czech Republic
Ranking 85

27 y/o | Right handed
JL.STRUFF
Jan-Lennard Struff
GER Germany
Ranking 86

35 y/o | Right handed
J.DE JONG
Jesper De Jong
NED Netherlands
Ranking 87

24 y/o | Right handed
K.MAJCHRZAK
Kamil Majchrzak
POL Poland
Ranking 88

29 y/o | Right handed
B.VAN DE ZANDSCHULP
Botic Van De Zandschulp
NED Netherlands
Ranking 89

29 y/o | Right handed
C.NORRIE
Cameron Norrie
GBR Great Britain
Ranking 90

29 y/o | Left handed
A.WALTON
Adam Walton
AUS Australia
Ranking 91

26 y/o | Right handed
J.DUCKWORTH
James Duckworth
AUS Australia
Ranking 92

33 y/o | Right handed
L.NARDI
Luca Nardi
ITA Italy
Ranking 94

21 y/o | Right handed
R.OPELKA
Reilly Opelka
USA United States
Ranking 95

27 y/o | Right handed
H.DELLIEN
Hugo Dellien
BOL Bolivia
Ranking 96

31 y/o | Right handed
M.NAVONE
Mariano Navone
ARG Argentina
Ranking 98

24 y/o | Right handed
M.MCDONALD
Mackenzie Mcdonald
USA United States
Ranking 99

30 y/o | Right handed
P.CARRENO BUSTA
Pablo Carreno Busta
ESP Spain
Ranking 100

33 y/o | Right handed
A.CAZAUX
Arthur Cazaux
FRA France
Ranking 113

22 y/o | Right handed
J.FARIA
Jaime Faria
POR Portugal
Ranking 115

21 y/o | Right handed
V.ROYER
Valentin Royer
FRA France
Ranking 120

23 y/o | Right handed
T.ATMANE
Terence Atmane
FRA France
Ranking 121

23 y/o | Left handed
D.LAJOVIC
Dusan Lajovic
SRB Serbia
Ranking 124

34 y/o | Right handed
T.SCHOOLKATE
Tristan Schoolkate
AUS Australia
Ranking 127

24 y/o | Right handed
S.OFNER
Sebastian Ofner
AUT Austria
Ranking 128

29 y/o | Right handed
T.MONTEIRO
Thiago Monteiro
BRA Brazil
Ranking 130

30 y/o | Left handed
M.FUCSOVICS
Marton Fucsovics
HUN Hungary
Ranking 134

33 y/o | Right handed
E.NAVA
Emilio Nava
USA United States
Ranking 138

23 y/o | Right handed
S.WAWRINKA
Stan Wawrinka
SUI Switzerland
Ranking 139

40 y/o | Right handed
F.PASSARO
Francesco Passaro
ITA Italy
Ranking 140

24 y/o | Right handed
PH.HERBERT
Pierre-Hugues Herbert
FRA France
Ranking 149

34 y/o | Right handed
N.JARRY
Nicolas Jarry
CHI Chile
Ranking 150

29 y/o | Right handed
J.BROOKSBY
Jenson Brooksby
USA United States
Ranking 165

24 y/o | Right handed
R.GASQUET
Richard Gasquet
FRA France
Ranking 166

38 y/o | Right handed
E.RUUSUVUORI
Emil Ruusuvuori
FIN Finland
Ranking 254

26 y/o | Right handed
"""

# 1. Split into non-empty lines
lines = [l.strip() for l in raw_data.splitlines() if l.strip()]

# 2. Every 5 lines correspond to one player: code, name, country, ranking, age+handedness
rows = []
for i in range(0, len(lines), 5):
    try:
        code    = lines[i]
        name    = lines[i+1]
        country = "" if lines[i+2] == "---" else lines[i+2]
        # extract the integer after "Ranking"
        ranking = int(lines[i+3].replace("Ranking", "").strip())
        # extract the integer before "y/o"
        age      = int(lines[i+4].split("y/o")[0].strip())
        rows.append((code, name, country, ranking, age))
    except (IndexError, ValueError):
        # in case of any malformed block at the end, skip it
        continue

# 3. Build DataFrame and write CSV
df = pd.DataFrame(rows, columns=["Code", "Name", "Country", "Ranking", "Age"])
df.to_csv("tennis_players.csv", index=False)

print(f"Wrote {len(df)} players to tennis_players.csv")
