> [!NOTE]  
> Several job abilities have different recast timers than they would have if a regular player used them.

[^kick]: Monsters seem to be unable to benefit from `Kick Attacks` at all, no extra *single* attacks were observed on `MNK` monsters.

[^no_equip]: This job ability is linked with equipment and is unavailable as monsters technically have none.

[^solo]: This job ability specifically targets **allies** and monsters cannot form parties with one another.

## Warrior

| Job Ability       | Available in Monstrosity | Differences from Player JA Usage |
|:-----------------:|:------------------------:|:-------:|
| Mighty Strikes    | ✓ |
| Provoke           | ✕ |
| Berserk           | ✓ |
| Defender          | ✓ |
| Warcry            | ✓ |
| Aggressor         | ✓ |
| Retaliation       | ✕ |
| Warrior's Charge  | ??? |
| Tomahawk          | ??? |
| Restraint         | ✓ |
| Blood Rage        | ✓ |
| Brazen Rush       | ??? |

## Monk

| Job Ability       | Available in Monstrosity | Differences from Player JA Usage |
|:-----------------:|:------------------------:|:-------:|
| Hundred Fists     | ✓ |
| Boost             | ✓ | base recast: `15`s<br>buff duration: `180`s |
| Dodge             | ✓ | base recast: `300`s<br>buff duration: `120`s |
| Focus             | ✓ | base recast: `300`s<br>buff duration: `120`s |
| Chakra            | ✓ | base recast: `300`s |
| Chi Blast         | ✕ |
| Counterstance     | ✓ |
| Footwork [^kick]  | ✕ |
| Mantra            | ✓ |
| Formless Strikes  | ✓ |
| Perfect Counter   | ✓ |
| Impetus           | ??? |
| Inner Strength    | ??? |

rabbit
10733 => 10711 = 2.2
onyx rabbit
10351 => 10329 = 2.2
alabaster rabbit
10434 > 10412 = 2.2

<details>
<summary>Oddities</summary>
Mantra:
- HP increase for lv80 Gnole = 16058 > 16746 (688), which is far from expected.
- HP increase more consistent with having a "base" max HP of `[5734~5740]`
- If "base" max HP is 5735 then observed max HP = "base" max HP * 2.8
- Removing 1 HP merit reduces max HP by 28 (2.8 * 10)
- Mantra[3] HP Boost is 12% Max HP, 5735 * (2.8 + 0.12) = 16746.2
Chakra:
- Heals for 944 for lv80 Gnole, far lower than expected
- Much more consistent with hp value theorized "base" max HP value above, (~13% HP heal)
</details>

### White Mage

| Job Ability       | Available in Monstrosity | Differences from Player JA Usage |
|:-----------------:|:------------------------:|:-------:|
| Benediction       | ✓ |
| Divine Seal       | ✓ |
| Afflatus Solace   | ✓ |
| Afflatus Misery   | ✓ |
| Martyr            | ??? |
| Devotion          | ??? |
| Divine Caress     | ??? |
| Sacrosanctity     | ??? |
| Asylum            | ??? |

### Black Mage

### Red Mage

| Job Ability       | Available in Monstrosity | Differences from Player JA Usage |
|:-----------------:|:------------------------:|:-------:|
| Chainspell        | ✓ |
| Convert           | ✓ |
| Composure         | ✓ |
| Saboteur          | ✓ |
| Spontaneity       | ??? |
| Stymie            | ??? |

### Thief

### Paladin

| Job Ability               | Available in Monstrosity | Differences from Player JA Usage |
|:-------------------------:|:------------------------:|:-------:|
| Invincible                | ✓ |
| Holy Circle               | ✓ |
| Shield Bash [^no_equip]   | ✕ |
| Sentinel                  | ✓ |
| Cover [^no_equip] [^solo] | ✕ |
| Rampart                   | ??? |
| Majesty                   | ??? |
| Fealty                    | ??? |
| Chivalry                  | ??? |
| Divine Emblem             | ??? |
| Sepulcher                 | ??? |
| Palisade                  | ??? |
| Intervene                 | ??? |

### Dark Knight

| Job Ability               | Available in Monstrosity | Differences from Player JA Usage |
|:-------------------------:|:------------------------:|:-------:|
| Blood Weapon              | ✓ |
| Arcane Circle             | ✓ |
| Last Resort               | ✓ |
| Weapon Bash [^no_equip]   | ✕ |
| Souleater                 | ✓ |
| Consume Mana              | ✓ |
| Dark Seal                 | ??? |
| Diabolic Eye              | ??? |
| Nether Void               | ??? |
| Arcane Crest              | ??? |
| Scarlet Delirium          | ??? |
| Soul Enslavement          | ??? |

### Beastmaster

### Bard

### Ranger

### Samurai

| Job Ability               | Available in Monstrosity | Differences from Player JA Usage |
|:-------------------------:|:------------------------:|:-------:|
| Meikyo Shisui             | ✓ |
| Warding Circle            | ✓ |
| Third Eye                 | ✓ |
| Hasso [^no_equip]         | ✕ |
| Meditate                  | ✓ |
| Seigan [^no_equip]        | ✕ |
| Sekkanoki                 | ??? |
| Konzen-ittai              | ??? |
| Shikikoyo                 | ??? |
| Blade Bash                | ??? |
| Sengikori                 | ??? |
| Hamanoha                  | ??? |
| Hagakure                  | ??? |
| Yaegasumi                 | ??? |

### Ninja

### Dragoon

### Summoner

### Blue Mage

### Corsair

| Job Ability               | Available in Monstrosity | Differences from Player JA Usage |
|:-------------------------:|:------------------------:|:-------:|
| Wild Card                 | ✓ |
| Phantom Roll              | ✓ |
| Double-Up                 | ✓ |
| Quick Draw [^no_equip]    | ✕ |
| Random Deal               | ??? |
| Snake Eye                 | ??? |
| Fold                      | ??? |
| Triple Shot               | ??? |
| Crooked Cards             | ??? |
| Cutting Cards             | ??? |