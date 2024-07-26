#	'ensure that formatted text option in draw.io is disabled everywhere'

ARG=""

all:
	./0D/das2json/das2json scanner3.drawio
	python3 main.py . 0D/python ${ARG} 'main' scanner3.drawio.json

#########

# to install required libs, do this once
install-js-requires:
	npm install ohm-js yargs prompt-sync
