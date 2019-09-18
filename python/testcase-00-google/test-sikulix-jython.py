import org.sikuli.script.SikulixForJython
from sikuli.Sikuli import *

textedit = App('open -a "TextEdit"')
textedit.open()
sleep(1)
type("Knock, Knock, Neo")
textedit.close()
