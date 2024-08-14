# README: Simulace dynamiky HBV infekce

Tento projekt obsahuje kód pro simulaci dynamiky infekce virem hepatitidy B (HBV) pomocí soustavy obyčejných diferenciálních rovnic (ODE). Model vychází z práce "Matematické modelování interakce viru a imunitního systému uvnitř hostitele", která je přiřazena do projektu pod shodným jménem. Popisuje interakce mezi virem, infikovanými buňkami, zdravými buňkami, cytotoxickými T-lymfocyty (CTL) a protilátkami, s cílem pochopit dynamiku infekce a imunitní odpovědi. Samotný kód umožňuje sledovat vývoj populací jednotlivých složek modelu v čase.

## Základní struktura projektu

### 1. Import potřebných knihoven
Kód využívá následující knihovny:
- `scipy.integrate.solve_ivp`: Pro numerické řešení systému ODE.
- `matplotlib.pyplot`: Pro vizualizaci výsledků simulace.
- `numpy`: Pro efektivní práci s poli a další numerické operace.

### 2. Definice modelu (`model(t, u)`)
Funkce `model` definuje systém diferenciálních rovnic, které popisují změny v populacích následujících složek:
- `I` (Infikované buňky): Populace buněk infikovaných HBV.
- `V` (Virus): Koncentrace viru v těle.
- `T` (Zdravé buňky): Populace zdravých buněk, které mohou být infikovány.
- `E` (Cytotoxické T-lymfocyty, CTL): Imunitní buňky zodpovědné za ničení infikovaných buněk.
- `A` (Protilátky): Protilátky, které se vážou na virus a pomáhají při jeho odstranění.

### 3. Počáteční podmínky
Počáteční podmínky určují počáteční populace jednotlivých složek na začátku simulace:
- `I`: 1 infikovaná buňka.
- `V`: 1 virová částice.
- `T`: 1 milion zdravých buněk.
- `E`: 1000 CTL buněk.
- `A`: 1000 protilátek.

### 4. Řešení systému ODE
Časový interval pro simulaci je nastaven na 100 dnů. Systém ODE je vyřešen pomocí funkce `solve_ivp`, která numericky integruje diferenciální rovnice.

### 5. Vizualizace výsledků
Výsledky simulace jsou vykresleny do grafů, kde každá proměnná je zobrazena na samostatném grafu:
- `I (Infikované buňky)`
- `V (Virus)`
- `T (Zdravé buňky)`
- `E (CTL)`
- `A (Protilátky)`

Grafy ukazují změny v čase a umožňují vizualizovat dynamiku infekce a odpovědi imunitního systému.

## Použití
Pro nastavení jednotlivých parametrů jednoduše přiřaďte hodnotu dané proměnné.
Pro spuštění simulace a vykreslení grafů stačí spustit Python skript. Grafy budou automaticky vykresleny po dokončení simulace. 

## Závěr
Tento model poskytuje užitečný nástroj pro studium dynamiky infekce HBV uvnitř hostitele. Model může být použit k testování hypotéz o vlivu různých faktorů na průběh infekce a může být dále rozšiřován pro simulaci dalších virových onemocnění nebo jiných aspektů imunitní odpovědi. Může být dále rozšířen a upraven pro přesnější simulace nebo pro jiné virové infekce.
