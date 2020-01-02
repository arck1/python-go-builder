GO_SRC_DIR=./go/
PY_SRC_DIR=./py/
DIST=./dist/

GO_DIST=$(addsuffix $(GO_SRC_DIR), dist)
PY_DIST=$(addsuffix $(PY_SRC_DIR), dist)

GO_FLAGS=-buildmode=c-shared

include .env

#SRC_D = $(addprefix $(GO_SRC_DIR),$(SRC))
ifeq ($(SRC_D),)
	SRC_D=$(wildcard $(GO_SRC_DIR)*.go)
endif

ifeq ($(SRC),)
	SRC=$(notdir $(SRC_D))
endif

OBJ = $(SRC_D:%.go=%.so)


build: init $(OBJ)
	@echo "Objects builded: $(OBJ)"

%.so: %.go
	@echo "Building $<"
	go build $(GO_FLAGS) -o "$(GO_DIST)$(notdir $@)" $<

.PHONY: init
init:
	mkdir -p $(DIST)
	mkdir -p $(GO_DIST)
	mkdir -p $(PY_DIST)

.PHONY: clean
clean:
	rm -f $(DIST)/*
	rm -f $(GO_DIST)/*
	rm -f $(PY_DIST)/*

test:
	echo $(SRC)