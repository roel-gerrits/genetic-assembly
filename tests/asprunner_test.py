

from assembly.blocks import Blocks
from asp.asprunner import AspRunner
from genetic.bio import Bio


b = Blocks.from_string("""1 3 5 1 2
    2 5 5 3 4
    3 1 1 4 5
    4 0 0 5 5
    5 3 4 3 5
    6 0 0 2 4
    7 0 2 0 1
    8 2 2 2 3
    9 3 5 0 0
    10 1 1 2 3
    11 2 2 4 4
    12 2 2 5 5
    13 5 5 5 5
    """);

br = AspRunner(b)

br.add_bio(Bio(100, 0.1, 0.1, 100));
br.add_bio(Bio(100, 0.2, 0.1, 100));
br.add_bio(Bio(100, 0.3, 0.1, 100));

br.run()