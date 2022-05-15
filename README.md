# Algorithms for Graphs – Programmieraufgaben (Tampere University, 2022)

Drei Programmieraufgaben aus der Lehrveranstaltung **Algorithms for Graphs** an der **Tampere University** (Finnland), die ich im Frühjahr 2022 während meines Auslandssemesters gelöst habe.

**Autor:** Adrian Wimmer · **Uni:** Tampere University, Finnland · **Kurs:** Algorithms for Graphs · **Zeitraum:** Februar bis April 2022 · **Sprache:** Python 3

| # | Ordner | Algorithmus | Abgabe |
|---|---|---|---|
| 1 | [`01-bfs-shortest-path-trees`](01-bfs-shortest-path-trees) | Alle Bäume kürzester Wege (BFS) ab einem Startknoten | 13.02.2022 |
| 2 | [`02-floyd-warshall-all-paths`](02-floyd-warshall-all-paths) | Floyd-Warshall: Pfadmatrix aller minimal gewichteten Wege, mit Erkennung negativer Zyklen | 20.03.2022 |
| 3 | [`03-mst-cycle-elimination`](03-mst-cycle-elimination) | Minimaler Spannbaum durch Zyklen-Eliminierung (DFS) | April 2022 |

In jedem Ordner liegt eine eigene `graafi3.py`. Das ist die Graph-Hilfsklasse, die der Kurs vorgegeben hat („graafi“ ist Finnisch für Graph). Sie liest einen Graphen aus einer Textdatei ein, und ich habe sie für jede Aufgabe leicht angepasst.

## Ausführen

```bash
pip install -r requirements.txt   # numpy, nur für Aufgabe 2
cd 01-bfs-shortest-path-trees && python allMinSpanT.py
cd 02-floyd-warshall-all-paths && python allPathsFW.py
cd 03-mst-cycle-elimination   && python MSTCYCLE.py
```

Welcher Testgraph verwendet wird, steht jeweils im `__main__`-Block. Die Testgraphen liegen in `test_graphs/`.

---

## 1 · Alle Bäume kürzester Wege (BFS)

**Datei:** `allMinSpanT.py` · **Abgabe:** 13.02.2022

Die Breitensuche startet bei Knoten `s` und merkt sich für jeden Knoten **alle** Eltern, die genau eine Ebene näher am Start liegen. Das kartesische Produkt (`itertools.product`) über diese Elternlisten liefert alle verschiedenen Bäume kürzester Wege. Das Skript gibt jeden Baum als Dictionary `{Knoten: Elternknoten}` aus und schreibt ihn in eine eigene Datei `tree_<n>.txt`.

Beispiel (`G03Python.txt`, Start 4), Auszug:
```
{1: 4, 2: 1, 3: 4, 4: 'Nil', 5: 3, 6: 2, 7: 1}
{1: 4, 2: 1, 3: 4, 4: 'Nil', 5: 3, 6: 7, 7: 1}
...  (insgesamt 6 Bäume)
```

## 2 · Floyd-Warshall mit Pfadmatrix

**Datei:** `allPathsFW.py` · **Abgabe:** 20.03.2022

1. Floyd-Warshall berechnet die Distanzmatrix `d` und die Elternmatrix `p` eines gewichteten, gerichteten Graphen.
2. Drei Bedingungen markieren die Knotenpaare (i, j), für die **kein** minimal gewichteter Weg existiert:
   - j ist von i aus nicht erreichbar,
   - i liegt auf einem negativen Zyklus,
   - auf dem Weg von i nach j liegt ein negativer Zyklus.
3. Für alle übrigen Paare wird der Weg über `p` rekonstruiert und als Pfadmatrix ausgegeben.

Beispiel (`G03PythonFW.txt`):
```
[['<>' '<>' '<>' '<>' '<>' '<>']
 ['<>' '<>' '<>' '<>' '<>' '<>']
 ['<>' '<>' '<3>' '<3,4>' '<3,4,5>' '<3,6>']
 ['<>' '<>' '<4,5,3>' '<4>' '<4,5>' '<4,5,3,6>']
 ['<>' '<>' '<5,3>' '<5,3,4>' '<5>' '<5,3,6>']
 ['<>' '<>' '<6,3>' '<6,3,4>' '<6,3,4,5>' '<6>']]
```

## 3 · Minimaler Spannbaum durch Zyklen-Eliminierung

**Datei:** `MSTCYCLE.py` · **Abgabe:** April 2022

Das Gegenstück zu Kruskal: Statt Kanten hinzuzufügen, werden sie entfernt. Solange der Graph einen Zyklus enthält (|E| − |V| + 1 Durchläufe), passiert Folgendes:

1. Eine Tiefensuche mit Färbung weiß, grau und schwarz findet eine Rückwärtskante und damit einen Zyklus.
2. Der Zyklus wird über die Elternkette rekonstruiert.
3. Die **schwerste Kante** des Zyklus wird aus der Adjazenzliste gelöscht.

Übrig bleibt ein minimaler Spannbaum. Das Skript gibt außerdem alle gefundenen Zyklen aus.

Beispiel (`G04PythonMST.txt`):
```
Final MST:
{1: [4], 2: [3], 4: [1, 5, 6, 7], 3: [2, 5], 5: [3, 4], 6: [4], 7: [4]}
Detected Cycles
[[4, 1, 2, 4], [4, 2, 3, 4], [5, 4, 2, 3, 5], [4, 5, 3, 6, 4], [5, 4, 6, 5], [7, 5, 4, 7]]
```

---

*Der Code ist im Original-Abgabestand erhalten. Angepasst wurden nur die Dateipfade zu den Testgraphen.*
