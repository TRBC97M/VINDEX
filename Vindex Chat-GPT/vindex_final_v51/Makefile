.PHONY: probatio verifica auto-hospitium

probatio:
	bash ./tests/run_tests.sh

verifica:
	python3 instrumenta/vindex_verifica.py tests/casus/salve.vindex
	python3 instrumenta/vindex_verifica.py probationes/logica_brevis.vindex

auto-hospitium:
	chmod 755 ./compilator_vindex
	./compilator_vindex src/compilator_vindex.vindex /tmp/compilator_vindex_gen2
	chmod 755 /tmp/compilator_vindex_gen2
	/tmp/compilator_vindex_gen2 src/compilator_vindex.vindex /tmp/compilator_vindex_gen3
	chmod 755 /tmp/compilator_vindex_gen3
	cmp /tmp/compilator_vindex_gen2 /tmp/compilator_vindex_gen3
	cmp ./compilator_vindex /tmp/compilator_vindex_gen3
