#	'ensure that formatted text option in draw.io is disabled everywhere'

SRC=test.txt

all:
	./0D/das2json/das2json peephole.drawio
	./0D/das2json/das2json 0D/python/std/transpile.drawio
	python3 main.py . 0D/python ${SRC} main peephole.drawio.json transpile.drawio.json

clean:
	rm -f *.json
	rm -f *~

#########

# to install required libs, do this once
install-js-requires:
	npm install ohm-js yargs prompt-sync
