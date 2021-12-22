# Game of Life

The [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a cellular automation. This project is my own cli implementation of this automation, as suggested at the [Programming Projects for Advanced Beginners](https://robertheaton.com/2018/07/20/project-2-game-of-life/) series by [Robert Heaton](https://robertheaton.com/about/).

It is developed using Python 3, some of its libraries and tests.

The options available are:

- Board width. By default it fills the whole terminal window.
- Board Height. Also fills the terminal window if not specified.
- Life percentage. This is the chance of each cell initializing alive. It defaults to 50 if not specified.
- Load a file. This is an option to load the initial state of the board from a file.
- Interval between states. Defaults to 0.1s.
- Change the rules. There are three modes available. Classic, which is the normal mode. Immortal, where alive cells never dies. And Ressurection mode, where there is a 15% chance for each dead cell to become alive.
