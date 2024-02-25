# main.py
Starts the game

## __init__.py
Is empty, it needs to be there for the thing to work.

## util.py
does some important dataclass stuff

## errors.py
Defines a number of errors for us to throw if we need them

## *_test.py
Is a test file.

# Board.py
Defines the Board class,
A Board contains a 2D array of Tiles
This array is one of 2 pre determined layouts dependant on the number of players
A Board will tell each of it's tiles what it's directly adjacent tiles are
The Board will keep track of the available priest cult spaces
A Board can:
    - find all the tiles of a terrain type
    - find all the directly or indirectly adjacent tiles of a given tile on the board
    - given 2 different tiles, tell if they are directly or indirectly adjacent or not
    - filter a given set of tiles for any terrain type
    - mark a priest cult space as used when a player peforms that action and grants the cult advancement for it

## Tile.py
Defines the Tile class
A Tile can:
    - have it's terrain type changed if it is undeveloped
    - tell you whether a particular building is able to be built on this tile
    - have a valid building built on it

## board_layouts.py
Defines the default boards for <=5 players and 5>X<=7 players

## Cult.py
Defines the Cult Enum

## CultProgress.py
Defines the CultProgress class which keeps track of a player's cult progress.

## Terrain.py
Defines the Terrain Enum
Sets the order of terrain types for terraforming
Reports the cost of terraforming a tile from a given terrain type to another terrain type

## Building.py
Defines the Building Enum

# Action.py
Describes different types of actions:
    - location specific actions (terraform or build)
    - bonus actions             (stronghold or book)
    - cult actions              (priests and octogons)
    - shared actions            (communal octogons)
    - anytime actions           (scroll/power actions)
Lists all the actions in each of those categories and specifies price and effect

## AbstractResources.py
Defines a class for values that we aren't sure how to categorise

## Resources.py
Defines the resources class.

## Power.py
Defines the Power class which limits the number of power "blops" to 12
Describes the "3 bowls" system
Provides methods to easily gain and pay power

## PassToken.py
Defines the PassToken class
## pass_tokens.py
Lists all the data for each pass token
## FavourToken.py
Defines the FavourToken class
## favour_tokens.py
Lists all the data for each favour token
## RoundToken.py
Defines the RoundToken class
## round_token.py
Lists all the data for each round token
## TownToken.py
Defines the TownToken class
## town_tokens.py
Lists all the data for each town token

# Faction.py
Defines a faction colour Enum
Defines the Faction class which:
    - defines what income you get for each building
    - tracks accumulated resources
    - defines the cost of buildings and upgrades found on a player board
Defines a class for each faction which:
    - specifies the different costs and abilities for that faction