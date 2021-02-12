# How to set up a BedWars-Map
(Based on *https://github.com/BedwarsRel/BedwarsRel/wiki/Instructions#setup-game-single-server*)

# Info
If a text is like `/command <color>`, replace `<color>` with a color, e.g. `/command blue`. Another example: `/ban <user>` and `<user>` should be replace with a user, for example `/ban onlixx`. Don't type neither the `<` and `>` or the parameter/agrument (e.g. `color` or `game-name`). If you still don't get it, sorry, this is important. If you don't understand it, you can't really execute any commands. Because of that, I'll give you some more examples:

> - `/gamemode <mode>` can be `/gamemode creative`
> - `/tp <x> <y> <z>` can be `/tp 1 2 3`

Remember that the values given in the command (e.g. `creative` or `1`, `2` and `3`) are seperated with a space ( ). In almost all commands, the name can't contain spaces or special symbols like `+`, `-`, `.` or `,`. You can, in the most cases, use underscores (`_`) though.

Also, you can see a full list of commands here: https://github.com/BedwarsRel/BedwarsRel/wiki/Commands.

# Tutorial
## Create the world
1. Create the world using Multiverse by executing ` /mvcreate <world-name> normal -g VoidWorld`.Give it a cool name, beacuse it will be displayed later when joining the map.

2. Now teleport into the world using `/mvtp <world-name>`.

3. Confirm using `/mvconfirm`, you have 15 seconds time after step 2.

4. Go into creative mode using `/gm 1`.

5. This is optional, but recommended, becuase it can fix several spawn issues: do `/setblock 0 1 0 command_block` and `/setblock 0 2 0 stone_pressure_plate`, right click the command block and set the command to `tp @p 0 101 0` and hit *done*.

6. Now do `/setblock 0 100 0 stone` and start building!

7. You can use villager spawn eggs (search them in the creative menu) to create shops. Make sure they don't go away! You can use fence or barriers (`/give <your-name> barrier`).

## Setup the plugin
1. Do `/bw addgame <game-name> <max-players>` and make sure to remember the game name! It is really important. You will need it in almost every single command of the plugin. Name it e.g. `bw5`, if `bw5` already exists, `bw6`.

2. Execute `/bw addteam <game-name> <team-name> <color> <maximum-players>`. The color can be one of them: *GREEN, RED, BLUE, YELLOW, AQUA, BLACK, GOLD, DARK_BLUE, DARK_GREEN, DARK_RED, DARK_PURPLE, GRAY, DARK_GRAY, LIGHT_PURPLE, WHITE*.

3. Go to the location/base where the players of a specific team should spawn and type `/bw setspawn <game-name> <team>`.

4. Stand at the top of the bed, look at it and do `/bw setbed <game-name> <team>`. Make sure your position (above the bed) and facing (to the bed) is correct, or it will not work.

5. Create a resource spawner by standing on the block which should be a spawner and typing `/bw setspawner <game-name> <type>`, the type can be either *iron*, *gold* or *diamond*. If you want to create a double as fast spawner, execute the command twice at the same location! To delete all spawners in a game/map, do `/bw clearspawner {game}`.

6. Now, it's important that you select the **whole** map, just like you would with WorldEdit. This is really imporant, so be sure to practice first.

    > If you are confused with selecting areas, please practice first with basic WorldEdit-commands by executing `//loc1` and `//loc2`, to set the area and `//set stone` to fill the selected area with stone blocks. If you want to undo it, so its normal again, do `//undo`.

You can select a little bit more though, but not too much. So, to select a region, fly **up** to a **corner** of the region and do `/bw setregion <game-name> loc1`. Fly **down** to the other **corner** and type `/bw setregion <game-name> loc2`.

7. Teleport to the BedWars hub-world by executing `/warp bw`. Now go into the area, where players should teleport to if they click a join-sign for a map (currently fence). Make sure your position is correct (currently directly **below** the sign) and do `/bw setlobby <game-name>`.

8. This is the last step: do `/bw save <game-name>`.