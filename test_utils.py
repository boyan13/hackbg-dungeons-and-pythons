import unittest
from utils import ascii_image_extract


class test_utils(unittest.TestCase):

    def test_ascii_image_extract(self):
        self.maxDiff = None
        e = None
        file = "ascii_griffin.txt"
        expected = [
        "                           _",
        "                          _)\\.-.",
        "         .-.__,___,_.-=-. )\\`  a`\\_",
        "     .-.__\\__,__,__.-=-. `/  \\     `\\",
        "     {~,-~-,-~.-~,-,;;;;\\ |   '--;`)/",
        "      \\-,~_-~_-,~-,(_(_(;\\/   ,;/",
        "       \",-.~_,-~,-~,)_)_)'.  ;;(",
        "         `~-,_-~,-~(_(_(_(_\\  `;\\",
        "   ,          `\"~~--,)_)_)_)\\_   \\",
        "   |\\              (_(_/_(_,   \\  ;",
        "   \\ '-.       _.--'  /_/_/_)   | |",
        "    '--.\\    .'          /_/    | |",
        "        ))  /       \\      |   /.'",
        "       //  /,        | __.'|  ||",
        "      //   ||        /`    (  ||",
        "     ||    ||      .'       \\ \\\\",
        "     ||    ||    .'_         \\ \\\\",
        "      \\\\   //   / _ `\\        \\ \\\\__",
        "       \\'-'/(   _  `\\,;        \\ '--:,",
        "        `\"`  `\"` `-,,;         `\"`\",,;"
        ]

        try:
            res = ascii_image_extract(file)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()