#	'ensure that formatted text option in draw.io is disabled everywhere'

ARG=""

strippeddown: scanner3.drawio.json
	python3 main.py . 0D/python ${ARG} 'main' scanner3.drawio.json

full: scanner3.drawio.json
	python3 main-full.py . 0D/python ${ARG} 'main' scanner3.drawio.json

scanner3.drawio.json:
	./0D/das2json/das2json scanner3.drawio

#########

# to install required libs, do this once
install-js-requires:
	npm install ohm-js yargs prompt-sync
