.PHONY: probatio probatio-officina officina systema verifica auto-hospitium amorsa installa

probatio:
	./tests/run_tests.sh

probatio-officina:
	python3 -m unittest discover -s tests -p 'test_officina.py' -v

officina:
	cc -std=c11 -O2 -Wall -Wextra -Werror runtime/vindex_graphica_gtk.c -ldl -o vindex_graphica
	./compilator_vindex src/officina_vindex.vindex officina_vindex
	./compilator_vindex src/salutatio_vindex.vindex salutatio_vindex
	chmod 755 officina_vindex salutatio_vindex vindex_graphica vindex-officina vindex-salutatio
	./vindex_graphica --verifica-formam formae/officina.forma
	./vindex_graphica --verifica-formam formae/salutatio.forma

systema:
	./systema/construe_systema.sh
	./systema/uefi/construe_uefi.sh

verifica:
	./vindexc --verifica src/compilator_vindex.vindex

auto-hospitium:
	./compilator_vindex src/compilator_vindex.vindex /tmp/compilator_vindex_gen2
	chmod 755 /tmp/compilator_vindex_gen2
	/tmp/compilator_vindex_gen2 src/compilator_vindex.vindex /tmp/compilator_vindex_gen3
	cmp /tmp/compilator_vindex_gen2 /tmp/compilator_vindex_gen3

amorsa:
	./bootstrap/reconstruit.sh

installa:
	./installa_officinam.sh
