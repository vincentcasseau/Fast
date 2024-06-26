#
# -- Compilation des fortrans --
#
# Definis dans le Makefile :
# SOURCEF77 : liste des source f77
# LIBNAME : nom librairie
# Repertoire de production des .o fortrans
PRODDIR   = ../../build/$(ELSAPROD)/

# -- Ne pas modifier ci-dessous --
SRC77     = $(shell ../MakeObjs.mk "$(SOURCEF77)")
OBJS      = $(SRC77:%.for=%.o)
OBJS2     = $(shell ../MakeObjsPath.mk "$(OBJS)") 
LIB2      = $(shell ../MakeObjsPath.mk "lib$(LIBNAME).a")
all: link $(LIB2)

.SUFFIXES: .for .f

.for.o:
	echo "Compiling fortran 77: " $<
	@(cpp -traditional -I../../../KCore/KCore -I. -I../.. -DINTEGER_E="INTEGER*4" -DREAL_E="REAL*8" -DE_SCALAR_COMPUTER -DE_OMP_SOUS_DOMAIN $< > $(PRODDIR)/temp.f; \
	$(FC) $(FOPT0) $(FOPT1) $(FOPT2) $(FOPT3) -I../.. -c $(PRODDIR)/temp.f -o $@; rm $(PRODDIR)/temp.f)

link:	$(SRC77)
	@if [ -d ../../build/ ]; then :; else mkdir ../../build; fi
	@if [ -d $(PRODDIR) ]; then :; else mkdir $(PRODDIR); fi
	@for i in $(SRC77); do \
	../MakeLink.mk "`pwd`" $$i $(PRODDIR);\
	done

$(LIB2) : $(OBJS2)
	@echo Making $(DIRECTORY) library
	@ar r  $@ $(OBJS2) ; ranlib $(LIB2)
	@echo done
