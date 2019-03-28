#!/bin/make

########### CONFIGURATION ########################

NAME=informatica2019
REMOTE="massimo@massimolauria.net:/srv/www/massimolauria.net/courses/${NAME}/"
TIME   = $(shell date +%Y%m%d.%H%M)


########### BUILDING PARAMETERS ##################

EMACS=emacs

ifeq ($(shell uname -s),Darwin)
EMACS=/Applications/Emacs.app/Contents/MacOS/Emacs
EMACSCLIENT=/Applications/Emacs.app/Contents/MacOS/bin/emacsclient
endif


BUILD=site-build

########### THE RULES ############################

all: $(BUILD)
	$(EMACS) --batch -l publish.el --eval '(org-publish-project "main" nil)'

$(BUILD):
	$(EMACS) --batch -l publish.el --eval '(org-publish-project "main" t)'

clean:
	@rm -vrf $(BUILD)

pkg:
	@make clean
	@echo "Building $(NAME).SNAP.$(TIME).tar.gz"
	@$git archive HEAD | gzip -c > ../$(NAME).SNAP.$(TIME).tar.gz 2> /dev/null

deploy:
	rsync -rvz --chmod='u=rwX,go=rX' $(BUILD)/ $(REMOTE)


.PHONY: all clean pkg deploy
